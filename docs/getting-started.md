---
layout: docs
title: Getting Started
permalink: /docs/getting-started/
---

Welcome! This guide will help you get your Analytiq Pages Starter site up and running in just a few minutes.

## Quick Start

Creating a company website requires only two steps:

1. **Click "Use this template"** to fork the repository along with its built-in GitHub Action workflow
2. **Enable GitHub Pages** in Settings → Pages, and re-run the Action pipeline to build the site

That's it! Your site will be live at `https://yourusername.github.io/repo-name/` once the workflow completes.

## Basic Configuration

### 1. Update Site Information

Edit `_config.yml` to customize your site:

```yaml
title: Your Company Name
author:
  name: Your Name
  email: "hello@yourcompany.com"
description: Your company description
```

### 2. Update Repository URL

Set your GitHub repository URL:

```yaml
repository: yourusername/your-repo-name
```

### 3. Customize Navigation

Edit the `header_pages` section in `_config.yml` to customize your navigation menu:

```yaml
header_pages:
  - title: "Products"
    url: "#"
    children:
      - title: "Overview"
        url: "/products"
      - title: "Features"
        url: "/features"
```

### 4. Add Social Media Links

Configure social links in `_config.yml`:

```yaml
social_links:
  twitter: yourcompany
  github: yourcompany
  linkedin: yourcompany
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

## Creating Your First Page

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

## Creating Your First Blog Post

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

4. **Create a splash image** (see [User Guide](/docs/user-guide/) for details)

## Common Issues

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

### Changes Not Appearing

- Restart the Jekyll server
- Clear browser cache
- Check for syntax errors in `_config.yml` (YAML is sensitive to indentation)

## Next Steps

Now that you're set up, explore these resources:

- [User Guide](/docs/user-guide/) - Comprehensive guide to customization and content management
- [Architecture](/docs/architecture/) - Technical details and project structure
- [API Reference](/docs/api-reference/) - Configuration reference

## Need Help?

- Check the [User Guide](/docs/user-guide/) for detailed customization options
- Review [Jekyll Documentation](https://jekyllrb.com/docs/)
- Check the [Theme Repository](https://github.com/analytiq-hub/analytiq-pages-theme)
- [Contact support](/contact/)

---

Ready to customize your site? Continue to the [User Guide](/docs/user-guide/).
