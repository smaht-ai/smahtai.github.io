---
layout: post
title: "From Jekyll Minima to Tailwind: A Seamless Migration Story"
date: 2025-08-20
author: Andrei Radulescu-Banu
mathjax: true
image: /assets/images/jekyll-tailwind.png
categories: [webdev, jekyll, tailwind]
description: "How Claude Code migrated a Jekyll Minima site to Tailwind CSS — covering the migration workflow and Tailwind's advantages for AI-assisted web development."
---

I can't believe it. Claude Code was able to update my Jekyll-based site [bitdribble.github.io](https://bitdribble.github.io) to use Tailwind pretty much with no intervention. The transformation from the old, less flexible Minima theme to a modern Tailwind-powered setup was vibe coded with a few light touches.

## The Challenge with Minima

For years, I've been running my personal knowledge repository on Jekyll with the default Minima theme. While Minima served its purpose, it had several limitations. The look and feel was outdated, and layouts were especially rigid.

## Enter Tailwind CSS

Tailwind CSS has become the go-to utility-first CSS framework for modern web development, and for good reason: 
- It is much simpler than CSS
- It is responsove out of the box, built with mobile-first principles
- AI editors like Claude Code and Cursor are very fluent with Tailwind.

## The Migration Process

What surprised me most was how seamless the migration turned out to be.

### Development Environment Setup

The migration was performed on **Fedora Linux** using a simple but effective workflow:

1. **Repository Setup:** Checked out the Git repository from the command line:
   ```bash
   git clone https://github.com/bitdribble/bitdribble.github.io.git
   cd bitdribble.github.io
   ```

2. **IDE Integration:** Loaded the project in **Cursor** (this works equally well in **VSCode**):

3. **Claude Code Extension:** Enabled the Claude Code add-in, which, like Cursor, provides:
   - Intelligent code suggestions and refactoring
   - Context-aware assistance with Jekyll and Tailwind
   - Seamless understanding of project structure and dependencies

### How Claude Code Transformed the Migration

The AI assistant proved exceptionally capable at understanding both Jekyll's architecture and Tailwind's utility-first approach. Here's what made it work so well:

### 1. Jekyll's Markdown Flexibility

