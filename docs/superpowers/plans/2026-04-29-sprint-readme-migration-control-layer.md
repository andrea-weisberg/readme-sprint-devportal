# Sprint ReadMe Migration Control Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repeatable migration control layer that inventories the WordPress WXR export and current ReadMe repository, maps published WordPress pages to ReadMe Markdown files, and produces parity and launch-risk reports.

**Architecture:** Add a small stdlib-only Python package under `tools/migration_control/` plus `unittest` coverage under `tests/migration_control/`. The CLI reads the WordPress XML export and the ReadMe repo, writes deterministic CSV and Markdown reports under `review/migration-control/`, and makes no content edits.

**Tech Stack:** Python 3 standard library, `xml.etree.ElementTree`, `argparse`, `csv`, `dataclasses`, `unittest`, existing ReadMe Markdown repository structure.

---

## Scope

This plan implements Phase 1 from `docs/superpowers/specs/2026-04-29-sprint-developer-readme-migration-design.md`: control layer and reports.

It does not rewrite links, repair Markdown, download assets, push to ReadMe, or change production DNS. Those belong in later plans after this control layer creates the migration working surface.

## File Structure

- Create `tools/migration_control/__init__.py`: package marker and version.
- Create `tools/migration_control/models.py`: shared dataclasses for WordPress, ReadMe, parity, and risk rows.
- Create `tools/migration_control/paths.py`: URL, slug, path, and title normalization helpers.
- Create `tools/migration_control/wxr.py`: WordPress WXR parser.
- Create `tools/migration_control/readme_repo.py`: ReadMe repository scanner for Markdown, navigation, links, images, and assets.
- Create `tools/migration_control/review_report.py`: parser for the existing `review/review_report_2026-02-16.md` risk list.
- Create `tools/migration_control/matching.py`: deterministic page matching and parity row generation.
- Create `tools/migration_control/risk.py`: launch-risk queue generation.
- Create `tools/migration_control/writers.py`: CSV and Markdown report writers.
- Create `tools/migration_control/cli.py`: command-line entrypoint.
- Create `tools/migration_control/README.md`: local usage and report descriptions.
- Create `tests/migration_control/test_wxr.py`: WXR parsing coverage.
- Create `tests/migration_control/test_readme_repo.py`: ReadMe scanner coverage.
- Create `tests/migration_control/test_matching.py`: parity matching coverage.
- Create `tests/migration_control/test_risk.py`: launch-risk generation coverage.
- Create `tests/migration_control/test_writers_cli.py`: report writer and CLI smoke coverage.

## Report Outputs

The CLI will write these files under `review/migration-control/`:

- `wordpress_inventory.csv`
- `readme_inventory.csv`
- `parity_map.csv`
- `risk_queue.csv`
- `summary.md`

## Task 1: Add Shared Models And WXR Parser Tests

**Files:**
- Create: `tools/migration_control/__init__.py`
- Create: `tools/migration_control/models.py`
- Create: `tools/migration_control/paths.py`
- Create: `tests/migration_control/test_wxr.py`

- [ ] **Step 1: Create the package marker**

Write `tools/migration_control/__init__.py` with this content:

```python
"""Migration control tools for the Sprint developer portal ReadMe migration."""

__version__ = "0.1.0"
```

- [ ] **Step 2: Add shared dataclasses**

Write `tools/migration_control/models.py` with this content:

```python
"""Shared data models for migration control reports."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class WordPressPage:
    source_id: str
    title: str
    slug: str
    status: str
    url: str
    parent_id: str
    menu_order: int
    content_chars: int
    content_text: str
    acf_keys: Tuple[str, ...]
    links: Tuple[str, ...]
    post_type: str = "page"

    @property
    def launch_scope(self) -> bool:
        return self.post_type == "page" and self.status == "publish"


@dataclass(frozen=True)
class WordPressAttachment:
    source_id: str
    title: str
    url: str
    filename: str
    mime_type: str


@dataclass(frozen=True)
class WordPressExport:
    pages: Tuple[WordPressPage, ...]
    attachments: Tuple[WordPressAttachment, ...]


@dataclass(frozen=True)
class ReadMePage:
    path: str
    title: str
    slug: str
    content_chars: int
    content_text: str
    links: Tuple[str, ...]
    images: Tuple[str, ...]
    legacy_wordpress_links: Tuple[str, ...]


@dataclass(frozen=True)
class ReadMeInventory:
    pages: Tuple[ReadMePage, ...]
    assets: Tuple[str, ...]
    order_entries: Tuple[str, ...]


@dataclass(frozen=True)
class ParityRow:
    wp_id: str
    wp_title: str
    wp_url: str
    wp_slug: str
    wp_status: str
    matched_path: str
    match_kind: str
    match_confidence: float
    migration_status: str
    review_risk: str
    notes: str


@dataclass(frozen=True)
class RiskItem:
    priority: int
    category: str
    file_or_source: str
    message: str
    evidence: str
    recommended_action: str
```

- [ ] **Step 3: Add normalization helpers**

Write `tools/migration_control/paths.py` with this content:

```python
"""Path and slug normalization helpers."""

from __future__ import annotations

import os
import re
from pathlib import Path
from urllib.parse import unquote, urlparse


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def slugify(value: str) -> str:
    cleaned = clean_text(value).lower()
    cleaned = re.sub(r"[^a-z0-9]+", "-", cleaned)
    return cleaned.strip("-")


def normalize_path(value: str) -> str:
    if not value:
        return ""

    parsed = urlparse(value)
    raw_path = parsed.path if parsed.scheme or parsed.netloc else value
    raw_path = unquote(raw_path).split("#", 1)[0].split("?", 1)[0]
    raw_path = raw_path.replace("\\", "/")
    raw_path = re.sub(r"/+", "/", raw_path)
    raw_path = raw_path.strip("/")

    if raw_path.endswith(".html"):
        raw_path = raw_path[:-5]
    if raw_path.endswith("/index"):
        raw_path = raw_path[:-6]

    return raw_path.lower()


def readme_doc_key(markdown_path: str) -> str:
    path = Path(markdown_path)
    parts = path.parts
    if parts and parts[0] == "docs":
        path = Path(*parts[1:])
    path_without_suffix = path.with_suffix("")
    return normalize_path(path_without_suffix.as_posix())


def filename_slug(markdown_path: str) -> str:
    return slugify(Path(markdown_path).stem)


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def resolve_local_target(repo_root: Path, source_file: str, target: str) -> Path:
    target_without_fragment = target.split("#", 1)[0].split("?", 1)[0]
    source_dir = (repo_root / source_file).parent
    return (source_dir / os.path.normpath(target_without_fragment)).resolve()
```

- [ ] **Step 4: Write the failing WXR tests**

Write `tests/migration_control/test_wxr.py` with this content:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.migration_control.wxr import parse_wxr


