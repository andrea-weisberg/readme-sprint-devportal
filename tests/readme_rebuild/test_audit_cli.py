import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tests.migration_control.test_wxr import WXR_FIXTURE


class RebuildCliSmokeTests(TestCase):
    def test_cli_renders_staging_site(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text(WXR_FIXTURE, encoding="utf-8")
            (root / "docs").mkdir()
            output_root = root / "rebuild" / "readme-site"

            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.readme_rebuild.cli",
                    "--wordpress-export",
                    str(xml_path),
                    "--repo-root",
                    str(root),
                    "--output-root",
                    str(output_root),
                    "--report-root",
                    str(root / "review" / "rebuild"),
                ],
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(f"Rendered staging site: {output_root}", result.stdout)
            self.assertEqual(
                (output_root / "API Reference" / "shared" / "activate.md").read_text(encoding="utf-8"),
                "# Activate Card\n",
            )
            self.assertEqual(
                (output_root / "API Reference" / "shared" / "_order.yaml").read_text(encoding="utf-8"),
                "- activate\n",
            )
