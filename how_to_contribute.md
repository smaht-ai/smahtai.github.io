---
layout: page
title: How to Contribute
permalink: /how-to-contribute/
---

<div class="max-w-4xl mx-auto px-4 sm:px-6 md:px-8 py-8 md:py-12">
  <p class="text-lg text-gray-700 mb-8">
    This site is open for contributions. You can propose a new blog post, fix a typo, or add a page. Here’s how.
  </p>

  <section class="mb-10">
    <h2 class="text-2xl font-semibold text-gray-900 mb-4">1. Check out the repository</h2>
    <p class="text-gray-700 mb-3">
      Clone the site repository to your machine (the “sandbox”):
    </p>
    <pre class="bg-gray-100 rounded-lg p-4 text-sm overflow-x-auto mb-3"><code>git clone https://github.com/smaht-ai/smahtai.github.io.git
cd smahtai.github.io</code></pre>
    <p class="text-gray-700 mb-3">
      Install <strong>GNU make</strong> if you don’t have it (e.g. <code class="bg-gray-100 px-1 rounded">apt install make</code> on Debian/Ubuntu, <code class="bg-gray-100 px-1 rounded">brew install make</code> on macOS). Then install dependencies and start the local preview server using the project’s Makefile:
    </p>
    <pre class="bg-gray-100 rounded-lg p-4 text-sm overflow-x-auto mt-3"><code>make install
make serve</code></pre>
    <p class="text-gray-700 mt-3">
      Open <code class="bg-gray-100 px-1 rounded">http://localhost:4000</code> in your browser to preview your changes. Use <code class="bg-gray-100 px-1 rounded">make build</code> for a one-off build, or <code class="bg-gray-100 px-1 rounded">make clean</code> to clear the Jekyll output.
    </p>
  </section>

  <section class="mb-10">
    <h2 class="text-2xl font-semibold text-gray-900 mb-4">2. Create a branch</h2>
    <p class="text-gray-700 mb-3">
      Create a new branch for your work. Use a short, descriptive name (e.g. <code class="bg-gray-100 px-1 rounded">add-blog-post-xyz</code> or <code class="bg-gray-100 px-1 rounded">fix-about-typo</code>).
    </p>
    <pre class="bg-gray-100 rounded-lg p-4 text-sm overflow-x-auto"><code>git checkout -b your-branch-name</code></pre>
  </section>

  <section class="mb-10">
    <h2 class="text-2xl font-semibold text-gray-900 mb-4">3. Add a blog post or a page</h2>

    <h3 class="text-xl font-medium text-gray-900 mb-2">Adding a blog post</h3>
    <ul class="list-disc pl-6 text-gray-700 space-y-1 mb-4">
      <li>Create a new file in <code class="bg-gray-100 px-1 rounded">_posts/</code> with the naming convention: <code class="bg-gray-100 px-1 rounded">YYYY-MM-DD-your-post-title.md</code>.</li>
      <li>Add YAML front matter with <code class="bg-gray-100 px-1 rounded">layout: post</code>, <code class="bg-gray-100 px-1 rounded">title</code>, <code class="bg-gray-100 px-1 rounded">date</code>, <code class="bg-gray-100 px-1 rounded">author</code>, <code class="bg-gray-100 px-1 rounded">categories</code>, and optionally <code class="bg-gray-100 px-1 rounded">image</code> for a splash image.</li>
      <li>Write your content in Markdown below the front matter.</li>
    </ul>

    <h3 class="text-xl font-medium text-gray-900 mb-2">Adding or editing a page</h3>
    <ul class="list-disc pl-6 text-gray-700 space-y-1">
      <li>Create or edit a <code class="bg-gray-100 px-1 rounded">.md</code> file in the site root (e.g. <code class="bg-gray-100 px-1 rounded">about.md</code>, <code class="bg-gray-100 px-1 rounded">contact.md</code>) or in a subfolder.</li>
      <li>Use front matter with <code class="bg-gray-100 px-1 rounded">layout: page</code>, <code class="bg-gray-100 px-1 rounded">title</code>, and <code class="bg-gray-100 px-1 rounded">permalink</code> (e.g. <code class="bg-gray-100 px-1 rounded">/my-page/</code>).</li>
      <li>If you add a new page that should appear in the menu, add it under the appropriate section in <code class="bg-gray-100 px-1 rounded">_config.yml</code> (<code class="bg-gray-100 px-1 rounded">header_pages</code> and <code class="bg-gray-100 px-1 rounded">site_map</code>).</li>
    </ul>
  </section>

  <section class="mb-10">
    <h2 class="text-2xl font-semibold text-gray-900 mb-4">4. Make a pull request</h2>
    <p class="text-gray-700 mb-3">
      Commit your changes, push your branch to GitHub, and open a pull request (PR) against <code class="bg-gray-100 px-1 rounded">main</code>.
    </p>
    <pre class="bg-gray-100 rounded-lg p-4 text-sm overflow-x-auto mb-3"><code>git add .
