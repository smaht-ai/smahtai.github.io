---
layout: post
title: "Build Your Company Website with Analytiq Pages"
date: 2025-08-30
author: Andrei Radulescu-Banu
mathjax: false
image: /assets/images/analytiq_pages.png
categories: [webdev, jekyll, tailwind, github-pages, company-website]
---

Setting up a professional company website shouldn't require a team of developers or expensive hosting solutions. **Analytiq Pages** is our streamlined approach to building beautiful, fast company websites using GitHub Pages, Jekyll, and Tailwind CSS - completely free and with enterprise-grade reliability.

📢 [Join the Analytiq Pages discussion on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7367581674697629697/)

## Why Analytiq Pages?

After building numerous company websites and helping startups establish their web presence, we've distilled the best practices into a reproducible system that delivers:

- **Zero hosting costs** with GitHub Pages
- **Professional design** with Tailwind CSS
- **Easy content creation** using Markdown
- **Git sandbox** edited with Claude Code, Cursor to create content and visualizations
- **Fast deployment** with git-based workflows
- **Enterprise reliability** backed by GitHub's infrastructure

## The Analytiq Pages Stack

<div class="grid md:grid-cols-3 gap-8 my-8">
  <div class="bg-white rounded-lg shadow-lg p-6 border border-gray-200">
    <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center mb-4">
      <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
      </svg>
    </div>
    <h3 class="text-xl font-semibold text-gray-900 mb-3">GitHub Pages</h3>
    <p class="text-gray-600">Free, reliable hosting with enterprise-grade infrastructure</p>
  </div>

  <div class="bg-white rounded-lg shadow-lg p-6 border border-gray-200">
    <div class="w-12 h-12 bg-red-600 rounded-lg flex items-center justify-center mb-4">
      <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
        <path d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.024-.105-.949-.199-2.403.041-3.439.219-.937 1.404-5.965 1.404-5.965s-.359-.72-.359-1.781c0-1.663.967-2.911 2.168-2.911 1.024 0 1.518.769 1.518 1.688 0 1.029-.653 2.567-.992 3.992-.285 1.193.6 2.165 1.775 2.165 2.128 0 3.768-2.245 3.768-5.487 0-2.861-2.063-4.869-5.008-4.869-3.41 0-5.409 2.562-5.409 5.199 0 1.033.394 2.143.889 2.747.099.12.112.225.085.345-.09.375-.293 1.199-.334 1.363-.053.225-.172.271-.402.165-1.495-.69-2.433-2.878-2.433-4.646 0-3.776 2.748-7.252 7.92-7.252 4.158 0 7.392 2.967 7.392 6.923 0 4.135-2.607 7.462-6.233 7.462-1.214 0-2.357-.629-2.747-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24.009 12.017 24c6.624 0 11.99-5.367 11.99-11.987C24.007 5.367 18.641.001 12.017.001z"/>
      </svg>
    </div>
    <h3 class="text-xl font-semibold text-gray-900 mb-3">Jekyll</h3>
    <p class="text-gray-600">Write content in simple Markdown</p>
  </div>

  <div class="bg-white rounded-lg shadow-lg p-6 border border-gray-200">
    <div class="w-12 h-12 bg-cyan-500 rounded-lg flex items-center justify-center mb-4">
      <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
        <path d="M12.001,4.8c-3.2,0-5.2,1.6-6,4.8c1.2-1.6,2.6-2.2,4.2-1.8c0.913,0.228,1.565,0.89,2.288,1.624 C13.666,10.618,15.027,12,18.001,12c3.2,0,5.2-1.6,6-4.8c-1.2,1.6-2.6,2.2-4.2,1.8c-0.913-0.228-1.565-0.89-2.288-1.624 C16.337,6.182,14.976,4.8,12.001,4.8z M6.001,12c-3.2,0-5.2,1.6-6,4.8c1.2-1.6,2.6-2.2,4.2-1.8c0.913,0.228,1.565,0.89,2.288,1.624 c1.177,1.194,2.538,2.576,5.512,2.576c3.2,0,5.2-1.6,6-4.8c-1.2,1.6-2.6,2.2-4.2,1.8c-0.913-0.228-1.565-0.89-2.288-1.624 C10.337,13.382,8.976,12,6.001,12z"/>
      </svg>
    </div>
    <h3 class="text-xl font-semibold text-gray-900 mb-3">Tailwind CSS</h3>
    <p class="text-gray-600">Embed HTML+Tailwind directly in Markdown for sophisticated layouts</p>
  </div>
</div>

## Setting Up Your Company Website

