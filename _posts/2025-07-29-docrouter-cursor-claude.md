---
layout: post
title: "DocRouter.AI: Adventures in CSS and AI Coding"
date: 2025-07-29
author: Andrei Radulescu-Banu
image: /assets/images/doc_router_cursor_claude.png
categories: [ai, programming, tech, reviews]
description: "How DocRouter.AI was built with Cursor and Claude Code — lessons on AI-assisted coding, schemas, web forms, FormIO/Tailwind integration, and MongoDB design."
---

DocRouter.AI transforms messy, multi-layout business documents into clean, structured data using large language models (LLMs) and schema-driven orchestration. We focus on regulated industries like insurance, healthcare, and supply chain, where precision is non-negotiable. It's a horizontal data layer application that plugs into vertical-specific apps, acting as an AI accelerator across sectors.

## DocRouter.AI User Experience

<img src="/assets/images/doc_router_user_experience.png" alt="DocRouter.AI User Experience" style="display: block; margin: 2rem auto; width: 80%; border-radius: 0.5rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);">

We're developing DocRouter.AI as open source because experience shows it leads to better-designed, more resilient code over time. Business value comes from our SaaS version at app.docrouter.ai and enterprise on-VPC installations. We also offer consulting to help other companies build software using similar styles and tools.

<img src="/assets/images/doc_router_repo.png" alt="DocRouter.AI Repository" style="display: block; margin: 2rem auto; width: 80%; border-radius: 0.5rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);">

