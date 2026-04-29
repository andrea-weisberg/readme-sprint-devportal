# Sprint ReadMe Rebuild Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a new XML-first ReadMe rebuild pipeline that generates a clean, top-bar-driven developer portal structure from the WordPress export, rewrites embedded internal links, preserves all source information, and emits a migration audit that explains exactly what changed.

**Architecture:** Keep the existing migrated `docs/` tree as a reference input only. Implement a new rebuild pipeline under `tools/readme_rebuild/` that reads the WordPress XML, classifies every page into the approved IA, generates a staging site under `rebuild/readme-site/`, validates coverage and links, and writes audit artifacts under `review/rebuild/` before any cutover into canonical docs paths.

**Tech Stack:** Python 3, existing `tools.migration_control` XML/path helpers, Markdown file generation, YAML `_order.yaml` generation, `unittest`, git.

---

## File Structure

### New package: `tools/readme_rebuild/`

- `tools/readme_rebuild/__init__.py`
  - package marker
- `tools/readme_rebuild/models.py`
  - dataclasses for classified pages, destination pages, link rewrites, and audit rows
- `tools/readme_rebuild/inventory.py`
  - turn WordPress XML pages plus reference repo signals into rebuild input records
- `tools/readme_rebuild/ia.py`
  - top-bar and section classification rules for `Guides`, `API Reference`, `Reports`, `Tools`
- `tools/readme_rebuild/mapping.py`
  - source page -> destination section/path/slug mapping logic
- `tools/readme_rebuild/links.py`
  - embedded internal-link rewrite planner and helpers
- `tools/readme_rebuild/render.py`
  - write staging Markdown pages and `_order.yaml` files into `rebuild/readme-site/`
- `tools/readme_rebuild/audit.py`
  - write coverage, move/split/merge, and link rewrite reports into `review/rebuild/`
- `tools/readme_rebuild/cli.py`
  - end-to-end CLI entrypoint for inventory, mapping, render, and audit
- `tools/readme_rebuild/README.md`
  - operator runbook for rebuilding and validating the staging site

### New tests: `tests/readme_rebuild/`

- `tests/readme_rebuild/test_inventory.py`
- `tests/readme_rebuild/test_ia.py`
- `tests/readme_rebuild/test_mapping.py`
- `tests/readme_rebuild/test_links.py`
- `tests/readme_rebuild/test_render.py`
- `tests/readme_rebuild/test_audit_cli.py`

### New generated outputs

- `rebuild/readme-site/`
  - staging site output, including section folders and `_order.yaml`
- `review/rebuild/`
  - `page_mapping.csv`
  - `link_rewrites.csv`
  - `content_moves.csv`
  - `summary.md`

### Existing files to reuse or update

- `tools/migration_control/wxr.py`
  - reuse parser rather than reimplementing XML parsing
- `tools/migration_control/paths.py`
  - reuse normalization helpers
- `docs/superpowers/specs/2026-04-29-sprint-developer-readme-migration-design.md`
  - implementation source spec

---

### Task 1: Scaffold the XML-first rebuild package

**Files:**
- Create: `tools/readme_rebuild/__init__.py`
- Create: `tools/readme_rebuild/models.py`
- Create: `tools/readme_rebuild/cli.py`
- Create: `tests/readme_rebuild/test_audit_cli.py`

- [ ] **Step 1: Write the failing CLI smoke test**

```python
from pathlib import Path
from subprocess import run
from sys import executable
from tempfile import TemporaryDirectory
from unittest import TestCase


class RebuildCliSmokeTests(TestCase):
    def test_cli_prints_rebuild_summary(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text(WXR_FIXTURE, encoding="utf-8")
            (root / "docs").mkdir()

            result = run(
                [
                    executable,
                    "-m",
                    "tools.readme_rebuild.cli",
                    "--wordpress-export",
                    str(xml_path),
                    "--repo-root",
                    str(root),
                    "--output-root",
                    str(root / "rebuild" / "readme-site"),
                    "--report-root",
                    str(root / "review" / "rebuild"),
                ],
                text=True,
                capture_output=True,
            )

        self.assertNotEqual(result.returncode, 0)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.readme_rebuild.test_audit_cli -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.readme_rebuild'`

- [ ] **Step 3: Write the minimal package and CLI shell**

