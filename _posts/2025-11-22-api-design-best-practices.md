---
layout: post
title: "Configuration API Design: Making Static Sites Configurable"
date: 2025-11-22 14:00:00 -0400
categories: engineering jekyll
author: "Engineering Team"
image: /assets/images/blog/api-design.svg
---

While static sites don't have REST APIs, they do have configuration APIs—the interfaces through which developers customize and extend the site. In Jekyll-based sites like Analytiq Pages Starter, good configuration design is crucial for usability and maintainability.

## What is a Configuration API?

In static site generators, the configuration API includes:

- **Site configuration** (`_config.yml`): Global settings and metadata
- **Front matter**: Page-specific configuration
- **Template variables**: Data available in Liquid templates
- **Includes**: Reusable components with parameters

## Design Principles

### 1. Clear and Intuitive Structure

Configuration should be self-documenting:

```yaml
# Good: Clear, hierarchical structure
header_pages:
  - title: "Products"
    url: "#"
    children:
      - title: "Overview"
        url: "/products"

# Bad: Flat, unclear structure
nav_products_title: "Products"
nav_products_url: "/products"
```

### 2. Sensible Defaults

Provide defaults that work out of the box:

```yaml
# Theme provides sensible defaults
theme: analytiq-pages-theme

# Pagination has reasonable defaults
pagination:
  enabled: true
  per_page: 5  # Not too many, not too few
```

### 3. Consistent Naming Conventions

Use consistent patterns throughout:

- **kebab-case** for URLs: `/docs/getting-started/`
- **snake_case** for YAML keys: `header_pages`, `site_map`
- **camelCase** for JavaScript variables (if needed)

### 4. Type Safety Through Documentation

Document expected types clearly:

```yaml
# Site Configuration API
title: string          # Required
author:
  name: string         # Optional
  email: string        # Optional
pagination:
  enabled: boolean     # Required
  per_page: integer    # Required
```

## Front Matter API Design

Front matter provides page-specific configuration:

### Essential Fields

Every page should have:

```yaml
---
layout: page          # Required: Which template to use
title: Page Title     # Required: Page title
permalink: /page/     # Recommended: Explicit URL
---
```

### Optional but Useful

```yaml
---
description: SEO description
image: Featured image URL
categories: Content organization
---
```

## Template Variable API

Make data easily accessible in templates:

### Site-Wide Variables

```liquid
{{ site.title }}           # Site title
{{ site.description }}     # Site description
{{ site.header_pages }}    # Navigation structure
{{ site.posts }}           # All blog posts
```

### Page Variables

```liquid
{{ page.title }}           # Page title
{{ page.url }}            # Page URL
{{ page.content }}        # Page content
{{ page.date }}           # Publication date
```

### Pagination Variables

```liquid
{{ paginator.page }}              # Current page
{{ paginator.total_pages }}       # Total pages
{{ paginator.next_page_path }}    # Next page URL
```

## Include API Design

Includes should be flexible and well-documented:

### Parameter Documentation

```liquid
{% comment %}
  Parameters:
    - file: (required) Path to .excalidraw file
    - mode: (optional) "static", "interactive", or "link"
{% endcomment %}
{% include excalidraw.html file="/path/to/file.excalidraw" mode="static" %}
```

### Sensible Defaults

```liquid
# Works with just required parameter
{% include excalidraw-static.html file="/diagram.excalidraw" %}

# Optional parameters enhance functionality
{% include excalidraw.html file="/diagram.excalidraw" mode="interactive" height="800px" %}
```

## Error Handling

### Clear Error Messages

When configuration is invalid:

```yaml
# Jekyll will show clear errors:
# "Liquid Exception: Invalid syntax for include tag"
# "Configuration file contains invalid YAML"
```

### Validation Patterns

- **Required fields**: Document clearly, fail fast if missing
- **Type checking**: Use appropriate YAML types
- **Value validation**: Check ranges, formats where applicable

## Documentation Best Practices

### Provide Examples

Every configuration option should have examples:

```yaml
# Example: Multi-level navigation
header_pages:
  - title: "Products"
    url: "#"
    children:
      - title: "Overview"
        url: "/products"
```

### Show Common Patterns

Document typical use cases:

```yaml
# Pattern: Simple page
---
layout: page
title: About
permalink: /about/
---

# Pattern: Blog post
---
layout: post
title: "Post Title"
date: 2025-11-29 10:00:00 -0400
categories: engineering
---
```

## Versioning and Compatibility

### Backward Compatibility

When adding new configuration options:

- Make them optional with sensible defaults
- Don't break existing configurations
- Document migration paths for breaking changes

### Theme Versioning

```yaml
# Gemfile
gem "analytiq-pages-theme",
    git: "https://github.com/analytiq-hub/analytiq-pages-theme.git",
    tag: "v0.1.8"  # Pin to specific version
```

## Real-World Example: Analytiq Pages Starter

The Analytiq Pages Starter demonstrates these principles:

### Clean Configuration Structure

```yaml
# Site metadata (clear, required fields)
title: Your Company Name
author:
  name: Your Name
  email: "hello@yourcompany.com"

# Navigation (hierarchical, intuitive)
header_pages:
  - title: "Products"
    children:
      - title: "Overview"
        url: "/products"

# Pagination (sensible defaults)
pagination:
  enabled: true
  per_page: 5
```

### Well-Documented APIs

- [API Reference](/docs/api-reference/) documents all configuration options
- Examples for every major feature
- Clear parameter tables with types and descriptions

## Conclusion

Good configuration API design makes static sites more maintainable and easier to customize. By following these principles—clear structure, sensible defaults, consistent naming, and comprehensive documentation—you create an interface that's both powerful and approachable.

Check out our [API Reference](/docs/api-reference/) to see these principles in action with the Analytiq Pages Starter.

---

*Posted by Engineering Team on November 22, 2025*
