---
layout: default
title: "Events"
permalink: /events/
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
  <header class="mb-12 pb-8 border-b border-gray-200">
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3">Events</h1>
    <p class="text-gray-600 text-xl leading-relaxed">
      In the Greater Boston area
    </p>
  </header>

  <main class="space-y-16">
    <!-- Smaht events -->
    <section aria-labelledby="smaht-events-heading" class="border-b border-gray-200 pb-8">
      <h2 id="smaht-events-heading" class="text-2xl font-bold text-gray-900 mb-1">
        Smaht.ai events
      </h2>
      <p class="text-gray-600">
        Coming soon —
        <a href="{{ site.apply_url }}" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-800 font-medium">apply to join</a>
        for Slack updates, or browse
        <a href="{{ '/talks/' | relative_url }}" class="text-blue-600 hover:text-blue-800 font-medium">member talks</a>.
      </p>
    </section>

    <!-- Greater Boston -->
    <section aria-labelledby="boston-events-heading">
      <h2 id="boston-events-heading" class="text-2xl md:text-3xl font-bold text-gray-900 mb-3">
        Greater Boston events
      </h2>
      <p class="text-gray-600 mb-6 max-w-2xl">
        We recommend the following calendars as having pretty good coverage of what’s happening locally:
      </p>
      <ul class="space-y-3 text-gray-800">
        <li>
          <a href="{{ site.event_calendars.startup_boston }}"
             target="_blank"
             rel="noopener noreferrer"
             class="text-blue-600 hover:text-blue-800 font-medium">
            Startup Boston
          </a>
          <span class="text-gray-600"> — startup events, grants, pitches, and deadlines across New England</span>
        </li>
        <li>
          <a href="{{ site.event_calendars.aicamp_boston }}"
             target="_blank"
             rel="noopener noreferrer"
             class="text-blue-600 hover:text-blue-800 font-medium">
            AI Camp Boston
          </a>
          <span class="text-gray-600"> — AI meetups and workshops in US-Boston</span>
        </li>
        <li>
          <a href="{{ site.event_calendars.ai_blueprint_ma }}"
             target="_blank"
             rel="noopener noreferrer"
             class="text-blue-600 hover:text-blue-800 font-medium">
            AI Blueprint for MA
          </a>
          <span class="text-gray-600"> — in-person AI events calendar for Boston</span>
        </li>
      </ul>
    </section>
  </main>
</div>
