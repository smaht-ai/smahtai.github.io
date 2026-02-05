---
layout: post
title: "How To Create Document Workflows With Temporal And DocRouter.AI"
date: 2025-12-25 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/temporal_docrouter_workflows.svg
categories: [tech, programming, ai, tutorials]
---

🚀 Just spent the last few days building a powerful multi-step document processing pipeline — and it handles 200+ page medical records like a champ!

Single-prompt tools like DocRouter.AI shine for ~20-25 page docs… but what about massive collated files with labs, facesheets, insurance cards, and multiple patients mixed together? → One prompt = impossible.

**Enter the solution: Temporal + DocRouter.AI in a smart, scalable workflow.**

This post describes a real-world implementation that uses [Temporal](https://temporal.io/) to orchestrate document processing workflows with [DocRouter.AI](http://docrouter.ai), solving the challenge of processing massive medical records through intelligent multi-step orchestration.

The implementation is available at [doc-router-temporal](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025) and processes medical documents containing hundreds of pages, extracting patient names, dates of birth, and medical insurance information.

## The Problem: Massive Medical Records Need Smart Orchestration

Medical records often come as massive collated files containing 200+ pages with:
- Lab results and test reports
- Patient facesheets with demographics
- Insurance cards and coverage details
- Clinical notes and progress reports
- Multiple patients' information mixed together

**The challenge**: These documents are too large to process in a single LLM prompt due to token limits (typically 128K-200K tokens). One prompt = impossible for comprehensive extraction.

**The solution**: A multi-step workflow that intelligently orchestrates the process:

1. **Split**: Break the massive PDF into individual pages
2. **Classify**: Identify each page's type and which patient it belongs to
3. **Group**: Intelligently group pages by patient
4. **Extract**: Process each patient's page bundle for precise, targeted extraction

## Why This Pattern Rocks

This Temporal + DocRouter.AI combination delivers powerful advantages:

✅ **Constant memory usage** — scales effortlessly to 1,000+ pages without running out of resources

✅ **Super general pattern** → classify → group → process per group → works for any document type

✅ **Fully durable & retry-safe** thanks to Temporal's built-in resilience

✅ **Built lightning-fast** in just a couple of days using AI tools

✅ **Parallel processing** — handles multiple patients simultaneously while maintaining order

✅ **Production-ready** with automatic error handling, timeouts, and state management

<div data-excalidraw="/assets/excalidraw/document_processing_solution.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/document_processing_solution.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

## The Smart Workflow in Action

Here's how the Temporal + DocRouter.AI workflow processes massive medical records:

🔹 **Temporal splits** the 200+ page PDF into individual pages

🔹 **Uploads them one by one** to DocRouter.AI for processing

🔹 **DocRouter classifies each page** → identifies patient name + document type (lab results, insurance card, facesheet, etc.)

🔹 **Temporal intelligently groups pages by patient** using fuzzy name matching and DOB correlation

🔹 **Sends each patient's page bundle back to DocRouter.AI** for precise, targeted extraction

🔹 **Temporal aggregates everything** → clean, complete per-patient results

## Technical Implementation

## Why Temporal?

[Temporal](https://temporal.io/) provides durable workflow orchestration that's perfect for this use case. Unlike traditional approaches (queues, background jobs, or simple scripts), Temporal handles:

- **Durable execution**: Resumes from crashes during 200-page processing
- **Parallel processing**: Processes multiple pages simultaneously while maintaining order
- **Error handling**: Automatic retries for API rate limits and network issues
- **State management**: Tracks processed pages and identified patients
- **Long-running workflows**: Handles processes that take minutes to hours

Temporal's architecture is built around two key concepts: **Workflows** (orchestration logic) and **Activities** (actual work). The diagram below illustrates how these components work together:

<div data-excalidraw="/assets/excalidraw/temporal_workflows_activities.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/temporal_workflows_activities.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

## The Workflow Implementation

The implementation uses a hierarchical workflow structure with two main workflows:

1. **Classify and Group PDF Pages** (`ClassifyAndGroupPDFPagesWorkflow`): Chunks the PDF, classifies each page, and groups pages by patient
2. **Extract Insurance Information** (`ClassifyGroupAndExtractInsuranceWorkflow`): Creates patient-specific PDFs and extracts insurance card data

The main workflow (`ClassifyGroupAndExtractInsuranceWorkflow`) orchestrates the entire process:

<div data-excalidraw="/assets/excalidraw/temporal_docrouter_workflow.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/temporal_docrouter_workflow.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

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

## Creating Schemas and Prompts with Claude Agent

Before building the Temporal workflow, we created the extraction schemas and prompts using the **Claude Agent for DocRouter.AI** (an MCP server at [`doc-router/packages/typescript/mcp`](https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/mcp)).

The Claude Agent allows Claude Code to create extraction schemas and prompts. For example, you can prompt: *"Create a schema for extracting patient information from medical record pages"* and it will validate, create, and test the schema automatically.

The diagram below illustrates how DocRouter.AI operations work and how they integrate with Temporal workflows:

<div data-excalidraw="/assets/excalidraw/docrouter_operations.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/docrouter_operations.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

**Key distinction**: DocRouter.AI implements **discrete operations** (single prompt-and-schema processing per document), while Temporal implements the **workflow orchestration** (chunking, grouping, uploading pages for classification, and uploading chunks for extraction).

For this implementation, we created:
- **`medical_page_classifier`**: Classifies pages as labs, facesheets, insurance cards, clinical notes, or other document types
- **`insurance_card`**: Extracts insurance card information from patient pages

## Workflow Implementation

The main workflow (`ClassifyGroupAndExtractInsuranceWorkflow`) orchestrates the entire process. Complete implementation: [`workflows/classify_group_and_extract_insurance.py`](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/workflows/classify_group_and_extract_insurance.py).

### Step 1: Classify and Group Pages

The workflow calls `ClassifyAndGroupPDFPagesWorkflow` to:
1. **Chunk the PDF** into individual pages
2. **Classify each page** using DocRouter.AI
3. **Group pages by patient** using name and DOB matching

The grouping logic ([`activities/group_classification_results.py`](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/activities/group_classification_results.py)) includes name normalization, DOB parsing, and fuzzy matching with Levenshtein distance to handle typos and variations.

### Step 2: Extract Insurance Information

For each patient group, the workflow:
1. **Creates patient-specific PDFs** with only that patient's pages ([`activities/create_and_upload_patient_pdf.py`](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/activities/create_and_upload_patient_pdf.py))
2. **Uploads them to DocRouter.AI** for insurance card extraction
3. **Polls for completion** and retrieves results

To avoid passing large binary data through Temporal, PDFs are read from disk and uploaded directly to DocRouter.AI.

## Creating Temporal Workflows with Cursor

The Temporal workflow was developed in **Cursor** using natural language prompts. Cursor's AI understood the codebase context and Temporal patterns, enabling rapid development without deep workflow expertise.

**Key benefits:**
- Context awareness across multiple files and existing activities
- Automatic Temporal pattern suggestions (activities, workflows, child workflows)
- Natural language refactoring and error handling implementation

**Example development prompts:**

*"Create a workflow that processes each patient's pages into separate PDFs, uploads them with insurance_card tag, waits for completion, then retrieves insurance extraction results."*

*"Add fuzzy name matching to group pages with names differing by up to 2 letters using Levenshtein distance."*

*"Handle edge cases where medical records contain individual patient names vs. multiple patient summaries."*

Cursor handled the complex Temporal implementation, error handling, and performance optimizations, resulting in production-ready code in just a few hours.

## Key Implementation Details

### Design Decisions

- **Avoid large data transfer**: PDFs are read from disk and uploaded directly to DocRouter.AI, not passed through Temporal
- **Parallel processing**: Multiple patients processed concurrently with status polling
- **Error handling**: Retry logic, graceful degradation, and timeout handling
- **State management**: Only document IDs and metadata flow through Temporal to keep history efficient

## Results

The implementation successfully processes massive medical record documents with hundreds of pages, extracting patient names, dates of birth, and medical insurance information. It handles large documents (200+ pages), parallel patient processing, error recovery, and long-running operations.

### Running the Workflow

```bash
# Start the Temporal worker
python worker.py

# In another terminal, run the client
python client_classify_group_and_extract_insurance.py <path_to_pdf>
```

See the [README](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/README.md) and [client script](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/client_classify_group_and_extract_insurance.py) for details.

The workflow returns JSON with file name, page classifications, schedule pages, and patient data with insurance information.

## We're in a New Era

**What used to take months of engineering can now be shipped in days.**

This Temporal + DocRouter.AI pipeline was built end-to-end using Claude Code-based Agent (for prompts + schemas) + Cursor (for Temporal workflows). I barely knew Temporal before starting — didn't matter. AI tools let me iterate fast, prototype, and perfect the logic in record time.

The result: reliable, scalable document processing with durable workflows, parallel processing, and rapid schema iteration. The implementation took just 2 days to build and handles 200+ page medical records like a champ.

If you're building AI-powered document workflows (especially in healthcare), this combo is 🔥.

Code available at [doc-router-temporal](https://github.com/analytiq-hub/doc-router-temporal/tree/blog_post_dec_2025).

- [Temporal Documentation](https://docs.temporal.io/)
- [DocRouter.AI Documentation](https://docrouter.ai/docs/quick-start)
- [DocRouter.AI MCP Server](https://docrouter.ai/docs/mcp)