WXR_FIXTURE = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <item>
      <title>Activate Card</title>
      <link>https://developer.sprint.paymentology.com/profile-api-reference/activate/</link>
      <content:encoded><![CDATA[<p>Use <a href="https://developer.sprint.paymentology.com/card-api/">Card API</a>.</p>]]></content:encoded>
      <wp:post_id>101</wp:post_id>
      <wp:post_name>activate</wp:post_name>
      <wp:status>publish</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>7</wp:post_parent>
      <wp:menu_order>3</wp:menu_order>
      <wp:postmeta>
        <wp:meta_key>api_content_builder_0_request</wp:meta_key>
        <wp:meta_value>request xml</wp:meta_value>
      </wp:postmeta>
    </item>
    <item>
      <title>Draft API</title>
      <link>https://developer.sprint.paymentology.com/draft-api/</link>
      <content:encoded><![CDATA[Draft body]]></content:encoded>
      <wp:post_id>102</wp:post_id>
      <wp:post_name>draft-api</wp:post_name>
      <wp:status>draft</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>0</wp:menu_order>
    </item>
    <item>
      <title>Dispute Form</title>
      <link>https://developer.sprint.paymentology.com/wp-content/uploads/dispute.docx</link>
      <wp:post_id>201</wp:post_id>
      <wp:post_type>attachment</wp:post_type>
      <wp:attachment_url>https://developer.sprint.paymentology.com/wp-content/uploads/dispute.docx</wp:attachment_url>
      <wp:postmeta>
        <wp:meta_key>_wp_attached_file</wp:meta_key>
        <wp:meta_value>2026/04/dispute.docx</wp:meta_value>
      </wp:postmeta>
    </item>
  </channel>
</rss>
"""


class WxrParserTests(TestCase):
    def test_parse_wxr_extracts_pages_attachments_and_acf_keys(self):
        with TemporaryDirectory() as tmp:
            xml_path = Path(tmp) / "export.xml"
            xml_path.write_text(WXR_FIXTURE, encoding="utf-8")

            export = parse_wxr(xml_path)

        self.assertEqual(len(export.pages), 2)
        self.assertEqual(len(export.attachments), 1)

        page = export.pages[0]
        self.assertEqual(page.source_id, "101")
        self.assertEqual(page.title, "Activate Card")
        self.assertEqual(page.slug, "activate")
        self.assertEqual(page.status, "publish")
        self.assertEqual(page.parent_id, "7")
        self.assertEqual(page.menu_order, 3)
        self.assertTrue(page.launch_scope)
        self.assertIn("api_content_builder_0_request", page.acf_keys)
        self.assertEqual(page.links, ("https://developer.sprint.paymentology.com/card-api/",))
        self.assertIn("Use Card API.", page.content_text)

        draft = export.pages[1]
        self.assertFalse(draft.launch_scope)

        attachment = export.attachments[0]
        self.assertEqual(attachment.source_id, "201")
        self.assertEqual(attachment.filename, "dispute.docx")
```

- [ ] **Step 5: Run the WXR tests and confirm they fail for the right reason**

Run:

```bash
python3 -m unittest tests.migration_control.test_wxr -v
```

Expected output includes:

```text
ModuleNotFoundError: No module named 'tools.migration_control.wxr'
```

## Task 2: Implement The WXR Parser

**Files:**
- Create: `tools/migration_control/wxr.py`
- Test: `tests/migration_control/test_wxr.py`

- [ ] **Step 1: Implement the parser**

Write `tools/migration_control/wxr.py` with this content:

```python
"""WordPress WXR export parser."""

from __future__ import annotations

import html
import re
from pathlib import Path
from typing import Iterable, List, Tuple
from xml.etree import ElementTree

from .models import WordPressAttachment, WordPressExport, WordPressPage
from .paths import clean_text


NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp": "http://wordpress.org/export/1.2/",
}

LINK_RE = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")


def parse_wxr(xml_path: Path) -> WordPressExport:
    tree = ElementTree.parse(xml_path)
    root = tree.getroot()

    pages: List[WordPressPage] = []
    attachments: List[WordPressAttachment] = []

    for item in root.findall("./channel/item"):
        post_type = _text(item, "wp:post_type")
        if post_type == "page":
            pages.append(_parse_page(item))
        elif post_type == "attachment":
            attachments.append(_parse_attachment(item))

    return WordPressExport(
        pages=tuple(sorted(pages, key=lambda page: (page.menu_order, page.title.lower(), page.source_id))),
        attachments=tuple(sorted(attachments, key=lambda attachment: attachment.url.lower())),
    )


def _parse_page(item: ElementTree.Element) -> WordPressPage:
    content = _text(item, "content:encoded")
    acf_keys = tuple(sorted(set(_acf_keys(item))))

    return WordPressPage(
        source_id=_text(item, "wp:post_id"),
        title=clean_text(_text(item, "title")),
        slug=clean_text(_text(item, "wp:post_name")),
        status=clean_text(_text(item, "wp:status")),
        url=clean_text(_text(item, "link")),
        parent_id=clean_text(_text(item, "wp:post_parent")),
        menu_order=_int_text(item, "wp:menu_order"),
        content_chars=len(content),
        content_text=_html_to_text(content),
        acf_keys=acf_keys,
        links=tuple(_extract_links(content)),
    )


def _parse_attachment(item: ElementTree.Element) -> WordPressAttachment:
    url = clean_text(_text(item, "wp:attachment_url") or _text(item, "link"))
    filename = Path(url).name

    return WordPressAttachment(
        source_id=_text(item, "wp:post_id"),
        title=clean_text(_text(item, "title")),
        url=url,
        filename=filename,
        mime_type=clean_text(_text(item, "wp:post_mime_type")),
    )


def _text(parent: ElementTree.Element, tag: str) -> str:
    value = parent.findtext(tag, default="", namespaces=NS)
    return value or ""


def _int_text(parent: ElementTree.Element, tag: str) -> int:
    value = clean_text(_text(parent, tag))
    try:
        return int(value)
    except ValueError:
        return 0


def _acf_keys(item: ElementTree.Element) -> Iterable[str]:
    for meta in item.findall("wp:postmeta", NS):
        key = clean_text(_text(meta, "wp:meta_key"))
        if key.startswith("api_content_builder") or key.startswith("_api_content_builder"):
            yield key


def _extract_links(content: str) -> Tuple[str, ...]:
    links = [clean_text(match.group(1)) for match in LINK_RE.finditer(content)]
    return tuple(link for link in links if link)


def _html_to_text(content: str) -> str:
    without_tags = TAG_RE.sub(" ", content)
    return clean_text(html.unescape(without_tags))
```

- [ ] **Step 2: Run the WXR tests and confirm they pass**

Run:

```bash
python3 -m unittest tests.migration_control.test_wxr -v
```

Expected output includes:

```text
test_parse_wxr_extracts_pages_attachments_and_acf_keys ... ok
OK
```

- [ ] **Step 3: Commit WXR parser**

Run:

```bash
git add tools/migration_control/__init__.py tools/migration_control/models.py tools/migration_control/paths.py tools/migration_control/wxr.py tests/migration_control/test_wxr.py
git commit -m "feat: parse wordpress migration export"
```

Expected output includes:

```text
[codex/sprint-readme-migration-design
 5 files changed
```

## Task 3: Add And Implement The ReadMe Repository Scanner

**Files:**
- Create: `tools/migration_control/readme_repo.py`
- Create: `tests/migration_control/test_readme_repo.py`

- [ ] **Step 1: Write the failing ReadMe scanner tests**

Write `tests/migration_control/test_readme_repo.py` with this content:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.migration_control.readme_repo import scan_readme_repo


class ReadMeRepoScannerTests(TestCase):
    def test_scan_readme_repo_extracts_markdown_assets_order_and_links(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs" / "profile-api-reference"
            docs.mkdir(parents=True)
            (root / "assets").mkdir()
            (root / "assets" / "sample.csv").write_text("a,b\n", encoding="utf-8")
            (root / "docs" / "_order.yaml").write_text("- profile-api-reference\n", encoding="utf-8")
            (docs / "activate.md").write_text(
                "---\n"
                "title: Activate Card\n"
                "slug: activate\n"
                "---\n"
                "# Activate Card\n"
                "See [legacy](https://developer.sprint.paymentology.com/card-api/).\n"
                "![Report](../../assets/sample.csv)\n"
                '<img src="../../assets/missing.png" />\n',
                encoding="utf-8",
            )

            inventory = scan_readme_repo(root)

        self.assertEqual(inventory.assets, ("assets/sample.csv",))
        self.assertEqual(inventory.order_entries, ("profile-api-reference",))
        self.assertEqual(len(inventory.pages), 1)

        page = inventory.pages[0]
        self.assertEqual(page.path, "docs/profile-api-reference/activate.md")
        self.assertEqual(page.title, "Activate Card")
        self.assertEqual(page.slug, "activate")
        self.assertIn("https://developer.sprint.paymentology.com/card-api/", page.links)
        self.assertIn("../../assets/sample.csv", page.images)
        self.assertIn("../../assets/missing.png", page.images)
        self.assertEqual(page.legacy_wordpress_links, ("https://developer.sprint.paymentology.com/card-api/",))
```

- [ ] **Step 2: Run the ReadMe scanner tests and confirm they fail for the right reason**

Run:

```bash
python3 -m unittest tests.migration_control.test_readme_repo -v
```

Expected output includes:

```text
ModuleNotFoundError: No module named 'tools.migration_control.readme_repo'
```

- [ ] **Step 3: Implement the scanner**

Write `tools/migration_control/readme_repo.py` with this content:

```python
"""ReadMe repository scanner."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple

