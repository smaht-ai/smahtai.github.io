---
layout: post
title: "How We Built the DocRouter n8n Nodes With Cursor (In the Open)"
date: 2026-01-31 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/n8n_gmail_to_docrouter.png
categories: [ai, programming, engineering, tutorials]
description: "How the n8n-nodes-docrouter package was built and published in a single Cursor session — with examples for document listing, chat, and Gmail automation workflows."
---

We shipped **[n8n-nodes-docrouter](https://www.npmjs.com/package/n8n-nodes-docrouter)**—a full set of n8n community nodes and credentials for [DocRouter.ai](https://app.docrouter.ai). This post does three things: **how to use the nodes** (with examples), **how we built them** in a single Cursor thread while cross-checking the real backend in `../doc-router`, and **how this blog post was written**.

---

## How to Use the DocRouter n8n Nodes

### Install the package

The easiest way is in the n8n UI: **Settings → Community Nodes → Install**, then enter the package name **n8n-nodes-docrouter**.[^1]

The DocRouter nodes then become available in the node search list.

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_docrouter_nodes.png" alt="DocRouter nodes in n8n" data-modal-src="/assets/images/n8n_docrouter_nodes.png" /></span>
</div>

### Credentials

You need one of two credential types:

- **DocRouter Organization API** – organization-level token. Use it for: Documents, Tags, LLM, Prompts, Schemas, Knowledge Base, Webhook.
- **DocRouter Account API** – account-level token. Use it only for the **DocRouter Account** node (users and organizations).

Create the API token in **DocRouter** (Settings → User → Developer). Then create the credential in **n8n** (Settings → Credentials or when adding a DocRouter node), paste your API token from DocRouter, and optionally override the base URL for self-hosted or staging (default: `https://app.docrouter.ai/fastapi`).

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_org_creds.png" alt="DocRouter Organization API credential in n8n" data-modal-src="/assets/images/n8n_org_creds.png" /></span>
</div>

### Example: List documents and get one

1. Add a **DocRouter Document** node.
2. Choose credential: **DocRouter Organization API**.
3. Operation: **List** (optional: limit, skip, name search).
4. Run the workflow → you get a list of documents (and total count).
5. Add another **DocRouter Document** node, Operation: **Get**, set **Document ID** (e.g. from the first node’s output: `{% raw %}{{ $json.id }}{% endraw %}`).
6. Run → you get that document’s metadata; if it has content, it’s in **binary** (downloadable).

<div class="grid md:grid-cols-2 gap-4 md:gap-6 my-4 md:my-6">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_list_documents.png" alt="DocRouter List Documents in n8n" data-modal-src="/assets/images/n8n_list_documents.png" /></span>
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_get_document.png" alt="DocRouter Get Document in n8n" data-modal-src="/assets/images/n8n_get_document.png" /></span>
</div>

### Example: Chat with a knowledge base

1. Add a **DocRouter Knowledge Base** node.
2. Credential: **DocRouter Organization API**.
3. Operation: **Chat**.
4. Set **Knowledge Base ID**, **Model** (e.g. `gpt-4o-mini`), **Messages** (JSON array, e.g. `[{"role":"user","content":"What do we have on resumes?"}]`).
5. **Stream**: off → you get a single JSON object with `text`, `tool_calls`, `tool_results`. Stream on → you get the same shape after the node parses SSE for you.
6. Run → the output has the assistant’s answer and any tool calls (e.g. `search_knowledge_base`) and results.

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_chat_with_kb.png" alt="DocRouter Chat with Knowledge Base in n8n" data-modal-src="/assets/images/n8n_chat_with_kb.png" /></span>
</div>

### Example: Manage users (account admin)

1. Add a **DocRouter Account** node.
2. Credential: **DocRouter Account API** (account-level token).
3. Operation: **List Users** (optional: limit, skip, organization ID filter, search name).
4. Or **Create User** (email, name, password), **Update User** (user ID + optional name, password, role, etc.), **Delete User** (user ID).

Same node supports **List / Get / Create / Update / Delete Organizations** with the same account credential.

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_list_users.png" alt="DocRouter List Users in n8n" data-modal-src="/assets/images/n8n_list_users.png" /></span>
</div>

### Example: Webhook trigger

1. Add a **DocRouter Webhook** node (trigger).
2. Configure **Webhook path** and, if you use HMAC in DocRouter, the **Secret** and optional **Timestamp tolerance**.
3. When DocRouter sends an event to that URL, the workflow runs; you can verify the signature and use the payload in the next nodes.

For a deep-dive into DocRouter's webhook implementation, see [How We Built Webhooks With Cursor and Claude Code](/ai/programming/engineering/how-we-built-webhooks-with-cursor-and-claude-code/).

### Example: Gmail to DocRouter

This workflow uploads Gmail attachments to DocRouter:

- **Gmail Trigger** (with “download attachments”) → **Split Out** on `$binary` so each attachment becomes its own item.
- **Code** node renames the binary key to `attachment`.
- **DocRouter Document** node uploads each file to DocRouter.

You need **Gmail OAuth2** and **DocRouter Organization API** credentials.

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_gmail_to_docrouter.png" alt="Gmail to DocRouter workflow in n8n" data-modal-src="/assets/images/n8n_gmail_to_docrouter.png" /></span>
</div>

<div align="center">
<button type="button" class="n8n-json-modal-trigger" id="n8n-gmail-json-btn">Download workflow JSON</button>
</div>

Other nodes (**DocRouter Tag**, **LLM**, **Prompt**, **Schema**) follow the same pattern: pick operation (List, Get, Create, Update, Delete—or operation-specific ones like Run LLM, Validate Schema, Search KB), fill resource IDs and body fields, run.

---

## How It Was Implemented “In the Open”

The nodes were built in **one Cursor thread**, with the codebase and the **real DocRouter backend** in `../doc-router` open in the same workspace. That made it possible to implement, then immediately check and fix behavior against the actual API and Python code.

### What we had at the start

- An n8n community node repo derived from the n8n starter (with Example and GitHub Issues nodes).
- DocRouter Organization API credentials type already present.
- A goal: “Build n8n nodes for DocRouter.ai” and, step by step, add all the APIs we use.

### Prompts and steps (in order)

Roughly, the conversation went like this:

1. **Document node and binary content**  
   Ask: what’s the right n8n pattern for document content—binary vs base64? Answer: use the **binary** property. Then: add an “Output Document As” option; later: remove it and only support binary when content exists.

2. **Webhook trigger**  
   Ask: add a trigger node for DocRouter webhooks with HMAC verification and optional timestamp check. Implemented; then we hit `_a.trim is not a function` because the secret wasn’t always a string—fixed with a type guard (`typeof rawSecret === 'string' ? rawSecret.trim() : ''`).

3. **Tags, then “Custom API Call”**  
   Ask: add a node for DocRouter tags (List, Get, Create, Update, Delete). After that, “remove the Custom API Call option.” That option comes from n8n core for credential-based nodes. We can’t remove it from the UI, so we handled `__CUSTOM_API_CALL__` in the switch and threw a clear error telling users to use the HTTP Request node for custom calls. That pattern was reused in every DocRouter node.

4. **GitHub nodes gone**  
   Ask: remove all GitHub-related nodes, credentials, and icons. We deleted those files and cleaned up `package.json`.

5. **LLM, Prompts, Schemas, Knowledge Base**  
   One after the other: “Add a node for DocRouter LLM (run, get, update, delete result),” “Add a node for DocRouter Prompts (all APIs),” “Add a node for DocRouter Schemas (including validate and list versions),” “Add a node for DocRouter Knowledge Base (list, get, create, update, delete, list documents/chunks, search, chat, reconcile).” Each time we followed the same structure: operations, parameters, one List/Get-style “run once” path and per-item paths for Create/Update/Delete, plus the `__CUSTOM_API_CALL__` branch.

6. **Knowledge Base Chat and streaming**  
   In use we saw: with **stream on**, the result was parsed correctly; with **stream off**, the API was still returning SSE. Prompt: “When stream is off, the result is still sent as stream, is that correct?” We fixed the **n8n node** first: detect SSE-shaped responses and always parse them into one object (`text`, `tool_calls`, `tool_results`) so the output is consistent. Then: “Look under ../doc-router, is stream=false supported as a parameter?” We checked the Python API: the parameter existed but the KB chat handler always returned a streaming response. So the next prompt was: “Fix it in ../doc-router.” We added a non-streaming path in `run_kb_chat`: when `request.stream` is false, run the same agentic loop but collect into a single dict and return JSON instead of `StreamingResponse`. After that: “Fix the n8n node now to expect non-streaming response in non-streaming mode”—so when stream is off we use the response as-is (one JSON object) and only parse SSE when stream is on.

7. **Account node**  
   “Create a docrouter node for accounts, with all apis for account/users and account/organizations.” We already had DocRouter Account API credentials. We added the **DocRouter Account** node with List/Get/Create/Update/Delete for both Users and Organizations, using the account-level API and the same patterns as the other nodes.

8. **Publishing**  
   “I’d like to publish it as n8n-nodes-docrouter” → we confirmed the name, fixed the README to match the real package contents, removed the wrong `main` field from `package.json`, and left publish steps (including `npm publish --otp=...` for 2FA). Then: “Publish it.” The `prepublishOnly` script was still `n8n-node prerelease`, which blocked publish and said to use `npm run release`. We changed it to `npm run build` so `npm publish` builds and publishes; publish then succeeded. “OK - the README was not updated to reflect the correct package contents” → we rewrote the README with the actual nodes and credentials, installation, and usage. “What version is the package now” → 0.1.0. “Bump version and release” → we bumped to 0.1.1 and ran `npm publish` again (tag `v0.1.1` was created in git).

### Hooking up to ../doc-router

Having the **doc-router** source code in the same workspace (as `../doc-router`) was critical:

- **Stream parameter:** We didn’t assume the API “must” support `stream=false`; we searched the Python routes and `run_kb_chat` and saw the parameter existed but the handler always returned a stream. So we fixed the backend first, then the node.
- **Optional parameters:** The Knowledge Base node had “Could not get parameter” for optional fields like `coalesceNeighborsSearch` and `maxTokens`. We avoided calling `getNodeParameter` for those unless the parameter key existed in `this.getNode().parameters`, matching how n8n omits optional params.
- **SSE shape:** We matched the backend’s SSE format (`data: {"type":"tool_call",...}`, `data: {"chunk":"H",...}`, etc.) so the node’s parser could aggregate tool calls, tool results, and text chunks correctly.

So: **implement in the node repo, verify and fix against the real API and backend in doc-router.** No guessing the contract.

### How this blog post was written

You’re reading the result of another Cursor prompt in the same “in the open” style:

- **Request:** Write a markdown blog post that (1) at the top explains how to use the DocRouter n8n nodes with examples, (2) in the middle explains step-by-step how the nodes were created in this Cursor thread, what prompts were used, and how we hooked up to the ../doc-router sandbox to review and fix things, and (3) explains how the blog post itself was written. 

- **What Cursor did:** It read a couple of existing posts for front matter and tone, and created a new one, as a synthesis of the conversation summary and the steps we just walked through: usage first, then implementation story and prompts, then “how this post was written.” So this post is both the doc and the meta-story of how it was generated.

- ... Then, a few **manual touch-ups** finished the blog post.

[n8n-nodes-docrouter on npm](https://www.npmjs.com/package/n8n-nodes-docrouter) · [Source on GitHub](https://github.com/analytiq-hub/n8n-nodes-docrouter) · [DocRouter docs](https://docrouter.ai/docs)

----

## Footnotes

[^1]: **Alternative ways to install (npm or Docker):** Where n8n is installed, run `npm install n8n-nodes-docrouter` and restart n8n. For Docker, set `N8N_COMMUNITY_PACKAGES=n8n-nodes-docrouter`.

<style>
.n8n-img-cred-wrap { display: flex; justify-content: center; margin: 1rem 0; }
.n8n-img-cred-wrap .n8n-img-modal-wrap { max-width: 50%; }
.n8n-img-cred-wrap .n8n-img-modal-wrap img { width: 100%; height: auto; display: block; }
.n8n-img-modal-wrap { position: relative; display: inline-block; }
.n8n-img-modal-wrap::after { content: "Click to expand"; position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%); background: rgba(0,0,0,0.75); color: #fff; padding: 4px 10px; border-radius: 4px; font-size: 12px; white-space: nowrap; opacity: 0; transition: opacity 0.2s ease; pointer-events: none; }
.n8n-img-modal-wrap:hover::after { opacity: 1; }
.n8n-img-modal-backdrop { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 9999; align-items: center; justify-content: center; cursor: pointer; }
.n8n-img-modal-backdrop.is-open { display: flex; }
.n8n-img-modal-backdrop img { max-width: 95vw; max-height: 95vh; object-fit: contain; pointer-events: none; }
.n8n-img-modal-trigger { cursor: pointer; }
.n8n-json-modal-trigger { cursor: pointer; padding: 0.4rem 0.8rem; background: #2563eb; color: #fff; border: none; border-radius: 6px; font-size: 14px; margin-top: 0.5rem; }
.n8n-json-modal-trigger:hover { background: #1d4ed8; }
</style>
<div class="n8n-img-modal-backdrop" id="n8n-img-modal" role="button" tabindex="-1" aria-label="Close">
  <img src="" alt="" id="n8n-img-modal-img" />
</div>
<script type="text/template" id="n8n-gmail-workflow-json">{"name":"DocRouter Gmail Upload Short","nodes":[{"parameters":{"pollTimes":{"item":[{"mode":"everyMinute"}]},"simple":false,"filters":{},"options":{"downloadAttachments":true}},"type":"n8n-nodes-base.gmailTrigger","typeVersion":1.3,"position":[208,-16],"id":"62e7e68f-a33f-42c1-b5de-020ca2a7a0df","name":"Gmail Trigger","credentials":{"gmailOAuth2":{"id":"NefrrTfahhV9uXug","name":"Gmail account"}}},{"parameters":{"jsCode":"const results = [];\n\nfor (const item of $input.all()) {\n  const bin = item.binary || {};\n  const keys = Object.keys(bin);\n  \n  if (keys.length > 0) {\n    const originalKey = keys[0];\n    results.push({\n      json: item.json,\n      binary: { attachment: bin[originalKey] }\n    });\n  }\n}\n\nreturn results;"},"type":"n8n-nodes-base.code","typeVersion":2,"position":[592,-16],"id":"d93ed3f1-754d-4ffa-877f-c82e7c9f3d3b","name":"Rename Attachment Keys"},{"parameters":{"content":"### Split email attachments\n* Multiple nodes needed to set up attachment file name, file size as item keys","height":288,"width":416},"type":"n8n-nodes-base.stickyNote","position":[320,-144],"typeVersion":1,"id":"fc9a3c70-546a-4d6d-a2f4-22bbd0cba8e1","name":"Sticky Note"},{"parameters":{"fieldToSplitOut":"$binary","options":{}},"type":"n8n-nodes-base.splitOut","typeVersion":1,"position":[368,-16],"id":"cc7d3c12-4a7b-4353-837e-3fdbede2073b","name":"Split Out Attachments"},{"parameters":{"content":"### Upload to DocRouter.AI \n** Upload to DocRouter with optional prompt tag","height":288,"width":304},"type":"n8n-nodes-base.stickyNote","position":[768,-144],"typeVersion":1,"id":"cbd3794c-9056-4cef-89ac-889bb56fc8a7","name":"Sticky Note1"},{"parameters":{"binaryPropertyName":"attachment"},"type":"n8n-nodes-docrouter.docRouterDocument","typeVersion":1,"position":[848,-16],"id":"40e9452f-187e-47d8-9641-143f5b01f605","name":"DocRouter Document","credentials":{"docRouterOrgApi":{"id":"XW25oTYKlQBYzt7L","name":"DocRouter Organization"}}},{"parameters":{"content":"# How To Build An N8N->DocRouter.AI Workflow\n### Upload Gmail Attachments to DocRouter.AI","height":96,"width":896,"color":4},"type":"n8n-nodes-base.stickyNote","position":[176,-304],"typeVersion":1,"id":"b6f9f696-e5f7-4070-9252-ae9b5a30df48","name":"Sticky Note2"}],"pinData":{},"connections":{"Gmail Trigger":{"main":[[{"node":"Split Out Attachments","type":"main","index":0}]]},"Rename Attachment Keys":{"main":[[{"node":"DocRouter Document","type":"main","index":0}]]},"Split Out Attachments":{"main":[[{"node":"Rename Attachment Keys","type":"main","index":0}]]}},"active":false,"settings":{"executionOrder":"v1","availableInMCP":false},"versionId":"14a77060-d11b-4a65-9167-ad47acf49b6b","meta":{"templateCredsSetupCompleted":true,"instanceId":"8ab29dcbe42ee02938bb9d98be601e8a092f5bed9d589cf469bcf275a53670cb"},"id":"imAPYvqkas1yKQKM","tags":[]}</script>
<script>
(function() {
  var imgBackdrop = document.getElementById('n8n-img-modal');
  var modalImg = document.getElementById('n8n-img-modal-img');
  var imgTriggers = document.querySelectorAll('.n8n-img-modal-trigger');
  function openImgModal(src, alt) { modalImg.src = src; modalImg.alt = alt; imgBackdrop.classList.add('is-open'); }
  function closeImgModal() { imgBackdrop.classList.remove('is-open'); }
  imgTriggers.forEach(function(el) { el.addEventListener('click', function() { openImgModal(el.dataset.modalSrc, el.alt); }); });
  imgBackdrop.addEventListener('click', closeImgModal);

  var jsonTemplate = document.getElementById('n8n-gmail-workflow-json');
  var jsonBtn = document.getElementById('n8n-gmail-json-btn');
  if (jsonBtn && jsonTemplate) {
    jsonBtn.addEventListener('click', function() {
      var json = JSON.parse(jsonTemplate.textContent);
      var blob = new Blob([JSON.stringify(json, null, 2)], { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'gmail-to-docrouter-workflow.json';
      a.click();
      setTimeout(function() { URL.revokeObjectURL(a.href); }, 100);
    });
  }
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeImgModal();
  });
})();
</script>