```python
"""XML-first ReadMe rebuild pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Build a staging ReadMe site from the Sprint WordPress XML export.")
    parser.add_argument("--wordpress-export", required=True, type=Path)
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--report-root", required=True, type=Path)
    parser.parse_args(argv)
    raise NotImplementedError("Rebuild pipeline not implemented yet.")


if __name__ == "__main__":
    raise SystemExit(main())
```

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class RebuildSummary:
    source_pages: int
    rendered_pages: int
    rewritten_links: int
```

- [ ] **Step 4: Update the smoke test to expect the explicit placeholder failure**

```python
self.assertIn("NotImplementedError", result.stderr)
```

- [ ] **Step 5: Run test to verify it passes**

Run: `python3 -m unittest tests.readme_rebuild.test_audit_cli -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add tools/readme_rebuild tests/readme_rebuild/test_audit_cli.py
git commit -m "feat: scaffold readme rebuild pipeline"
```

### Task 2: Build rebuild inventory from WordPress XML

**Files:**
- Create: `tools/readme_rebuild/inventory.py`
- Modify: `tools/readme_rebuild/models.py`
- Create: `tests/readme_rebuild/test_inventory.py`
- Reference: `tools/migration_control/wxr.py`

- [ ] **Step 1: Write the failing inventory test for source-page extraction**

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest import TestCase

from tests.migration_control.test_wxr import WXR_FIXTURE
from tools.readme_rebuild.inventory import build_inventory


class InventoryTests(TestCase):
    def test_build_inventory_extracts_launch_pages_and_links(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text(WXR_FIXTURE, encoding="utf-8")

            inventory = build_inventory(xml_path, root)

        self.assertEqual(len(inventory.pages), 1)
        self.assertEqual(inventory.pages[0].source_url, "https://developer.sprint.paymentology.com/card-api/activate/")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.readme_rebuild.test_inventory -v`
Expected: FAIL with `ImportError` for `build_inventory`

- [ ] **Step 3: Add inventory dataclasses and parser wrapper**

```python
@dataclass(frozen=True)
class SourcePage:
    source_id: str
    title: str
    source_url: str
    slug: str
    section_hint: str
    content_text: str
    links: tuple[str, ...]


@dataclass(frozen=True)
class RebuildInventory:
    pages: tuple[SourcePage, ...]
    attachments: tuple[str, ...]
```

```python
from pathlib import Path

from tools.migration_control.wxr import parse_wxr
from tools.readme_rebuild.models import RebuildInventory, SourcePage


def build_inventory(wordpress_export: Path, repo_root: Path) -> RebuildInventory:
    export = parse_wxr(wordpress_export)
    pages = tuple(
        SourcePage(
            source_id=page.source_id,
            title=page.title,
            source_url=page.url,
            slug=page.slug,
            section_hint=page.url.split("/", 3)[3] if page.url.count("/") >= 3 else "",
            content_text=page.content_text,
            links=page.links,
        )
        for page in export.pages
        if page.launch_scope
    )
    attachments = tuple(attachment.url for attachment in export.attachments)
    return RebuildInventory(pages=pages, attachments=attachments)
```

- [ ] **Step 4: Harden the test fixture expectations**

```python
self.assertGreaterEqual(len(inventory.attachments), 1)
self.assertIn("card-api", inventory.pages[0].source_url)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m unittest tests.readme_rebuild.test_inventory -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add tools/readme_rebuild/models.py tools/readme_rebuild/inventory.py tests/readme_rebuild/test_inventory.py
git commit -m "feat: build rebuild inventory from xml"
```

### Task 3: Encode the new information architecture and source-page mapping

**Files:**
- Create: `tools/readme_rebuild/ia.py`
- Create: `tools/readme_rebuild/mapping.py`
- Modify: `tools/readme_rebuild/models.py`
- Create: `tests/readme_rebuild/test_ia.py`
- Create: `tests/readme_rebuild/test_mapping.py`

- [ ] **Step 1: Write the failing classification and mapping tests**

```python
from unittest import TestCase

from tools.readme_rebuild.ia import classify_page
from tools.readme_rebuild.mapping import map_page
from tools.readme_rebuild.models import SourcePage


class IaTests(TestCase):
    def test_classify_client_testing_guide_as_guides(self):
        page = SourcePage("1", "Client Testing Guide", "https://developer.sprint.paymentology.com/get-started/client-testing-guide/", "client-testing-guide", "", "body", ())
        result = classify_page(page)
        self.assertEqual(result.top_bar, "Guides")

    def test_classify_card_method_page_as_api_reference(self):
        page = SourcePage("2", "ActivateToken", "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/", "activatetoken", "", "body", ())
        result = classify_page(page)
        self.assertEqual(result.subsection, "Card API")
```