from .models import ReadMeInventory, ReadMePage
from .paths import clean_text, filename_slug, relative_posix


MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"""href=["']([^"']+)["']""", re.IGNORECASE)
HTML_IMAGE_RE = re.compile(r"""src=["']([^"']+)["']""", re.IGNORECASE)
ORDER_RE = re.compile(r"^\s*-\s+(.+?)\s*$")
LEGACY_HOST = "developer.sprint.paymentology.com"


def scan_readme_repo(repo_root: Path) -> ReadMeInventory:
    docs_root = repo_root / "docs"
    pages = tuple(_scan_page(repo_root, path) for path in sorted(docs_root.rglob("*.md")))
    assets = tuple(sorted(relative_posix(path, repo_root) for path in (repo_root / "assets").rglob("*") if path.is_file()))
    order_entries = tuple(_scan_order_entries(docs_root))

    return ReadMeInventory(pages=pages, assets=assets, order_entries=order_entries)


def _scan_page(repo_root: Path, path: Path) -> ReadMePage:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _parse_frontmatter(text)
    markdown_links = _clean_targets(MARKDOWN_LINK_RE.findall(body))
    html_links = _clean_targets(HTML_LINK_RE.findall(body))
    markdown_images = _clean_targets(MARKDOWN_IMAGE_RE.findall(body))
    html_images = _clean_targets(HTML_IMAGE_RE.findall(body))
    links = tuple(markdown_links + html_links)
    images = tuple(markdown_images + html_images)
    legacy_links = tuple(link for link in links if LEGACY_HOST in link)
    rel_path = relative_posix(path, repo_root)

    return ReadMePage(
        path=rel_path,
        title=frontmatter.get("title") or _first_heading(body) or path.stem.replace("-", " ").title(),
        slug=frontmatter.get("slug") or filename_slug(rel_path),
        content_chars=len(body),
        content_text=body,
        links=links,
        images=images,
        legacy_wordpress_links=legacy_links,
    )


def _parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    block = text[4:end]
    body = text[end + 5 :]
    data: Dict[str, str] = {}

    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[clean_text(key)] = clean_text(value).strip('"\'')

    return data, body


def _first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return clean_text(line[2:])
    return ""


def _clean_targets(targets: List[str]) -> List[str]:
    cleaned: List[str] = []
    for target in targets:
        value = clean_text(target).strip("<>")
        if value and " " in value:
            value = value.split(" ", 1)[0]
        if value:
            cleaned.append(value)
    return cleaned


def _scan_order_entries(docs_root: Path) -> List[str]:
    entries: List[str] = []
    for order_file in sorted(docs_root.rglob("_order.yaml")):
        for line in order_file.read_text(encoding="utf-8").splitlines():
            match = ORDER_RE.match(line)
            if match:
                entries.append(match.group(1).strip('"\''))
    return entries
