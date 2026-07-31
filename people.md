---
layout: default
title: People
permalink: /people/
description: "Meet members of Smaht.AI — AI engineers and entrepreneurs in our community."
---

<div class="max-w-6xl mx-auto">
  <header class="mb-10 md:mb-12 text-center max-w-2xl mx-auto">
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3">People</h1>
    <p class="text-lg text-gray-600 leading-relaxed">
      Members of Smaht.AI — experienced AI engineers and entrepreneurs building products and companies.
    </p>
  </header>

  <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
    {% assign people = site.members | sort: "order" %}
    {% for member in people %}
    <a href="{{ member.url | relative_url }}"
       class="community-card p-5 block no-underline hover:no-underline group">
      {% if member.image %}
      <div class="mb-4 rounded-lg overflow-hidden bg-gray-50 aspect-[4/5]">
        <img src="{{ member.image | relative_url }}"
             alt="{{ member.title | escape }}"
             class="w-full h-full object-contain"
             width="400"
             height="500"
             loading="lazy">
      </div>
      {% endif %}
      <h2 class="text-lg font-semibold text-gray-900 mb-1 group-hover:text-[var(--smaht-blue)] transition-colors">
        {{ member.title | escape }}
      </h2>
      {% if member.role %}
      <p class="text-sm text-[var(--smaht-blue)] font-medium mb-2">{{ member.role | escape }}</p>
      {% endif %}
      {% if member.summary %}
      <p class="text-sm text-gray-600 mb-0">{{ member.summary | escape }}</p>
      {% endif %}
    </a>
    {% endfor %}
  </div>
</div>
