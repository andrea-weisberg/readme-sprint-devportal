import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase


class RebuildCliSmokeTests(TestCase):
    def test_cli_placeholder_exits_with_not_implemented_error(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text("<rss/>", encoding="utf-8")
            (root / "docs").mkdir()

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
                    str(root / "rebuild" / "readme-site"),
                    "--report-root",
                    str(root / "review" / "rebuild"),
                ],
                text=True,
                capture_output=True,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("NotImplementedError", result.stderr)
