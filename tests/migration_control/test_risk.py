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
                        links=(
                            "https://developer.sprint.paymentology.com/missing-target/",
                            "../../assets/missing-form.docx",
                        ),
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
        missing_assets = [risk for risk in risks if risk.category == "missing_asset"]
        self.assertEqual({risk.evidence for risk in missing_assets}, {"../../assets/missing.csv", "../../assets/missing-form.docx"})
