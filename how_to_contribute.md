---
layout: page
title: How to Contribute
permalink: /how-to-contribute/
---

<div class="max-w-4xl mx-auto px-4 sm:px-6 md:px-8 py-8 md:py-12 space-y-8">
  <!-- Intro -->
  <header class="rounded-xl bg-gradient-to-br from-gray-50 to-blue-50 border border-gray-100 p-6 md:p-8">
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3">How to Contribute</h1>
    <p class="text-lg text-gray-700 leading-relaxed">
      This site is open for contributions. Propose a blog post, fix a typo, or add a page—here’s how.
    </p>
  </header>

  <!-- Step 1 -->
  <section class="rounded-xl border border-gray-200 bg-white shadow-sm overflow-hidden">
    <div class="flex items-center gap-3 border-b border-gray-100 bg-gray-50/80 px-6 py-4">
      <span class="flex h-8 w-8 items-center justify-center rounded-full bg-blue-100 text-sm font-semibold text-blue-700">1</span>
      <h2 class="text-xl font-semibold text-gray-900 m-0">Check out the repository</h2>
    </div>
    <div class="p-6 space-y-4">
      <p class="text-gray-700 leading-relaxed">Clone the site repository to your machine (the “sandbox”):</p>
      <pre class="rounded-lg border border-gray-200 bg-gray-50 p-4 text-sm font-mono text-gray-800 overflow-x-auto"><code>git clone https://github.com/smaht-ai/smahtai.github.io.git
cd smahtai.github.io</code></pre>
      <p class="text-gray-700 leading-relaxed">Install <strong>GNU make</strong> if needed (e.g. <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">apt install make</code> or <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">brew install make</code>). Then:</p>
      <pre class="rounded-lg border border-gray-200 bg-gray-50 p-4 text-sm font-mono text-gray-800 overflow-x-auto"><code>make install
make serve</code></pre>
      <p class="text-gray-600 text-sm leading-relaxed">Open <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">http://localhost:4000</code> to preview. Use <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">make build</code> for a one-off build, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">make clean</code> to clear output.</p>
    </div>
  </section>

  <!-- Step 2 -->
  <section class="rounded-xl border border-gray-200 bg-white shadow-sm overflow-hidden">
    <div class="flex items-center gap-3 border-b border-gray-100 bg-gray-50/80 px-6 py-4">
      <span class="flex h-8 w-8 items-center justify-center rounded-full bg-blue-100 text-sm font-semibold text-blue-700">2</span>
      <h2 class="text-xl font-semibold text-gray-900 m-0">Create a branch</h2>
    </div>
    <div class="p-6 space-y-4">
      <p class="text-gray-700 leading-relaxed">Create a new branch with a short, descriptive name (e.g. <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">add-blog-post-xyz</code> or <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">fix-about-typo</code>).</p>
      <pre class="rounded-lg border border-gray-200 bg-gray-50 p-4 text-sm font-mono text-gray-800 overflow-x-auto"><code>git checkout -b your-branch-name</code></pre>
    </div>
  </section>

  <!-- Step 3 -->
  <section class="rounded-xl border border-gray-200 bg-white shadow-sm overflow-hidden">
    <div class="flex items-center gap-3 border-b border-gray-100 bg-gray-50/80 px-6 py-4">
      <span class="flex h-8 w-8 items-center justify-center rounded-full bg-blue-100 text-sm font-semibold text-blue-700">3</span>
      <h2 class="text-xl font-semibold text-gray-900 m-0">Add a blog post or a page</h2>
    </div>
    <div class="p-6 space-y-6">
      <div>
        <h3 class="text-base font-semibold text-gray-900 mb-2">Adding a blog post</h3>
        <ul class="list-disc pl-5 space-y-1.5 text-gray-700 text-sm leading-relaxed">
          <li>New file in <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">_posts/</code>: <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">YYYY-MM-DD-your-post-title.md</code>.</li>
          <li>Front matter: <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">layout: post</code>, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">title</code>, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">date</code>, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">author</code>, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">categories</code>, optional <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">image</code>.</li>
          <li>Write content in Markdown below the front matter.</li>
        </ul>
      </div>
      <div>
        <h3 class="text-base font-semibold text-gray-900 mb-2">Adding or editing a page</h3>
        <ul class="list-disc pl-5 space-y-1.5 text-gray-700 text-sm leading-relaxed">
          <li>Create or edit a <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">.md</code> file (e.g. <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">about.md</code>, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">contact.md</code>) with <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">layout: page</code>, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">title</code>, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">permalink</code>.</li>
          <li>To show in the menu, add the page under <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">_config.yml</code> (<code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">header_pages</code> and <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">site_map</code>).</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Step 4 -->
  <section class="rounded-xl border border-gray-200 bg-white shadow-sm overflow-hidden">
    <div class="flex items-center gap-3 border-b border-gray-100 bg-gray-50/80 px-6 py-4">
      <span class="flex h-8 w-8 items-center justify-center rounded-full bg-blue-100 text-sm font-semibold text-blue-700">4</span>
      <h2 class="text-xl font-semibold text-gray-900 m-0">Make a pull request</h2>
    </div>
    <div class="p-6 space-y-4">
      <p class="text-gray-700 leading-relaxed">Commit, push your branch, and open a PR against <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">main</code>.</p>
      <pre class="rounded-lg border border-gray-200 bg-gray-50 p-4 text-sm font-mono text-gray-800 overflow-x-auto"><code>git add .