```python
class MappingTests(TestCase):
    def test_map_api_reference_page_to_canonical_path(self):
        page = SourcePage("2", "ActivateToken", "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/", "activatetoken", "", "body", ())
        destination = map_page(page)
        self.assertEqual(destination.path, "API Reference/card-api/activatetoken.md")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.readme_rebuild.test_ia tests.readme_rebuild.test_mapping -v`
Expected: FAIL with missing imports/functions

- [ ] **Step 3: Implement classification and destination models**

```python
@dataclass(frozen=True)
class Classification:
    top_bar: str
    subsection: str
    reason: str


@dataclass(frozen=True)
class DestinationPage:
    source_url: str
    path: str
    title: str
    top_bar: str
    subsection: str
    slug: str
```

```python
def classify_page(page: SourcePage) -> Classification:
    url = page.source_url.lower()
    if "/tools/" in url:
        return Classification("Tools", "Tools", "tool utility url")
    if "/reports/" in url or "report" in page.title.lower():
        subsection = "Card API" if "/card-api/" in url else "Companion API" if "/companion-api/" in url else "QR Payments" if "/qr-payments-api/" in url else "Chargeback API" if "/chargeback-api/" in url else "Shared"
        return Classification("Reports", subsection, "report url or title")
    if "/api-reference/" in url or "/chargeback-api/" in url:
        subsection = "Card API" if "/card-api/" in url else "Companion API" if "/companion-api/" in url else "QR Payments" if "/qr-payments-api/" in url else "Chargeback API"
        return Classification("API Reference", subsection, "reference path")
    return Classification("Guides", "Shared", "default shared guide")
```

```python
def map_page(page: SourcePage) -> DestinationPage:
    classification = classify_page(page)
    section_slug = classification.subsection.lower().replace(" ", "-")
    slug = page.slug or page.title.lower().replace(" ", "-")
    if classification.top_bar == "API Reference":
        path = f"API Reference/{section_slug}/{slug}.md"
    elif classification.top_bar == "Reports":
        path = f"Reports/{section_slug}/{slug}.md"
    elif classification.top_bar == "Tools":
        path = f"Tools/{slug}.md"
    else:
        path = f"Guides/{slug}.md"
    return DestinationPage(page.source_url, path, page.title, classification.top_bar, classification.subsection, slug)
```

- [ ] **Step 4: Expand tests for hybrid IA edge cases**

```python
def test_map_choose_api_page_to_guides(self):
    page = SourcePage("3", "Our APIs", "https://developer.sprint.paymentology.com/get-started/our-apis/", "our-apis", "", "body", ())
    destination = map_page(page)
    self.assertEqual(destination.path, "Guides/our-apis.md")
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m unittest tests.readme_rebuild.test_ia tests.readme_rebuild.test_mapping -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add tools/readme_rebuild/ia.py tools/readme_rebuild/mapping.py tools/readme_rebuild/models.py tests/readme_rebuild/test_ia.py tests/readme_rebuild/test_mapping.py
git commit -m "feat: encode rebuild information architecture"
```

### Task 4: Plan and emit internal-link rewrites

**Files:**
- Create: `tools/readme_rebuild/links.py`
- Modify: `tools/readme_rebuild/models.py`
- Create: `tests/readme_rebuild/test_links.py`

- [ ] **Step 1: Write the failing link rewrite planner test**

```python
from unittest import TestCase

from tools.readme_rebuild.links import rewrite_links
from tools.readme_rebuild.models import DestinationPage, SourcePage


class LinkRewriteTests(TestCase):
    def test_rewrite_links_updates_wordpress_internal_targets(self):
        page = SourcePage(
            "1",
            "Client Testing Guide",
            "https://developer.sprint.paymentology.com/get-started/client-testing-guide/",
            "client-testing-guide",
            "",
            "See https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/ next.",
            ("https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",),
        )
        destinations = {
            "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/": DestinationPage(
                "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",
                "API Reference/card-api/activatetoken.md",
                "ActivateToken",
                "API Reference",
                "Card API",
                "activatetoken",
            )
        }
        rewritten, audit_rows = rewrite_links(page, destinations)
        self.assertIn("/api-reference/card-api/activatetoken", rewritten)
        self.assertEqual(len(audit_rows), 1)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.readme_rebuild.test_links -v`
Expected: FAIL with missing `rewrite_links`

- [ ] **Step 3: Implement rewrite and audit row support**

