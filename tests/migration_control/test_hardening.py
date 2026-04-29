import csv
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.migration_control.hardening import apply_hardening


class HardeningTests(TestCase):
    def test_apply_hardening_rewrites_safe_links_and_splits_fences(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs" / "guide"
            target_dir = root / "docs" / "reference"
            review_dir = root / "review" / "migration-control"
            docs.mkdir(parents=True)
            target_dir.mkdir(parents=True)
            review_dir.mkdir(parents=True)

            source_file = docs / "source.md"
            source_file.write_text(
                "[Ref](https://developer.sprint.paymentology.com/reference/path/#request)\n"
                "```,```xml\n",
                encoding="utf-8",
            )
            (target_dir / "index.md").write_text("# Target\n", encoding="utf-8")

            parity_path = review_dir / "parity_map.csv"
            with parity_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=[
                        "wp_id",
                        "wp_title",
                        "wp_url",
                        "wp_slug",
                        "wp_status",
                        "matched_path",
                        "match_kind",
                        "match_confidence",
                        "migration_status",
                        "review_risk",
                        "notes",
                    ],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "wp_id": "1",
                        "wp_title": "Reference",
                        "wp_url": "https://developer.sprint.paymentology.com/reference/path/",
                        "wp_slug": "path",
                        "wp_status": "publish",
                        "matched_path": "docs/reference/index.md",
                        "match_kind": "url_path",
                        "match_confidence": "1.0",
                        "migration_status": "matched",
                        "review_risk": "",
                        "notes": "",
                    }
                )

            risk_path = review_dir / "risk_queue.csv"
            with risk_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=["priority", "category", "file_or_source", "message", "evidence", "recommended_action"],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "priority": "1",
                        "category": "rewriteable_legacy_link",
                        "file_or_source": "docs/guide/source.md",
                        "message": "rewrite",
                        "evidence": "https://developer.sprint.paymentology.com/reference/path/#request",
                        "recommended_action": "Rewrite to target represented by docs/reference/index.md.",
                    }
                )
                writer.writerow(
                    {
                        "priority": "1",
                        "category": "malformed_code_fence",
                        "file_or_source": "docs/guide/source.md",
                        "message": "fence",
                        "evidence": "```,```",
                        "recommended_action": "Split fences.",
                    }
                )

            result = apply_hardening(root, risk_path, parity_path)
            updated = source_file.read_text(encoding="utf-8")

        self.assertEqual(result.rewritten_links, 1)
        self.assertEqual(result.fixed_fences, 1)
        self.assertEqual(result.files_changed, 1)
        self.assertIn("[Ref](../reference#request)", updated)
        self.assertIn("```\n\n```xml", updated)

    def test_apply_hardening_skips_non_safe_rewrites(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs" / "guide"
            review_dir = root / "review" / "migration-control"
            docs.mkdir(parents=True)
            review_dir.mkdir(parents=True)

            source_file = docs / "source.md"
            original = "[Ref](https://developer.sprint.paymentology.com/reference/path/)\n"
            source_file.write_text(original, encoding="utf-8")

            parity_path = review_dir / "parity_map.csv"
            with parity_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=[
                        "wp_id",
                        "wp_title",
                        "wp_url",
                        "wp_slug",
                        "wp_status",
                        "matched_path",
                        "match_kind",
                        "match_confidence",
                        "migration_status",
                        "review_risk",
                        "notes",
                    ],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "wp_id": "1",
                        "wp_title": "Reference",
                        "wp_url": "https://developer.sprint.paymentology.com/reference/path/",
                        "wp_slug": "path",
                        "wp_status": "publish",
                        "matched_path": "docs/reference/index.md",
                        "match_kind": "title",
                        "match_confidence": "0.75",
                        "migration_status": "needs-review",
                        "review_risk": "",
                        "notes": "",
                    }
                )

            risk_path = review_dir / "risk_queue.csv"
            with risk_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=["priority", "category", "file_or_source", "message", "evidence", "recommended_action"],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "priority": "1",
                        "category": "rewriteable_legacy_link",
                        "file_or_source": "docs/guide/source.md",
                        "message": "rewrite",
                        "evidence": "https://developer.sprint.paymentology.com/reference/path/",
                        "recommended_action": "Rewrite to target represented by docs/reference/index.md.",
                    }
                )

            result = apply_hardening(root, risk_path, parity_path)
            updated = source_file.read_text(encoding="utf-8")

        self.assertEqual(result.rewritten_links, 0)
        self.assertEqual(updated, original)
