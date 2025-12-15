---
layout: post
title: "Markdown Feature Test: Comprehensive Testing"
date: 2025-11-29 10:00:00 -0400
categories: testing documentation
author: "Documentation Team"
image: /assets/images/blog/markdown-test.svg
---

This blog post serves as a comprehensive test of all Markdown features available in Jekyll. It demonstrates formatting, syntax, and rendering capabilities.

## Headers

All header levels are demonstrated below:

# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

## Text Formatting

### Basic Formatting

- **Bold text** using double asterisks
- *Italic text* using single asterisks
- ***Bold and italic*** using triple asterisks
- ~~Strikethrough text~~ using double tildes
- `Inline code` using backticks
- <mark>Highlighted text</mark> using HTML

### Emphasis Variations

- **Bold** (alternative: __Bold__)
- *Italic* (alternative: _Italic_)
- ***Bold Italic*** (alternative: ___Bold Italic___)

## Lists

### Unordered Lists

- First item
- Second item
- Third item
  - Nested item 1
  - Nested item 2
    - Deeply nested item
- Fourth item

### Ordered Lists

1. First numbered item
2. Second numbered item
3. Third numbered item
   1. Nested numbered item
   2. Another nested item
4. Fourth numbered item

### Mixed Lists

1. Ordered item with unordered sub-items
   - Unordered sub-item 1
   - Unordered sub-item 2
2. Another ordered item
   - More unordered items
   - And another

### Task Lists

- [x] Completed task
- [x] Another completed task
- [ ] Incomplete task
- [ ] Another incomplete task
  - [x] Nested completed task
  - [ ] Nested incomplete task

### Definition Lists

Term 1
: Definition 1
: Alternative definition 1

Term 2
: Definition 2 with *italic* and **bold** text
: Another definition for term 2

## Links

### Inline Links

- [Link to Google](https://www.google.com)
- [Link with title](https://www.example.com "Example Website")
- [Relative link to about page](/about/)
- [Link to another blog post](/engineering/best-practices/building-scalable-systems/)

### Reference-Style Links

This is a [reference link][ref1] and here's [another one][ref2].

[ref1]: https://www.example.com "Example Reference"
[ref2]: /docs/getting-started/ "Getting Started Guide"

### Auto-links

- https://www.github.com
- <https://www.github.com>
- <user@example.com>

## Images

### Basic Image

![Alt text for image](/assets/images/blog/welcome.svg)

### Image with Title

![Scalable Systems](/assets/images/blog/scalable-systems.svg "Scalable Systems Architecture")

### Reference-Style Image

![API Design][api-image]

[api-image]: /assets/images/blog/api-design.svg "API Design Diagram"

## Code Blocks

### Inline Code

Use `console.log()` to output to the console. The `process.env.NODE_ENV` variable controls the environment.

### Code Blocks with Syntax Highlighting

#### JavaScript

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}

const user = "World";
console.log(greet(user));
```

#### Python

```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Usage
for num in fibonacci(100):
    print(num)
```

#### YAML

```yaml
site:
  title: "My Site"
  author:
    name: "John Doe"
    email: "john@example.com"
  pagination:
    enabled: true
    per_page: 10
```

#### JSON

```json
{
  "name": "Markdown Test",
  "version": "1.0.0",
  "features": [
    "headers",
    "lists",
    "code blocks",
    "tables"
  ]
}
```

#### HTML

```html
<div class="container">
  <h1>Hello World</h1>
  <p>This is a <strong>test</strong> paragraph.</p>
</div>
```

#### CSS

```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
  font-size: 2rem;
}
```

#### Shell/Bash

```bash
#!/bin/bash
echo "Installing dependencies..."
npm install
echo "Building project..."
npm run build
```

#### SQL

```sql
SELECT 
  users.id,
  users.name,
  COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
HAVING COUNT(orders.id) > 5;
```

#### Ruby

```ruby
class BlogPost
  attr_accessor :title, :content, :date
  
  def initialize(title, content, date)
    @title = title
    @content = content
    @date = date
  end
  
  def published?
    @date <= Date.today
  end
end
```

#### Liquid Template

```liquid
{% if page.title %}
  <h1>{{ page.title }}</h1>
{% endif %}

