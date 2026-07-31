---
layout: post
title: "How To Train Your AI Agent"
date: 2025-10-02
author: Andrei Radulescu-Banu
image: /assets/images/how_to_train_your_ai_agent.png
categories: [ai, programming, tutorials]
description: "A six-step framework for building AI agents: tools, knowledge bases, planning, evaluation, and MCP Server integration — with Claude Code and Cursor examples."
---

Developing an AI agent comes down to a number of intertwined yet distinct challenges:
1. Create the __runtime infrastructure__ for the agent itself
2. Add __tools__ for the task
3. __Planning__: Making agent tackle the __specific problem__ you're aiming to solve
4. Create a [__knowledge base__](/docs/knowledge-bases/) the agent can use to inform its execution steps
5. Set up an __evaluation infrastructure__ to track progress and catch agent mistakes
6. __Integrate__ the agent into the larger application

Whether the AI agent is __fully autonomous__ or works with __human-in-the-loop__ oversight, development includes roughly the steps outlined above. Each step calls for its own set of techniques and tools.

![Steps To Develop An AI Agent](/assets/images/ai_agent_steps_to_develop.png)

## Examples: Windsurf, Cursor and Claude Code

Let's start with some examples the reader may be familiar with: 
* AI Editors like [__Windsurf__](https://windsurf.com/), [__Cursor__](https://cursor.com/), [__Github Copilot__](https://github.com/features/copilot)
* Command line tools like [__Claude Code__](https://www.claude.com/product/claude-code). 

The latter, __Claude Code__, also has a [__VSCode__ extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) by the same name.

In each case, the underlying AI agents are integrated with the text editor (our __Step 6__). 

While __Windsurf__, __Cursor__ and __Claude Code__ each have their own agent infrastructure (our __Step 1__), the latter, __Claude Code__ is different in that it is available as a [__command line tool__](https://docs.claude.com/en/docs/claude-code/quickstart) which can be executed standalone, in [interactive](https://docs.claude.com/en/docs/claude-code/interactive-mode) or [non-interactive mode](https://docs.claude.com/en/docs/claude-code/cli-reference?utm_source=chatgpt.com). 

__Anthropic__ has also developed a [__Claude Agent SDK__](https://docs.claude.com/en/api/client-sdks), with __Typescript__, __Python__ and __shell command__ flavors. The __Claude Agent SDK__ can be used both for coding tasks and for more general tasks - for example, for document processing, or for support message processing, or for marketing research and outreach.

An Agent SDK is not available for __Windsurf__ or __Claude Code__.

The __knowledge base__ (__Step 3__) for these agents is embedded into the language models themselves. These coding agents can code in __Python__, __Typescript__, __C__, __C++__ or __Java__. The language models are trained on these programming languages. 

While these agents do not technically require an external __knowledge base__ for pure coding skills, they use a __web search__ tool to look up product and API documentation. The web search tool comes handy when implementing __coding tasks__ against specific coding libraries and APIs.

 __Windsurf__, __Cursor__, __Github Copilot__ use multiple-vendor language models, in addition to models used in-house. __Claude Code__ on the other hand, only uses __Anthropic__ language models.

Custom AI Agents, though, don't have all necessary knowledge baked into their LLM model - and often need an __external knowledge base__, adapted to their task (__Step 3__).

For example - one of our customer companies develops a lab information management system that uses a scripting language to define web forms. The forms are used to manage lab processes in Biotech, Food Manufacturing, or Forensics. The AI Agent we developed employs an __external knowledge base__  to provide full documentation and examples for the scripting language. The generalist LLMs, while trained on __Python__, __Typescript__ and other programming languages, would not have baked-in information about the custom scripting language for web forms.

Custom AI agents need to implement their own __external knowledge base__ and __problem-solving tools__. These are both integrated into the Agent using an [__MCP Server__](/docs/mcp/).

![Extending Claude Code](/assets/images/ai_agent_extending_claude_code.png)

 __MCP__ support is already available in all AI Editors. The editors can act as __MCP Clients__, and can, for example, read external Github repositories through a __Github MCP Server__. Any MCP Server is supported.

An __MCP Server__, thus, can be used to make your AI agent __act__ on your __specific tasks__, and to access your __external knowledge base__.

But having the __tools__ and the __knowledge base__ is not sufficient. The agent must also be steered through __task planning__ (our __Step 4__).

The approach each of the AI editors takes to __steer__ their __coding task__ is proprietary, and slightly different. A lot of the steering is done through proprietary system prompts. Some have [reverse engineered these system prompts](https://beyondthehype.dev/p/inside-claude-code-prompt-engineering-masterpiece) through intercepting API calls - but, for the most part, they remain hidden.

Each AI editor, however, supports extending the system prompt through a configuration file: __CLAUDE.md__ for Claude Code, __Cursor Rules__ for Cursor,__Windsurf Rules__ for Windsurf. It is these configuration files - CLAUDE.md in particular - that will be used to __steer our Custom AI Agent__.

Windsurf, Cursor, Github Copilot also use a __tab-completion model__, which employs a smaller, faster LLM acting directly in the editor buffer. Claude Code does not have that feature. 

Evaluation for these AI editors is also proprietary (__Step 5__). Custom AI Agents would need their own evaluation infrastructure developed from scratch.

Here is a Comparison Table for the AI editors we described: 

<table style="width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 14px;">
  <thead>
    <tr style="background: #1e40af !important; color: white !important;">
      <th style="padding: 12px 16px; text-align: white; font-weight: 600; background: #1e40af !important; color: white !important;">Step</th>
      <th style="padding: 12px 16px; text-align: left; font-weight: 600; background: #1e40af !important; color: white !important;">Windsurf, Cursor, Github Copilot</th>
      <th style="padding: 12px 16px; text-align: left; font-weight: 600; background: #1e40af !important; color: white !important;">Claude Code</th>
      <th style="padding: 12px 16px; text-align: left; font-weight: 600; background: #1e40af !important; color: white !important;">Custom Agent</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #fef3c7;">
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; font-weight: 600; color: #92400e;">1. Runtime Infrastructure</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Proprietary, integrated with text editors</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Proprietary, available as command-line tool + VSCode extension</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Claude Code + Claude Agent SDK (TypeScript/Python/Shell)</td>
    </tr>
    <tr style="background: #dbeafe;">
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; font-weight: 600; color: #1e40af;">2. Task Planning</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Proprietary system prompt. Windsurf Rules file for Windsurf. Cursor Rules file for Cursor</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Proprietary system prompt. CLAUDE.md for custom planning.</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Custom via CLAUDE.md + editable system prompts (Claude Agent SDK)</td>
    </tr>
    <tr style="background: #f3e8ff;">
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; font-weight: 600; color: #7c3aed;">3. Knowledge Base</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Embedded in LLM training + web search for API docs. Extensible through MCP.</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Embedded in LLM training + web search for API docs. Extensible through MCP.</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">External vector DB (Pinecone/Weaviate/Qdrant) + custom MCP server tools</td>
    </tr>
    <tr style="background: #fecaca;">
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; font-weight: 600; color: #dc2626;">4. Evaluation Infrastructure</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Proprietary, internal evaluation systems</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Proprietary, internal evaluation systems</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #d1d5db; color: #374151;">Custom evaluation scripts + LLM Judge + web visualization dashboard</td>
    </tr>
    <tr style="background: #d1fae5;">
      <td style="padding: 12px 16px; font-weight: 600; color: #059669;">5. Integration</td>
      <td style="padding: 12px 16px; color: #374151;">Native text editor integration</td>
      <td style="padding: 12px 16px; color: #374151;">Command-line + VSCode extension</td>
      <td style="padding: 12px 16px; color: #374151;">Custom VSCode extension</td>
    </tr>
  </tbody>
</table>

## Separation of concerns: Infrastructure vs. Task-Specific Planning

When it comes to building the agent, we separate out the __Infrastructure__ design from the __Task Planning__, for a couple of reasons:
- Often times, the __task__ solved by the agent needs to be flexible and can change in the product lifecycle. This calls for __infrastructure__ to be separated out from the __task customization__. Sometimes, the __task__ or its __subtasks__ are not even fully known or understood at the outset of the AI Agent project.
- The __infrastructure__ is now available ready-made, and may not have to be built from scratch.

Adopting a ready-made, battle tested __AI Agent Infrastructure__ that is __steerable__ for your task will accelerate your AI Agent design.

![Claude Code Online System Architecture](/assets/images/ai_agent_online_system.png)

## The AI Agent Infrastructure

As of this writing, our go-to stack for agent creation is the [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) shell command, complemented by the [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk). Its advantages:
- A suite of powerful features like [__CLAUDE.md__](https://docs.claude.com/en/docs/claude-code/memory#claude-md-imports) customization, __subcommands__ for modular execution, __subagents__ for hierarchical delegation
- [__MCP server support__](https://docs.claude.com/en/docs/mcp), which lets you seamlessly extend the agent, and steer it to solve the __task__ at hand.
- Built-in [__prompt caching__](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#how-prompt-caching-works), and discounted packaged price for utilization, when using a Claude subscription.

No agent is complete without a solid __knowledge base__, and without good __evaluation infrastructure__.

The Claude Agent SDK doesn't ship with either out of the box. You'll need to craft them yourself. 

For the vector database powering the __knowledge base__, we've used [__Pinecone__](https://www.pinecone.io/), prized for its straightforward SaaS model that gets you up and running quick. Pinecone [documentation](https://docs.pinecone.io/guides/get-started/overview) is also very accessible.

That said, there are multiple Vector DB alternatives: __Weaviate__, __Qdrant__, or __ChromaDB__. Even traditional players like __Postgres__ or __MongoDB__ have jumped on the vector bandwagon, now offering built-in support for vector tables or collections.

In our architecture, we __centralize all custom interfaces__ for the agent within the __MCP server__. This ensures portability and testability across setups. The __MCP server__ includes a `vector_db_lookup()` interface to let the agent look up the __knowledge base__.

## Indexing Your Knowledge Base

To build the knowledge base, you need:
- A collection of knowledge base files - we usually convert them all to __Markdown__, and store them in an __S3__ bucket, or in a __MongoDB collection__
- A __vector DB index__ in your DB of choice
- An __indexing script__, that runs periodically, and uploads the knowledge base markdown files into the vector DB index, mapped through an __LLM embedding__.

<img src="/assets/images/indexing_flow.png" alt="Knowledge Base Indexing Flow" style="width: 100%; height: auto;">

The lookup operation is what you'd expect - the searched text is mapped through the same __LLM embedding__, and looked up for __similarity__ with existing chunks in the vector db index - returning the most closely similar chunks from the __knowledge base__.

## Tuning AI Agent Actions via the MCP Server

With the knowledge base available, and searchable - we now let the AI agent use it through __MCP Server__ tools.

These tools can:
- Look up knowledge base articles for similarity
- Perform file reads and edits that are specialised to your file format
- Validate file edits, and run unit tests

The tools take parameters, and are self-describing. The LLM model can figure out, to a good extent, which tools to call, and which parameters to pass - however, that is not sufficient for good agent design, because:
- The same operation may be solved by different tools.
- Or, the tools need to be called in a certain order.

This is why step is crucial: __Task Planning__, which steers the agent in how it uses the __MCP Server__ tools.

## Task Planning

Task planning is designed partly through editing __CLAUDE.md__, and partly through changing the system prompt. 
- With the command-line __Claude Code__ tool, its internal system prompt is not editable.
- But with __Claude Agent SDK__, it is.

In __CLAUDE.md__, we specify how to approach the various custom problems the agent might encounter. __Claude Code__ has built-in support for the __ToDoWrite__ tool. In __CLAUDE.md__, we specify what are the __ToDo__ tasks, for each problem the AI Agent might encounter.

## The Claude Code Event Loop

The __Claude Code__ agent itself has a baked-in [event loop](https://blog.promptlayer.com/claude-code-behind-the-scenes-of-the-master-agent-loop/?utm_source=chatgpt.com), which takes user input, file attachments and screenshots - puts __CLAUDE.md__ in context, determines its __ToDo__ tasks, and iterates through __MCP Server__ tools and other built-in tools to solve the task.

The user can interrupt the flow at any moment, and continue it with altered instructions.

From there, the agent marches forward, step by step. It can go solo or pause for human nods, calling on more __MCP__ and __built-in tools__ as needed to create new files, edit existing ones, or query the knowledge base. 

<img src="/assets/images/ai_agent_event_loop.png" alt="Claude Code Event Loop" style="width: 100%; height: auto;">

## Tuning the Agent through Evaluation

Once the __infrastructure__ is stood up, the __knowledge base__ available, the __MCP server__ working, and the agent begins to be integrated in the larger application - you need to __tune__ the agent and __adapt__ it to the task at hand.

__Tuning__ can mean:
- Adding or updating to the __knowledge base__
- Adding or updating the __MCP server tools__
- Improving the __CLAUDE.md__ design, to steer the running agent through its __ToDo__s.

__Evaluation__ is an essential step here. 

<img src="/assets/images/ai_agent_offline_evaluation.png" alt="Claude Code Offline System Architecture" style="width: 80%; height: auto;">

Kick things off by:
- Assembling a __ground-truth dataset__ — a curated set of benchmark problems mirroring real-world scenarios. 
- Create an __evaluation script__ that, for each item, spins up a fresh __Claude Code__ instance to tackle the problem in pure automated mode, assuming no user intervention. 
- Once the ___Claude Code__ instance completes processing a __dataset item__, a second forked instance of __Claude Code__ runs to evaluate and judge the output, for a number of metrics, as __LLM Judge__.

The metrics tracked by the __LLM Judge__ are:
- __Accuracy:__ How spot-on are the results?
- __Completeness:__ Does it cover all requirements without omissions?
- For MCP interfaces leaning on vector DB retrieval: __Accuracy__ and __completeness__ of the chunks pulled back.
- Completion rate of the __ToDo__'s
- Drilling deeper, for select MCP tools: __Per-tool breakdowns__ of response __accuracy__ and __completeness__.
- __Number of failed validations__ during the actual run
- __Validation tests__ run by the LLM judge at eval time, using the same MCP validation tools you added
- Other statistics: __number of steps__ to solve the question,  __LLM models__ used, __in__ and __out__ tokens, __cached__ tokens, __cost__

## Bringing Eval to Life: Visualization

Raw eval logs are hard to monitor without an __at-a-glance view__. 

In our approach, we build a custom web visualiser of eval results, with:
- A quick-scan table, one row per question, for instant overviews.
- A radar chart aggregating metrics into a visual story of strengths and gaps.
- Distributions to reveal patterns across the board.
- Per-question deep dives on tool usage: At-a-glance summaries of which tools fired, what inputs they took, the outputs they spat, and any ToDo progress where relevant.

## Iteration and Improvement

Here's how the development loop flows in practice:
- Bootstrap your ground-truth dataset with questions to get baseline momentum.
- Start the evaluation suite and scrutinize the metrics
- For each metrics shortfall, triage the root cause: 
  - Does the __knowledge base__ require new or updated data? 
  - Is the problem caused by Vector DB __chunking__, __indexing__, or __retrieval__?
  - Is an __MCP tool__ not working properly? Or is a new __MCP tool__ needed?
  - Or perhaps __CLAUDE.md__ itself needs a refresh to better guide the agent?

As problems are discovered, and fixed, the ground truth dataset is expanded. Re-running over previously-working dataset items ensures the new fixes don't break old functionality.