**GitHub Repository:** [github.com/analytiq-hub/doc-router](https://github.com/analytiq-hub/doc-router)

A revolution is underway in software development with tools like Cursor and Claude Code. I'll dive into how we built DocRouter.AI, sharing lessons that could apply to your projects. (I've detailed my tool usage in a previous LinkedIn post, so I won't repeat it here.)

## My Background: From Embedded Systems to AI-Driven Front Ends

I come from a world of cloud, back-end, and embedded work, starting long ago with Linux kernel programming, computer networks, then high performance computing for Wall St, followed by robotics/ROS/computer vision.

In short, my expertise is embedded back-end, and data science. When starting DocRouter.AI, I had zero hands-on experience with front-end development— no JavaScript, TypeScript, or React.

But tools like GitHub Copilot (which helped me learn Apache Spark and Terraform from scratch in prior roles) paved the way. 

By fall of last year, Cursor enabled me to build DocRouter.AI with a Next.js front end, FastAPI back end, and AWS via Terraform. Claude Code exploded about a month ago, and I've began using it intensively.

## Lessons from AI Coding Tools: What Works and What Doesn't

<img src="/assets/images/claude_code_vs_cursor.png" alt="Claude Code vs Cursor" style="display: block; margin: 2rem auto; width: 80%; border-radius: 0.5rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);">

We often hear engineers claiming they can "zero-shot vibe code" entire apps from scratch. That's possible for simple, UI-focused apps, but for anything complex, the human engineer must stay in the loop. Knowing when to let AI take over and when to intervene is becoming a black art.

For DocRouter.AI, we use FastAPI on the back end, with all functions in a single file (`main.py`) to simplify AI editing—easier for pattern searching and consistency. If designing for humans, I'd split it into 8-10 files. But, for AI editors, a single large file simplifies things.

AI agents have "personalities." Claude Code Agent outperforms Cursor Agent right now. I use Cursor in manual mode, attaching specific files. Keeping FastAPI in one file reduces attachment hassle.

AI editors love "improving" code inconsistently. Most of `main.py`, our FastAPI interface, was built with Cursor. But for web form support (more on why below), I tasked Claude Code with creating similar FastAPI endpoints (create, list, get, update, delete) to our existing schema ones.

Claude did great but switched to identifying things with UUIDs instead of our MongoDB `_id` scheme. I almost did not notice it. I caught it by asking Claude Code to explain in practice how the new APIs are used. 

## Why Schemas, Web Forms, and MongoDB?

I'm a fan of the simplest tool for the job. DocRouter.AI stores documents, LLM prompts, and extraction schemas—MongoDB collections are ideal. Mongo handles blobs via GridFS, avoiding external storage like S3 (which Postgres would require).

**Schemas:** LLMs can output free-form or structured JSON. Providers support JSON schemas for precise LLM output. For docs, we classify types (e.g., via LLM prompt) then extract a specific schema—like date, patient name, DOB, address, diagnostics, doctor details in a medical prescription.

DocRouter.AI lets users configure extraction [schemas](/docs/schemas/) for all doc types.

**Web Forms:** Schemas are too abstract for end users accustomed to ERPs (e.g., Epic for EHR, Salesforce for CRM). End users are instead familiar with entering data into web forms tailored to their process.

We had to add web form support to DocRouter.AI: LLM extractions map to pre-populated form fields. LLM-as-judge scores confidence, so users focus on low-confidence fields—cutting effort by up to 90%.

To stay horizontal (not vertical-specific), we avoid hard-coding web forms. Instead, we integrate a schema builder, and a web form builder.

The web form builder was pretty complicated.

But the schema builder was vibe-coded in Cursor (manual mode, incremental development: first do the FastAPI back end, then the Axios APIs, then the UI components, and the unit testers). It worked out of the box!

For comparison, Base44 solo entrepreneur Maor Shlomo (podcast interview) uses MongoDB too, seeing it as AI-era friendly over SQL. He uses plain React and JavaScript; I use Next.js and TypeScript. His simpler stack might ease things—worth pondering.

Note that Next.js has server-side capabilities, but we use FastAPI for most back-end functions.

## DocRouter.AI Document Processing

### The Need for Human-in-the-Loop

LLMs are precise with context, but humans must correct rare errors.

The goal is to make human reviews simple - and focus them on likely mistakes.

Ease of adoption is also key. We must adapt to existing workflows, — and plug DocRouter gradually in the customer process.

Our multi-vertical approach gets many more use cases compared to a vertical approach - but demands flexibility and portable software design.

### How DocRouter.AI Works

Here is an example DocRouter.AI use from one of our pilots with an insurance company:

We process Acord forms for personal/commercial insurance: We extract insured name/address, insurance type, and can extract coverage limits, loss runs, etc.

- Files arrive as email attachments; tools like n8n upload via REST APIs to DocRouter workspace.
- We configure the extraction formats (e.g., insured details) and prompts (descriptions, examples, counter-examples).
- These are stored as JSON schemas 
- We upload representative datasets of documents, and iterate schema & prompt design, as well as vendor-agnostic LLM choice, for best accuracy/cost.
- We monitor accuracy, and tweak prompts (add examples/counter-examples) for edge cases.

Extracted data can be corrected by the human-in-the-loop, and is available via REST APIs for ERP upload (e.g., TMS for insurance, Epic for hospitals).

### The User Perspective: Streamlining Reviews

Before DocRouter, users had to manually enter PDF data into ERP web/UI forms—a laborious process!

DocRouter pre-fills 90%+ fields with LLM extractions and, when configured, with confidence scores from LLM-as-Judge. Users then focus on low-confidence fields, ensuring perfect accuracy with minimal effort.

The human-in-the-loop is critical in regulated fields (healthcare, insurance, fintech, supply chain, legal) where errors in amounts, inventories, or obligations are unacceptable.

### Achieving Accuracy and Flexibility

But direct LLM review is impractical. Users prefer familiar web forms.

We are designing the system so project managers can configure tailored web forms linked to extractions and confidences. For each doc, users review pre-populated forms flagged by confidence metrics.

## Implementing the Web Form Builder: CSS Adventures

Vibe coding couldn't handle this yet—AI tools aren't ready for complex builders.

### FormIO Builder in DocRouter.AI

We integrated FormIO (nice UI npm package). But issues arose:

- FormIO elements didn't display right. Cursor/Claude couldn't fix immediately.
- Root cause: FormIO uses Bootstrap; DocRouter uses Tailwind. Global CSS conflicts.

Added `@tsed/react-formio` (React support) and `@tsed/tailwind-formio` (Bootstrap-Tailwind fix). Forms showed, but Tailwind broke—AI couldn't diagnose.

Expert friends suggested including FormIO components through iframes or a shadow DOM.

- **Shadow DOM:** Claude iterated but drag-and-drop failed across the boundary with the thin DOM (FormIO incompatibility).
- **iframes:** Overkill with API messaging for config/state.

Stuck, I fiddled with CSS via browser inspector. Solution: Redefine Tailwind breakpoints last in global.css order:

```css
// FormIO + Bootstrap
@import 'formiojs/dist/formio.full.min.css';

// Tailwind
@tailwind base; 
@tailwind components;
@tailwind utilities;

// Correction so Bootstrap works in FormIO
@import "~@tsed/tailwind-formio/styles/index.css"; 

// Correction to correction 
// so Tailwind responsiveness works
@import './formio-custom.css'; 
```

## Key Takeaway: AI Tools Are Game-Changers, But Humans Are Essential

The programmer must guide AI—tools are amazing, but tough problems (like CSS conflicts) need human expertise. We're not fully autonomous coding yet, especially for intricate integrations.

If you're building AI-accelerated tools or facing similar challenges, let's connect! What are your experiences with Cursor, Claude Code, or CSS headaches? Share in the comments.