**Almost all Jekyll pages can be written in pure Markdown**. Take a look at my [markdown example page](https://bitdribble.github.io/markdown/) - it's a full demonstration of how Jekyll processes Markdown content beautifully, even with the new Tailwind styling.
- Content creators don't need to know HTML or CSS
- Blog posts remain simple and focused on content

### 2. Inline HTML When Needed

When you need more sophisticated layouts or Tailwind-specific components, Jekyll's Markdown processor allows you to **embed HTML+Tailwind directly in your Markdown files**. For example, I was able to create a sophisticated three-column layout for my about page by simply adding:

```html
<div class="bg-white rounded-lg shadow-lg p-8">
  <div class="grid md:grid-cols-3 gap-8 items-start">
    <!-- Column content here -->
  </div>
</div>
```

**Live Example:** Here's that same three-column layout in action with actual content:

<div class="bg-white rounded-lg shadow-lg p-8 my-6">
  <div class="grid md:grid-cols-3 gap-8 items-start">
    <div class="text-center">
      <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
        </svg>
      </div>
      <h3 class="text-lg font-semibold text-gray-900 mb-2">Markdown Content</h3>
      <p class="text-gray-600 text-sm">Write content in simple Markdown syntax without worrying about styling complexities.</p>
    </div>
    
    <div class="text-center">
      <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path>
        </svg>
      </div>
      <h3 class="text-lg font-semibold text-gray-900 mb-2">Tailwind Styling</h3>
      <p class="text-gray-600 text-sm">Add sophisticated layouts with utility-first CSS classes when you need more control.</p>
    </div>
    
    <div class="text-center">
      <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
        </svg>
      </div>
      <h3 class="text-lg font-semibold text-gray-900 mb-2">Jekyll Processing</h3>
      <p class="text-gray-600 text-sm">Jekyll seamlessly processes both Markdown and HTML, giving you complete flexibility.</p>
    </div>
  </div>
</div>

This flexibility gives you the best of both worlds - simple content editing in Markdown, with the power to create complex layouts when needed.

### 3. Enhanced Features with Jekyll

The Jekyll + Tailwind combination also preserves and enhances Jekyll's powerful features. Take a look at the [markdown example page](https://bitdribble.github.io/markdown/) which demonstrates:

**Code Syntax Highlighting:** Jekyll automatically highlights code blocks with proper syntax coloring for multiple languages:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**MathJax Integration:** Mathematical formulas can be enabled by adding `mathjax: true` to the page front matter:

```yaml
---
layout: page
title: Your Page Title
mathjax: true
---
```

Then you can write beautiful mathematical expressions:
- Inline math: $E = mc^2$ 
- Display equations: 
$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

**Page Headers:** Jekyll's front matter system makes it easy to configure pages with metadata, layout selection, and feature toggles like MathJax - all while maintaining the flexibility to use Tailwind styling throughout the content.

## The Payoff

The transformation has been dramatic. Here's a side-by-side comparison of the old Minima theme versus the new Tailwind-powered design:

<div class="grid md:grid-cols-2 gap-8 my-8">
  <div class="space-y-4">
    <h3 class="!text-sm font-semibold text-gray-900">Before: Jekyll Minima Theme</h3>
    <img src="/assets/images/bitdribble_github_io_old.png" alt="Old Jekyll Minima Site" class="w-full rounded-lg shadow-lg border border-gray-200">
    <p class="text-base text-gray-600 italic">The original site using Jekyll's Minima theme with dark styling</p>
  </div>
  
  <div class="space-y-4">
    <h3 class="!text-sm font-semibold text-gray-900">After: Tailwind CSS Design</h3>
    <img src="/assets/images/bitdribble_github_io_new.png" alt="New Tailwind CSS Site" class="w-full rounded-lg shadow-lg border border-gray-200">
    <p class="text-base text-gray-600 italic">The modern site with Tailwind CSS featuring improved navigation and visual hierarchy</p>
  </div>
</div>

The site now boasts:
- **Modern visuals**: Professional and polished
- **Performance**: Purged CSS for leaner loads
- **Flexibility**: I can create any layout I can imagine without fighting the framework

## Why Jekyll + Tailwind Rocks

- **Content Teams**: Edit in Markdown, no CSS needed. 
- **Developers**: Modern tooling, reusable components
- **Businesses**: Fast, SEO-friendly, low-cost hosting (GitHub Pages, Netlify)


## Technical Implementation

The migration involved several key technical steps that Claude Code helped orchestrate seamlessly:

### 1. Tailwind CSS Integration

**Adding the Tailwind CLI:**
```bash
# Downloaded the standalone Tailwind CLI binary
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x tailwindcss-linux-x64
mv tailwindcss-linux-x64 tailwindcss
```

**Created Tailwind Configuration:**
```javascript
// tailwind.config.js
module.exports = {
  content: [
    './_includes/**/*.html',
    './_layouts/**/*.html', 
    './_posts/**/*.md',
    './*.html',
    './*.md',
    './**/*.md'
  ],
  theme: {
    extend: {
      // Custom colors and styling
    },
  },
  plugins: [],
}
```

**Build Process Integration:**
Created a `Makefile` to streamline development with proper process management: `make dev` starts the web server locally, and `Ctrl-C` stops it: 
```makefile
# Development with live reload and signal handling
dev:
	@echo "Starting development environment..."
	@trap 'echo "Stopping all processes..."; kill 0' INT; \
	./tailwindcss -o assets/css/tailwind.css --watch & \
	TAILWIND_PID=$$!; \
	bundle exec jekyll serve & \
	JEKYLL_PID=$$!; \
	echo "Development server running. Press Ctrl+C to stop both processes."; \
	wait

# Production build
build:
	./tailwindcss -o assets/css/tailwind.css --minify
	bundle exec jekyll build
```

### 2. Replacing the Minima Theme

**Removed Theme Dependency:**
```yaml
# _config.yml - Commented out the minima theme
# theme: minima  # Removed - using Tailwind CSS instead
```

**Layout System Redesign:**
- **`_layouts/default.html`**: Created a new base layout with Tailwind styling
- **`_layouts/home.html`**: Redesigned blog listing with card-based design
- **`_layouts/page.html`**: Clean page layout with proper typography
- **`_layouts/post.html`**: Enhanced blog post layout with better readability

### 3. Component Migration Strategy

**Navigation System:**
Replaced Minima's navigation with a modern Tailwind-based header featuring:
- Responsive dropdown menus
- Clean typography and spacing

### 4. Content Preservation

**Front Matter Compatibility:**
All existing blog posts and pages continued to work without modification. Jekyll's front matter system remained unchanged:
```yaml
---
layout: post
title: "My Blog Post"
date: 2025-01-20
categories: [webdev, jekyll]
---
```

## Conclusion

Jekyll + Tailwind is a powerhouse for blogs and company sites, blending content simplicity with design flexibility. Claude Code nailed the migration, delivering a stunning result with minimal effort. Check the [source code](https://github.com/bitdribble/bitdribble.github.io) or [live site](https://bitdribble.github.io) to see it in action!