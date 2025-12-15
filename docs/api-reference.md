---
layout: docs
title: API Reference
permalink: /docs/api-reference/
---

This reference documents the configuration and template APIs available in the Analytiq Pages Starter. Since this is a static site generator, there are no REST APIs—instead, this documents the configuration options, front matter fields, Liquid template variables, and includes available for customizing your site.

## Site Configuration API (`_config.yml`)

The `_config.yml` file configures your entire site. All settings are available as `site.*` variables in templates.

### Site Metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Site title displayed in header and meta tags |
| `author.name` | string | No | Author name for blog posts |
| `author.email` | string | No | Author email address |
| `description` | string | No | Site description for SEO |
| `baseurl` | string | No | Base URL for site (empty for root) |
| `url` | string | No | Full site URL (defaults to GitHub Pages URL) |
| `repository` | string | No | GitHub repository (format: `org/repo`) |

**Example:**
```yaml
title: Your Company Name
author:
  name: Your Name
  email: "hello@yourcompany.com"
description: Your company description
repository: yourorg/yourrepo
```

### Theme Configuration

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `theme` | string | Yes | Theme name (must be `analytiq-pages-theme`) |

**Example:**
```yaml
theme: analytiq-pages-theme
```

### Navigation API

#### Header Navigation (`header_pages`)

Configure the main navigation menu:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Menu item label |
| `url` | string | Yes | URL or `"#"` for dropdown |
| `children` | array | No | Submenu items |
| `button_style` | string | No | `"solid"` to render as button |

**Example:**
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
    button_style: "solid"
```

#### Footer Sitemap (`site_map`)

Configure footer navigation:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Section title |
| `links` | array | Yes | Array of link objects with `title` and `url` |

**Example:**
```yaml
site_map:
  - title: "Products"
    links:
      - title: "Overview"
        url: "/products"
```

### Collections API

Configure Jekyll collections (like blog posts):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `output` | boolean | No | Generate HTML files (default: `false`) |
| `permalink` | string | No | URL pattern for collection items |

**Example:**
```yaml
collections:
  posts:
    output: true
    permalink: /:categories/:title/
```

### Pagination API

Configure blog pagination using `jekyll-paginate-v2`:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `enabled` | boolean | Yes | Enable pagination |
| `per_page` | integer | Yes | Posts per page |
| `permalink` | string | No | URL pattern (default: `/page/:num/`) |
| `sort_field` | string | No | Field to sort by (default: `date`) |
| `sort_reverse` | boolean | No | Reverse sort order (default: `true`) |
| `trail.before` | integer | No | Pages before current in trail |
| `trail.after` | integer | No | Pages after current in trail |

**Example:**
```yaml
pagination:
  enabled: true
  per_page: 5
  permalink: '/page/:num/'
  sort_field: 'date'
  sort_reverse: true
  trail:
    before: 2
    after: 2
```

### Plugins API

List enabled Jekyll plugins:

| Plugin | Description |
|--------|-------------|
| `jekyll-feed` | Generates RSS feed for blog posts |
| `jekyll-seo-tag` | Adds SEO meta tags to pages |
| `jekyll-pdf-embed` | Allows embedding PDF files |
| `jekyll-paginate-v2` | Advanced pagination for blog |

**Example:**
```yaml
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-pdf-embed
  - jekyll-paginate-v2
