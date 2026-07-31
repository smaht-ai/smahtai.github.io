---
layout: post
title: "How to Build a Learning Agent: Architecture, Knowledge Base, and Production Lessons"
date: 2026-06-20 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/learning-agent-splash.png
categories: [ai, programming, engineering]
description: "Architecture, knowledge base design, and production lessons for building a learning agent."
---


Building a production-grade learning agent is fundamentally different from wiring up a general-purpose chatbot. A true learning agent maintains strict boundaries, grounds every factual claim in curated knowledge, orchestrates specialized behaviors, remembers users across sessions, and generates structured artifacts that drive real growth. It must feel intelligent and safe while remaining observable and operable.

This post walks through exactly how we designed, built, and operate such a system—end to end.

## What Makes a Learning Agent Different

A learning agent is purpose-built for structured human development. Users engage in three distinct modes:

- **Learn mode**: Socratic exploration of concepts. The agent never lectures; it guides discovery, requires verification, and keeps every example or definition strictly inside the knowledge base.
- **Prepare mode**: Application to real, upcoming situations. The agent helps users pressure-test decisions and craft opening moves.
- **Reflect mode**: Extraction of insight from past experience. The agent distinguishes between surface tactics (“I’ll try harder”) and deeper pattern recognition (“I realized I feared conflict because…”).

The agent refuses to become a general chatbot. Off-topic queries are declined. Every response is either retrieved from the knowledge base or explicitly hedged.

## High-Level Architecture

The system is deliberately layered so each part can evolve independently:

<div data-excalidraw="/assets/excalidraw/learning-agent.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/learning-agent.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;"><strong>Figure 1:</strong> Learning agent architecture.</p>

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

**Core technology choices**:
- **Frontend**: React + TypeScript — implements the three journeys and real-time streaming UI.
- **Backend**: An async Python web framework — the orchestrator agent and subagents.
- **AI**: A managed LLM API — we use Sonnet-class models for reasoning agents and faster, cheaper models for routing and fact extraction. Any capable provider works here.
- **Knowledge**: A hybrid RAG knowledge base (BM25 + vector retrieval) backed by object storage. Source documents include the core text plus structured curriculum files (definitions, applications, and examples for each learning unit).
- **Memory**: A cross-session memory layer that extracts and embeds facts into a vector store.
- **State**: PostgreSQL.
- **Workflows**: A workflow engine for all background processing.
- **Observability**: An LLM observability platform (traces), OpenTelemetry + an ops metrics stack, product analytics.
- **GitOps**: GitOps tooling on Kubernetes.
- **Local dev**: A containerized dev environment + Docker Compose + pre-commit hooks.

## The Request Lifecycle (Mental Model)

Every user message follows a predictable, observable path:

