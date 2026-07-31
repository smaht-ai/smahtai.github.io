---
layout: default
title: "Talks"
permalink: /talks/
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="mb-12 pb-8 border-b border-gray-200">
        <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3">Talks</h1>
        <p class="text-gray-600 text-xl leading-relaxed">
            Speaking engagements and public presentations from Smaht.ai members
        </p>
    </header>

    <main>
        <div class="space-y-8" id="talks-container">
            {% include talk-card.html
                title="DocRouter Flows: Visual Workflow Automation for Intelligent Document Processing"
                speaker="Andrei Radulescu-Banu"
                date="Jul 30, 2026"
                event="Anote AI"
                event_url="https://anote.ai/"
                logos="/assets/images/anote_logo.png"
                image="/assets/images/docrouter-flows-splash.png"
                links="https://www.youtube.com/watch?v=n9UUKHSgScU;Recording|https://www.linkedin.com/feed/update/urn:li:activity:7488415996815441920/;LinkedIn Post|/ai/engineering/docrouter-flows-visual-workflow-automation-for-intelligent-document-processing/;Blog Post"
                abstract="Most document AI tools give you one-step LLM processing. The second a customer needs branching, agents, or human-in-the-loop, you need more. DocRouter Flows is a visual, document-native workflow system with first-class OCR/LLM nodes, sandboxed Python, and durable execution via node-level checkpoints—no Temporal cluster required. Lightweight to run, and in production at scale."
            %}

            {% include talk-card.html
                title="How AI Agent Memory Works"
                speaker="Andrei Radulescu-Banu"
                date="Jul 23, 2026"
                event="AI Camp"
                event_url="https://www.aicamp.ai/event/eventdetails/W2026072314"
                logos="/assets/images/ai-camp.png"
                image="/assets/images/mem0-integration-splash.png"
                links="https://www.aicamp.ai/event/eventdetails/W2026072314;Event Details|https://www.linkedin.com/feed/update/urn:li:activity:7486257884524363777/;LinkedIn Post|/ai/engineering/agents/rag/how-mem0-works-and-how-we-integrated-it/;Blog Post"
                abstract="How to design AI agent memory and how it behaves in production: extracting memory facts from the incoming prompt, deduplicating and reconciling them with existing entries in AWS Aurora pgvector, injecting prior facts into LLM context, and scalability/optimization strategies for selecting only the most relevant facts. Covered implementation with Mem0 and custom save &amp; retrieve LLM prompts—now a standard capability across ChatGPT, Claude, Grok, and Gemini."
            %}

            {% include talk-card.html
                title="How To Embed an AI Copilot in Your Application"
                speaker="Andrei Radulescu-Banu"
                date="Mar 11, 2026"
                event="AI Camp"
                event_url="https://www.aicamp.ai/event/eventdetails/W2026031215"
                logos="/assets/images/ai-camp.png"
                image="/assets/images/how_to_embed_an_ai_agent_into_your_application.png"
                links="https://www.aicamp.ai/event/eventdetails/W2026031215;Event Details|https://www.linkedin.com/feed/update/urn:li:activity:7438324189578588160/;LinkedIn Post|/ai/programming/engineering/product/how-we-built-the-document-agent/;Blog Post"
                abstract="How we embedded an AI copilot into DocRouter as a tool-calling Document Agent: the agent loop, tool approval UX, context injection, and the backend patterns that make agents reliable in production."
            %}

            {% include talk-card.html
                title="The 'One Codebase, Many Products' Playbook"
                speaker="Andrei Radulescu-Banu"
                date="Dec 11, 2025"
                event="AI Camp"
                event_url="https://www.aicamp.ai/event/eventdetails/W2025121015"
                logos="/assets/images/ai-camp.png"
                image="/assets/images/talk-one-codebase.png"
                links="https://www.aicamp.ai/event/eventdetails/W2025121015;Event Details|https://docs.google.com/presentation/d/1WdNXNv6BRgBLsRHzxYlesLZewE-cCmvkBtzfGvXGkGI/edit?slide=id.g3aea72bb1c1_0_0#slide=id.g3aea72bb1c1_0_0;Slides|https://www.linkedin.com/feed/update/urn:li:activity:7405411102974451712/;LinkedIn Post|/ai/webdev/programming/one-codebase-many-products-playbook/;Blog Post"
                abstract="Shared our journey with The 'One Codebase, Many Products' Playbook at AnalytiqHub.com, turning one framework into a powerhouse for AI products. From building DocRouter.AI in 3 months to launching SigAgent.AI in 3 weeks, and customized AI portals for clients – it's all about slashing dev time with 90%+ reuse. Core Playbook Steps: Build Shared Foundations (React UI, FastAPI backend, MongoDB storage, and Claude Agent for workflows), Integrate Smartly (LiteLLM for LLMs and Stripe for seamless billing), and Scale with Ease (open-core for community, closed forks for clients)."
            %}

            {% include talk-card.html
                title="SigAgent.AI - Tracing Claude Agents"
                speaker="Andrei Radulescu-Banu"
                date="Nov 17, 2025"
                event="AI Tinkerers"
                event_url="https://boston.aitinkerers.org/"
                logos="/assets/images/aitinkerers-1.png"
                image="/assets/images/sigagent_ai_tinkerers_talk.png"
                links="https://boston.aitinkerers.org/p/ai-tinkerers-boston-meetup-november-2025;Event Details|https://docs.google.com/presentation/d/1Lakbp-TgHqwUkISHb3TLrk-uMCMDem26Mm-Mr0rtEsU/edit?slide=id.g1efc3f84a80_0_21#slide=id.g1efc3f84a80_0_21;Slides|https://www.linkedin.com/feed/update/urn:li:activity:7395834753372876800/;LinkedIn Post"
                abstract="AI agents have become powerful and reliable, but you need to build them right. With 50% of new agents now built with Claude Code, the ecosystem has opened up for integration with MCP, marketplaces, plugins, and SKILLS.md. What's missing? AI Agent Evaluation for debugging during development, and for guardrails and monetization during deployment. SigAgent.AI specializes in tracing Claude agents using Open Telemetry and step-by-step, hook-level monitoring. We covered how to build Claude Agents with SigAgent.AI traceability, what works and what doesn't with MCP tools, CLAUDE.md, SKILLS.md and MCP-as-code, and how to stand up agent infrastructure for value-based and usage-based pricing."
            %}

            {% include talk-card.html
                title="How To Integrate Stripe Into Your AI Application"
                speaker="Andrei Radulescu-Banu"
                date="Oct 24, 2025"
                event="AI Tinkerers"
                event_url="https://boston.aitinkerers.org/"
                logos="/assets/images/aitinkerers-1.png"
                image="/assets/images/how_to_integrate_stripe.png"
                links="https://boston.aitinkerers.org/p/ai-tinkerers-boston-meetup-october-2025;Event Details|https://www.linkedin.com/feed/update/urn:li:activity:7387836092588240896/;LinkedIn Post|/tech/programming/ai/tutorials/how-we-integrated-stripe-into-docrouter-ai/;Blog Post"
                abstract="How did we built Stripe billing into DocRouter.AI? The talk covered why Stripe was the right choice for scaling metered AI usage, our SPU (Service Processing Units) credit system inspired by Databricks DBUs, free tier → plans → a-la-carte credits with consumption waterfall, dynamic pricing config 100% in Stripe metadata, async Stripe API calls in FastAPI, and our MongoDB backend schema."
            %}

            {% include talk-card.html
                title="How To Train Your AI Agent"
                speaker="Andrei Radulescu-Banu"
                date="Oct 15, 2025"
                event="AI Camp"
                event_url="https://www.aicamp.ai/event/eventdetails/W2025101515"
                logos="/assets/images/ai-camp.png"
                image="/assets/images/how_to_train_your_ai_agent.png"
                links="https://www.aicamp.ai/event/eventdetails/W2025101515;Event Details|https://docs.google.com/presentation/d/1GFcD4bruJBJPFeJkPp_K-MfkU8ZrHtgfrV7WoLumKd4;Slides|https://www.linkedin.com/feed/update/urn:li:activity:7384733807968526337/;LinkedIn Post"
                abstract="What are the steps to create an AI Agent? Our AI Camp talk is a deep-dive into how AI Agents are implemented, in practice. With lessons learned from our DocRouter.AI coding agent, and our consulting engagement implementing a coding agent for lab information management systems company Starlims."
            %}

            {% include talk-card.html
                title="Engineering with Guardrails: Innovating in Regulated Spaces"
                speaker="Ilsa Webeck, Andrei Radulescu-Banu, Marjan Monfared"
                date="September 9, 2025"
                event="Startup Boston Week 2025"
                event_url="https://sbw2025.sched.com/event/264KN/engineering-with-guardrails-innovating-in-regulated-spaces"
                logos="/assets/images/startup_boston_week.png"
                image="/assets/images/engineering_with_guardrails.png"
                links="https://sbw2025.sched.com/event/264KN/engineering-with-guardrails-innovating-in-regulated-spaces;Event Details|https://streamyard.com/watch/GWAw3FHAfUZy;Recording|https://www.linkedin.com/feed/update/urn:li:activity:7371516401406124032/;LinkedIn Post|/ai/programming/tech/reviews/engineering-with-guardrails-innovating-in-regulated-spaces/;Blog Post"
                abstract="Building fast doesn’t mean ignoring the rules—especially in healthcare, fintech, AI, or consumer hardware. Our panel explores how to embed compliance into the development process without slowing innovation - for CTOs, technical founders, and engineering leaders operating in regulated industries. Moderated by Rabeeh Majidi."
            %}

            {% include talk-card.html
                title="GradeAssist AI: A School Quiz Grader"
                speaker="Andrei Radulescu-Banu"
                date="May 21, 2025"
                event="AI Tinkerers"
                event_url="https://boston.aitinkerers.org/talks/rsvp_9vvWQ2XeaSc"
                logos="/assets/images/aitinkerers-1.png"
                image="/assets/images/talk-gradeassist.jpg"
                abstract="GradeAssist is a new tool for teachers, using AI to grade open-form school quizzes, with teacher-in-the-loop – using <a href='https://www.linkedin.com/company/docrouter/' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>DocRouter</a> as an AI middleware, with a new front-end UI generated by Bolt AI."
                links="https://boston.aitinkerers.org/talks/rsvp_9vvWQ2XeaSc;Event Details|https://www.linkedin.com/feed/update/urn:li:activity:7331067862704402432/;LinkedIn Post"
            %}

            {% include talk-card.html
                title="An AI Backbone for Document Processing"
                speaker="Andrei Radulescu-Banu"
                date="May 9, 2025"
                event="Mindstone Boston"
                logos="/assets/images/mindstonehq_logo.jpg"
                image="/assets/images/talk-ai-backbone-doc-processing.jpg"
                abstract="At the <a href='https://www.linkedin.com/company/sundaiclub/' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>Sundai</a> MIT hackathon, we recently develop a flow that grades 5th grade quizzes against a configured rubric. <a href='https://docrouter.ai' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>DocRouter.AI</a> implements the back end, with the teacher-in-the-loop able to correct the evaluations. We reviewed this hack!<br><br>A front-end UI specialized for this use case can be quickly developed with tools like Manus, Bolt AI, Cursor, Windsurf. The DocRouter is the a tech stack accelerator, just managing prompts and evaluations, with human-in-the loop, hiding the complexity of LLM workflows."
                links="https://community.mindstone.com/annotate/article_AuDOhLA5awWaoXV98L;Recording with Transcript|https://docs.google.com/presentation/d/18SrBsdJrV9LC6-wlRLZ9p8COGKyhjB-JrmVr4bHZ6zk/edit#slide=id.g31c1d6a1bb0_3_0;Presentation Slides"
            %}

            {% include talk-card.html
                title="AI Document Workflows"
                speaker="Andrei Radulescu-Banu"
                date="April 28, 2025"
                event="AI Tinkerers & CarGURUS"
                logos="/assets/images/aitinkerers-1.png,/assets/images/cargurus.png"
                image="/assets/images/talk-ai-workflows.jpg"
                abstract="<a href='https://docrouter.ai/' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>DocRouter.AI</a> is a drag-and-drop UI that transforms unstructured docs into ERP data – integrated with MCP clients like Claude Desktop – building web dashboards, dynamically – for example, allowing consulting companies to optimize internal engineering resources allocated to contracted projects."
                links="https://www.linkedin.com/feed/update/urn:li:activity:7323312770257481728/;LinkedIn Post"
            %}

            {% include talk-card.html
                title="Smart Document Router"
                speaker="Andrei Radulescu-Banu"
                date="February 26, 2025"
                event="PyData Boston & MODERNA"
                logos="/assets/images/Screenshot-From-2025-02-27-08-17-51-300x225.png,/assets/images/moderna.png"
                image="/assets/images/talk-docrouter-pydata-moderna.jpg"
                abstract="The <a href='https://docrouter.ai/' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>DocRouter.AI</a> is an <a href='https://docs.google.com/presentation/d/14nAjSmZA1WGViqSk5IZuzggSuJZQPYrwTGsPjO6FPfU' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>open source</a> Document Understanding Tool. It performs data extraction, at scale, for intelligent automation in a number of verticals: Supply Chain, Healthcare, Finance.<br><br>It is implemented using:<br>– NextJS, NextAuth, TailwindCSS<br>– FastAPI, Pydantic<br>– AWS, MongoDB<br>– LiteLLM<br>– OpenAI, Anthropic, Gemini, Groq/DeepSeek<br><br>To Andrei's surprise, the <a href='https://www.cursor.com/' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>Cursor</a> AI editor wrote most of the <a href='https://docrouter.ai/' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>DocRouter.AI</a> code! We discussed how <a href='https://docrouter.ai/' target='_blank' rel='noopener noreferrer' class='text-blue-600 hover:text-blue-800'>DocRouter.AI</a> was coded."
                links="https://www.youtube.com/watch?v=dVro-Z6SDxU;Recording|https://docs.google.com/presentation/d/14nAjSmZA1WGViqSk5IZuzggSuJZQPYrwTGsPjO6FPfU;PyData Smart Document Router Presentation|https://www.linkedin.com/posts/benjamin-batorsky_pydata-bostons-february-event-another-smashing-activity-7300998869515935745-4nJ9;LinkedIn Post"
            %}

            {% include talk-card.html
                title="Coding With AI"
                speaker="Andrei Radulescu-Banu"
                date="October 30, 2024"
                event="AI CAMP & VERACODE"
                event_url="https://www.aicamp.ai/event/eventdetails/W2024092514"
                logos="/assets/images/ai-camp.png,/assets/images/veracode.png"
                image="/assets/images/talk-coding-ai-camp.png"
                abstract="A practical look at writing software with AI tools: Scripting Claude.AI, Using the Cline VsCode add-on (open source), Using Cursor"
                links="https://www.youtube.com/watch?v=r9Q18X-Ko4Q;Watch Recording|https://docs.google.com/presentation/d/1_Urn3qlczQ9DtF3bDyGUl1_B0q7-Kwe37m5cpR53oOU/edit#slide=id.g1efc3f84a80_0_21;Coding With AI Slides"
            %}

            {% include talk-card.html
                title="AI Human-in-the-Loop Panel"
                speaker="Andrei Radulescu-Banu, Dipali Trivedi, Brian Benedict"
                date="September 24, 2024"
                event="AI Furnace & Aethos"
                image="/assets/images/talk-human-loop.png"
                abstract="Panel discussion on how human-in-the-loop is implemented in practice, when used during LLM development vs in end products, LLM model evaluation, and the importance of humans understanding AI-generated code. Moderated by Nico van Wijk."
                links="https://www.linkedin.com/feed/update/urn:li:activity:7244538705946771456/;Andrei's Blog Post"
            %}

            {% include talk-card.html
                title="LLM Orchestration At Scale"
                speaker="Andrei Radulescu-Banu"
                date="July 26, 2024"
                event="AI Camp"
                event_url="https://www.aicamp.ai/event/eventdetails/W2024072614"
                logos="/assets/images/ai-camp.png"
                image="/assets/images/talk-llm-orchestration-ai-camp.png"
                abstract="Why do we need to orchestrate Large Language Models (LLMs)? We will talk about Perplexity.AI's approach, shared openly in their podcasts – and at enterprise workflow automation with unstructured data at scale."
                links="https://www.aicamp.ai/event/eventdetails/W2024072614;Event Details"
            %}

            {% include talk-card.html
                title="How To Build A Self-Driving Car – A Look at Robotics System Design"
                speaker="Andrei Radulescu-Banu"
                date="February 21, 2024"
                event="AI Camp"
                event_url="https://www.aicamp.ai/event/eventdetails/W2024022114"
                logos="/assets/images/ai-camp.png"
                image="/assets/images/talk-self-driving.png"
                abstract="Sensors, control, planner, perception, mapping – how is a self-driving car built? An introduction for general engineering audiences, zeroing in on the integration of ROS (Robot Operating System) and system design principles in constructing autonomous vehicles."
                links="https://docs.google.com/presentation/d/1zl9OxqveTH6ASSh2oFmGDQUA-CwMWr-D6tjHNFMAnvs;How to Make a Self-Driving Car|https://www.aicamp.ai/event/eventdetails/W2024022114;Event Details|/ai/programming/tech/reviews/how-to-make-a-self-driving-car/;Blog Post"
            %}

            {% include talk-card.html
                title="Using LLMs and NLP for Digital Health Automation"
                speaker="Andrei Radulescu-Banu"
                date="January 31, 2024"
                event="AI Camp"
                event_url="https://www.aicamp.ai/event/eventdetails/W2024013114"
                logos="/assets/images/ai-camp.png"
                image="/assets/images/talk-digital-health-ai-camp.png"
                abstract="Review of Large Language Models (LLMs) and Natural Language Processing (NLP) applications for business process automation in digital health: Nurse doing pre-op patient screening; and Insurance Claims Processing Automation"
                links="https://www.aicamp.ai/event/eventdetails/W2024013114;Event Details"
            %}
        </div>
    </main>
</div>
