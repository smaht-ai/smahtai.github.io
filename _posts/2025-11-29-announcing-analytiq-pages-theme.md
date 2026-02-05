---
layout: post
title: "Announcing Analytiq Pages Theme: A Modern Jekyll Theme with Tailwind CSS"
date: 2025-11-29
author: Andrei Radulescu-Banu
mathjax: false
image: /assets/images/announcing_analytiq_pages_theme.png
categories: [webdev, jekyll, tailwind, github-pages, theme, release]
---

🎉 **We're excited to announce the release of Analytiq Pages Theme v0.1.6** - a modern, feature-rich Jekyll theme that transforms our Analytiq Pages approach into a reusable, professional-grade solution for building beautiful company websites.

## The Evolution: From Method to Theme

Analytiq Pages started as a methodology for building company websites using Jekyll, GitHub Pages, and Tailwind CSS. Today, we're proud to release it as **Analytiq Pages Theme** - a fully packaged Jekyll theme that makes this powerful combination accessible to everyone.

<div class="grid md:grid-cols-2 gap-8 my-8">
  <div class="bg-white rounded-lg shadow-lg p-6 border border-gray-200">
    <div class="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center mb-4">
      <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
      </svg>
    </div>
    <h3 class="text-xl font-semibold text-gray-900 mb-3">Before: Analytiq Pages</h3>
    <p class="text-gray-600">A methodology requiring manual setup of Jekyll, Tailwind, and custom configurations for each site.</p>
  </div>

  <div class="bg-white rounded-lg shadow-lg p-6 border border-gray-200">
    <div class="w-12 h-12 bg-green-600 rounded-lg flex items-center justify-center mb-4">
      <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
        <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
      </svg>
    </div>
    <h3 class="text-xl font-semibold text-gray-900 mb-3">Now: Analytiq Pages Theme</h3>
    <p class="text-gray-600">A complete, ready-to-use Jekyll theme with all features pre-configured and professionally designed.</p>
  </div>
</div>

## ✨ What's New in Analytiq Pages Theme

### 🚀 Advanced Features

- **Tailwind CSS Integration**: Modern, responsive design with utility-first styling
- **Enhanced Syntax Highlighting**: Beautiful code blocks with copy functionality using highlight.js
- **Interactive Diagrams**: Full Excalidraw integration for creating and embedding technical diagrams
- **Professional Blog Layouts**: Complete blog system with sidebar, pagination, and category support
- **Responsive Navigation**: Mobile-first navigation with dropdown menus and hamburger menu
- **Dark Theme Support**: Built-in dark mode (Minima skin) for modern aesthetics

### 🛠 Developer Experience

- **Three Customization Hooks**: Override `custom-head.html`, `custom-header.html`, and `custom-footer.html` for site-specific modifications
- **Reusable Components**: Pre-built Tailwind components (alerts, buttons, cards)
- **SEO Optimized**: Integrated jekyll-seo-tag for better search engine visibility
- **PDF Embedding**: Native support for embedding PDF documents
- **RSS Feed Generation**: Automatic blog feed generation with jekyll-feed

### 🎨 Content Features

- **MathJax Support**: Render mathematical equations in your content
- **Multiple Layouts**: Specialized layouts for homepages, blog posts, documentation, and more
- **Excalidraw Editor**: Built-in diagram editor accessible at `/excalidraw-edit`
- **Smart Embeds**: Flexible diagram embedding with static, interactive, and link modes

## Installation: Get Started in Minutes

### Option 1: Quick Start with Existing Site

Add to your Jekyll site's `Gemfile`:

```ruby

gem "analytiq-pages-theme", git: "https://github.com/analytiq-hub/analytiq-pages-theme"
```

Or for a specific stable version:

```ruby

gem "analytiq-pages-theme", git: "https://github.com/analytiq-hub/analytiq-pages-theme", tag: "v0.1.6"
```

Update your `_config.yml`:

```yaml
theme: analytiq-pages-theme
```

Install and serve:

```bash
bundle install
bundle exec jekyll serve
```

### Option 2: New Site from Scratch

The simplest way to get started:

```bash
# Create new Jekyll site
jekyll new my-company-site
cd my-company-site

# Replace minima theme with analytiq-pages-theme in Gemfile
sed -i 's/gem "minima".*/gem "analytiq-pages-theme", git: "https:\/\/github.com\/analytiq-hub\/analytiq-pages-theme", tag: "v0.1.6"/' Gemfile

# Configure theme in _config.yml
sed -i 's/^theme: .*/theme: analytiq-pages-theme/' _config.yml

# Install and serve
bundle install
bundle exec jekyll serve
```

Or if you prefer manual editing:

```bash
# Create new Jekyll site
jekyll new my-company-site
cd my-company-site

# Edit Gemfile: replace the minima line with:
# gem "analytiq-pages-theme", git: "https://github.com/analytiq-hub/analytiq-pages-theme", tag: "v0.1.6"

# Edit _config.yml: replace the theme line with:
# theme: analytiq-pages-theme

# Install and serve
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000` to see your new site!

### Option 3: Local Installation (Alternative)

If you encounter repository access issues, you can install the theme locally:

```bash
# Download the theme release
curl -L https://github.com/analytiq-hub/analytiq-pages-theme/archive/refs/tags/v0.1.6.zip -o theme.zip
unzip theme.zip
mv analytiq-pages-theme-0.1.6/ _themes/analytiq-pages-theme/

# Or clone locally if you have access
git clone https://github.com/analytiq-hub/analytiq-pages-theme.git _themes/analytiq-pages-theme
cd _themes/analytiq-pages-theme && git checkout v0.1.6

# Add to _config.yml
echo "theme: _themes/analytiq-pages-theme" >> _config.yml
```

## Key Improvements Over Manual Setup

### Before (Analytiq Pages Method)
- Manual Tailwind CSS configuration
- Custom Jekyll setup for each project
- Repeated configuration of syntax highlighting
- Manual Excalidraw integration setup
- No standardized component library

### After (Analytiq Pages Theme)
- **One-line installation**: `theme: analytiq-pages-theme`
- **Pre-configured features**: Everything works out of the box
- **Professional components**: Reusable Tailwind components included
- **Advanced integrations**: Excalidraw, MathJax, PDF embeds ready to use
- **Consistent experience**: Standardized layouts and styling across sites

## Showcase: Real-World Examples

The theme powers several professional websites:

- **[Analytiq Hub](https://analytiqhub.com)** - Business intelligence and analytics platform
- **[DocRouter.AI](https://docrouter.ai)** - AI-powered document routing solution
- **[SigAgent.AI](https://sigagent.ai)** - Signature analysis and automation platform
- **[Bitdribble](https://bitdribble.github.io)** - Technology consulting and development

## Migration Guide: Upgrading from Analytiq Pages

If you're currently using the Analytiq Pages methodology, migration is straightforward:

1. **Add the theme** to your Gemfile and `_config.yml`
2. **Remove manual Tailwind configuration** (now handled by the theme)
3. **Update custom includes** to use the new hook system
4. **Migrate Excalidraw files** to `assets/excalidraw/` directory

Your existing content and configuration will continue to work seamlessly.

## Technical Architecture

The theme is built with modern web standards:

```
analytiq-pages-theme/
├── _layouts/           # 5 specialized layouts
├── _includes/          # 16+ reusable components
├── assets/
│   ├── css/           # Tailwind + custom styles
│   └── js/            # Pagination, Excalidraw renderer
├── _config.yml        # Default configuration
└── analytiq-pages-theme.gemspec
```

**Dependencies:**
- Jekyll >= 3.9, < 5.0 (supports both GitHub Pages and Jekyll 4.x)
- jekyll-feed ~> 0.12
- jekyll-seo-tag ~> 2.6
- jekyll-pdf-embed ~> 1.1

## Why Choose Analytiq Pages Theme?

### For Startups & Small Businesses
- **Zero hosting costs** with GitHub Pages
- **Professional appearance** without design costs
- **Content-first approach** with Markdown simplicity
- **Scalable foundation** that grows with your business

### For Agencies & Consultants
- **Rapid deployment** for client websites
- **Consistent branding** across projects
- **Advanced features** for technical content
- **Easy customization** for client-specific needs

### For Enterprise Teams
- **Git-based workflows** for version control and collaboration
- **Security compliance** with GitHub's enterprise infrastructure
- **SEO optimization** built-in
- **Extensible architecture** for custom requirements

## Troubleshooting

### Jekyll Version Compatibility

The theme supports both Jekyll 3.9+ (GitHub Pages) and Jekyll 4.x (modern installations). If you encounter version conflicts:

```bash
# For GitHub Pages compatibility (Jekyll 3.x)
gem "github-pages", group: :jekyll_plugins

# For modern Jekyll 4.x installations
gem "jekyll", "~> 4.3"
```

The theme will work with either version automatically.

### Bundle Install Issues

```bash
# Clear bundle cache
bundle cache clean --force

# Clear bundler git cache
rm -rf ~/.local/share/gem/ruby/cache/bundler/git/

# Try installing again
bundle install
```

### Theme Not Loading

- Verify `_config.yml` has `theme: analytiq-pages-theme`
- Clear Jekyll cache: `rm -rf _site .jekyll-cache`
- Rebuild: `bundle exec jekyll build`

## Getting Help & Contributing

- **Documentation**: Comprehensive README at [analytiq-pages-theme](https://github.com/analytiq-hub/analytiq-pages-theme)
- **Issues & Support**: GitHub Issues for bug reports and feature requests
- **Contributing**: Pull requests welcome for theme improvements
- **Migration Support**: Contact us for help upgrading from manual Analytiq Pages setups

## How This Fits Into Your Stack

Analytiq Pages Theme transforms our proven methodology into a professional, reusable solution that makes building beautiful company websites accessible to everyone. Whether you're launching a startup, building client sites, or managing enterprise web presence, this theme delivers the perfect balance of simplicity and power.

Ready to upgrade your web presence? Try Analytiq Pages Theme today!

---

*This theme powers the very website you're reading now. Experience the Analytiq Pages Theme in action and see the [source code](https://github.com/analytiq-hub/analytiq-hub.github.io) for implementation examples.*

*📢 [Join the discussion on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7367581674697629697/) about modern Jekyll themes and web development workflows.*