git commit -m "Add blog post: Your title"
git push origin your-branch-name</code></pre>
      <p class="text-gray-700 text-sm leading-relaxed">On GitHub, go to <a href="https://github.com/smaht-ai/smahtai.github.io" class="text-blue-600 hover:text-blue-800 underline font-medium">smaht-ai/smahtai.github.io</a>, use “Compare &amp; pull request”, add a description, and submit.</p>
    </div>
  </section>

  <!-- Step 5 -->
  <section class="rounded-xl border border-gray-200 bg-white shadow-sm overflow-hidden">
    <div class="flex items-center gap-3 border-b border-gray-100 bg-gray-50/80 px-6 py-4">
      <span class="flex h-8 w-8 items-center justify-center rounded-full bg-blue-100 text-sm font-semibold text-blue-700">5</span>
      <h2 class="text-xl font-semibold text-gray-900 m-0">After your PR is approved</h2>
    </div>
    <div class="p-6 space-y-2">
      <p class="text-gray-700 leading-relaxed">Once merged into <code class="rounded bg-gray-200 px-1.5 py-0.5 text-sm font-mono">main</code>, a <strong>GitHub Action</strong> builds the site and deploys to GitHub Pages. Your changes go live shortly after.</p>
      <p class="text-gray-600 text-sm">Workflow and build status: repository <strong>Actions</strong> tab.</p>
    </div>
  </section>

  <!-- Theme -->
  <section class="rounded-xl border border-gray-200 bg-white shadow-sm overflow-hidden">
    <div class="border-b border-gray-100 bg-gray-50/80 px-6 py-4">
      <h2 class="text-xl font-semibold text-gray-900">Theme: Analytiq Pages</h2>
    </div>
    <div class="p-6 space-y-4">
      <p class="text-gray-700 leading-relaxed">This site uses Jekyll and the <strong>Analytiq Pages Theme</strong> for layout, styling, and components. The theme is a separate repo and is included as a dependency.</p>
      <ul class="list-disc pl-5 space-y-1.5 text-gray-700 text-sm leading-relaxed">
        <li><strong>Theme repo:</strong> <a href="https://github.com/analytiq-hub/analytiq-pages-theme" class="text-blue-600 hover:text-blue-800 underline">github.com/analytiq-hub/analytiq-pages-theme</a></li>
        <li>Version is pinned in <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">Gemfile</code>. <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">make install</code> fetches the theme.</li>
        <li>To upgrade: edit <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">gem "analytiq-pages-theme"</code> in <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">Gemfile</code>, then run <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">make install</code>.</li>
      </ul>
      <p class="text-gray-600 text-sm leading-relaxed">Content and overrides (<code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">_config.yml</code>, <code class="rounded bg-gray-200 px-1.5 py-0.5 text-xs font-mono">_includes/</code>, pages, posts) live here; the theme provides the base.</p>
    </div>
  </section>

  <!-- Additional Details -->
  <section class="rounded-xl border border-gray-200 bg-white shadow-sm overflow-hidden">
    <div class="border-b border-gray-100 bg-gray-50/80 px-6 py-4">
      <h2 class="text-xl font-semibold text-gray-900">Additional Details</h2>
    </div>
    <div class="p-6">
      <div class="grid gap-6 sm:grid-cols-1 md:grid-cols-2">
        <div class="rounded-lg border border-gray-100 bg-gray-50/50 p-4">
          <h3 class="text-sm font-semibold text-gray-900 mb-2">Add images</h3>
          <p class="text-gray-700 text-sm leading-relaxed">Put files under <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">assets/images/</code> (e.g. <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">assets/images/blog/</code>). Reference as <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">/assets/images/yourfile.png</code> or with <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">relative_url</code> in Liquid.</p>
        </div>
        <div class="rounded-lg border border-gray-100 bg-gray-50/50 p-4">
          <h3 class="text-sm font-semibold text-gray-900 mb-2">Create SVG files</h3>
          <p class="text-gray-700 text-sm leading-relaxed">Add <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">.svg</code> in <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">assets/images/</code> or <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">assets/images/blog/</code>. Use <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">viewBox</code>, minimal paths; optional <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">&lt;title&gt;</code>/<code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">&lt;desc&gt;</code>. See <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">SVG_STYLING_GUIDE.md</code>.</p>
        </div>
        <div class="rounded-lg border border-gray-100 bg-gray-50/50 p-4">
          <h3 class="text-sm font-semibold text-gray-900 mb-2">Excalidraw diagrams</h3>
          <p class="text-gray-700 text-sm leading-relaxed">Save <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">.excalidraw</code> in <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">assets/excalidraw/</code>. Embed with <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">excalidraw-static.html</code> include. Use <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">/excalidraw-edit</code> to create or edit in the browser.</p>
        </div>
        <div class="rounded-lg border border-gray-100 bg-gray-50/50 p-4">
          <h3 class="text-sm font-semibold text-gray-900 mb-2">Vibe-code with AI editors</h3>
          <p class="text-gray-700 text-sm leading-relaxed">Use <strong>Cursor</strong>, <strong>Claude Code</strong>, <strong>Windsurf</strong>, or <strong>GitHub Copilot</strong>. Point the AI at <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">AGENTS.md</code> and this page; have it draft posts or pages, then review, <code class="rounded bg-gray-200 px-1 py-0.5 text-xs font-mono">make serve</code>, and open a PR.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer CTA -->
  <div class="rounded-lg border border-gray-200 bg-gray-50 px-6 py-4 text-center">
    <p class="text-gray-600 text-sm m-0">
      Questions? <a href="/contact/" class="text-blue-600 hover:text-blue-800 underline font-medium">Contact us</a> or open an issue on the <a href="https://github.com/smaht-ai/smahtai.github.io" class="text-blue-600 hover:text-blue-800 underline font-medium">repository</a>.
    </p>
  </div>
</div>