1. **Ingress** — POST or streaming endpoint receives the message. Auth middleware validates the JWT (using your identity provider's public key). Rate-limit and concurrency semaphores protect expensive paths.
2. **Guardrail check** — Input guardrail (managed service or mock) runs before any LLM call.
3. **Persistence** — User message is written to PostgreSQL immediately. The question is also copied to a background thread for memory fact extraction so it does not block the request path.
4. **Memory retrieve** — Relevant user facts are fetched from the memory layer (vector search) and held for prompt assembly.
5. **Agent selection** — Based on **chat state** (`Orchestrator`, `Learn`, `Prepare`, or `Reflect`), the runtime selects the active agent.
6. **Prompt assembly** — The agent LLM prompt is built from: system prompt for the selected agent, conversation history (including prior tool call request/reply pairs), the new user question, tool definitions, and retrieved memory facts appended last (to preserve prompt cache).
7. **LLM call with tools** — All agents share two tools: `KnowledgeBaseTool` and `UpdateChatStateTool`. The LLM is invoked with the assembled prompt and tool list.
8. **Tool loop** — The LLM either requests a tool call or responds directly. Typically it calls `KnowledgeBaseTool` first; tool output is appended to context and the LLM is called again. It may then call `UpdateChatStateTool` to save chat state—either enabling a subagent (Learn, Prepare, or Reflect) or returning control to the orchestrator. When no further tools are needed, the agent streams the final answer via Server-Sent Events.
9. **Output guardrails** — Checked every N characters during the stream. Violations truncate the response cleanly.
10. **Completion** — LLM response is persisted. Background tasks fire: memory write (the user's question was already copied to a background thread at ingress), search index update, and full telemetry emission.
11. **Artifact generation** — At natural close points the agent emits a special `{...}` json record in its text response (not via a tool). The frontend extracts it, transforms it, and POSTs it to be stored as JSONB.

## Chat State, Agents, and Tools

Each conversation carries a **chat state**: `Orchestrator`, `Learn`, `Prepare`, or `Reflect`. This state determines which agent handles the next turn. When an agent calls `UpdateChatStateTool`, the new state is saved and survives restarts.

**Orchestrator Agent** — Determines which chat phase the conversation is in and delegates to the appropriate subagent. It **never** speaks directly to the user.

**Subagents** (Learn, Prepare, Reflect) — Handle user-facing dialogue when chat state matches their mode. Depending on state, they stream a response or return control to the orchestrator.

Tool request/response pairs are formatted as ordinary chat messages in the conversation chain, so prior tool calls remain visible in context on subsequent turns.

### Shared tools

All three subagents share the same two tools:

**KnowledgeBaseTool**
- Query curriculum content through semantic search / RAG retrieval

**UpdateChatStateTool**
- Saves the new chat state
- Enables a subagent (Learn, Prepare, or Reflect) or returns control to the orchestrator

Cards (Learn, Reflect, Prepare) are **not** created through a tool. They are emitted as JSON in the agent's text response (`{...}`).

### Orchestrator routing
The orchestrator is the single entry point for every message. It **never** speaks directly to the user. Its only job is classification and clean handoff.

Routing heuristics (implemented via structured output + confidence scoring):
- Direct “What is X?” or “Explain X” questions → Learn
- Retrospective language (“I had…”, “We tried…”, “I realized…”) → Reflect
- Situations, upcoming decisions, tensions, “How should I…” → Prepare
- Low confidence on Learn or Reflect → fallback to Prepare

When routing completes, the orchestrator calls `UpdateChatStateTool` to save state as Learn, Prepare, or Reflect. When a subagent finishes its flow, it calls the same tool to set state back to `Orchestrator`.

This separation keeps each agent's prompt focused and makes debugging easier—you always know which agent is active from chat state.

## Specialized Agent Behaviors

Each agent has its own prompt file, model, and hard constraints.

**Learn Agent** (Sonnet)
- Flow: Calibrate → Prime → Ground → Explore → Transfer → Verify (mandatory) → Close
- Verify step forces the user to articulate the concept in their own words.
- Close emits a structured Learn Card.
- Constraints: 2–3 sentence turns, zero invented examples, no “Great point!” affirmations, KB-only retrieval.

**Prepare Agent** (Sonnet)
- First-turn rule: Lead with a directional hypothesis using an embedded concept index. Do **not** call the knowledge base on turn 1 (latency + not yet needed).
- Close emits a Prepare Card containing situation, insight, and suggested opening.

**Reflect Agent** (Sonnet)
- Core distinction: insight vs. tactic. The agent gently redirects “I’ll try harder next time” toward examining underlying assumptions.
- Canonical concept names must surface by turn 2–3 using the exact names from the curriculum index.
- Close emits a Reflect Card.

All three agents share three policy files injected at the system-prompt level:
- Hostile-framing policy (hedge unverified claims)
- No-code-generation policy
- No-tool-leakage policy (tools must execute silently)

## Grounding and Safety

**Knowledge retrieval** happens exclusively through `KnowledgeBaseTool`—semantic search over the curated knowledge base. Agents are instructed to retrieve concept definitions on first reference and narrative examples only when going deeper.

**Guardrails** operate at two layers:
1. Prompt-level policies (above).
2. A managed guardrails service (input + output) — content filters, topic denials, PII entity redaction, regex for secrets removal, and profanity word lists.

Output guardrails run during streaming so a violation mid-response truncates cleanly and logs the redaction event to the observability platform.

## Structuring the Knowledge Base as Curriculum

A learning agent's knowledge base is not a pile of PDFs waiting to be chunked. It is a **curriculum**: a catalog of learning units, each documenting a core idea and how to apply it in practice. That structure is what makes retrieval useful—the agent gets definitions, applications, and stories in context, not random paragraphs.

### What each learning unit contains

Every unit in the curriculum follows a consistent schema. The exact field names vary by domain, but the layers are always the same:

| Layer | Purpose | Typical content |
| --- | --- | --- |
| **Concept** | What the idea means | Definition, core idea, anchor quotes |
| **Context** | Why it matters broadly | Summary and key points at a field or societal level |
| **Organizational application** | How teams apply it | Practices, norms, and decision patterns |
| **Personal application** | How an individual applies it | Mindset shifts and concrete behaviors |
| **Examples** | Grounded narrative cases | Situation → action → outcome, with tags for retrieval |
| **Guidance** | How to use it well | Decision rules, diagnostics, common errors, do/don't lists |
| **Relationships** | Links across the curriculum | Related, reinforcing, or tension concepts |

Beyond standalone units, the curriculum can include **lessons** (intro → concept → application sections) and **scenarios** (guided practice prompts tied to specific units). Relationship metadata connects them so agents and the UI can suggest what to explore next.

### Example: a unit on accountability

**Concept** — Accountability means bearing the consequences of a decision or action, with recognition proportional to contribution. It is not punishment; it is clarity about who owns an outcome and what happens next.

**Applications** — At the organizational level: every initiative needs a clear owner; well-designed experiments that fail still deserve recognition for the learning they produce. At the personal level: own your decisions, ask for clarity on decision rights before acting, and treat feedback as input for improvement rather than judgment.

**Examples** — Narrative cases make the idea concrete:

- *The well-designed experiment* — A team runs a carefully scoped pilot. Results show the approach will not work, but the experiment was sound. Leadership recognizes the learning produced and shares it across teams; the owner stays motivated to experiment again.
- *Unclear ownership* — A cross-functional project stalls because no one knows who owns key decisions. Leadership pauses, assigns a single owner with explicit authority, and the team adopts documenting decision rights at kickoff.

Each example follows the same **situation → action → outcome** pattern so agents can retrieve and retell grounded stories instead of inventing plausible-sounding ones.

### Example: a unit on distributed knowledge

**Concept** — Useful knowledge is dispersed: no single person holds everything needed for good decisions. Progress depends on surfacing what each person knows about their context, strengths, and constraints.

**Applications** — Organizations build networks for sharing ideas, encourage challenge, and run experiments rather than assuming leadership has all the answers. Individuals develop domain expertise, share it openly, and seek input before deciding on behalf of others.

**Examples**:

- *Dispersed knowledge* — A leader facing a decision that affects multiple functions seeks input from people who understand local constraints. The decision improves; contributors feel empowered rather than overridden.
- *Standing on shoulders* — A newcomer wants to replace existing processes from scratch. A mentor explains that accumulated organizational know-how is an asset to build on—even while outdated assumptions should still be challenged.

### How agents query the curriculum

Agents do not rely on parametric memory for curriculum content. They call `KnowledgeBaseTool` with targeted queries:

- First time naming a concept: `"[Concept name] definition core idea"`
- Going deeper with stories: `"[Concept name] example story application"`
- Connecting to the user's situation: `"[Concept name] application [context keyword]"`

Retrieved chunks supply definitions, case studies, and application guidance. Card artifacts pull their `concept` field from this retrieved material—the one place where the agent must be accurate to the source, not paraphrasing from training data.

Cards themselves are not tools. They are JSON emitted in the agent's text response once the user has articulated personal understanding.

### Two delivery paths, one curriculum

| Path | Role |
| --- | --- |
| **Hybrid knowledge base** (object storage → chunked → RAG) | Runtime grounding for chat agents via `KnowledgeBaseTool` |
| **Structured JSON documents** (bundled or served via content API) | Browseable library UI, concept detail pages, and editorial workflows |

Both reflect the same architecture: a catalog of learning units, each with **definition + multi-level application + narrative examples + relationships**. That consistency is what keeps coaching tied to your material rather than generic LLM knowledge—and what makes it possible to audit whether the agent stayed on curriculum.

## Cross-Session Memory

Generic agents forget everything between conversations. A learning agent should not.

After every exchange a background task passes the conversation to the memory layer, which uses an LLM to extract atomic facts. These facts are embedded and stored in a vector store. Before the next agent LLM call, relevant facts are retrieved via vector search and injected into the prompt—appended last, alongside tool definitions and conversation history, to preserve prompt cache.

## Structured Artifacts and the Personal Dashboard

At the end of a conversation the subagent emits a card for display in the UI that includes:
- The core concept and its definition (grounded in the knowledge base)
- How the user connected the concept to their situation
- How the user plans to apply the concept when next encountering the situation
- What other situations the concept applies to
- The user's breakthrough realization, if any

The agent prompt describes how the card should be generated. The card is written by the LLM as JSON at the end of its text response—not through a tool call—and parsed and rendered by the UI as a bordered summary with a concept header and key-value items.

These cards are also saved back in the Postgres database, stored as JSONB. They power the personal dashboard, which additionally shows:
- Follow-up reflection prompts generated by a background workflow after a conversation goes idle.
- AI-generated insight sections (pattern detection across concepts, depth recommendations, growth evidence) computed by a background pipeline once the user has sufficient history.
- Suggested next concepts and practice nudges.

All heavy insight work happens in background workflows running either periodically or triggered by events.

## Observability as the Operating Surface

You cannot operate an agentic system without ops monitoring. The agent emits:
- Full LLM observability traces for every LLM call (including token usage, guardrail decisions, and redaction events).
- OpenTelemetry metrics and spans for the entire request path.
- Structured logs with correlation IDs.
- Product analytics events.

When something goes wrong—empty retrieval, guardrail trigger, client disconnect, orchestrator routing failure—we have the exact trace and can reproduce it.

## Local Development & Safe Deployment

Developers work inside a containerized dev environment that is portable across Linux, Mac, and Windows. It includes:
- Docker Compose with a local PostgreSQL instance
- Version-managed tooling
- Git pre-commit/pre-push hooks (linting, type checks, security scans)
- AI editors that can run infrastructure CLI commands for debugging — invaluable for quick and accurate troubleshooting of ops issues.

Production deploys via GitOps. Most changes are safe to make in prompt files, agent routing logic, or dashboard components. Schema changes, new guardrail policies, or workflow engine modifications require more ceremony and testing.

## Key Lessons

1. **Orchestrator + subagents + chat state** beats a single monolithic prompt. Persisted chat state and a single `UpdateChatStateTool` keep routing predictable.
2. **Structure the knowledge base as curriculum**, not documents. Definitions, applications, and narrative examples in a consistent schema make retrieval—and auditability—dramatically better than raw PDF chunks alone.
3. **Dual guardrails** (prompt-level + managed service) catch different classes of problems and make the system defensible. Evaluate managed guardrail services carefully—they vary significantly in flexibility and configurability.
4. **Memory must be observable and rate-limited**. The memory layer + vector store works well once you add the right connection hygiene and semaphores.
5. **Background workflows are non-negotiable** for card generation and insight pipelines. They keep the real-time path fast and the dashboard snappy.
6. **Observability is the product**. Without LLM observability traces and structured metrics you are flying blind the moment an agent does something surprising.

## Closing Thoughts

A production learning agent is not “just an LLM with retrieval.” It is a carefully orchestrated socio-technical system: persisted chat state, grounded knowledge via shared tools, persistent memory, streaming UX, background insight pipelines, multi-layer safety, and deep observability.

The architecture described here has proven robust in production. It scales, it fails gracefully, and—most importantly—users and operators alike can understand what the system is doing at any moment.

If you’re building something similar, start with the mental model of request flow, chat state, and the two shared agent tools. Layer on a structured curriculum for the knowledge base early—it pays off in grounding quality. Everything else (memory, guardrails, background workflows, dashboard artifacts) becomes much easier once that foundation is solid.

What part of building learning agents are you wrestling with right now? I’d love to hear about it.
