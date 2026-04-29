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
            self.assertTrue((output_dir / "wordpress_inventory.csv").exists())
            self.assertTrue((output_dir / "wordpress_attachments.csv").exists())
            self.assertTrue((output_dir / "readme_inventory.csv").exists())
            self.assertTrue((output_dir / "readme_assets.csv").exists())
            self.assertTrue((output_dir / "readme_order_entries.csv").exists())
            self.assertTrue((output_dir / "parity_map.csv").exists())
            self.assertTrue((output_dir / "risk_queue.csv").exists())

            with (output_dir / "wordpress_inventory.csv").open(newline="", encoding="utf-8") as handle:
                wordpress_rows = list(csv.DictReader(handle))
            with (output_dir / "wordpress_attachments.csv").open(newline="", encoding="utf-8") as handle:
                attachment_rows = list(csv.DictReader(handle))
            with (output_dir / "readme_inventory.csv").open(newline="", encoding="utf-8") as handle:
                readme_rows = list(csv.DictReader(handle))
            with (output_dir / "readme_assets.csv").open(newline="", encoding="utf-8") as handle:
                asset_rows = list(csv.DictReader(handle))
            with (output_dir / "readme_order_entries.csv").open(newline="", encoding="utf-8") as handle:
                order_rows = list(csv.DictReader(handle))
            with (output_dir / "parity_map.csv").open(newline="", encoding="utf-8") as handle:
                parity_rows = list(csv.DictReader(handle))
            summary = (output_dir / "summary.md").read_text(encoding="utf-8")

        self.assertEqual(wordpress_rows[0]["title"], "Activate Card")
        self.assertIn("api_content_builder_0_request", wordpress_rows[0]["acf_keys"])
        self.assertIn("https://developer.sprint.paymentology.com/card-api/", wordpress_rows[0]["links"])
        self.assertEqual(attachment_rows[0]["filename"], "dispute.docx")
        self.assertEqual(readme_rows[0]["path"], "docs/profile-api-reference/activate.md")
        self.assertEqual(asset_rows, [])
        self.assertEqual(order_rows[0]["entry"], "profile-api-reference")
        self.assertEqual(parity_rows[0]["wp_title"], "Activate Card")
        self.assertEqual(parity_rows[0]["migration_status"], "matched")
        self.assertIn("wordpress_attachments.csv", summary)
        self.assertIn("readme_assets.csv", summary)
        self.assertIn("readme_order_entries.csv", summary)
