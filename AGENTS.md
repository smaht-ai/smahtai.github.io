This file provides guidance for AI agents (Claude, Cursor, etc.) working with the Analytiq Pages Starter codebase.

## Important Notes for Agents

- This is a **static site generator**, not a dynamic web application
- There are **no REST APIs** - only configuration and template APIs
- Content is written in **Markdown** with YAML front matter
- **Liquid** is used for templating, not a programming language
- Files in `exclude` list are **not processed** by Jekyll
- The theme is loaded from a **Git repository** (GitHub)
- All pages are **pre-rendered** at build time, not runtime

## Project Overview

The Analytiq Pages Starter is a Jekyll-based static site generator template that uses the Analytiq Pages Theme. It's designed for creating professional company websites, product pages, and documentation sites.

### Key Technologies

- **Jekyll**: Static site generator (Ruby-based)
- **Analytiq Pages Theme**: Theme providing layouts, styling, and components
- **Tailwind CSS**: Utility-first CSS framework (loaded via CDN)
- **Liquid**: Templating language used by Jekyll
- **GitHub Pages**: Deployment platform (via GitHub Actions)

## Project Structure

```
/
├── _config.yml              # Site configuration (YAML)
├── _includes/               # Site-specific includes (overrides theme)
│   ├── apply-cta.html       # Membership apply CTA
│   ├── custom-head.html     # Favicon, SEO/JSON-LD, analytics
│   ├── json-ld.html         # Structured data
│   └── talk-card.html       # Talk listing card
├── _posts/                  # Blog posts collection
├── assets/                  # Static assets
│   ├── css/community.css    # Site design tokens and shared styles
│   ├── excalidraw/          # Excalidraw diagram files
│   └── images/              # Image files (logo, events, blog)
├── .github/workflows/       # GitHub Actions workflows
├── *.md                     # Root-level pages (index, about, events, talks, etc.)
├── 404.html                 # Custom 404 error page
├── excalidraw.html          # Excalidraw editor page
├── favicon.ico              # Site favicon
├── Gemfile                  # Ruby dependencies
├── Gemfile.lock             # Locked dependency versions
├── LICENSE                  # License file
├── Makefile                 # Build automation
├── README.md                # Project documentation
├── AGENTS.md                # Agent guidance (this file; excluded from Jekyll)
└── scripts/                 # Local check scripts
```

## Important Files

### Configuration

- **`_config.yml`**: Main site configuration
  - Site metadata (title, author, description)
  - Navigation menus (`header_pages`, `site_map`)
  - Collections configuration (`posts`)
  - Pagination settings
  - Plugin list

### Content Files

- **Root `.md` files**: Main site pages (index.md, about.md, events.md, talks.md, technology.md, contact.md, etc.)
  - Use front matter to specify layout and metadata
  - Markdown/HTML content below front matter

- **`_posts/YYYY-MM-DD-title.md`**: Blog posts
  - Must follow date-prefixed naming convention
  - Use `layout: post`
  - Categories are space-separated or YAML arrays in front matter

There is **no** `docs/` collection on this site. Product documentation lives on external sites (e.g. DocRouter) when needed.
### Theme Integration

- **Theme**: Specified in `_config.yml` as `theme: analytiq-pages-theme`
- **Theme version**: Pinned in `Gemfile` (currently v1.0.5)
- **Overrides**: Create files in `_includes/` or `_layouts/` to override theme defaults

## Common Tasks

### Adding a New Page

1. Create `.md` file at root or in appropriate directory
2. Add front matter:
   ```yaml
   ---
   layout: page
   title: Page Title
   permalink: /page-url/
   ---
   ```
3. Add navigation link in `_config.yml` if needed

### Adding a Blog Post

1. Create file in `_posts/` with format: `YYYY-MM-DD-title.md`
2. Create SVG splash image (see "Creating SVG Splash Images" below)
3. Add front matter:
   ```yaml
   ---
   layout: post
   title: "Post Title"
   date: 2025-11-29 10:00:00 -0400
   categories: category1 category2
   author: "Author Name"
   image: /assets/images/blog/image.svg
   ---
   ```

**Important**: Blog posts must use **today's date** in both the filename and the `date` field in front matter. Do not use future dates or past dates - always use the current date when creating a new blog post.

### Membership apply CTA

Use the shared include instead of hardcoding the Google Form URL:

```liquid
&#123;% include apply-cta.html %&#125;
&#123;% include apply-cta.html style="band" title="Join Smaht.AI" description="Selective free membership for AI builders." %&#125;
&#123;% include apply-cta.html style="link" text="apply to be a member" %&#125;
```