git commit -m "Add blog post: Your title"
git push origin your-branch-name</code></pre>
    <p class="text-gray-700">
      Then on GitHub, go to <a href="https://github.com/smaht-ai/smahtai.github.io" class="text-blue-600 hover:text-blue-800 underline">smaht-ai/smahtai.github.io</a>, use the “Compare &amp; pull request” prompt, add a short description of your change, and submit the PR.
    </p>
  </section>

  <section class="mb-10">
    <h2 class="text-2xl font-semibold text-gray-900 mb-4">5. After your PR is approved</h2>
    <p class="text-gray-700 mb-3">
      Once a maintainer approves and merges your pull request into <code class="bg-gray-100 px-1 rounded">main</code>, a <strong>GitHub Action</strong> runs automatically: it builds the Jekyll site and deploys it to GitHub Pages. Your changes will appear on the live website shortly after the merge.
    </p>
    <p class="text-gray-700">
      You can see the workflow and build status under the repository’s <strong>Actions</strong> tab.
    </p>
  </section>

  <section class="mb-10">
    <h2 class="text-2xl font-semibold text-gray-900 mb-4">Theme: Analytiq Pages</h2>
    <p class="text-gray-700 mb-3">
      This site is built with Jekyll and uses the <strong>Analytiq Pages Theme</strong> for layout, styling, and components (navigation, blog, footer, etc.). The theme is a separate GitHub repository and is included as a dependency.
    </p>
    <ul class="list-disc pl-6 text-gray-700 space-y-1 mb-3">
      <li><strong>Theme repository:</strong> <a href="https://github.com/analytiq-hub/analytiq-pages-theme" class="text-blue-600 hover:text-blue-800 underline">github.com/analytiq-hub/analytiq-pages-theme</a></li>
      <li>The exact version is pinned in this site’s <code class="bg-gray-100 px-1 rounded">Gemfile</code> (e.g. by git tag). When you run <code class="bg-gray-100 px-1 rounded">make install</code>, the Makefile installs dependencies and fetches the theme from that repository.</li>
      <li>To change the theme version (e.g. to use a newer release), update the <code class="bg-gray-100 px-1 rounded">gem "analytiq-pages-theme"</code> line in <code class="bg-gray-100 px-1 rounded">Gemfile</code> and run <code class="bg-gray-100 px-1 rounded">make install</code> again.</li>
    </ul>
    <p class="text-gray-700">
      Content and site-specific overrides (e.g. <code class="bg-gray-100 px-1 rounded">_config.yml</code>, <code class="bg-gray-100 px-1 rounded">_includes/</code>, and your pages and posts) live in this repository; the theme provides the base look and behavior.
    </p>
  </section>

  <section class="mb-10">
    <h2 class="text-2xl font-semibold text-gray-900 mb-4">Additional Details</h2>

    <p class="text-gray-700 font-medium mb-1">Add images</p>
    <p class="text-gray-700 mb-4">Put image files under <code class="bg-gray-100 px-1 rounded">assets/images/</code> (e.g. <code class="bg-gray-100 px-1 rounded">assets/images/blog/</code> for post splashes). Reference them in Markdown or HTML as <code class="bg-gray-100 px-1 rounded">/assets/images/yourfile.png</code> or with <code class="bg-gray-100 px-1 rounded">{{ '/assets/images/yourfile.png' | relative_url }}</code> in Liquid.</p>

    <p class="text-gray-700 font-medium mb-1">Create SVG files</p>
    <p class="text-gray-700 mb-4">Add <code class="bg-gray-100 px-1 rounded">.svg</code> files in <code class="bg-gray-100 px-1 rounded">assets/images/</code> (or <code class="bg-gray-100 px-1 rounded">assets/images/blog/</code> for post graphics). Use a <code class="bg-gray-100 px-1 rounded">viewBox</code>, keep paths minimal, and optionally add <code class="bg-gray-100 px-1 rounded">&lt;title&gt;</code> / <code class="bg-gray-100 px-1 rounded">&lt;desc&gt;</code> for accessibility. See <code class="bg-gray-100 px-1 rounded">SVG_STYLING_GUIDE.md</code> in the repo for patterns.</p>

    <p class="text-gray-700 font-medium mb-1">Create Excalidraw diagrams</p>
    <p class="text-gray-700 mb-4">Save <code class="bg-gray-100 px-1 rounded">.excalidraw</code> JSON files in <code class="bg-gray-100 px-1 rounded">assets/excalidraw/</code>. Embed in content with the theme’s <code class="bg-gray-100 px-1 rounded">excalidraw-static.html</code> include (see existing posts for examples). Use <code class="bg-gray-100 px-1 rounded">/excalidraw-edit</code> to create or edit diagrams in the browser.</p>

    <p class="text-gray-700 font-medium mb-1">Vibe-code content with AI editors</p>
    <p class="text-gray-700 mb-4">You can use <strong>Cursor</strong>, <strong>Claude Code</strong>, <strong>Windsurf</strong>, or <strong>GitHub Copilot</strong> to draft or edit posts and pages. Open the repo in the editor, point the AI at <code class="bg-gray-100 px-1 rounded">AGENTS.md</code> (and this page) for conventions, then ask it to add a post, a page, or assets—then review, run <code class="bg-gray-100 px-1 rounded">make serve</code>, and open a PR.</p>
  </section>

  <p class="text-gray-600 mt-8">
    Questions? <a href="/contact/" class="text-blue-600 hover:text-blue-800 underline">Contact us</a> or open an issue on the <a href="https://github.com/smaht-ai/smahtai.github.io" class="text-blue-600 hover:text-blue-800 underline">repository</a>.
  </p>
</div>
