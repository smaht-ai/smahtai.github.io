---
layout: docs
title: Architecture
permalink: /docs/architecture/
---

This guide explains the architecture of the Analytiq Pages Starter and how it integrates with the Analytiq Pages Theme.

## Overview

The starter is built on Jekyll with a modular theme-based architecture that separates presentation (theme) from content (site). The theme provides layouts, styling, and reusable components, while the starter contains your site-specific content, configuration, and any customizations.

{% include excalidraw-static.html file="/assets/excalidraw/analytiq-pages-architecture.excalidraw" %}

<div class="text-sm text-gray-500 mt-2 mb-6 text-center">
  <a href="{{ '/excalidraw-edit' | relative_url }}?file={{ '/assets/excalidraw/analytiq-pages-architecture.excalidraw' | relative_url }}" 
     class="text-gray-500 hover:text-gray-700 no-underline" 
     target="_blank">
    Edit diagram
  </a>
</div>

## Component Architecture

### Site Structure (Starter)

The starter repository contains your site-specific content and configuration:

- **Content Files**: Markdown files for pages, blog posts, and documentation stored at the root level
- **Configuration**: `_config.yml` defines site metadata, navigation, pagination, and theme settings
- **Site-Specific Overrides**: Custom includes (like `docs-widget.html`) that override theme defaults
- **Static Assets**: Images, documents, and other media files in `assets/`
- **Blog Posts**: Posts stored in `_posts/` directory with date-prefixed filenames
- **Collections**: Posts collection configured for blog functionality

### Theme Layer (Analytiq Pages Theme)

The theme provides the presentation layer:

- **Layouts**: HTML templates for different page types (default, page, post, docs)
- **Includes**: Reusable components (header, footer, navigation)
- **Assets**: CSS, JavaScript, and common images
- **Tailwind CSS**: Styling framework via CDN
- **Excalidraw Integration**: Support for rendering Excalidraw diagrams

## How It Works

### 1. Theme Inheritance

```yaml
# Gemfile
gem "analytiq-pages-theme",
    git: "https://github.com/analytiq-hub/analytiq-pages-theme.git",
    tag: "v0.1.8"
```

Jekyll loads the theme from the Git repository (version v0.1.8), making all theme assets available to your site. The theme is specified in `_config.yml`:

```yaml
theme: analytiq-pages-theme
```

### 2. Override Mechanism

Your site can override any theme file by creating a file with the same path:

```
analytiq-pages-starter/
├── _includes/
│   └── docs-widget.html      # Overrides theme's docs-widget
├── _layouts/                  # Custom layouts (if needed)
│   └── custom.html
└── assets/
    └── images/                # Site-specific images
        └── blog/              # Blog post images
```

The starter currently overrides `docs-widget.html` to provide custom documentation navigation.

### 3. Content Rendering Flow

1. **Request**: User visits a page (e.g., `/docs/getting-started/`)
2. **Content Load**: Jekyll finds the markdown file (`docs/getting-started.md`)
3. **Layout Application**: Uses the layout specified in front matter (`layout: docs`)
4. **Theme Resolution**: Looks for layout in site first, then in theme
5. **Includes Processing**: Processes all include directives from theme and site overrides
6. **Override Check**: Uses site's include if it exists, otherwise theme's
7. **HTML Generation**: Converts markdown to HTML and applies layout
8. **Static Output**: Generates final HTML file in `_site/` directory

## Key Features

### Responsive Design

The theme uses Tailwind CSS with a mobile-first approach:

- **Breakpoints**: sm (640px), md (768px), lg (1024px), xl (1280px)
- **Flexible Layouts**: Flexbox and Grid for complex layouts
- **Typography Plugin**: Prose classes for beautiful markdown rendering
- **CDN Delivery**: Tailwind CSS loaded via CDN for fast performance

### Documentation System

The docs layout provides a specialized environment for documentation:

- **Sidebar Widget**: Custom navigation menu via `_includes/docs-widget.html` override
- **Prose Styling**: Enhanced markdown rendering with proper spacing
- **Code Highlighting**: Syntax highlighting for code blocks
- **Responsive Layout**: Sidebar collapses on mobile devices
- **Excalidraw Diagrams**: Support for embedding Excalidraw diagrams via `excalidraw-wrapper` divs

### Blog System

Built-in blog with pagination support:

- **Collections**: Posts organized as a Jekyll collection
- **Pagination**: Uses `jekyll-paginate-v2` plugin (5 posts per page)
- **Categories**: Organize posts by category (e.g., "company announcements", "engineering")
- **RSS Feed**: Automatic feed generation with `jekyll-feed`
- **Post Previews**: Excerpt support with images
- **Permalink Structure**: Posts use `/:categories/:title/` permalink format

### Plugins

The starter uses the following Jekyll plugins:

- **jekyll-feed**: Generates RSS feed for blog posts
- **jekyll-seo-tag**: Adds SEO meta tags to pages
- **jekyll-pdf-embed**: Allows embedding PDF files in pages
- **jekyll-paginate-v2**: Advanced pagination for blog and other pages

## Configuration

### Site Configuration (`_config.yml`)

Key configuration sections:

```yaml
# Site Metadata
title: Your Company Name
author:
  name: Your Name
  email: "hello@yourcompany.com"
description: Your company description

# Theme
theme: analytiq-pages-theme

# Navigation
header_pages:
  - title: "Products"
    url: "#"
    children:
      - title: "Overview"
        url: "/products"
      - title: "Features"
        url: "/features"

# Collections
collections:
  posts:
    output: true
    permalink: /:categories/:title/

# Pagination
pagination:
  enabled: true
  per_page: 5
  permalink: '/page/:num/'
  sort_field: 'date'
  sort_reverse: true

# Plugins
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-pdf-embed
  - jekyll-paginate-v2
```

### Theme Customization

You can customize the theme without modifying it:

1. **Override Includes**: Create `_includes/filename.html` in your site (e.g., `docs-widget.html`)
2. **Override Layouts**: Create `_layouts/filename.html` in your site
3. **Add Custom CSS**: Include custom styles in `_includes/custom-head.html`
4. **Extend JavaScript**: Add scripts via custom includes

## Deployment Architecture

### GitHub Pages Deployment

The starter includes a GitHub Actions workflow (`.github/workflows/pages.yml`) for automatic deployment:

<div class="flex justify-center" style="margin: 2rem 0 -10rem 0;">
  <div style="transform: scale(0.7); transform-origin: top center; display: inline-block;">
    <div class="excalidraw-static" data-excalidraw="{{ '/assets/excalidraw/github-pages-deployment.excalidraw' | relative_url }}" style="margin: 0;">
      <div class="loading" style="padding: 2rem; text-align: center; color: #666;">Loading diagram...</div>
    </div>
  </div>
</div>
{% unless page.excalidraw_renderer_loaded %}
  <script type="module" src="{{ '/assets/js/excalidraw/render-excalidraw.js' | relative_url }}" defer></script>
  {% assign page.excalidraw_renderer_loaded = true %}
{% endunless %}

<div class="text-sm text-gray-500 mb-6 text-center" style="margin-top: -8rem;">
  <a href="{{ '/excalidraw-edit' | relative_url }}?file={{ '/assets/excalidraw/github-pages-deployment.excalidraw' | relative_url }}" 
     class="text-gray-500 hover:text-gray-700 no-underline" 
     target="_blank">
    Edit diagram
  </a>
</div>

### Build Process

1. **Dependency Resolution**: Bundler downloads the theme gem (v0.1.8) from GitHub
2. **Theme Installation**: Theme files are available to Jekyll
3. **Site Build**: Jekyll processes all content and applies theme
4. **Asset Processing**: Copies assets, processes includes
5. **Static Generation**: Creates static HTML files in `_site/`
6. **Artifact Upload**: GitHub Actions uploads `_site/` as artifact
7. **Deployment**: GitHub Pages serves the static files

### GitHub Actions Workflow

The workflow runs on:
- Push to `main` branch
- Manual workflow dispatch

It uses:
- Ruby 3.2
- Bundler cache for faster builds
- GitHub Pages deployment action
- Production environment for optimized builds

## File Organization

### Actual Structure

```
analytiq-pages-starter/
├── _config.yml              # Site configuration
├── _includes/               # Site-specific includes (overrides)
│   └── docs-widget.html    # Custom docs navigation widget
├── _posts/                  # Blog posts collection
│   ├── 2025-11-01-welcome-to-our-blog.md
│   ├── 2025-11-15-building-scalable-systems.md
│   └── 2025-11-22-api-design-best-practices.md
├── docs/                    # Documentation pages
│   ├── getting-started.md
│   ├── user-guide.md
│   ├── api-reference.md
│   └── architecture.md
├── assets/                  # Static assets
│   ├── excalidraw/          # Excalidraw diagram files
│   │   └── analytiq-pages-architecture.excalidraw
│   └── images/
│       └── blog/            # Blog post images
│           ├── welcome.svg
│           ├── scalable-systems.svg
│           └── api-design.svg
├── .github/
│   └── workflows/
│       └── pages.yml        # GitHub Actions deployment workflow
├── index.md                 # Homepage
├── about.md                 # About page
├── contact.md               # Contact page
├── products.md              # Products overview
├── features.md              # Features page
├── case-studies.md          # Case studies
├── blog.md                  # Blog listing page
├── talks.md                 # Talks page
├── 404.html                 # Custom 404 page
├── favicon.ico              # Site favicon
├── Gemfile                  # Ruby dependencies
├── Gemfile.lock             # Locked dependency versions
├── LICENSE                  # License file
├── Makefile                 # Build shortcuts
└── README.md                # Project documentation
```

### Content Organization