```python
@dataclass(frozen=True)
class LinkRewrite:
    source_page: str
    original_url: str
    rewritten_url: str
    status: str
```

```python
def rewrite_links(page: SourcePage, destinations: dict[str, DestinationPage]) -> tuple[str, tuple[LinkRewrite, ...]]:
    rewritten = page.content_text
    rows = []
    for link in page.links:
        destination = destinations.get(link)
        if not destination:
            continue
        new_url = "/" + destination.path.replace(".md", "").replace("API Reference", "api-reference").replace("Guides", "guides").replace("Reports", "reports").replace("Tools", "tools")
        rewritten = rewritten.replace(link, new_url)
        rows.append(LinkRewrite(page.source_url, link, new_url, "rewritten"))
    return rewritten, tuple(rows)
```

- [ ] **Step 4: Add an unmapped-link test**

```python
def test_rewrite_links_leaves_unmapped_links_unchanged(self):
    page = SourcePage("1", "Guide", "https://developer.sprint.paymentology.com/get-started/guide/", "guide", "", "See https://developer.sprint.paymentology.com/missing/.", ("https://developer.sprint.paymentology.com/missing/",))
    rewritten, audit_rows = rewrite_links(page, {})
    self.assertIn("https://developer.sprint.paymentology.com/missing/", rewritten)
    self.assertEqual(audit_rows, ())
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m unittest tests.readme_rebuild.test_links -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add tools/readme_rebuild/links.py tools/readme_rebuild/models.py tests/readme_rebuild/test_links.py
git commit -m "feat: add rebuild link rewrite planner"
```

### Task 5: Render the staging ReadMe site and navigation

**Files:**
- Create: `tools/readme_rebuild/render.py`
- Modify: `tools/readme_rebuild/cli.py`
- Create: `tests/readme_rebuild/test_render.py`

- [ ] **Step 1: Write the failing render test**

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.readme_rebuild.models import DestinationPage
from tools.readme_rebuild.render import render_site


class RenderTests(TestCase):
    def test_render_site_writes_markdown_and_order_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            pages = (
                DestinationPage("https://developer.sprint.paymentology.com/get-started/our-apis/", "Guides/our-apis.md", "Our APIs", "Guides", "Shared", "our-apis"),
                DestinationPage("https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/", "API Reference/card-api/activatetoken.md", "ActivateToken", "API Reference", "Card API", "activatetoken"),
            )
            render_site(root, pages, {"Guides/our-apis.md": "# Our APIs\n", "API Reference/card-api/activatetoken.md": "# ActivateToken\n"})
            self.assertTrue((root / "Guides" / "_order.yaml").exists())
            self.assertTrue((root / "API Reference" / "card-api" / "activatetoken.md").exists())
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.readme_rebuild.test_render -v`
Expected: FAIL with missing `render_site`

- [ ] **Step 3: Implement renderer and `_order.yaml` writer**

```python
from collections import defaultdict
from pathlib import Path


def render_site(output_root: Path, pages: tuple[DestinationPage, ...], content_by_path: dict[str, str]) -> None:
    sections = defaultdict(list)
    for page in pages:
        file_path = output_root / page.path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content_by_path[page.path], encoding="utf-8")
        sections[str(file_path.parent.relative_to(output_root))].append(file_path.stem)

    for folder, entries in sections.items():
        order_path = output_root / folder / "_order.yaml"
        order_path.write_text("".join(f"- {entry}\n" for entry in sorted(entries)), encoding="utf-8")
```

- [ ] **Step 4: Teach the CLI to call the renderer**

```python
content_by_path = {destination.path: f"# {destination.title}\n" for destination in mapped_pages}
render_site(args.output_root, tuple(mapped_pages), content_by_path)
print(f"Rendered staging site: {args.output_root}")
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m unittest tests.readme_rebuild.test_render tests.readme_rebuild.test_audit_cli -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add tools/readme_rebuild/render.py tools/readme_rebuild/cli.py tests/readme_rebuild/test_render.py tests/readme_rebuild/test_audit_cli.py
git commit -m "feat: render staging readme rebuild site"
```

### Task 6: Emit the migration audit and operator runbook

**Files:**
- Create: `tools/readme_rebuild/audit.py`
- Create: `tools/readme_rebuild/README.md`
- Modify: `tools/readme_rebuild/cli.py`
- Modify: `tests/readme_rebuild/test_audit_cli.py`

- [ ] **Step 1: Write the failing audit-report test**

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.readme_rebuild.audit import write_audit_reports
from tools.readme_rebuild.models import DestinationPage, LinkRewrite


class AuditTests(TestCase):
    def test_write_audit_reports_writes_mapping_and_link_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_audit_reports(
                root,
                pages=(
                    DestinationPage("https://developer.sprint.paymentology.com/get-started/our-apis/", "Guides/our-apis.md", "Our APIs", "Guides", "Shared", "our-apis"),
                ),
                link_rewrites=(
                    LinkRewrite("https://developer.sprint.paymentology.com/get-started/our-apis/", "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/", "/api-reference/card-api/activatetoken", "rewritten"),
                ),
            )
            self.assertTrue((root / "page_mapping.csv").exists())
            self.assertTrue((root / "link_rewrites.csv").exists())
            self.assertTrue((root / "summary.md").exists())
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.readme_rebuild.test_audit_cli -v`
Expected: FAIL with missing `write_audit_reports`