The fastest way to get started is by using our reference implementation at [analytiqhub.com](https://analytiqhub.com/) as your starting point. This site demonstrates all the Analytiq Pages features in action and serves as a complete template for your company website. You'll clone this proven foundation and customize it with your branding, content, and specific requirements.

Let's walk through creating a professional company website using the Analytiq Pages approach.

### Step 1: Repository Setup

Start by forking the Analytiq Pages reference implementation:

1. **Fork the repository**: Go to [https://github.com/analytiq-hub/analytiq-hub.github.io](https://github.com/analytiq-hub/analytiq-hub.github.io) and click "Fork"
2. **Rename your fork**: In your forked repository settings, rename it to `your-company.github.io`
3. **Clone for local development**:

```bash
# Clone your forked repository
git clone https://github.com/your-company/your-company.github.io.git
cd your-company.github.io
```

### Step 2: Customize for Your Company

Replace all Analytiq Hub references with your company information:

**Key files to update:**

1. **`_config.yml`** - Site configuration:
```yaml
title: Your Company Name
email: contact@yourcompany.com
description: Your company description
baseurl: ""
url: "http://your-company.github.io"
github_username: yourcompany
```

2. **`index.md`** - Homepage content
3. **`about.md`** - Company information  
4. **`_posts/`** - Replace sample blog posts with your content
5. **`assets/images/`** - Replace logos and images
6. **`CNAME`** - Update with your custom domain (if using one)

**GitHub Pages setup:**
- Go to your repository Settings → Pages
- Set source to "Deploy from a branch" → main
- Add custom domain if you have one

The forked template already includes Tailwind CSS configuration, so your site is ready to run locally with `make dev` or deploy immediately to GitHub Pages.

### Step 3: Local Development Setup

Install [local development prerequisites](https://analytiqhub.com/docs/local_development) and start developing locally:

```bash
# Install dependencies
make install

# Start development server
make dev
```

For complete setup instructions including Ruby, Bundler, and troubleshooting, see the full [Local Development Setup guide](https://analytiqhub.com/docs/local_development).

Point your web browser to the local development server at [http://localhost:4000](http://localhost:4000). 

After editing files in the sandbox, manually or with Claude Code, Cursor or the preferred AI editor, they are automatically refreshed on the development server. 
* Changes to the menu or the footing require a restart of the local development server.
* When later the github pages pipeline is setup, a push of local changes will trigger the web site update at https://your-company.github.io

### Step 4: Essential Company Pages

Update the core pages with your company information:
- **`index.md`** - Homepage with compelling hero section and company value proposition
- **`about.md`** - Company story, team information, and mission
- **`contact.md`** - Contact information and inquiry forms

### Step 5: Header and Footer Customization

Start by configuring your site navigation in **`_config.yml`**:

```yaml
# Header navigation menu
header_pages:
  - title: "Services"
    url: "#"
    children:
      - title: "Consulting"
        url: "/consulting"
      - title: "Development"
        url: "/development"
  - title: "Case Studies"
    url: "/case-studies"
  - title: "Blog"
    url: "/blog"
  - title: "About"
    url: "/about"
  - title: "Contact"
    url: "/contact"
    button_style: "solid"

# Footer sitemap
site_map:
  - title: "Services"
    links:
      - title: "Consulting"
        url: "/consulting"
      - title: "Case Studies"
        url: "/case-studies"
  - title: "Company"
    links:
      - title: "About"
        url: "/about"
      - title: "Contact"
        url: "/contact"
```

Then customize the visual elements:
- **`_includes/custom-header.html`** - Company logo, announcements, search
- **`_includes/custom-footer.html`** - Contact info, social links, legal pages

### Step 6: Blog Setup

Jekyll's blog functionality is ready out of the box:
- Create posts in `_posts/` using the format: `YYYY-MM-DD-post-title.md`
- Posts automatically appear on your homepage and `/blog` page
- Use front matter to set title, author, categories, and featured images

### Step 7: Case Studies

Showcase your work with detailed case studies:
- Add case studies to the `_case_studies/` collection
- Use the case study template for consistent formatting
- Include client results, project images, and key outcomes

### Step 8: (Advanced) Custom Components

The template includes Tailwind-powered components for:
- Call-to-action sections
- Team member profiles  
- Service feature cards
- Client testimonials

Your AI editor can help create custom components by combining Jekyll's liquid templating with Tailwind's utility classes.

### Step 9: (Advanced) Custom Layouts

Create specialized page layouts by extending the base templates:
- **`_layouts/landing.html`** - For marketing campaigns and product launches
- **`_layouts/portfolio.html`** - Showcase projects with image galleries
- **`_layouts/team.html`** - Team member profiles with bios and photos

Copy existing layouts as starting points and modify with your specific content structure and Tailwind styling.

## Deployment and Domain Setup

### GitHub Pages Configuration

1. **Enable GitHub Pages** in repository settings
2. **Set source** to "Deploy from a branch" → main
3. **Custom domain**: Add your company domain in settings

### Domain Configuration

**DNS Setup:**
```
# For apex domain (company.com)
A record: 185.199.108.153
A record: 185.199.109.153
A record: 185.199.110.153
A record: 185.199.111.153

# For www subdomain
CNAME record: your-company.github.io
```

**CNAME File:**
```bash
echo "your-company.com" > CNAME
```

## Analytiq Pages Best Practices

### Content Strategy
- **Homepage**: Clear value proposition and call-to-action
- **About**: Company story and team credibility
- **Services/Products**: Detailed offering descriptions
- **Blog**: Regular insights to build authority
- **Contact**: Multiple ways to reach you

### SEO Foundation
- **Meta descriptions**: Add to each page's front matter
- **Google Analytics**: Add tracking code to `_includes/custom-head.html`

## Maintenance and Updates

The beauty of Analytiq Pages is its simplicity:

```bash
# Update content
git add .
git commit -m "Update company blog post"
git push origin main
# Site updates automatically within minutes
```

## Why Companies Choose Analytiq Pages

* **Startups**: Get online fast without burning budget on hosting or developers
* **Agencies**: Deliver professional sites quickly for clients
* **Enterprise**: Maintain security and compliance with git-based workflows
* **Content Teams**: Edit in Markdown without technical dependencies

## Conclusion

Analytiq Pages combines the best of modern web development - GitHub's reliability, Markdown simplicity, and Tailwind's design power - into a streamlined system perfect for company websites. Whether you're launching a startup or refreshing an enterprise web presence, this approach delivers professional results without the complexity.

Ready to build your company website? Check out our [Analytiq Pages starter template](https://github.com/analytiq-hub/analytiq-pages) or [contact us](/contact) for custom implementation support.

---

*Want to see Analytiq Pages in action? This very website was built using these exact techniques. View the [source code](https://github.com/analytiq-hub/analytiq-hub.github.io) to see how we implement our own recommendations.*