{% for post in site.posts limit:5 %}
  <article>
    <h2>{{ post.title }}</h2>
    <p>{{ post.excerpt }}</p>
  </article>
{% endfor %}
```

### Code Block Without Language

```
This is a plain code block
without syntax highlighting.
It preserves formatting and spacing.
```

## Blockquotes

### Simple Blockquote

> This is a simple blockquote.
> It can span multiple lines.
> Each line starts with `>`.

### Nested Blockquotes

> This is the outer blockquote.
> 
> > This is a nested blockquote.
> > It can go multiple levels deep.
> 
> Back to the outer blockquote.

### Blockquote with Formatting

> This blockquote contains **bold text**, *italic text*, and `inline code`.
> 
> It can also contain:
> - Lists
> - Multiple items
> - And more

### Blockquote with Code

> Here's a code example in a blockquote:
> 
> ```python
> print("Hello from blockquote!")
> ```

## Tables

### Basic Table

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data 1   | Data 2   |
| Row 2    | Data 3   | Data 4   |
| Row 3    | Data 5   | Data 6   |

### Table with Alignment

| Left Aligned | Center Aligned | Right Aligned |
|:-------------|:--------------:|--------------:|
| Left         | Center         | Right         |
| More left    | More center    | More right    |
| Even more    | Even more      | Even more     |

### Table with Formatting

| Feature | Status | Notes |
|---------|--------|-------|
| **Bold** | ✅ Working | *Italic* works too |
| `Code` | ✅ Working | Inline code renders |
| [Link](/) | ✅ Working | Links are clickable |
| ~~Strikethrough~~ | ✅ Working | Text can be struck |

### Complex Table

| Language | Type | Year | Popularity |
|:---------|:----:|:----:|:----------:|
| JavaScript | Dynamic | 1995 | ⭐⭐⭐⭐⭐ |
| Python | Dynamic | 1991 | ⭐⭐⭐⭐⭐ |
| Java | Static | 1995 | ⭐⭐⭐⭐ |
| C++ | Static | 1985 | ⭐⭐⭐⭐ |
| Ruby | Dynamic | 1995 | ⭐⭐⭐ |

## Horizontal Rules

Three or more hyphens, asterisks, or underscores create a horizontal rule:

---

***

___

## Escaped Characters

Special characters can be escaped with backslashes:

- \*Not italic\*
- \**Not bold\**
- \`Not code\`
- \[Not a link\]
- \# Not a header

## HTML Elements

### Basic HTML

<div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
  This is a <strong>div</strong> with custom styling.
</div>

### HTML Lists

<ul style="list-style-type: square;">
  <li>Custom styled list item 1</li>
  <li>Custom styled list item 2</li>
</ul>

### HTML Details/Summary

<details>
  <summary>Click to expand</summary>
  
  This is hidden content that appears when you click the summary.
  
  - It can contain lists
  - And other markdown
  - **Including formatting**
</details>

### HTML Abbreviations

<abbr title="HyperText Markup Language">HTML</abbr> and <abbr title="Cascading Style Sheets">CSS</abbr> are web technologies.

## Math (if supported)

Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

## Footnotes

Here's a sentence with a footnote[^1]. And another reference[^2].

[^1]: This is the first footnote.
[^2]: This is the second footnote with **bold** and *italic* text.

## Line Breaks

This line ends with two spaces.  
This creates a line break.

This line ends normally.
This continues on the same line.

## Special Characters and Entities

- Copyright: ©
- Trademark: ™
- Registered: ®
- Em dash: —
- En dash: –
- Ellipsis: …
- Less than: <
- Greater than: >
- Ampersand: &

## Mixed Content Example

Here's a paragraph with **bold**, *italic*, `code`, and a [link](https://example.com).

1. First item with **bold** text
2. Second item with *italic* text
   - Nested item with `code`
   - Another nested item
3. Third item

> This is a blockquote with:
> - A list
> - **Bold text**
> - `Inline code`
> 
> And a code block:
> 
> ```javascript
> console.log("Hello!");
> ```

## Liquid Template Examples

### Escaped Liquid Code

When documenting Liquid syntax, use `{% raw %}` tags:

{% raw %}
```liquid
{{ site.title }}
{% if page.title %}
  <h1>{{ page.title }}</h1>
{% endif %}
```
{% endraw %}

### Actual Liquid Code

The site title is: {{ site.title }}

{% if page.title %}
This page has a title: **{{ page.title }}**
{% endif %}

## Excalidraw Diagram

Here's an example of embedding an Excalidraw diagram:

{% include excalidraw-static.html file="/assets/excalidraw/analytiq-pages-architecture.excalidraw" %}

<div class="text-sm text-gray-500 mt-2 mb-6 text-center">
  <a href="{{ '/excalidraw-edit' | relative_url }}?file={{ '/assets/excalidraw/analytiq-pages-architecture.excalidraw' | relative_url }}" 
     class="text-gray-500 hover:text-gray-700 no-underline" 
     target="_blank">
    Edit diagram
  </a>
</div>

## Long Content Test

This section tests how the markdown renderer handles longer content blocks. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

## Conclusion

This post demonstrates all major Markdown features including:

- ✅ Headers (all 6 levels)
- ✅ Text formatting (bold, italic, strikethrough)
- ✅ Lists (ordered, unordered, nested, task lists)
- ✅ Links (inline, reference, auto-links)
- ✅ Images (inline, reference)
- ✅ Code blocks (with and without syntax highlighting)
- ✅ Blockquotes (simple, nested, with formatting)
- ✅ Tables (basic, aligned, formatted)
- ✅ Horizontal rules
- ✅ Escaped characters
- ✅ HTML elements
- ✅ Footnotes
- ✅ Line breaks
- ✅ Special characters
- ✅ Liquid template syntax
- ✅ Excalidraw diagrams

All features should render correctly in the Jekyll static site generator.

---

*Posted by Documentation Team on November 29, 2025*

