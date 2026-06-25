#!/usr/bin/env python3
"""Static checks for local Jekyll content when Ruby is unavailable."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTENT_SUFFIXES = {".md", ".html"}
SKIP_NAMES = {"README.md", "AGENTS.md", "CLAUDE.md", "SVG_STYLING_GUIDE.md", "LICENSE"}
SKIP_DIRS = {".git", ".jekyll-cache", ".sass-cache", "_site", "vendor"}
URL_RE = re.compile(
    r"\[[^\]]+\]\(([^)]+)\)|(?:action|href|src)=[\"']([^\"']+)[\"']",
    re.IGNORECASE,
)
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
FENCED_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
POST_URL_RE = re.compile(r"{%\s*post_url\s+([^%\s]+)\s*%}")
POST_FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-.+\.md$")
GENERATED_PATHS = {
    "/feed.xml",
    "/assets/js/excalidraw/render-excalidraw.js",
}
PLACEHOLDER_RE = re.compile(
    r"\b(yourusername|yourrepo|yourcompany|analytiq-pages-starter)\b",
    re.IGNORECASE,
)
LIVE_PAGE_PLACEHOLDER_RE = re.compile(
    r"\b(Speaker Name|https?://example\.com(?:/[^)\s\"']*)?)\b",
    re.IGNORECASE,
)
PLACEHOLDER_CHECK_FILES = {
    ROOT / "README.md",
    ROOT / "_config.yml",
}
CONFIG = ROOT / "_config.yml"
CNAME = ROOT / "CNAME"
ALLOWED_LAYOUTS = {"default", "docs", "excalidraw-editor", "page", "post"}


def content_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in CONTENT_SUFFIXES:
            continue
        if path.name in SKIP_NAMES or SKIP_DIRS.intersection(path.parts):
            continue
        files.append(path)
    return sorted(files)


def parse_front_matter(path: Path) -> dict[str, Any]:
    match = FRONT_MATTER_RE.match(path.read_text(encoding="utf-8", errors="ignore"))
    if not match:
        return {}
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        return {}
    return data


def front_matter_string(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip().strip('"').strip("'")


def front_matter_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        return [item for item in value.split() if item]
    return []


def generated_paths_for_file(path: Path) -> set[str]:
    relative = path.relative_to(ROOT)
    front_matter = parse_front_matter(path)
    permalink = front_matter_string(front_matter.get("permalink"))
    if permalink:
        normalized = permalink if permalink.startswith("/") else f"/{permalink}"
        return {normalized.rstrip("/") or "/", f"{normalized.rstrip('/')}/"}
    if "_posts" in relative.parts:
        # This repo config uses /:categories/:title/; uncategorized posts use /title/.
        title = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
        categories = front_matter_list(front_matter.get("categories"))
        prefix = "/" + "/".join(categories) if categories else ""
        return {f"{prefix}/{title}/"}
    if path.name == "index.md":
        return {"/"}
    stem_path = "/" + str(relative.with_suffix(""))
    return {stem_path, f"{stem_path}/", "/" + str(relative.with_suffix(".html"))}


def generated_paths(files: list[Path]) -> set[str]:
    paths = {"/", "/404.html"}
    for path in files:
        paths.update(generated_paths_for_file(path))
    return paths


def is_external_or_template(link: str) -> bool:
    return (
        link.startswith(("http://", "https://", "mailto:", "tel:", "#"))
        or "{{" in link
        or "{%" in link
    )


def external_url_error(link: str) -> str | None:
    if not link.startswith(("http://", "https://")):
        return None
    parsed = urlparse(link)
    if not parsed.netloc:
        return "must include a host"
    return None


def check_local_link(link: str, pages: set[str]) -> bool:
    clean = link.split("#", 1)[0].split("?", 1)[0]
    if not clean:
        return True
    if clean.startswith("/"):
        if clean in GENERATED_PATHS:
            return True
        candidate = ROOT / clean.lstrip("/")
        if candidate.exists():
            return True
        normalized = clean.rstrip("/") or "/"
        return normalized in pages or f"{normalized}/" in pages
    candidate = ROOT / clean
    return candidate.exists()


def collect_nav_links(items: object) -> list[str]:
    links: list[str] = []
    if isinstance(items, list):
        for item in items:
            links.extend(collect_nav_links(item))
        return links
    if not isinstance(items, dict):
        return links
    url = items.get("url")
    if isinstance(url, str):
        links.append(url)
    links.extend(collect_nav_links(items.get("children")))
    links.extend(collect_nav_links(items.get("links")))
    return links


def site_url_host(site_url: str) -> str:
    parsed = urlparse(site_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return ""
    if parsed.path not in {"", "/"} or parsed.params or parsed.query or parsed.fragment:
        return ""
    return parsed.hostname or ""


def main() -> int:
    files = content_files()
    pages = generated_paths(files)
    failures: list[str] = []

    path_sources: dict[str, Path] = {}
    for path in files:
        for generated_path in generated_paths_for_file(path):
            if generated_path in path_sources:
                failures.append(
                    f"{path.relative_to(ROOT)}: generated path {generated_path} "
                    f"duplicates {path_sources[generated_path].relative_to(ROOT)}"
                )
            else:
                path_sources[generated_path] = path

    for path in sorted(PLACEHOLDER_CHECK_FILES):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if PLACEHOLDER_RE.search(text):
            failures.append(f"{path.relative_to(ROOT)}: starter placeholder remains")

    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
    if CNAME.is_file():
        custom_domain = CNAME.read_text(encoding="utf-8").strip().lower()
        configured_host = site_url_host(front_matter_string(config.get("url"))).lower()
        if not custom_domain:
            failures.append("CNAME: custom domain is empty")
        elif "/" in custom_domain or ":" in custom_domain:
            failures.append("CNAME: custom domain must be a bare hostname")
        elif not configured_host:
            failures.append("_config.yml: url must be an absolute root URL")
        elif configured_host != custom_domain:
            failures.append(
                f"_config.yml: url host {configured_host} does not match CNAME {custom_domain}"
            )

    for link in collect_nav_links(config.get("header_pages")) + collect_nav_links(
        config.get("site_map")
    ):
        if error := external_url_error(link):
            failures.append(f"_config.yml: external navigation URL {link} {error}")
            continue
        if is_external_or_template(link):
            continue
        if not check_local_link(link, pages):
            failures.append(f"_config.yml: missing navigation target {link}")

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        text_without_examples = INLINE_CODE_RE.sub("", FENCED_BLOCK_RE.sub("", text))
        for post_ref in POST_URL_RE.findall(text_without_examples):
            post_path = ROOT / "_posts" / f"{post_ref}.md"
            if not post_path.is_file():
                failures.append(f"{path.relative_to(ROOT)}: missing post_url target {post_ref}")

        for match in URL_RE.finditer(text_without_examples):
            link = next(group for group in match.groups() if group)
            if link == "#" and path.parent == ROOT:
                failures.append(f"{path.relative_to(ROOT)}: live page placeholder link remains")
                continue
            if error := external_url_error(link):
                failures.append(
                    f"{path.relative_to(ROOT)}: external URL {link} {error}"
                )
                continue
            if is_external_or_template(link):
                continue
            if not check_local_link(link, pages):
                failures.append(f"{path.relative_to(ROOT)}: missing local link {link}")

        if path.parent == ROOT and LIVE_PAGE_PLACEHOLDER_RE.search(text_without_examples):
            failures.append(f"{path.relative_to(ROOT)}: live page placeholder remains")

        front_matter = parse_front_matter(path)
        relative = path.relative_to(ROOT)
        layout = front_matter_string(front_matter.get("layout"))
        if not layout and "_includes" not in relative.parts:
            failures.append(f"{relative}: missing front matter layout")
        elif layout and layout not in ALLOWED_LAYOUTS:
            failures.append(f"{relative}: unknown front matter layout {layout}")
        if "_posts" in relative.parts:
            filename_match = POST_FILENAME_RE.match(path.name)
            front_matter_date = front_matter_string(front_matter.get("date"))
            if not filename_match:
                failures.append(f"{relative}: post filename must start with YYYY-MM-DD")
            elif not front_matter_date.startswith(filename_match.group(1)):
                failures.append(
                    f"{relative}: filename date does not match front matter date"
                )
        image = front_matter_string(front_matter.get("image"))
        if image and (error := external_url_error(image)):
            failures.append(
                f"{path.relative_to(ROOT)}: external front matter image {image} {error}"
            )
            continue
        if image and not is_external_or_template(image) and not check_local_link(image, pages):
            failures.append(f"{path.relative_to(ROOT)}: missing front matter image {image}")

    if failures:
        for failure in failures:
            print(f"FAIL\t{failure}")
        return 1
    print(f"PASS\tchecked {len(files)} content files and {len(pages)} generated paths")
    return 0


if __name__ == "__main__":
    sys.exit(main())