```

## Front Matter API

Front matter defines page metadata and is available as `page.*` variables in templates.

### Common Front Matter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `layout` | string | Yes | Layout template to use |
| `title` | string | Yes | Page title |
| `permalink` | string | No | Custom URL path |
| `description` | string | No | Page description for SEO |
| `image` | string | No | Featured image URL |

### Page Layout Front Matter

For standard pages (`layout: page`):

```yaml
---
layout: page
title: Services
permalink: /services/
description: Our service offerings
---
```

### Post Layout Front Matter

For blog posts (`layout: post`):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `date` | datetime | Yes | Publication date |
| `categories` | array/string | No | Space-separated categories |
| `author` | string | No | Author name |
| `image` | string | No | Post preview image |

**Example:**
```yaml
---
layout: post
title: "Your Post Title"
date: 2025-11-29 10:00:00 -0400
categories: engineering api
author: "Author Name"
image: /assets/images/blog/image.svg
---
```

### Docs Layout Front Matter

For documentation pages (`layout: docs`):

```yaml
---
layout: docs
title: Troubleshooting
permalink: /docs/troubleshooting/
---
```

## Liquid Template API

Liquid is the templating language used by Jekyll. Variables and filters are available in all templates.

### Site Variables

Access site configuration:

| Variable | Description |
|----------|-------------|
| `site.title` | Site title from `_config.yml` |
| `site.description` | Site description |
| `site.author` | Author object |
| `site.header_pages` | Header navigation array |
| `site.posts` | All blog posts collection |

**Example:**
```liquid
{% raw %}<h1>{{ site.title }}</h1>
<p>{{ site.description }}</p>{% endraw %}
```

### Page Variables

Access current page data:

| Variable | Description |
|----------|-------------|
| `page.title` | Page title from front matter |
| `page.url` | Page URL path |
| `page.date` | Page/post date |
| `page.categories` | Post categories array |
| `page.content` | Page content (markdown rendered) |

**Example:**
```liquid
{% raw %}<h1>{{ page.title }}</h1>
<div>{{ page.content }}</div>{% endraw %}
```

### Common Liquid Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `relative_url` | Convert to relative URL | `{% raw %}{{ '/about' \| relative_url }}{% endraw %}` |
| `date` | Format date | `{% raw %}{{ page.date \| date: "%B %d, %Y" }}{% endraw %}` |
| `markdownify` | Convert markdown to HTML | `{% raw %}{{ content \| markdownify }}{% endraw %}` |
| `strip_html` | Remove HTML tags | `{% raw %}{{ content \| strip_html }}{% endraw %}` |
| `truncate` | Limit text length | `{% raw %}{{ content \| truncate: 200 }}{% endraw %}` |
| `slugify` | Convert to URL slug | `{% raw %}{{ title \| slugify }}{% endraw %}` |
| `where` | Filter array | `{% raw %}{{ site.posts \| where: "category", "engineering" }}{% endraw %}` |
| `sort` | Sort array | `{% raw %}{{ site.posts \| sort: "date" }}{% endraw %}` |
| `first` | Get first item | `{% raw %}{{ site.posts \| first }}{% endraw %}` |
| `last` | Get last item | `{% raw %}{{ site.posts \| last }}{% endraw %}` |

### Pagination Variables

Available on paginated pages:

| Variable | Description |
|----------|-------------|
| `paginator.page` | Current page number |
| `paginator.per_page` | Posts per page |
| `paginator.posts` | Posts for current page |
| `paginator.total_posts` | Total number of posts |
| `paginator.total_pages` | Total number of pages |
| `paginator.previous_page` | Previous page number (or `nil`) |
| `paginator.next_page` | Next page number (or `nil`) |
| `paginator.previous_page_path` | Path to previous page |
| `paginator.next_page_path` | Path to next page |

**Example:**
```liquid
{% raw %}{% for post in paginator.posts %}
  <article>
    <h2>{{ post.title }}</h2>
    {{ post.content }}
  </article>
{% endfor %}

{% if paginator.next_page %}
  <a href="{{ paginator.next_page_path }}">Next Page</a>
{% endif %}{% endraw %}
```

## Include API

Theme includes are reusable components. Override them by creating files in `_includes/`.

### Excalidraw Includes

#### `excalidraw-static.html`

Render Excalidraw diagram as static SVG.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | string | Yes | Path to `.excalidraw` file |

**Example:**
```liquid
{% include excalidraw-static.html file="/assets/excalidraw/diagram.excalidraw" %}
```

#### `excalidraw.html`

Smart Excalidraw embed with multiple rendering modes.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | string | Yes | Path to `.excalidraw` file |
| `mode` | string | No | `"static"` (default), `"interactive"`, or `"link"` |
| `width` | string | No | Width for interactive mode (default: `"100%"`) |
| `height` | string | No | Height for interactive mode (default: `"600px"`) |

**Example:**
```liquid
{% include excalidraw.html file="/assets/excalidraw/diagram.excalidraw" mode="static" %}
```

### Custom Includes

Create custom includes in `_includes/`:

**Example (`_includes/custom-head.html`):**
```html
<style>
  /* Custom CSS */
