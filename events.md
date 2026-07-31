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
      <p class="text-gray-600 mb-8 max-w-2xl">
        We recommend the following calendars as having pretty good coverage of what’s happening locally:
      </p>

      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {% for cal in site.event_calendars %}
        <a href="{{ cal.url }}"
           target="_blank"
           rel="noopener noreferrer"
           class="group flex flex-col rounded-xl border border-gray-200 bg-white p-6 shadow-sm hover:shadow-md hover:border-blue-300 transition-all duration-200 no-underline text-inherit focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
          <div class="h-16 mb-5 flex items-center justify-center rounded-lg bg-gray-50 px-4">
            <img src="{{ cal.logo | relative_url }}"
                 alt="{{ cal.name | escape }} logo"
                 class="max-h-12 max-w-full w-auto object-contain"
                 loading="lazy">
          </div>
          <div class="flex items-start justify-between gap-2 mb-2">
            <h3 class="text-lg font-semibold text-gray-900 group-hover:text-blue-700 transition-colors">
              {{ cal.name }}
            </h3>
            <svg class="w-4 h-4 mt-1.5 shrink-0 text-gray-400 group-hover:text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
            </svg>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed flex-grow">
            {{ cal.description }}
          </p>
          <p class="mt-4 text-sm font-medium text-blue-600 group-hover:text-blue-800">
            Open calendar
            <span class="sr-only">(opens in a new tab)</span>
          </p>
        </a>
        {% endfor %}
      </div>
    </section>
  </main>
</div>