The form URL lives in `_config.yml` as `apply_url`.

### Embedding Excalidraw Diagrams

```liquid
&#123;% include excalidraw-static.html file="/assets/excalidraw/diagram.excalidraw" %&#125;
```

Add edit link:
```liquid
<div class="text-sm text-gray-500 mt-2 mb-6 text-center">
  <a href="&#123;&#123; '/excalidraw-edit' | relative_url &#125;&#125;?file=&#123;&#123; '/assets/excalidraw/diagram.excalidraw' | relative_url &#125;&#125;" 
     class="text-gray-500 hover:text-gray-700 no-underline" 
     target="_blank">
    Edit diagram
  </a>
</div>
```

## Creating SVG and Excalidraw Diagrams

### SVG Diagrams

SVG diagrams are ideal for:
- **Blog post splash images** (see "Creating SVG Splash Images" below)
- **Simple illustrations** embedded in content
- **Icons and graphics** that need to scale perfectly

**Best Practices for SVG Diagrams**:

1. **Use semantic structure**: Group related elements with `<g>` tags
2. **Define reusable elements**: Use `<defs>` for gradients, patterns, and markers
3. **Optimize for size**: Remove unnecessary attributes, use minimal paths
4. **Ensure accessibility**: Add `<title>` and `<desc>` elements for screen readers
5. **Use relative units**: Prefer `viewBox` over fixed pixel dimensions when possible
6. **Consistent styling**: Use CSS classes or inline styles consistently

**File Organization**:
- Blog splash images: `/assets/images/blog/*.svg`
- Event calendar logos: `/assets/images/events/*`
- Brand logo: `/assets/images/smaht-logo*`
- General illustrations: `/assets/images/*.svg`

**Creating SVG Splash Images**:

Blog posts should include a custom SVG splash image that appears at the top of the post. Follow these guidelines:

**Aspect Ratio**: Use **4:3** aspect ratio (800x600 viewBox)

**File Location**: Save in `/assets/images/blog/` with a descriptive filename (e.g., `api-design.svg`, `scalable-systems.svg`)

**Structure**:
1. **Background**: Use a linear gradient with brand colors
2. **Central Icon/Illustration**: Place at y=200, centered horizontally (x=400)
3. **Title Text**: Position at y=360, font-size 40-42px, bold, white, centered
4. **Subtitle Text**: Position at y=400, font-size 22px, rgba white with 0.9 opacity, centered

**Template**:
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="gradientId" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#COLOR1;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#COLOR2;stop-opacity:1" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="800" height="600" fill="url(#gradientId)"/>

  <!-- Central Icon/Illustration -->
  <g transform="translate(400, 200)">
    <!-- Your icon/illustration here -->
    <!-- Keep it around 200px wide/tall, centered -->
  </g>

  <!-- Title -->
  <text x="400" y="360" font-family="Arial, sans-serif" font-size="40" font-weight="bold"
        fill="white" text-anchor="middle">Post Title</text>

  <!-- Subtitle -->
  <text x="400" y="400" font-family="Arial, sans-serif" font-size="22"
        fill="rgba(255,255,255,0.9)" text-anchor="middle">Post Subtitle or Description</text>
</svg>
```

**Design Tips**:
- Use white text/icons on gradient backgrounds for contrast
- Keep icons simple and recognizable (browser windows, code brackets, architecture diagrams, etc.)
- Use brand colors for gradients (purple/blue, green/blue combinations work well)
- Ensure text is readable - use white or very light colors
- Icons should be approximately 200px wide/tall and centered

**For detailed styling alternatives and techniques**, see `SVG_STYLING_GUIDE.md` which includes:
- Background styling options (gradients, patterns, solid colors)
- Icon/illustration styling techniques (glassmorphism, neumorphism, line art, etc.)
- Text styling alternatives (shadows, gradients, outlines)
- Color scheme combinations
- Layout variations
- Quick reference templates

### Excalidraw Diagrams

Excalidraw diagrams are ideal for:
- **Architecture diagrams** showing system components and relationships
- **Flowcharts and process diagrams**
- **Complex technical illustrations** that benefit from interactive editing
- **Diagrams that may need frequent updates**

**Best Practices for Excalidraw Diagrams**:

1. **Use descriptive filenames**: `architecture-diagram.excalidraw`, `deployment-flow.excalidraw`
2. **Organize with frames**: Use Excalidraw frames to group related elements
3. **Consistent styling**: Use a consistent color palette and font sizes
4. **Clear labels**: Ensure all components are clearly labeled
5. **Logical flow**: Arrange elements top-to-bottom or left-to-right for readability
6. **Export considerations**: Diagrams render as static images, so ensure they're readable without interaction

**File Organization**:
- Store all Excalidraw files in `/assets/excalidraw/`
- Use kebab-case for filenames: `diagram-name.excalidraw`

**Creating Excalidraw Diagrams**:

1. **Use the Excalidraw editor**: Access via `/excalidraw-edit.html` or use excalidraw.com
2. **Save as JSON**: Excalidraw files are JSON format with `.excalidraw` extension
3. **Embed in content**: Use the `excalidraw-static.html` include (see above)
4. **Add edit links**: Always include an edit link below embedded diagrams for easy updates

**When to Use SVG vs Excalidraw**:

- **Use SVG** for:
  - Simple illustrations and icons
  - Blog post splash images
  - Graphics that need precise control
  - Small, static diagrams

- **Use Excalidraw** for:
  - Complex architecture diagrams
  - Flowcharts with multiple components
  - Diagrams that may need collaborative editing
  - Technical illustrations with many elements

## Liquid Template Syntax

### Escaping Liquid Code in Documentation

When documenting Liquid syntax in markdown files, wrap examples in `&#123;% raw %&#125;` tags:

```liquid
&#123;% raw %&#125;&#123;&#123; site.title &#125;&#125;&#123;% endraw %&#125;
```

This prevents Jekyll from processing the Liquid code during build.

**Note**: In this documentation file (AGENTS.md), Liquid syntax examples use HTML entities (`&#123;` for `{` and `&#125;` for `}`) to prevent Jekyll from processing them, since this file is excluded from Jekyll processing.

### Common Variables

- `site.*`: Site configuration from `_config.yml`
- `page.*`: Current page front matter
- `paginator.*`: Pagination data (on paginated pages)
- `post.*`: Post data (in post layouts)

### Common Filters

- `relative_url`: Convert to relative URL
- `date`: Format dates
- `markdownify`: Convert markdown to HTML
- `where`: Filter arrays
- `sort`: Sort arrays

## Build and Deployment

### Local Development

```bash
bundle install
bundle exec jekyll serve
```

Visit http://localhost:4000

### Deployment

- **GitHub Pages**: Automatic via GitHub Actions workflow
- **Workflow**: `.github/workflows/pages.yml`
- **Trigger**: Push to `main` branch or manual dispatch

## Best Practices

1. **Always use front matter**: Every content file needs `layout` and `title`
2. **Use permalinks**: Explicit permalinks prevent URL changes
3. **Follow naming conventions**: kebab-case for files, space-separated categories
4. **Test locally**: Always test changes with `bundle exec jekyll serve`
5. **Exclude non-content files**: Add files like `AGENTS.md` to `exclude` in `_config.yml`

## Troubleshooting

### File Not Appearing on Site

- Check if file is in `exclude` list in `_config.yml`
- Verify front matter is correct
- Check for YAML syntax errors
- Restart Jekyll server

### Liquid Syntax Errors

- Wrap example code in `&#123;% raw %&#125;` tags
- Check for unclosed tags: `&#123;% if %&#125;...&#123;% endif %&#125;`
- Verify variable names match front matter

### Theme Not Loading

- Verify `theme: analytiq-pages-theme` in `_config.yml`
- Check Gemfile has correct theme reference
- Run `bundle install`

## Documentation References

- Theme and Jekyll docs: see Analytiq Pages Theme README and [Jekyll Documentation](https://jekyllrb.com/docs/)
- Site check: `python3.11 scripts/check_site.py`

## Quick Reference

### File Structure
```
project-root/
├── _config.yml              # Site configuration (YAML)
├── _includes/               # Site-specific includes
│   ├── apply-cta.html
│   ├── custom-head.html
│   ├── json-ld.html
│   └── talk-card.html
├── _posts/                  # Blog posts
├── assets/
│   ├── css/community.css    # Design tokens
│   ├── excalidraw/
│   └── images/
├── events.md / talks.md / technology.md / …
├── favicon.ico
├── Gemfile
├── AGENTS.md
└── scripts/check_site.py
```

### Essential Commands
```bash
bundle install              # Install dependencies
bundle exec jekyll serve    # Start local development server
# Visit http://localhost:4000
python3.11 scripts/check_site.py
```

### Front Matter Templates

**Basic Page**:
```yaml
---
layout: page
title: Page Title
permalink: /page-url/
---
```

**Blog Post**:
```yaml
---
layout: post
title: "Post Title"
date: 2025-11-29 10:00:00 -0400
categories: category1 category2
author: "Author Name"
image: /assets/images/blog/image.svg
---
```