</style>
```

Automatically included by theme's `head.html`.

## Layout API

Available layouts and their usage:

### `default`

Standard page layout with header and footer.

**Usage:**
```yaml
---
layout: default
title: Home
---
```

### `page`

Content-focused page layout.

**Usage:**
```yaml
---
layout: page
title: About
permalink: /about/
---
```

### `post`

Blog post layout with date, author, and categories.

**Usage:**
```yaml
---
layout: post
title: "Post Title"
date: 2025-11-29 10:00:00 -0400
categories: engineering
---
```

### `docs`

Documentation layout with sidebar navigation.

**Usage:**
```yaml
---
layout: docs
title: Getting Started
permalink: /docs/getting-started/
---
```

### `excalidraw-editor`

Excalidraw diagram editor layout.

**Usage:**
```yaml
---
layout: excalidraw-editor
permalink: /excalidraw-edit
---
```

## Collections API

### Posts Collection

The `posts` collection contains blog posts.

**Access in templates:**
```liquid
{% raw %}{% for post in site.posts %}
  <h2>{{ post.title }}</h2>
{% endfor %}{% endraw %}
```

**Post properties:**
- `post.title` - Post title
- `post.date` - Publication date
- `post.categories` - Categories array
- `post.author` - Author name
- `post.image` - Preview image URL
- `post.url` - Post URL
- `post.content` - Post content
- `post.excerpt` - Post excerpt

## Pagination API

Pagination is configured in `_config.yml` and available via `paginator` object.

**Access paginated posts:**
```liquid
{% raw %}{% for post in paginator.posts %}
  <!-- Post content -->
{% endfor %}{% endraw %}
```

**Pagination controls:**
```liquid
{% raw %}{% if paginator.previous_page %}
  <a href="{{ paginator.previous_page_path }}">Previous</a>
{% endif %}

Page {{ paginator.page }} of {{ paginator.total_pages }}

{% if paginator.next_page %}
  <a href="{{ paginator.next_page_path }}">Next</a>
{% endif %}{% endraw %}
```

## Error Handling

### Configuration Errors

If `_config.yml` has syntax errors:

- Jekyll build will fail
- Check YAML syntax (indentation, quotes)
- Validate with online YAML validator

### Template Errors

If Liquid templates have errors:

- Jekyll will show error messages during build
- Check for unclosed tags: `{% raw %}{% if %}...{% endif %}{% endraw %}`
- Verify variable names match front matter

### Common Issues

| Issue | Solution |
|-------|----------|
| Variable not found | Check spelling and ensure it exists in front matter or `_config.yml` |
| Filter error | Verify filter syntax and input type |
| Include not found | Check file exists in `_includes/` or theme |
| Layout not found | Verify layout exists in theme or create override |

## Best Practices

### Configuration

- Use consistent indentation (2 spaces)
- Quote strings with special characters
- Group related settings with comments
- Keep sensitive data out of `_config.yml`

### Front Matter

- Always include `layout` and `title`
- Use `permalink` for consistent URLs
- Add `description` for SEO
- Use kebab-case for permalinks

### Templates

- Use `relative_url` filter for internal links
- Escape user content: `{% raw %}{{ content \| escape }}{% endraw %}`
- Check for nil values: `{% raw %}{% if variable %}...{% endif %}{% endraw %}`
- Use includes for reusable components

---

## Additional Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [Analytiq Pages Theme](https://github.com/analytiq-hub/analytiq-pages-theme)
- [Getting Started Guide](/docs/getting-started/)
- [User Guide](/docs/user-guide/)
- [Architecture](/docs/architecture/)