- **Root-level Pages**: Main site pages (index, about, contact, etc.) are markdown files at the root
- **Documentation**: All docs pages in `docs/` directory with `layout: docs`
- **Blog Posts**: Posts in `_posts/` with date prefix (YYYY-MM-DD-title.md)
- **Assets**: Images organized by purpose (blog images in `assets/images/blog/`)

## Best Practices

### Content Organization

- **Use Permalinks**: Define explicit permalinks in front matter for consistent URLs
- **Consistent Naming**: Use kebab-case for file names
- **Category Hierarchy**: Organize posts by category (space-separated in front matter)
- **Asset Management**: Keep images close to content in `/assets/images/`
- **Front Matter**: Always include layout, title, and permalink in front matter

### Theme Customization

- **Minimal Overrides**: Only override what you need to change (currently just `docs-widget.html`)
- **Document Changes**: Comment why you're overriding theme files
- **Version Control**: Track theme version in Gemfile for reproducibility (currently v0.1.8)
- **Test Locally**: Always test changes with `bundle exec jekyll serve`

### Performance

- **Image Optimization**: Compress images before adding to repository
- **SVG for Icons**: Use SVG for logos and icons (as seen in blog images)
- **Minimal Dependencies**: Only include necessary Jekyll plugins
- **CDN Usage**: Leverage CDN for third-party resources (Tailwind, fonts)
- **Static Generation**: All pages are pre-rendered for fast loading

## Extending the Starter

### Adding a New Page

1. Create a markdown file at the root (e.g., `services.md`)
2. Add front matter with layout and permalink:
   ```yaml
   ---
   layout: page
   title: Services
   permalink: /services/
   ---
   ```
3. Add navigation link in `_config.yml` under `header_pages`

### Adding a New Documentation Section

1. Create markdown file in `docs/` directory (e.g., `docs/troubleshooting.md`)
2. Set front matter with `layout: docs` and `permalink`:
   ```yaml
   ---
   layout: docs
   title: Troubleshooting
   permalink: /docs/troubleshooting/
   ---
   ```
3. Add link to `_includes/docs-widget.html` navigation
4. Content will automatically use docs layout with sidebar

### Adding a Blog Post

1. Create file in `_posts/` with format: `YYYY-MM-DD-post-title.md`
2. Include front matter:
   ```yaml
   ---
   layout: post
   title: "Your Post Title"
   date: 2025-11-29 10:00:00 -0400
   categories: category1 category2
   author: "Author Name"
   image: /assets/images/blog/image.svg
   ---
   ```
3. Post will appear on blog page and in RSS feed

### Custom Styling

Create `_includes/custom-head.html`:

```html
<style>
  /* Your custom CSS */
  .my-custom-class {
    /* styles */
  }
</style>
```

This file is automatically included by the theme's `head.html`.

### Excalidraw Diagrams

To add an Excalidraw diagram:

1. Create diagram file in `assets/excalidraw/` (e.g., `my-diagram.excalidraw`)
2. Reference it in markdown using the include:
   ```liquid
   {% include excalidraw-static.html file="/assets/excalidraw/my-diagram.excalidraw" %}
   ```
3. The theme's JavaScript will render it automatically
4. Add an edit link (optional):
   ```liquid
   <div class="text-sm text-gray-500 mt-2 mb-6 text-center">
     <a href="{{ '/excalidraw-edit' | relative_url }}?file={{ '/assets/excalidraw/my-diagram.excalidraw' | relative_url }}" 
        class="text-gray-500 hover:text-gray-700 no-underline" 
        target="_blank">
       Edit diagram
     </a>
   </div>
   ```

## Troubleshooting

### Theme Not Loading

- Check Gemfile has correct theme reference with tag v0.1.8
- Run `bundle install` to download theme
- Verify `_config.yml` has `theme: analytiq-pages-theme`
- Check GitHub repository access (theme is private/public)

### Styles Not Applying

- Clear Jekyll cache: `bundle exec jekyll clean`
- Check for syntax errors in overridden files
- Verify Tailwind CDN is loading in browser dev tools
- Ensure no conflicting CSS in custom includes

### Build Failures

- Check Jekyll version compatibility (via github-pages gem)
- Ensure all plugins are listed in Gemfile
- Review build logs for specific error messages
- Verify Ruby version matches workflow (3.2)

### GitHub Pages Deployment Issues

- Check GitHub Actions workflow runs successfully
- Verify repository has Pages enabled with GitHub Actions source
- Check workflow permissions (contents: read, pages: write)
- Review workflow logs for build errors

## Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Analytiq Pages Theme Repository](https://github.com/analytiq-hub/analytiq-pages-theme)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Collections](https://jekyllrb.com/docs/collections/)

---

**Next Steps:**
- Explore the [Getting Started](/docs/getting-started/) guide
- Learn about [customization options](/docs/user-guide/)
- Check out the [API Reference](/docs/api-reference/)
