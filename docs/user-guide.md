---
layout: docs
title: User Guide
permalink: /docs/user-guide/
---

This comprehensive guide covers customization and content management for your Analytiq Pages Starter site.

## Table of Contents

- [Site Configuration](#site-configuration)
- [Local Development](#local-development)
- [Project Structure](#project-structure)
- [Adding Pages](#adding-pages)
- [Managing Blog Posts](#managing-blog-posts)
- [Customizing Navigation](#customizing-navigation)
- [Working with Assets](#working-with-assets)
- [Deployment](#deployment)
- [Customization Options](#customization-options)

## Site Configuration

### Basic Settings

Edit `_config.yml` to configure your site:

```yaml
# Site Metadata
title: Your Company Name
author:
  name: Your Name
  email: "hello@yourcompany.com"
description: Your company description

# Theme
theme: analytiq-pages-theme
```

### Social Media Links

Add social media links in `_config.yml`:

```yaml
social_links:
  twitter: yourcompany
  github: yourcompany
  linkedin: yourcompany
```

### Update Repository URL

Set your GitHub repository URL in `_config.yml`:

```yaml
repository: yourusername/your-repo-name
```

This is used for generating edit links and other GitHub-related features.

### Footer Sitemap

Configure the footer navigation:

```yaml
site_map:
  - title: "Products"
    links:
      - title: "Overview"
        url: "/products"
      - title: "Features"
        url: "/features"
```

## Local Development

### Prerequisites

Before you can run the site locally, make sure you have the following installed:

- **Ruby** 3.2 or later ([Install Ruby](https://www.ruby-lang.org/en/documentation/installation/))
- **Bundler** gem (`gem install bundler`)
- **Git** for version control
- **Make** (optional but recommended - see installation instructions below)

**Verify your installation:**
```bash
ruby --version  # Should be 3.2 or later
bundle --version
git --version
make --version
```

### Installing Dependencies

Once prerequisites are installed, install the project dependencies:

1. **Install Ruby dependencies**:
   ```bash
   bundle install
   ```
   This installs Jekyll and all required gems specified in the `Gemfile`.

2. **Install Make (optional but recommended)**:
   
   Make is a build automation tool that simplifies running common commands. It's usually pre-installed on Linux and macOS, but you may need to install it on Windows.
   
   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt-get install make
   ```
   
   **macOS:**
   Make is pre-installed. If you need to update it, install via Homebrew:
   ```bash
   brew install make
   ```
   
   **Windows:**
   - Install via [Chocolatey](https://chocolatey.org/): `choco install make`
   - Or use [GnuWin32](http://gnuwin32.sourceforge.net/packages/make.htm)
   - Or use WSL (Windows Subsystem for Linux) which includes make

### Starting the Server

Once dependencies are installed, use one of these methods:

**Using Make (recommended):**
```bash
make serve
```

**Using Bundler directly:**
```bash
bundle exec jekyll serve
```

**With live reload:**
```bash
bundle exec jekyll serve --livereload
```

The site will be available at **http://localhost:4000**

### Building for Production

To build the site without running a server:

```bash
bundle exec jekyll build
```

The generated site will be in the `_site/` directory.

### Other Useful Commands

```bash
# Clean the build directory
bundle exec jekyll clean

# Build and serve (using Make)
make build
make serve
```

## Project Structure

Understanding the key directories:

```
analytiq-pages-starter/
├── _config.yml          # Site configuration
├── _includes/           # Custom includes (overrides theme)
├── _posts/              # Blog posts
├── docs/                # Documentation pages
├── assets/              # Static assets (images, diagrams)
│   ├── excalidraw/     # Excalidraw diagram files
│   └── images/         # Image files
├── *.md                 # Root-level pages
└── Gemfile              # Ruby dependencies
```

## Adding Pages

### Creating a New Page

1. **Create a new markdown file** at the root (e.g., `services.md`)

2. **Add front matter**:
   ```yaml
   ---
   layout: page
   title: Services
   permalink: /services/
   ---
   ```

3. **Add your content** in Markdown below the front matter

4. **Add to navigation** in `_config.yml` under `header_pages`

### Page Layouts

Available layouts:

- **`default`**: Standard page layout with header and footer
- **`page`**: Content-focused page layout
- **`post`**: Blog post layout
- **`docs`**: Documentation layout with sidebar

### Adding Documentation Pages

1. Create markdown file in `docs/` directory (e.g., `docs/troubleshooting.md`)
2. Set front matter:

```yaml
---
layout: docs
title: Troubleshooting
permalink: /docs/troubleshooting/
---
```

3. Add link to `_includes/docs-widget.html` navigation
4. Content will automatically use docs layout with sidebar

## Managing Blog Posts

### Creating a Blog Post

1. **Create a file** in `_posts/` with format: `YYYY-MM-DD-title.md`

2. **Add front matter**:
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

3. **Write your content** in Markdown

4. **Create a splash image** - Blog posts should include a custom SVG splash image. See the SVG Styling Guide in the repository for details on creating splash images.

5. Post will appear on blog page and in RSS feed

### Post Categories

Organize posts by category:

- Categories are space-separated in front matter
- Posts appear under `/category-name/` URLs
- Categories are displayed as badges on the blog listing

### Post Images

Add images to blog posts:

1. Place images in `assets/images/blog/`
2. Reference in front matter: `image: /assets/images/blog/image.svg`
3. Images appear as previews on the blog listing page

## Customizing Navigation

### Header Navigation

Configure multi-level dropdown menus in `_config.yml`:

```yaml
header_pages:
  - title: "Products"
    url: "#"
    children:
      - title: "Overview"
        url: "/products"
      - title: "Features"
        url: "/features"
  - title: "Get Started"
    url: "/contact"
    button_style: "solid"  # Makes it a button
```

### Documentation Sidebar

Customize the docs sidebar by editing `_includes/docs-widget.html`:

```html
<a href="/docs/your-page/"
   class="flex items-center px-2 py-1 text-xs text-gray-700 hover:text-blue-600">
  Your Page Name
</a>
```

## Working with Assets

### Images

Store images in `assets/images/`:

- **Blog images**: `assets/images/blog/`
- **General images**: `assets/images/`
- **Logo**: `assets/images/logo.png`

Reference images in Markdown:

```markdown
![Alt text](/assets/images/image.png)
```

### Excalidraw Diagrams

To add an Excalidraw diagram:

1. Create diagram file in `assets/excalidraw/` (e.g., `my-diagram.excalidraw`)
2. Reference it in markdown:

```liquid
{% include excalidraw-static.html file="/assets/excalidraw/my-diagram.excalidraw" %}
```

3. The theme's JavaScript will render it automatically

### PDF Documents

Embed PDF files using the `jekyll-pdf-embed` plugin:

```markdown
{% pdf "/path/to/document.pdf" %}
```

## Deployment

### GitHub Pages (Recommended)

The repository includes a GitHub Actions workflow for automatic deployment:

1. **Push your code** to the `main` branch
2. **Enable GitHub Pages**:
   - Go to your repository **Settings** → **Pages**
   - Under "Source", select **GitHub Actions**
3. **The workflow will automatically build and deploy** your site
4. Your site will be live at `https://yourusername.github.io/repo-name/`

The workflow (`.github/workflows/pages.yml`) will:
- Build your Jekyll site
- Deploy it to GitHub Pages
- Run automatically on every push to `main`

### Manual Deployment

You can also deploy manually:

1. Build the site: `bundle exec jekyll build`
2. Upload the `_site/` directory to your hosting provider

## Customization Options

### Overriding Theme Components

You can override any theme file by creating a file with the same path:

**Override Includes:**
- Create `_includes/filename.html` in your site
- Example: `_includes/docs-widget.html` (already included)

**Override Layouts:**
- Create `_layouts/filename.html` in your site
- Extend theme layouts as needed

### Custom CSS

Add custom styles by creating `_includes/custom-head.html`:

```html
<style>
  /* Your custom CSS */
  .my-custom-class {
    color: blue;
  }
</style>
```

This file is automatically included by the theme's `head.html`.

### Custom JavaScript

Add custom scripts via includes:

1. Create `_includes/custom-footer.html`
2. Add your script tags:

```html
<script>
  // Your custom JavaScript
</script>
```

### Contact Form Setup

The contact form requires a form submission service:

1. Choose a service:
   - [Formspree](https://formspree.io/)
   - [Netlify Forms](https://www.netlify.com/products/forms/)
   - [Getform](https://getform.io/)

2. Update the form action in `contact.md`:

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

## Content Best Practices

### Markdown Formatting

Use standard Markdown syntax:

- **Bold**: `**text**`
- *Italic*: `*text*`
- Links: `[text](url)`
- Code: `` `code` `` or code blocks with triple backticks

### Front Matter

Always include essential front matter:

- `layout`: Page layout type
- `title`: Page title
- `permalink`: URL path (optional but recommended)

### File Naming

- Use kebab-case for file names: `my-page.md`
- Blog posts must start with date: `YYYY-MM-DD-title.md`
- Use descriptive names

## Advanced Customization

### Pagination

Configure pagination in `_config.yml`:

```yaml
pagination:
  enabled: true
  per_page: 5
  permalink: '/page/:num/'
```

### Collections

The starter uses a `posts` collection. You can add more:

```yaml
collections:
  posts:
    output: true
    permalink: /:categories/:title/
  your_collection:
    output: true
```

### SEO Optimization

The theme includes `jekyll-seo-tag` for automatic SEO:

- Meta tags are generated automatically
- Open Graph tags for social sharing
- Twitter Card support

Customize in front matter:

```yaml
---
title: Page Title
description: Page description for SEO
image: /assets/images/og-image.png
---
```

## Troubleshooting

### Bundle Install Fails

If you encounter issues installing gems:

```bash
# Update bundler
gem update bundler

# Try installing again
bundle install
```

### Port Already in Use

If port 4000 is already in use:

```bash
bundle exec jekyll serve --port 4001
```

### Styles Not Applying

- Clear Jekyll cache: `bundle exec jekyll clean`
- Check for syntax errors in overridden files
- Verify Tailwind CDN is loading in browser dev tools

### Content Not Updating

- Restart Jekyll server: `bundle exec jekyll serve`
- Clear browser cache
- Check for syntax errors in Markdown
- Check for syntax errors in `_config.yml` (YAML is sensitive to indentation)

### Navigation Not Showing

- Verify `header_pages` configuration in `_config.yml`
- Check file paths are correct
- Ensure pages exist at specified URLs

---

**Need more details?** Check out the [Architecture](/docs/architecture/) guide or [API Reference](/docs/api-reference/).
