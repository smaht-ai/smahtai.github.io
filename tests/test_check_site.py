from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = ROOT / "scripts" / "check_site.py"


spec = importlib.util.spec_from_file_location("check_site", CHECKER_PATH)
assert spec is not None
check_site = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(check_site)


def test_local_paths_reject_parent_directory_escapes(
    tmp_path: Path,
    monkeypatch,
) -> None:
    site_root = tmp_path / "site"
    site_root.mkdir()
    outside = tmp_path / "outside.md"
    outside.write_text("outside\n", encoding="utf-8")
    monkeypatch.setattr(check_site, "ROOT", site_root)

    assert not check_site.check_local_link("../outside.md", set())
    assert not check_site.check_local_link("/../outside.md", set())
    assert not check_site.check_local_file("../outside.md")


def test_local_paths_reject_backslash_escapes(
    tmp_path: Path,
    monkeypatch,
) -> None:
    site_root = tmp_path / "site"
    site_root.mkdir()
    monkeypatch.setattr(check_site, "ROOT", site_root)

    assert not check_site.check_local_link(r"..\outside.md", set())
    assert not check_site.check_local_link(r"/assets\..\outside.md", set())
    assert not check_site.check_local_file(r"assets\image.png")


def test_local_paths_reject_protocol_relative_urls(
    tmp_path: Path,
    monkeypatch,
) -> None:
    site_root = tmp_path / "site"
    asset = site_root / "assets" / "image.png"
    asset.parent.mkdir(parents=True)
    asset.write_bytes(b"png")
    monkeypatch.setattr(check_site, "ROOT", site_root)

    assert not check_site.check_local_link("//assets/image.png", set())
    assert not check_site.check_local_file("//assets/image.png")


def test_local_paths_reject_uri_schemes_and_drive_labels(
    tmp_path: Path,
    monkeypatch,
) -> None:
    site_root = tmp_path / "site"
    asset = site_root / "assets" / "image.png"
    asset.parent.mkdir(parents=True)
    asset.write_bytes(b"png")
    monkeypatch.setattr(check_site, "ROOT", site_root)

    assert not check_site.check_local_link("file:assets/image.png", set())
    assert not check_site.check_local_link("C:/assets/image.png", set())
    assert not check_site.check_local_file("file:assets/image.png")


def test_local_paths_reject_encoded_aliases(
    tmp_path: Path,
    monkeypatch,
) -> None:
    site_root = tmp_path / "site"
    asset = site_root / "assets" / "image.png"
    asset.parent.mkdir(parents=True)
    asset.write_bytes(b"png")
    monkeypatch.setattr(check_site, "ROOT", site_root)

    assert not check_site.check_local_link("%2e%2e/outside.md", set())
    assert not check_site.check_local_link("assets%2fimage.png", set())
    assert not check_site.check_local_link("assets/image%2epng", set())
    assert not check_site.check_local_file("assets/image%zz")


def test_external_urls_reject_unsafe_spelling() -> None:
    assert check_site.external_url_error("https://example.com/bad path") == (
        "must not include whitespace"
    )
    assert check_site.external_url_error("https://example.com/bad%20path") == (
        "must not include encoded whitespace"
    )
    assert check_site.external_url_error("https://example.com/bad%2520path") == (
        "must not include encoded whitespace"
    )
    assert check_site.external_url_error(r"https://example.com\bad") == (
        "must not include backslashes"
    )
    assert check_site.external_url_error("https://example.com/%5cbad") == (
        "must not include encoded backslashes"
    )
    assert check_site.external_url_error("https://example.com/%255cbad") == (
        "must not include encoded backslashes"
    )
    assert check_site.external_url_error("https://example.com/%zz") == (
        "must not include malformed percent encoding"
    )
    assert check_site.external_url_error("https://example.com/%25zz") == (
        "must not include malformed percent encoding"
    )
    assert check_site.external_url_error("https://example.com/%7fname") == (
        "must not include encoded control characters"
    )
    assert check_site.external_url_error("https://example.com/%257fname") == (
        "must not include encoded control characters"
    )


def test_external_url_errors_skip_liquid_templates() -> None:
    assert (
        check_site.external_url_error("https://github.com/{{ site.repository }}")
        is None
    )


def test_local_paths_accept_files_inside_site_root(
    tmp_path: Path,
    monkeypatch,
) -> None:
    site_root = tmp_path / "site"
    asset = site_root / "assets" / "image.png"
    asset.parent.mkdir(parents=True)
    asset.write_bytes(b"png")
    monkeypatch.setattr(check_site, "ROOT", site_root)

    assert check_site.check_local_link("/assets/image.png", set())
    assert check_site.check_local_file("assets/image.png")
