#!/usr/bin/env python3
"""Static checks for local Jekyll content when Ruby is unavailable."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_SUFFIXES = {".md", ".html"}
SKIP_NAMES = {"README.md", "AGENTS.md", "CLAUDE.md", "SVG_STYLING_GUIDE.md", "LICENSE"}
SKIP_DIRS = {".git", ".jekyll-cache", ".sass-cache", "_site", "vendor"}
URL_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)|(?:src|href)=[\"']([^\"']+)[\"']")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
FENCED_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
GENERATED_PATHS = {
    "/feed.xml",
    "/assets/js/excalidraw/render-excalidraw.js",
}
PLACEHOLDER_RE = re.compile(
    r"\b(yourusername|yourrepo|yourcompany|analytiq-pages-starter)\b",
    re.IGNORECASE,
)
PLACEHOLDER_CHECK_FILES = {
    ROOT / "README.md",
    ROOT / "_config.yml",
}


def content_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in CONTENT_SUFFIXES:
            continue
        if path.name in SKIP_NAMES or SKIP_DIRS.intersection(path.parts):
            continue
        files.append(path)
    return sorted(files)


def parse_front_matter(path: Path) -> dict[str, str]:
    match = FRONT_MATTER_RE.match(path.read_text(encoding="utf-8", errors="ignore"))
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def generated_paths(files: list[Path]) -> set[str]:
    paths = {"/", "/404.html"}
    for path in files:
        relative = path.relative_to(ROOT)
        front_matter = parse_front_matter(path)
        permalink = front_matter.get("permalink")
        if permalink:
            normalized = permalink if permalink.startswith("/") else f"/{permalink}"
            paths.add(normalized.rstrip("/") or "/")
            paths.add(f"{normalized.rstrip('/')}/")
            continue
        if "_posts" in relative.parts:
            # This repo config uses /:categories/:title/; uncategorized posts use /title/.
            title = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
            categories = front_matter.get("categories", "").split()
            prefix = "/" + "/".join(categories) if categories else ""
            paths.add(f"{prefix}/{title}/")
            continue
        if path.name == "index.md":
            paths.add("/")
        else:
            stem_path = "/" + str(relative.with_suffix(""))
            paths.add(stem_path)
            paths.add(f"{stem_path}/")
            paths.add("/" + str(relative.with_suffix(".html")))
    return paths


def is_external_or_template(link: str) -> bool:
    return (
        link.startswith(("http://", "https://", "mailto:", "tel:", "#"))
        or "{{" in link
        or "{%" in link
    )


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


def main() -> int:
    files = content_files()
    pages = generated_paths(files)
    failures: list[str] = []

    for path in sorted(PLACEHOLDER_CHECK_FILES):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if PLACEHOLDER_RE.search(text):
            failures.append(f"{path.relative_to(ROOT)}: starter placeholder remains")

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        text_without_examples = INLINE_CODE_RE.sub("", FENCED_BLOCK_RE.sub("", text))
        for match in URL_RE.finditer(text_without_examples):
            link = next(group for group in match.groups() if group)
            if is_external_or_template(link):
                continue
            if not check_local_link(link, pages):
                failures.append(f"{path.relative_to(ROOT)}: missing local link {link}")

        front_matter = parse_front_matter(path)
        image = front_matter.get("image")
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
