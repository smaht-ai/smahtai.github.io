---
layout: page
title: Talks
permalink: /talks/
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <!-- Header -->
    <header class="mb-12 pb-8 border-b border-gray-200">
        <p class="text-gray-600 text-xl leading-relaxed">
            Speaking engagements and public presentations
        </p>
    </header>

    <main>
        <!-- Talks Container -->
        <div class="space-y-8" id="talks-container">
            {% include talk-card.html 
                title="Building Scalable AI Applications"
                speaker="Speaker Name"
                date="November 15, 2025"
                event="Tech Conference 2025"
                image="/assets/images/talks/building-scalable-ai-applications.svg"
                abstract="An exploration of architectural patterns and best practices for building AI applications that scale from prototype to production. Topics covered include model serving, caching strategies, monitoring, and cost optimization."
                links="https://example.com/slides;Slides|https://example.com/recording;Recording"
            %}

            {% include talk-card.html 
                title="Modern API Design Patterns"
                speaker="Speaker Name"
                date="October 8, 2025"
                event="Developer Meetup"
                image="/assets/images/talks/modern-api-design-patterns.svg"
                abstract="A deep dive into RESTful API design, GraphQL, and modern authentication patterns. Learn how to build developer-friendly APIs that are secure, performant, and easy to maintain."
                links="https://example.com/event;Event Details|https://example.com/slides;Slides"
            %}

            {% include talk-card.html 
                title="Building in Public: Lessons Learned"
                speaker="Speaker Name"
                date="September 20, 2025"
                event="Startup Conference"
                image="/assets/images/talks/building-in-public.svg"
                abstract="Share your journey, engage with your audience, and grow your business by building in public. This talk covers practical strategies for transparency, community building, and turning followers into customers."
                links="https://example.com/recording;Recording|https://example.com/linkedin;LinkedIn Post"
            %}
        </div>
    </main>
</div>