```

- [ ] **Step 4: Run the ReadMe scanner tests and confirm they pass**

Run:

```bash
python3 -m unittest tests.migration_control.test_readme_repo -v
```

Expected output includes:

```text
test_scan_readme_repo_extracts_markdown_assets_order_and_links ... ok
OK
```

- [ ] **Step 5: Run WXR and ReadMe tests together**

Run:

```bash
python3 -m unittest tests.migration_control.test_wxr tests.migration_control.test_readme_repo -v
```

Expected output includes:

```text
Ran 2 tests
OK
```

- [ ] **Step 6: Commit ReadMe scanner**

Run:

```bash
git add tools/migration_control/readme_repo.py tests/migration_control/test_readme_repo.py
git commit -m "feat: scan readme migration baseline"
```

Expected output includes:

```text
[codex/sprint-readme-migration-design
 2 files changed
```

## Task 4: Add And Implement Parity Matching

**Files:**
- Create: `tools/migration_control/matching.py`
- Create: `tests/migration_control/test_matching.py`

- [ ] **Step 1: Write the failing matching tests**

Write `tests/migration_control/test_matching.py` with this content:

```python
from unittest import TestCase

from tools.migration_control.matching import build_parity_map
from tools.migration_control.models import ReadMeInventory, ReadMePage, WordPressExport, WordPressPage


def wp_page(source_id, title, slug, url, status="publish"):
    return WordPressPage(
        source_id=source_id,
        title=title,
        slug=slug,
        status=status,
        url=url,
        parent_id="0",
        menu_order=0,
        content_chars=10,
        content_text="body",
        acf_keys=(),
        links=(),
    )


def readme_page(path, title, slug):
    return ReadMePage(
        path=path,
        title=title,
        slug=slug,
        content_chars=10,
        content_text="body",
        links=(),
        images=(),
        legacy_wordpress_links=(),
    )


class MatchingTests(TestCase):
    def test_build_parity_map_matches_by_url_slug_and_title(self):
        export = WordPressExport(
            pages=(
                wp_page("1", "Activate Card", "activate", "https://developer.sprint.paymentology.com/profile-api-reference/activate/"),
                wp_page("2", "Card Detail", "card-detail", "https://developer.sprint.paymentology.com/card-detail/"),
                wp_page("3", "Client Testing Guide", "client-testing", "https://developer.sprint.paymentology.com/client-testing-guide/"),
            ),
            attachments=(),
        )
        inventory = ReadMeInventory(
            pages=(
                readme_page("docs/profile-api-reference/activate.md", "Activate Card", "activate"),
                readme_page("docs/card-api/carddetail.md", "Card Detail", "carddetail"),
                readme_page("docs/Getting Started/client-testing-guide.md", "Client Testing Guide", "client-testing-guide"),
            ),
            assets=(),
            order_entries=(),
        )

        rows = build_parity_map(export, inventory, {})

        self.assertEqual([row.migration_status for row in rows], ["matched", "needs-review", "matched"])
        self.assertEqual(rows[0].matched_path, "docs/profile-api-reference/activate.md")
        self.assertEqual(rows[0].match_kind, "url_path")
        self.assertEqual(rows[1].match_kind, "title")
        self.assertEqual(rows[1].match_confidence, 0.75)
        self.assertEqual(rows[2].match_kind, "title")
        self.assertEqual(rows[2].migration_status, "matched")

    def test_build_parity_map_marks_missing_and_duplicates(self):
        export = WordPressExport(
            pages=(
                wp_page("1", "Missing Page", "missing-page", "https://developer.sprint.paymentology.com/missing-page/"),
                wp_page("2", "Activate", "activate", "https://developer.sprint.paymentology.com/activate/"),
                wp_page("3", "Private Page", "private-page", "https://developer.sprint.paymentology.com/private-page/", "private"),
            ),
            attachments=(),
        )
        inventory = ReadMeInventory(
            pages=(
                readme_page("docs/profile-api-reference/activate.md", "Activate", "activate"),
                readme_page("docs/card-api/activate.md", "Activate", "activate"),
            ),
            assets=(),
            order_entries=(),
        )

        rows = build_parity_map(export, inventory, {})

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0].migration_status, "missing")
        self.assertEqual(rows[1].migration_status, "duplicate")
        self.assertIn("Multiple ReadMe candidates", rows[1].notes)
```

- [ ] **Step 2: Run the matching tests and confirm they fail for the right reason**

Run:

```bash
python3 -m unittest tests.migration_control.test_matching -v
```

Expected output includes:

```text
ModuleNotFoundError: No module named 'tools.migration_control.matching'
```

- [ ] **Step 3: Implement parity matching**

Write `tools/migration_control/matching.py` with this content:

```python
"""WordPress-to-ReadMe parity matching."""

from __future__ import annotations

from collections import defaultdict
from typing import DefaultDict, Dict, Iterable, List, Sequence, Tuple

from .models import ParityRow, ReadMeInventory, ReadMePage, WordPressExport, WordPressPage
from .paths import filename_slug, normalize_path, readme_doc_key, slugify


def build_parity_map(
    wordpress_export: WordPressExport,
    readme_inventory: ReadMeInventory,
    review_risks: Dict[str, str],
) -> Tuple[ParityRow, ...]:
    index = _readme_index(readme_inventory.pages)
    rows: List[ParityRow] = []

    for page in wordpress_export.pages:
        if not page.launch_scope:
            continue

        rows.append(_match_page(page, index, review_risks))

    return tuple(rows)


def mapped_wordpress_paths(rows: Sequence[ParityRow]) -> Dict[str, str]:
    mapped: Dict[str, str] = {}
    for row in rows:
        if row.migration_status in {"matched", "needs-review"} and row.matched_path:
            mapped[normalize_path(row.wp_url)] = row.matched_path
            mapped[normalize_path(row.wp_slug)] = row.matched_path
    return mapped


def _match_page(
    page: WordPressPage,
    index: DefaultDict[str, List[ReadMePage]],
    review_risks: Dict[str, str],
) -> ParityRow:
    duplicate_notes: List[str] = []

    for kind, key, confidence in _wordpress_candidates(page):
        matches = index.get(key, [])
        if len(matches) == 1:
            matched_path = matches[0].path
            status = "needs-review" if confidence < 0.8 else "matched"
            review_risk = review_risks.get(matched_path, "")
            return ParityRow(
                wp_id=page.source_id,
                wp_title=page.title,
                wp_url=page.url,
                wp_slug=page.slug,
                wp_status=page.status,
                matched_path=matched_path,
                match_kind=kind,
                match_confidence=confidence,
                migration_status=status,
                review_risk=review_risk,
                notes="",
            )
        if len(matches) > 1:
            paths = ", ".join(match.path for match in matches)
            duplicate_notes.append(f"{kind}:{key} => {paths}")

    if duplicate_notes:
        return ParityRow(
            wp_id=page.source_id,
            wp_title=page.title,
            wp_url=page.url,
            wp_slug=page.slug,
            wp_status=page.status,
            matched_path="",
            match_kind="duplicate",
            match_confidence=0.0,
            migration_status="duplicate",
            review_risk="high",
            notes="Multiple ReadMe candidates: " + " | ".join(duplicate_notes),
        )

    return ParityRow(
        wp_id=page.source_id,
        wp_title=page.title,
        wp_url=page.url,
        wp_slug=page.slug,
        wp_status=page.status,
        matched_path="",
        match_kind="none",
        match_confidence=0.0,
        migration_status="missing",
        review_risk="high",
        notes="No ReadMe candidate matched URL path, slug, filename, or title.",
    )


def _readme_index(pages: Iterable[ReadMePage]) -> DefaultDict[str, List[ReadMePage]]:
    index: DefaultDict[str, List[ReadMePage]] = defaultdict(list)
    for page in pages:
        for key in _readme_candidates(page):
            if key:
                index[key].append(page)
    return index


def _readme_candidates(page: ReadMePage) -> Tuple[str, ...]:
    return tuple(
        sorted(
            {
                readme_doc_key(page.path),
                normalize_path(page.slug),
                filename_slug(page.path),
                slugify(page.title),
            }
        )
    )


