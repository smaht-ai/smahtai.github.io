---
layout: post
title: "Why I Prefer MongoDB For AI Applications"
date: 2026-02-17 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/mongodb-ai-applications-splash.png
categories: [tech, programming, ai, databases]
description: "Why MongoDB is ideal for AI applications: document-centric storage, vector search, knowledge bases, and horizontal scaling for DocRouter.AI and SigAgent.AI."
---

_This post was co-published by MongoDB at [mongodb.com](https://www.mongodb.com/company/blog/technical/why-i-prefer-mongodb-for-ai-applications)._

I use MongoDB as the primary database for AI-powered products like [DocRouter.AI](https://docrouter.ai) and [SigAgent.AI](https://sigagent.ai). This post explains how it's implemented—migrations, vector search, and knowledge bases—and why I prefer it over alternatives like Postgres for document-centric, JSON-heavy AI workloads. I want to store a very large number of documents (DocRouter) or logs (SigAgent) without spending much time tuning the database for horizontal scaling; MongoDB fits that need well.

## Brief trade-offs vs Postgres

Postgres with **jsonb** can model the same document-style records and even integrate vector search via extensions, but it shines most when you need **strong relational guarantees** and **complex joins** around a relatively **stable schema**. MongoDB is a better fit when **almost everything is a JSON document**, the schema **evolves quickly**, and you care more about **horizontal scaling** and **quick turnaround** than about classic SQL features. 

In my case, the workloads are heavily document- and log-centric, so the ergonomics and scaling model of MongoDB outweigh the benefits of staying inside the relational/Postgres ecosystem.

<div class="mt-6 overflow-x-auto">
  <table class="min-w-full border border-gray-200 text-sm text-left">
    <thead class="bg-gray-50">
      <tr>
        <th class="px-4 py-2 font-semibold text-gray-700 border-b border-gray-200">Aspect</th>
        <th class="px-4 py-2 font-semibold text-gray-700 border-b border-gray-200">MongoDB Approach</th>
        <th class="px-4 py-2 font-semibold text-gray-700 border-b border-gray-200">Postgres Alternative</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-100">
      <tr class="odd:bg-white even:bg-gray-50">
        <td class="px-4 py-2 align-top">Schema flexibility</td>
        <td class="px-4 py-2 align-top">Evolving via migrations; no enforcement from the DB, but disciplined application code keeps documents consistent.</td>
        <td class="px-4 py-2 align-top">Rigid but enforceable with DDL; great for stable relations, heavier for fast-changing AI schemas.</td>
      </tr>
      <tr class="odd:bg-white even:bg-gray-50">
        <td class="px-4 py-2 align-top">Scaling</td>
        <td class="px-4 py-2 align-top">Horizontal scaling and sharding are built-in; easy to grow with large document/log volumes.</td>
        <td class="px-4 py-2 align-top">Requires extensions or external tooling (e.g. Citus) and more tuning when pushing JSONB-heavy workloads.</td>
      </tr>
      <tr class="odd:bg-white even:bg-gray-50">
        <td class="px-4 py-2 align-top">Consistency model</td>
        <td class="px-4 py-2 align-top">Tunable; we use majority writes and typically read from secondaries, so most reads are eventually consistent.</td>
        <td class="px-4 py-2 align-top">Strong ACID semantics with primary reads by default; great when you need strict guarantees across transactions.</td>
      </tr>
      <tr class="odd:bg-white even:bg-gray-50">
        <td class="px-4 py-2 align-top">Vector search</td>
        <td class="px-4 py-2 align-top">Native <code>$vectorSearch</code> in MongoDB 8.2+/Atlas.</td>
        <td class="px-4 py-2 align-top">Via <code>pgvector</code>, which has mature support.</td>
      </tr>
      <tr class="odd:bg-white even:bg-gray-50">
        <td class="px-4 py-2 align-top">Joins &amp; relations</td>
        <td class="px-4 py-2 align-top">Limited</td>
        <td class="px-4 py-2 align-top">Strong</td>
      </tr>
      <tr class="odd:bg-white even:bg-gray-50">
        <td class="px-4 py-2 align-top">Dev speed</td>
        <td class="px-4 py-2 align-top">Quick iterations on JSON schemas and migrations; fits rapid AI product experiments.</td>
        <td class="px-4 py-2 align-top">Slower to evolve schemas cleanly; better when you already know the long-term relational shape.</td>
      </tr>
    </tbody>
  </table>
</div>

It's also totally reasonable to split responsibilities: e.g. **Postgres for relational metadata**, a dedicated vector store like **Pinecone/Weaviate/Qdrant** for embeddings, or **Redis** as an embedding cache in front of another database. For [DocRouter.AI](https://docrouter.ai) and [SigAgent.AI](https://sigagent.ai), I'm happy to trade some theoretical optimality for a **single operational datastore** (MongoDB handling documents, logs, and vectors) until scale or workload complexity justifies introducing extra systems.

## DocRouter and SigAgent: One Backend, Two Products

**DocRouter.AI** is a smart document router: you upload documents, define schemas and prompts, and it extracts structured data (e.g. from invoices, medical records, forms) using LLMs. **SigAgent** is a Claude agent monitor with a different UX and product focus, but it's built on the same stack.

Roughly **90% of the backend is shared**. Both use the same Python package, [analytiq_data](https://github.com/analytiq-hub/doc-router/tree/main/packages/python/analytiq_data): MongoDB client, migrations, queue layer, auth, and app startup. The same MongoDB database layout, indices, and migration history apply to both. Product-specific code lives in routes and frontends; the data layer is common.

<div data-excalidraw="/assets/excalidraw/mongodb_one_backend_two_products.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/mongodb_one_backend_two_products.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

## Strict Schema via Discipline: Migrations as "Schema"

MongoDB doesn't enforce a schema. I still want **predictable structure and safe upgrades**, so we enforce it in code and process:

- **Consistent document shape per collection.** We use a fixed set of field names and types in application code (and in TypeScript/Pydantic where applicable). In practice, each collection behaves like a table with a known "schema."
- **Every change goes through migrations.** Renaming fields, adding/removing fields, splitting or renaming collections—all of it is done in versioned migration classes with `up()` and `down()`. The current schema version is stored in a `migrations` collection; on startup we run `run_migrations(analytiq_client)` and bring the DB to the latest version.
- **Element types as schema.** We treat document fields as if they were typed: e.g. `schema_id`, `prompt_version`, `organization_id` are always present where we expect them. New code assumes the post-migration shape. So we get **comparable safety to Postgres** (known structure, no surprise shapes) while staying in a document model—as long as we're disciplined and never bypass migrations.

So: schema is "enforced" by convention and migrations, not by the database. That keeps development fast without giving up control.

## How Migrations and Indices Are Implemented

At a high level:

- **Migrations** are versioned Python classes with `up()`/`down()` methods that evolve collections in lockstep with the code.
- **Indices** are either created inside migrations (long-term, repeatable) or via a small helper at runtime for per-module needs.
- **Profiling tools** (Atlas Query Insights, profiler, Compass/Performance Advisor) surface slow queries that suggest new compound indexes.

### Migrations

Migrations live in [migration.py](https://github.com/analytiq-hub/doc-router/blob/main/packages/python/analytiq_data/migrations/migration.py). Each migration is a class with:

- `description`: short human-readable summary
- `up(db)`: apply the change (e.g. rename field, backfill, add index)
- `down(db)`: revert the change when possible

The runner loads the list `MIGRATIONS`, assigns a version by index, and stores the current version in `db.migrations` under `_id: "schema_version"`. On startup we run pending migrations in order. Examples from the codebase:

- **Field renames:** e.g. `RenameUserFields` (camelCase → snake_case)
- **New fields:** e.g. `LlmResultFieldsMigration` (adds `is_edited`, `is_verified`, timestamps)
- **Structural changes:** e.g. `RenameCollections` (schemas → schema_revisions, schema_versions → schemas), `UseMongoObjectIDs`

Collection layout and index strategy evolve in one place, with a clear history and rollback path.

### Indices

We manage indices in two ways:

1. **Inside migrations** for long-term indices. These are created with `create_index(..., background=True)` and dropped in `down()` so rollback is consistent.
2. **At runtime** via `ensure_index()` in `analytiq_data/mongodb/index.py`. Given a collection, index spec, and name, it creates the index if missing (and optionally drops other non-`_id` indexes). We use this for things like `payments_usage_records (org_id, timestamp)` when the payments module initializes.

Example index patterns:

- **Queue collections:** `(status, created_at)` for `find_one_and_update({ status: "pending" }, sort: { created_at: 1 })`.
- **docs:** `(organization_id, upload_date desc)` for paginated listing by org.
- **llm_runs:** `(document_id, prompt_id, prompt_version desc)` for "latest run by document and prompt," and `(document_id, prompt_revid)` for exact revision lookup.
- **document_index:** unique `(kb_id, document_id)` and a non-unique `document_id` index for cascade deletes.

To find candidates for new indices, we use **Atlas Query Insights** (filter by operations returning >1,000 documents, then add a compound index matching the filter and sort) or, on **Community Edition**, enable the database profiler and filter `system.profile` by `nReturned`:

```javascript
db.setProfilingLevel(1, { slowms: 100 })
db.system.profile.find({ nReturned: { $gt: 1000 } }).sort({ ts: -1 }).limit(20)
```

Level 2 profiling captures everything but has I/O cost, so we use it in short bursts or staging. Level 1 (slow only) is cheaper and still surfaces most heavy queries.

If you prefer GUIs over shell tools, both **MongoDB Compass** and the **Atlas Performance Advisor** surface similar slow-query/index recommendations in a more visual way, which is often easier when you're just getting started tuning a workload.

With schema and indices in place, here's how we run it.

## Dev/Prod Setup and Vector Search

Quickly, the environments look like this:

- **Local:** MongoDB running on `localhost` or via the Atlas Local Docker image (bundling `mongod` + `mongot`) for easy vector search testing.
- **Production:** MongoDB Atlas or AWS DocumentDB, configured for majority writes and read scaling.
- **Self-hosted:** MongoDB 8.2+ with `mongot` in a replica set, using the same `createSearchIndexes` / `$vectorSearch` APIs.

For **local development**, `MONGODB_URI` defaults to `mongodb://localhost:27017`. For vector search, we use the **MongoDB Atlas Local** Docker image (`mongodb/mongodb-atlas-local:latest`), which bundles `mongod` and **mongot** (the search/vector process) in one container.

For **production** we use **MongoDB Atlas**; for on-prem consulting we use **AWS DocumentDB**. The client is configured with `w='majority'`, `readPreference='secondaryPreferred'`, and `retryWrites=False` (DocumentDB doesn't support retryWrites).

For **self-hosted Community Edition**, vector search requires **MongoDB 8.2+** with **mongot** running alongside `mongod` in a replica set. The `createSearchIndexes` command and `$vectorSearch` aggregation work the same way across Atlas, Community 8.2+, and the local Docker image—no separate code path.

## Knowledge Bases on Top of Vector Search

We implement **knowledge bases** in the shared backend using MongoDB's vector search, with three key pieces: an indexing pipeline, a search pipeline, and a reconciliation service.

<div data-excalidraw="/assets/excalidraw/mongodb_knowledge_base_flow.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/mongodb_knowledge_base_flow.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

### Indexing: Blue-Green Atomic Swap

Each knowledge base gets its own vector collection (`kb_vectors_<kb_id>`). When a document is indexed, we chunk the text (via [Chonkie](https://github.com/chonkie-ai/chonkie), a small library for token/sentence/recursive text chunking), generate embeddings via [LiteLLM](https://github.com/BerriAI/litellm), a lightweight multi-provider LLM/embedding client, and then atomically swap old vectors for new ones inside a MongoDB transaction:

```python
async with await client.start_session() as session:
    async with session.start_transaction():
        # Delete old vectors for this document
        await vectors_collection.delete_many(
            {"document_id": document_id}, session=session
        )
        # Insert new vectors
        await vectors_collection.insert_many(new_vectors, session=session)
        # Update document_index entry
        await db.document_index.update_one(
            {"kb_id": kb_id, "document_id": document_id},
            {"$set": { ... }},
            upsert=True, session=session
        )
        # Update KB stats (document_count, chunk_count)
        await db.knowledge_bases.update_one(
            {"_id": ObjectId(kb_id)},
            {"$set": {"document_count": total_docs, "chunk_count": total_chunks}},
            session=session
        )
```

This blue-green pattern means a document is never in a half-indexed state: either all its new vectors are visible, or the old ones remain.

<div data-excalidraw="/assets/excalidraw/mongodb_blue_green_indexing.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/mongodb_blue_green_indexing.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

### Embedding Cache

Embeddings are cached in a global `embedding_cache` collection keyed by `(SHA-256 chunk hash, embedding model)`. When the same text chunk appears in multiple KBs (or is re-indexed after an edit), we skip the API call and reuse the cached vector. This saves both cost and latency—especially when re-indexing a large KB after a configuration change.

### Search

The query string is embedded with the same model, then we run an aggregation whose first stage is `$vectorSearch` (with `numCandidates = max(top_k * 10, 100)` for better recall). We apply filters (organization, tags, date range) in the vector index definition, add `vectorSearchScore` via `$meta`, and optionally coalesce neighboring chunks for richer context.

### Reconciliation: Keeping KBs in Sync

Documents and KBs can drift: a document's tags change, a document is deleted, or vectors are orphaned after a failed indexing run. The reconciliation service ([reconciliation.py](https://github.com/analytiq-hub/doc-router/blob/main/packages/python/analytiq_data/kb/reconciliation.py)) detects and fixes this:

- **Missing documents:** documents with matching tags but no `document_index` entry → queued for indexing.
- **Stale documents:** indexed documents whose tags no longer match the KB → removed.
- **Orphaned vectors:** vectors without a corresponding `document_index` entry → deleted.

Reconciliation uses a **distributed lock** (atomic `find_one_and_update` with a 10-minute TTL) so only one worker reconciles a given KB at a time. It processes documents in batches of 100 to keep memory bounded, and supports **dry-run mode** for auditing without side effects.

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

---

In short: we get **strict schema via migrations**, **predictable indexing**, **vector search for RAG with atomic updates**, and **self-healing knowledge bases**—with one backend shared between DocRouter and SigAgent, and the same patterns whether we run on local Mongo, Atlas, or DocumentDB.