- [ ] **Step 3: Implement CSV/Markdown audit outputs**

```python
import csv


def write_audit_reports(report_root: Path, pages: tuple[DestinationPage, ...], link_rewrites: tuple[LinkRewrite, ...]) -> None:
    report_root.mkdir(parents=True, exist_ok=True)
    with (report_root / "page_mapping.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source_url", "path", "title", "top_bar", "subsection", "slug"])
        writer.writeheader()
        for page in pages:
            writer.writerow(page.__dict__)
    with (report_root / "link_rewrites.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source_page", "original_url", "rewritten_url", "status"])
        writer.writeheader()
        for row in link_rewrites:
            writer.writerow(row.__dict__)
    (report_root / "summary.md").write_text(
        f"# Rebuild Summary\n\n- mapped pages: {len(pages)}\n- rewritten links: {len(link_rewrites)}\n",
        encoding="utf-8",
    )
```

- [ ] **Step 4: Document the operator workflow**

```md
# ReadMe Rebuild

## Run

```bash
python3 -m tools.readme_rebuild.cli \
  --wordpress-export "/Users/andreaweisberg/Downloads/paymentologysprintdeveloper.WordPress.2026-04-24.xml" \
  --repo-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex" \
  --output-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/rebuild/readme-site" \
  --report-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/rebuild"
```

## Verify

- review `review/rebuild/page_mapping.csv`
- review `review/rebuild/link_rewrites.csv`
- confirm no information-loss exceptions remain
```

- [ ] **Step 5: Run the focused tests and end-to-end CLI**

Run: `python3 -m unittest tests.readme_rebuild.test_audit_cli tests.readme_rebuild.test_render tests.readme_rebuild.test_links -v`
Expected: PASS

Run: `python3 -m tools.readme_rebuild.cli --wordpress-export "/Users/andreaweisberg/Downloads/paymentologysprintdeveloper.WordPress.2026-04-24.xml" --repo-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex" --output-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/rebuild/readme-site" --report-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/rebuild"`
Expected: exit 0 and printed staging/report paths

- [ ] **Step 6: Commit**

```bash
git add tools/readme_rebuild/audit.py tools/readme_rebuild/README.md tools/readme_rebuild/cli.py tests/readme_rebuild/test_audit_cli.py
git commit -m "feat: emit rebuild audit artifacts"
```

## Self-Review

### Spec coverage

- XML-first rebuild source of truth: Tasks 1-2
- new IA with `Guides`, `API Reference`, `Reports`, `Tools`: Task 3
- internal link rewrites: Task 4
- ReadMe-native staging rebuild output: Task 5
- migration report and no-information-loss audit trail: Task 6
- GitHub-sync-friendly `API Reference` structure: Task 3 through stable subsection mapping and slugging

### Placeholder scan

Search plan for placeholders before execution:

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path("docs/superpowers/plans/2026-04-29-sprint-readme-rebuild-implementation.md").read_text(encoding="utf-8")
red_flags = [
    "TB" + "D",
    "TO" + "DO",
    "implement " + "later",
    "appropriate " + "error handling",
    "handle " + "edge cases",
    "Write tests " + "for the above",
    "Similar " + "to Task",
]
matches = [flag for flag in red_flags if flag in text]
print(matches)
PY
```

Expected: `[]`

### Type consistency

- `SourcePage`, `DestinationPage`, `Classification`, `LinkRewrite`, and `RebuildSummary` are introduced once and reused consistently
- CLI arguments are kept stable across tasks: `--wordpress-export`, `--repo-root`, `--output-root`, `--report-root`