def _wordpress_candidates(page: WordPressPage) -> Tuple[Tuple[str, str, float], ...]:
    url_path = normalize_path(page.url)
    leaf = url_path.rsplit("/", 1)[-1] if url_path else ""

    candidates = [
        ("url_path", url_path, 1.0),
        ("slug", normalize_path(page.slug), 0.9),
        ("url_leaf", leaf, 0.85),
        ("title", slugify(page.title), 0.75),
    ]

    deduped: List[Tuple[str, str, float]] = []
    seen = set()
    for kind, key, confidence in candidates:
        if key and key not in seen:
            deduped.append((kind, key, confidence))
            seen.add(key)
    return tuple(deduped)
```

- [ ] **Step 4: Run the matching tests and confirm they pass**

Run:

```bash
python3 -m unittest tests.migration_control.test_matching -v
```

Expected output includes:

```text
Ran 2 tests
OK
```

- [ ] **Step 5: Run all implemented tests**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected output includes:

```text
Ran 4 tests
OK
```

- [ ] **Step 6: Commit parity matching**

Run:

```bash
git add tools/migration_control/matching.py tests/migration_control/test_matching.py
git commit -m "feat: map wordpress pages to readme docs"
```

Expected output includes:

```text
[codex/sprint-readme-migration-design
 2 files changed
```

## Task 5: Add And Implement Review Report Parsing And Risk Queue

**Files:**
- Create: `tools/migration_control/review_report.py`
- Create: `tools/migration_control/risk.py`
- Create: `tests/migration_control/test_risk.py`

- [ ] **Step 1: Write failing risk queue tests**

Write `tests/migration_control/test_risk.py` with this content:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.migration_control.models import ParityRow, ReadMeInventory, ReadMePage, WordPressExport, WordPressPage
from tools.migration_control.review_report import parse_review_report
from tools.migration_control.risk import generate_risk_queue


def page(path, text="", links=(), images=(), legacy=()):
    return ReadMePage(
        path=path,
        title=Path(path).stem,
        slug=Path(path).stem,
        content_chars=len(text),
        content_text=text,
        links=links,
        images=images,
        legacy_wordpress_links=legacy,
    )


class RiskQueueTests(TestCase):
    def test_parse_review_report_extracts_manual_risk_levels(self):
        markdown = (
            "### High Risk (1)\n"
            "- `docs/profile-api-reference/activate.md` (source: `activate`)\n"
            "\n"
            "### Medium Risk (1)\n"
            "- `docs/Getting Started/security.md` (source: `security`)\n"
        )
        with TemporaryDirectory() as tmp:
            report = Path(tmp) / "review.md"
            report.write_text(markdown, encoding="utf-8")

            risks = parse_review_report(report)

        self.assertEqual(risks["docs/profile-api-reference/activate.md"], "high")
        self.assertEqual(risks["docs/Getting Started/security.md"], "medium")

    def test_generate_risk_queue_flags_missing_sections_links_assets_and_review_pages(self):
        with TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            docs = repo_root / "docs" / "profile-api-reference"
            docs.mkdir(parents=True)
            source_doc = docs / "activate.md"
            source_doc.write_text("body", encoding="utf-8")

            inventory = ReadMeInventory(
                pages=(
                    page(
                        "docs/profile-api-reference/activate.md",
                        text="ICON_URL_1\n```,```xml\nimage.\n",
                        links=("https://developer.sprint.paymentology.com/missing-target/",),
                        images=("../../assets/missing.csv",),
                        legacy=("https://developer.sprint.paymentology.com/missing-target/",),
                    ),
                ),
                assets=(),
                order_entries=("profile-api-reference",),
            )
            export = WordPressExport(
                pages=(
                    WordPressPage(
                        source_id="1",
                        title="Missing Target",
                        slug="missing-target",
                        status="publish",
                        url="https://developer.sprint.paymentology.com/missing-target/",
                        parent_id="0",
                        menu_order=0,
                        content_chars=10,
                        content_text="body",
                        acf_keys=(),
                        links=(),
                    ),
                ),
                attachments=(),
            )
            parity = (
                ParityRow(
                    wp_id="1",
                    wp_title="Missing Target",
                    wp_url="https://developer.sprint.paymentology.com/missing-target/",
                    wp_slug="missing-target",
                    wp_status="publish",
                    matched_path="",
                    match_kind="none",
                    match_confidence=0.0,
                    migration_status="missing",
                    review_risk="high",
                    notes="No match",
                ),
            )

            risks = generate_risk_queue(repo_root, export, inventory, parity, {"docs/profile-api-reference/activate.md": "high"})

        categories = {risk.category for risk in risks}
        self.assertIn("missing_must_keep_section", categories)
        self.assertIn("missing_page", categories)
        self.assertIn("unmapped_legacy_link", categories)
        self.assertIn("missing_asset", categories)
        self.assertIn("icon_token", categories)
        self.assertIn("malformed_code_fence", categories)
        self.assertIn("manual_review", categories)
        self.assertTrue(all(risk.priority in {0, 1, 2} for risk in risks))
```

- [ ] **Step 2: Run the risk tests and confirm they fail for the right reason**

Run:

```bash
python3 -m unittest tests.migration_control.test_risk -v
```

Expected output includes:

```text
ModuleNotFoundError: No module named 'tools.migration_control.review_report'
```

- [ ] **Step 3: Implement existing review report parsing**

Write `tools/migration_control/review_report.py` with this content:

```python
"""Parser for the existing v1.0_codex review report."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict


RISK_HEADING_RE = re.compile(r"^###\s+(High|Medium|Low)\s+Risk", re.IGNORECASE)
PATH_RE = re.compile(r"^-\s+`([^`]+)`")


def parse_review_report(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}

    risks: Dict[str, str] = {}
    current_level = ""

    for line in path.read_text(encoding="utf-8").splitlines():
        heading = RISK_HEADING_RE.match(line)
        if heading:
            current_level = heading.group(1).lower()
            continue

        match = PATH_RE.match(line)
        if current_level and match:
            risks[match.group(1)] = current_level

    return risks
```

- [ ] **Step 4: Implement risk queue generation**

Write `tools/migration_control/risk.py` with this content:

```python
"""Launch risk queue generation."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple

from .matching import mapped_wordpress_paths
from .models import ParityRow, ReadMeInventory, ReadMePage, RiskItem, WordPressExport
from .paths import normalize_path, resolve_local_target


MUST_KEEP_SECTIONS = (
    "Getting Started",
    "profile-api-reference",
    "companion-api",
    "card-api",
    "NOTIFICATIONS",
    "tools",
)

ASSET_EXTENSIONS = {".csv", ".doc", ".docx", ".gif", ".jpeg", ".jpg", ".pdf", ".png", ".svg", ".xls", ".xlsx"}


def generate_risk_queue(
    repo_root: Path,
    wordpress_export: WordPressExport,
    readme_inventory: ReadMeInventory,
    parity_rows: Sequence[ParityRow],
    review_risks: Dict[str, str],
) -> Tuple[RiskItem, ...]:
    risks: List[RiskItem] = []

    risks.extend(_must_keep_section_risks(readme_inventory))
    risks.extend(_parity_risks(parity_rows))
    risks.extend(_readme_page_risks(repo_root, readme_inventory.pages, parity_rows))
    risks.extend(_manual_review_risks(review_risks))

    return tuple(sorted(_dedupe(risks), key=lambda risk: (risk.priority, risk.category, risk.file_or_source, risk.message)))


def _must_keep_section_risks(readme_inventory: ReadMeInventory) -> Iterable[RiskItem]:
    present = {_top_level(page.path) for page in readme_inventory.pages}
    order_present = set(readme_inventory.order_entries)

    for section in MUST_KEEP_SECTIONS:
        if section not in present and section not in order_present:
            yield RiskItem(
                priority=0,
                category="missing_must_keep_section",
                file_or_source=section,
                message=f"Must-keep section is absent from docs and navigation: {section}",
                evidence=section,
                recommended_action="Add or restore the section before launch.",
            )


def _parity_risks(parity_rows: Sequence[ParityRow]) -> Iterable[RiskItem]:
    for row in parity_rows:
        if row.migration_status == "missing":
            yield RiskItem(
                priority=0,
                category="missing_page",
                file_or_source=row.wp_url,
                message=f"Published WordPress page has no ReadMe match: {row.wp_title}",
                evidence=row.notes,
                recommended_action="Create or map the equivalent ReadMe page.",
            )
        elif row.migration_status == "duplicate":
            yield RiskItem(
                priority=0,
                category="duplicate_match",
                file_or_source=row.wp_url,
                message=f"Published WordPress page matched multiple ReadMe candidates: {row.wp_title}",
                evidence=row.notes,
                recommended_action="Choose the canonical ReadMe destination and update matching data.",
            )
        elif row.migration_status == "needs-review":
            yield RiskItem(
                priority=1,
                category="low_confidence_match",
                file_or_source=row.wp_url,
                message=f"Published WordPress page matched with low confidence: {row.wp_title}",
                evidence=f"{row.match_kind} confidence {row.match_confidence}",
                recommended_action="Review the match and confirm or remap the destination.",
            )


def _readme_page_risks(
    repo_root: Path,
    pages: Sequence[ReadMePage],
    parity_rows: Sequence[ParityRow],
) -> Iterable[RiskItem]:
    mapped_paths = mapped_wordpress_paths(parity_rows)

    for page in pages:
        for link in page.legacy_wordpress_links:
            normalized = normalize_path(link)
            if normalized in mapped_paths:
                yield RiskItem(
                    priority=1,
                    category="rewriteable_legacy_link",
                    file_or_source=page.path,
                    message="Legacy WordPress link can be rewritten to a mapped ReadMe destination.",
                    evidence=link,
                    recommended_action=f"Rewrite to target represented by {mapped_paths[normalized]}.",
                )
            else:
                yield RiskItem(
                    priority=0,
                    category="unmapped_legacy_link",
                    file_or_source=page.path,
                    message="Legacy WordPress link has no mapped ReadMe target.",
                    evidence=link,
                    recommended_action="Map the target page or keep the link only with an explicit launch waiver.",
                )

        for image in page.images:
            if _is_local_asset(image) and not resolve_local_target(repo_root, page.path, image).exists():
                yield RiskItem(
                    priority=0,
                    category="missing_asset",
                    file_or_source=page.path,
                    message="Referenced local asset is missing from the repository.",
                    evidence=image,
                    recommended_action="Restore the asset or update the page to a valid asset path.",
                )

        if "ICON_URL" in page.content_text:
            yield RiskItem(
                priority=1,
                category="icon_token",
                file_or_source=page.path,
                message="ReadMe page contains unresolved icon token text.",
                evidence="ICON_URL",
                recommended_action="Replace with a real asset reference or remove the broken visual token.",
            )

        if re.search(r"^image\.\s*$", page.content_text, re.MULTILINE):
            yield RiskItem(
                priority=1,
                category="image_token",
                file_or_source=page.path,
                message="ReadMe page contains a literal image token line.",
                evidence="image.",
                recommended_action="Replace with the intended image or remove the orphaned text.",
            )

        if "```,```" in page.content_text or re.search(r"```,```\w+", page.content_text):
            yield RiskItem(
                priority=1,
                category="malformed_code_fence",
                file_or_source=page.path,
                message="ReadMe page contains adjacent malformed code fences.",
                evidence="```,```",
                recommended_action="Split the fences into valid Markdown code blocks after checking rendered examples.",
            )


def _manual_review_risks(review_risks: Dict[str, str]) -> Iterable[RiskItem]:
    for path, level in review_risks.items():
        priority = 1 if level == "high" else 2
        yield RiskItem(
            priority=priority,
            category="manual_review",
            file_or_source=path,
            message=f"Existing v1.0_codex review marks this page as {level} risk.",
            evidence=level,
            recommended_action="Review against WordPress source content and record approval or required fixes.",
        )


def _top_level(path: str) -> str:
    parts = Path(path).parts
    if len(parts) >= 2 and parts[0] == "docs":
        return parts[1]
    return ""


def _is_local_asset(target: str) -> bool:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return False
    suffix = Path(target.split("#", 1)[0].split("?", 1)[0]).suffix.lower()
    return suffix in ASSET_EXTENSIONS


def _dedupe(risks: Iterable[RiskItem]) -> List[RiskItem]:
    seen: Set[Tuple[int, str, str, str, str]] = set()
    deduped: List[RiskItem] = []
    for risk in risks:
        key = (risk.priority, risk.category, risk.file_or_source, risk.message, risk.evidence)
        if key not in seen:
            deduped.append(risk)
            seen.add(key)
    return deduped
```

- [ ] **Step 5: Run the risk tests and confirm they pass**

Run:

```bash
python3 -m unittest tests.migration_control.test_risk -v
```

Expected output includes:

```text
Ran 2 tests
OK
```

- [ ] **Step 6: Run all tests**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected output includes:

```text
Ran 6 tests
OK
```

- [ ] **Step 7: Commit risk queue**

Run:

```bash
git add tools/migration_control/review_report.py tools/migration_control/risk.py tests/migration_control/test_risk.py
git commit -m "feat: generate migration launch risk queue"
```

Expected output includes:

```text
[codex/sprint-readme-migration-design
 3 files changed
```

## Task 6: Add Report Writers And CLI

**Files:**
- Create: `tools/migration_control/writers.py`
- Create: `tools/migration_control/cli.py`
- Create: `tests/migration_control/test_writers_cli.py`

- [ ] **Step 1: Write failing writer and CLI tests**

Write `tests/migration_control/test_writers_cli.py` with this content:

```python
import csv
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tests.migration_control.test_wxr import WXR_FIXTURE


class WritersCliTests(TestCase):
    def test_cli_writes_expected_reports(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text(WXR_FIXTURE, encoding="utf-8")
            docs = root / "docs" / "profile-api-reference"
            docs.mkdir(parents=True)
            (root / "docs" / "_order.yaml").write_text("- profile-api-reference\n", encoding="utf-8")
            (root / "assets").mkdir()
            (docs / "activate.md").write_text(
                "---\n"
                "title: Activate Card\n"
                "slug: activate\n"
                "---\n"
                "# Activate Card\n",
                encoding="utf-8",
            )
            output_dir = root / "review" / "migration-control"

            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.migration_control.cli",
                    "--wordpress-export",
                    str(xml_path),
                    "--readme-root",
                    str(root),
                    "--output-dir",
                    str(output_dir),
                ],
                text=True,
                capture_output=True,
                check=True,
            )

            self.assertIn("Parsed WordPress: 1 published pages, 1 non-public pages, 1 attachments", result.stdout)
            self.assertTrue((output_dir / "summary.md").exists())
            self.assertTrue((output_dir / "parity_map.csv").exists())
            self.assertTrue((output_dir / "risk_queue.csv").exists())

            with (output_dir / "parity_map.csv").open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))

        self.assertEqual(rows[0]["wp_title"], "Activate Card")
        self.assertEqual(rows[0]["migration_status"], "matched")
```

- [ ] **Step 2: Run the writer and CLI test and confirm it fails for the right reason**

Run:

```bash
python3 -m unittest tests.migration_control.test_writers_cli -v
```

Expected output includes:

```text
No module named tools.migration_control.cli
```

- [ ] **Step 3: Implement report writers**

Write `tools/migration_control/writers.py` with this content:

```python
"""Report writers for migration control outputs."""

from __future__ import annotations

import csv
from collections import Counter
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence, Type

from .models import ParityRow, ReadMeInventory, RiskItem, WordPressExport


def write_reports(
    output_dir: Path,
    wordpress_export: WordPressExport,
    readme_inventory: ReadMeInventory,
    parity_rows: Sequence[ParityRow],
    risks: Sequence[RiskItem],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_wordpress_inventory(output_dir / "wordpress_inventory.csv", wordpress_export)
    _write_readme_inventory(output_dir / "readme_inventory.csv", readme_inventory)
    _write_dataclass_csv(output_dir / "parity_map.csv", parity_rows, ParityRow)
    _write_dataclass_csv(output_dir / "risk_queue.csv", risks, RiskItem)
    _write_summary(output_dir / "summary.md", wordpress_export, readme_inventory, parity_rows, risks)


def _write_wordpress_inventory(path: Path, export: WordPressExport) -> None:
    fieldnames = [
        "source_id",
        "title",
        "slug",
        "status",
        "url",
        "parent_id",
        "menu_order",
        "content_chars",
        "acf_key_count",
        "link_count",
    ]
    rows = [
        {
            "source_id": page.source_id,
            "title": page.title,
            "slug": page.slug,
            "status": page.status,
            "url": page.url,
            "parent_id": page.parent_id,
            "menu_order": page.menu_order,
            "content_chars": page.content_chars,
            "acf_key_count": len(page.acf_keys),
            "link_count": len(page.links),
        }
        for page in export.pages
    ]
    _write_csv(path, fieldnames, rows)


def _write_readme_inventory(path: Path, inventory: ReadMeInventory) -> None:
    fieldnames = [
        "path",
        "title",
        "slug",
        "content_chars",
        "link_count",
        "image_count",
        "legacy_wordpress_link_count",
    ]
    rows = [
        {
            "path": page.path,
            "title": page.title,
            "slug": page.slug,
            "content_chars": page.content_chars,
            "link_count": len(page.links),
            "image_count": len(page.images),
            "legacy_wordpress_link_count": len(page.legacy_wordpress_links),
        }
        for page in inventory.pages
    ]
    _write_csv(path, fieldnames, rows)


def _write_dataclass_csv(path: Path, rows: Sequence[object], row_type: Type[Any]) -> None:
    fieldnames = list(row_type.__dataclass_fields__.keys())
    dict_rows = [asdict(row) for row in rows]
    _write_csv(path, fieldnames, dict_rows)


def _write_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_summary(
    path: Path,
    export: WordPressExport,
    inventory: ReadMeInventory,
    parity_rows: Sequence[ParityRow],
    risks: Sequence[RiskItem],
) -> None:
    status_counts = Counter(row.migration_status for row in parity_rows)
    priority_counts = Counter(risk.priority for risk in risks)
    published_pages = sum(1 for page in export.pages if page.launch_scope)
    non_public_pages = len(export.pages) - published_pages

    lines = [
        "# Migration Control Summary",
        "",
        "## Inventory",
        "",
        f"- WordPress published pages: {published_pages}",
        f"- WordPress non-public pages: {non_public_pages}",
        f"- WordPress attachments: {len(export.attachments)}",
        f"- ReadMe Markdown pages: {len(inventory.pages)}",
        f"- ReadMe assets: {len(inventory.assets)}",
        "",
        "## Parity Status",
        "",
    ]

    for status in ("matched", "needs-review", "missing", "duplicate", "out-of-scope"):
        lines.append(f"- {status}: {status_counts.get(status, 0)}")

    lines.extend(["", "## Risk Queue", ""])
    for priority in (0, 1, 2):
        lines.append(f"- P{priority}: {priority_counts.get(priority, 0)}")

    lines.extend(
        [
            "",
            "## Generated Files",
            "",
            "- `wordpress_inventory.csv`",
            "- `readme_inventory.csv`",
            "- `parity_map.csv`",
            "- `risk_queue.csv`",
        ]
    )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
```

- [ ] **Step 4: Implement the CLI**

Write `tools/migration_control/cli.py` with this content:

```python
"""Command-line entrypoint for migration control report generation."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence

from .matching import build_parity_map
from .readme_repo import scan_readme_repo
from .review_report import parse_review_report
from .risk import generate_risk_queue
from .writers import write_reports
from .wxr import parse_wxr


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Sprint developer portal migration control reports.")
    parser.add_argument("--wordpress-export", required=True, type=Path, help="Path to the WordPress WXR XML export.")
    parser.add_argument("--readme-root", required=True, type=Path, help="Path to the ReadMe repository root.")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory where reports will be written.")
    parser.add_argument(
        "--review-report",
        type=Path,
        default=None,
        help="Path to an existing review report. Defaults to review/review_report_2026-02-16.md under the ReadMe root.",
    )
    args = parser.parse_args(argv)

    review_report = args.review_report or args.readme_root / "review" / "review_report_2026-02-16.md"

    wordpress_export = parse_wxr(args.wordpress_export)
    readme_inventory = scan_readme_repo(args.readme_root)
    review_risks = parse_review_report(review_report)
    parity_rows = build_parity_map(wordpress_export, readme_inventory, review_risks)
    risks = generate_risk_queue(args.readme_root, wordpress_export, readme_inventory, parity_rows, review_risks)

    write_reports(args.output_dir, wordpress_export, readme_inventory, parity_rows, risks)

    published_pages = sum(1 for page in wordpress_export.pages if page.launch_scope)
    non_public_pages = len(wordpress_export.pages) - published_pages
    print(
        f"Parsed WordPress: {published_pages} published pages, "
        f"{non_public_pages} non-public pages, {len(wordpress_export.attachments)} attachments"
    )
    print(f"Scanned ReadMe: {len(readme_inventory.pages)} markdown files, {len(readme_inventory.assets)} assets")
    print(f"Generated parity rows: {len(parity_rows)}")
    print(f"Generated risk items: {len(risks)}")
    print(f"Wrote {args.output_dir / 'summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run the writer and CLI test and confirm it passes**

Run:

```bash
python3 -m unittest tests.migration_control.test_writers_cli -v
```

Expected output includes:

```text
test_cli_writes_expected_reports ... ok
OK
```

- [ ] **Step 6: Run all tests**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected output includes:

```text
Ran 7 tests
OK
```

- [ ] **Step 7: Commit report writers and CLI**

Run:

```bash
git add tools/migration_control/writers.py tools/migration_control/cli.py tests/migration_control/test_writers_cli.py
git commit -m "feat: write migration control reports"
```

Expected output includes:

```text
[codex/sprint-readme-migration-design
 3 files changed
```

## Task 7: Add Tool Documentation And Run The Real Migration Inventory

**Files:**
- Create: `tools/migration_control/README.md`
- Generate: `review/migration-control/wordpress_inventory.csv`
- Generate: `review/migration-control/readme_inventory.csv`
- Generate: `review/migration-control/parity_map.csv`
- Generate: `review/migration-control/risk_queue.csv`
- Generate: `review/migration-control/summary.md`

- [ ] **Step 1: Add tool documentation**

Write `tools/migration_control/README.md` with this content:

````markdown
# Migration Control

This package generates the Phase 1 control reports for migrating `developer.sprint.paymentology.com` from WordPress to ReadMe.

## Run

```bash
python3 -m tools.migration_control.cli \
  --wordpress-export "/Users/andreaweisberg/Downloads/paymentologysprintdeveloper.WordPress.2026-04-24.xml" \
  --readme-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex" \
  --output-dir "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/migration-control"
```

## Reports

- `wordpress_inventory.csv`: every WordPress page from the WXR export with status, slug, URL, parent, content size, ACF key count, and link count.
- `readme_inventory.csv`: every Markdown page under `docs/` with title, slug, content size, link count, image count, and legacy WordPress link count.
- `parity_map.csv`: one row per published WordPress page showing the matched ReadMe file, match confidence, migration status, review risk, and notes.
- `risk_queue.csv`: prioritized launch risks generated from missing pages, duplicate matches, missing must-keep sections, unmapped legacy links, missing assets, unresolved icon tokens, malformed code fences, and the existing manual review report.
- `summary.md`: human-readable counts for the current run.

## Priority Meanings

- `P0`: launch blocker until fixed, mapped, restored, or explicitly waived.
- `P1`: should be resolved before launch when the target is clear.
- `P2`: review or cleanup candidate that can be scheduled after launch if stakeholders accept it.

## Migration Rule

Keep content by default. The initial migration is not a content reduction exercise, and QR Payments remains present for launch unless separate usage and engineering validation approves removal.
````

- [ ] **Step 2: Run all tests before generating real reports**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected output includes:

```text
Ran 7 tests
OK
```

- [ ] **Step 3: Generate real migration control reports**

Run from the repository root:

```bash
python3 -m tools.migration_control.cli \
  --wordpress-export "/Users/andreaweisberg/Downloads/paymentologysprintdeveloper.WordPress.2026-04-24.xml" \
  --readme-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex" \
  --output-dir "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/migration-control"
```

Expected output includes:

```text
Parsed WordPress: 307 published pages, 19 non-public pages, 298 attachments
Scanned ReadMe: 313 markdown files, 8 assets
Generated parity rows: 307
Wrote /Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/migration-control/summary.md
```

- [ ] **Step 4: Inspect the generated summary**

Run:

```bash
sed -n '1,220p' review/migration-control/summary.md
```

Expected output includes:

```text
# Migration Control Summary
## Inventory
- WordPress published pages: 307
- WordPress non-public pages: 19
- WordPress attachments: 298
- ReadMe Markdown pages: 313
- ReadMe assets: 8
```

- [ ] **Step 5: Inspect top launch blockers**

Run:

```bash
python3 - <<'PY'
import csv
from pathlib import Path

path = Path("review/migration-control/risk_queue.csv")
with path.open(newline="", encoding="utf-8") as handle:
    rows = [row for row in csv.DictReader(handle) if row["priority"] == "0"]

for row in rows[:20]:
    print(f'P0 {row["category"]}: {row["file_or_source"]} :: {row["message"]}')
print(f"Total P0: {len(rows)}")
PY
```

Expected output includes one line per P0 item and a final `Total P0:` line.

- [ ] **Step 6: Commit documentation and generated reports**

Run:

```bash
git add tools/migration_control/README.md review/migration-control
git commit -m "docs: add migration control reports"
```

Expected output includes:

```text
[codex/sprint-readme-migration-design
 6 files changed
```

## Task 8: Final Verification

**Files:**
- Verify: `tools/migration_control/*.py`
- Verify: `tests/migration_control/*.py`
- Verify: `review/migration-control/*`

- [ ] **Step 1: Run the full test suite**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected output includes:

```text
Ran 7 tests
OK
```

- [ ] **Step 2: Regenerate the reports to prove repeatability**

Run:

```bash
python3 -m tools.migration_control.cli \
  --wordpress-export "/Users/andreaweisberg/Downloads/paymentologysprintdeveloper.WordPress.2026-04-24.xml" \
  --readme-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex" \
  --output-dir "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/migration-control"
```

Expected output includes:

```text
Parsed WordPress: 307 published pages, 19 non-public pages, 298 attachments
Scanned ReadMe: 313 markdown files, 8 assets
Generated parity rows: 307
Generated risk items:
Wrote /Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/migration-control/summary.md
```

- [ ] **Step 3: Confirm generated reports are deterministic**

Run:

```bash
git diff -- review/migration-control
```

Expected output:

```text
```

- [ ] **Step 4: Confirm the branch contains only intended migration-control changes**

Run:

```bash
git status --short
```

Expected output:

```text
```

If `git status --short` lists only expected files after the final report regeneration, add and commit them with:

```bash
git add review/migration-control
git commit -m "chore: refresh migration control report outputs"
```

If `git status --short` is empty, no refresh commit is needed.

## Coverage Review

- The WordPress inventory requirement is covered by Tasks 1, 2, 6, and 7.
- The ReadMe Markdown, navigation, link, image, and asset inventory requirement is covered by Tasks 3, 6, and 7.
- The parity map requirement is covered by Tasks 4, 6, and 7.
- The risk queue requirement is covered by Tasks 5, 6, and 7.
- The existing review report integration is covered by Task 5.
- Must-keep launch section checks are covered by Task 5.
- QR Payments is preserved by policy in the tool documentation; no deletion or deprecation automation is introduced.
- Automated content fixes are intentionally excluded from this Phase 1 plan.
