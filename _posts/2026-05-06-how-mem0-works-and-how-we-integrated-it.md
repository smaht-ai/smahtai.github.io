---
layout: post
title: "How AI Agent Memory Works (and How We Integrated Mem0)"
date: 2026-05-06 00:00:00 +0000
author: "Andrei Radulescu-Banu"
categories: [ai, engineering, agents, rag]
description: "A practical walkthrough of mem0 in production: async memory ingestion, reconciliation (dedupe + deletes), retrieval with Titan embeddings, and storage in Postgres/pgvector."
image: /assets/images/mem0-integration-splash.png
---

When you build an agent that chats with users over days or weeks, you quickly hit a ceiling: **context windows** are finite, and “just include the whole conversation” doesn’t scale. You need **durable memory** that’s:

- **Incrementally updated** as the conversation evolves
- **Deduplicated and reconciled** (so it doesn’t accumulate contradictions)
- **Fast to retrieve** at the start of each turn
- **Cheap enough** to run on every message

In a Learning Agent developed recently, we integrated [mem0](https://github.com/mem0ai/mem0) to do exactly that: extract durable facts from conversations and store them in a **PostgreSQL vector database** (pgvector), then retrieve the most relevant memories and inject them back into the agent prompt.

This post explains how the integration works end-to-end, using the architecture diagram below as the blueprint.

<div data-excalidraw="/assets/excalidraw/mem0-agent-system-diagram.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>

<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;">
  <strong>Figure 1:</strong> Agent + memory flow (mem0 integration).
</p>

<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/mem0-agent-system-diagram.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    Edit in Excalidraw
  </a>
</div>

---

## Mental model: two parallel paths

mem0 integration is easiest to understand as **two paths that run in parallel** on each user message:

<div class="not-prose grid grid-cols-1 sm:grid-cols-2 gap-4 my-6">
  <div class="rounded-xl border border-slate-200 dark:border-slate-600 bg-gradient-to-br from-amber-50/90 to-orange-50/70 dark:from-amber-950/35 dark:to-orange-950/25 p-5 shadow-sm ring-1 ring-amber-100/70 dark:ring-amber-800/30">
    <span class="inline-flex items-center rounded-full bg-amber-100/90 dark:bg-amber-900/50 px-2.5 py-0.5 text-xs font-semibold uppercase tracking-wide text-amber-900 dark:text-amber-100">In the background</span>
    <h3 class="text-lg font-semibold text-slate-900 dark:text-slate-50 mt-3 mb-2">Memory ingestion</h3>
    <p class="text-sm text-slate-700 dark:text-slate-300 m-0 leading-relaxed">Store or update long-term facts.</p>
  </div>
  <div class="rounded-xl border border-slate-200 dark:border-slate-600 bg-gradient-to-br from-blue-50/90 to-indigo-50/70 dark:from-blue-950/35 dark:to-indigo-950/25 p-5 shadow-sm ring-1 ring-blue-100/70 dark:ring-blue-800/30">
    <span class="inline-flex items-center rounded-full bg-blue-100/90 dark:bg-blue-900/50 px-2.5 py-0.5 text-xs font-semibold uppercase tracking-wide text-blue-900 dark:text-blue-100">In the foreground</span>
    <h3 class="text-lg font-semibold text-slate-900 dark:text-slate-50 mt-3 mb-2">Memory retrieval</h3>
    <p class="text-sm text-slate-700 dark:text-slate-300 m-0 leading-relaxed">Fetch relevant facts to condition the next agent response.</p>
  </div>
</div>

Memory ingestion is a slow operation. Facts need to be extracted from the user prompt, deduplicated, and reconciled with already-stored facts. 

Users, on the other hand, should get a response quickly, based on the last user prompt and on retrieval of previously stored memories. Memory ingestion should not block the chat experience.

---

## Memory ingestion (background path)

When the user enters a new message, we trigger a background task to select, save and reconcile new facts in the memory store.

The actual memory writes happen **while** or **after** the response is returned, keeping the **time-to-first-token** fast.

### What mem0 stores

mem0’s job is to convert raw conversation into **small, high-signal “facts”** such as:

- Stable user profile info (role, work context, preferences)
- A single current goal (with updates overwriting older ones)
- Progress on “principles” (mentioned → explored → applied)
- Session summaries and open loops that span sessions

Facts are stored as strings in the vector DB, where they become searchable through both vector and token search, for example:

```
"Name: Mike Smith"
"Role: Plant Manager"
"Work context: Texas refinery, 40 direct reports"
"Hobbies: soccer, hiking, theater"
```

### The prompts we configure for mem0

mem0 ships with default prompts for multiple internal operations, but we **override three key prompts** to make memory behave like a disciplined coaching “profile” instead of a grab-bag of notes:

- **`custom_fact_extraction_prompt`**: turns the latest turn (user and/or assistant text) into a short list of *candidate facts*
  - Focuses on facts important for our application
  - Explicitly excludes PII/credentials and low-signal chatter.
- **`custom_update_memory_prompt`**: reconciles *candidate facts* against what’s already stored and emits a full “edit plan” using **ADD / UPDATE / DELETE / NONE**.
  - This is where dedupe and contradiction-handling happens (e.g. we don't want to store“Role: Manager” repeated multiple times).
  - The vector database is then updated based on the resulting edit plan
- **`custom_memory_answer_prompt`**: used when mem0 is asked to answer based on stored memories.
  - It’s written as an internal component: return the relevant facts **without** mentioning “memories” or retrieval mechanics, so the *agent* can incorporate them naturally.

### The LLM used for ingestion and reconciliation

mem0 uses an LLM twice during ingestion:

1. **Fact extraction**: identify candidate facts from the new turn.
2. **Reconciliation / update**: decide how those facts modify existing memory (**ADD / UPDATE / DELETE / NONE**).

We run these steps on a low-latency, cost-efficient model: **Claude Haiku** (via **AWS Bedrock**) for both ingestion and reconciliation. GPT Mini or Gemini Flash models would work just as well.

## Memory retrieval (request path)

**Memory Retrieve** runs at the start of each agent turn: we load durable memory and attach it to the agent context.

This happens while we’re building the agent LLM prompt. Memory retrieval runs concurrently with other non-dependent work (like syncing any conversation context directory from object storage), but it’s still on the critical path for prompt construction.

### Retrieval uses embeddings (not keyword search)

To fetch “what matters now,” we embed the user’s current situation and run a nearest-neighbor search over stored memories.

For retrieval embeddings we use **Amazon Titan Embed Text v2** (via **AWS Bedrock**), which produces **1024-dimensional vectors**. Those vectors are stored and searched in Postgres using **pgvector**.

---

## Storage: Postgres and pgvector

Memory lives in a Postgres database with the `vector` extension enabled (pgvector). In production, this is **AWS Aurora Postgres**, and we connect through **RDS Proxy** for connection multiplexing. mem0 uses the `pgvector` provider.

At a high level, each memory row contains:

- **The memory text**
- **The user id** it belongs to
- **Metadata** (conversation id, message id, agent id, etc.)
- **An embedding vector** (Titan v2, 1024 dims)

mem0 also maintains an internal migrations table (e.g. `mem0migrations`) so it can evolve its schema safely over time.

---

## Using memory in the agent prompt

Once retrieved, memories are injected into the request metadata and/or prompt context so the agent can respond as if it “remembers”:

- Who the user is and what context they’re operating in
- What they were working on last time
- The current open loop (what to follow up on)

The key design point is that we **don’t** try to jam all past dialogue into context. Instead we provide:

- The agent’s system prompt
- Tool definitions
- The recent conversation window (last \(N\) messages)
- A compact, semantically-retrieved memory summary.

That makes the system more stable across long sessions while keeping costs and latency bounded. The memory summary is included last, so we can use LLM caching for the previous parts of the prompt.

---

## Summary

mem0 gives you a clean separation of concerns:

- **Ingestion** (Claude Haiku): extract candidate facts and reconcile them into durable memory.
- **Storage** (Postgres + pgvector): persist memories as vectors + metadata, organized into collections.
- **Retrieval** (Titan embeddings) and **Reconciliation** (Claude Sonnet): pull the most relevant facts at the start of each turn and inject them into the agent prompt.

The result is an agent that feels consistent over time without relying on ever-growing context windows—and without turning “memory” into an unbounded pile of stale notes.

<style>
.excalidraw-container {
  width: 100%;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  background: white;
  display: block;
  margin: 2rem 0;
  min-height: 400px;
}
.excalidraw-container svg {
  width: 100%;
  height: auto;
  display: block;
  margin: 0;
}
.loading-placeholder {
  padding: 2rem;
  text-align: center;
  color: #666;
}
</style>
<script type="module" src="/assets/js/excalidraw/render-excalidraw.js"></script>

