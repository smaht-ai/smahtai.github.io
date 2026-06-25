# Smaht.ai Website

Static Jekyll site for [smaht.ai](https://smaht.ai), the public home for the
Smaht.ai AI engineering and entrepreneurship community.

The site is built with the `analytiq-pages-theme` theme and published through
GitHub Pages from this repository.

## Local Checks

Ruby and Bundler are optional for the lightweight content audit:

```sh
make check
```

The checker validates local links, front matter image references, generated
Jekyll paths that the source content expects, and obvious starter-template
placeholder drift in repository-level site metadata. It also verifies that the
GitHub Pages `CNAME` custom domain matches the canonical `url` in `_config.yml`.

When Ruby dependencies are available, run the full Jekyll build:

```sh
make install
make build
```

## Editing

- Primary pages live at the repository root, such as `index.md`, `about.md`,
  `technology.md`, and `contact.md`.
- Blog posts live in `_posts/`.
- Site configuration, navigation, social links, and GitHub Pages metadata live
  in `_config.yml`.
- Images live under `assets/images/`.
- Excalidraw source diagrams live under `assets/excalidraw/`; rendered assets
  are checked in under `assets/images/` when used by pages or posts.

Do not leave starter-template placeholder values in live site metadata.
