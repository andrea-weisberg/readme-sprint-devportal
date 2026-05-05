from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.readme_rebuild.assets import sync_wordpress_images


class AssetSyncTests(TestCase):
    def test_sync_wordpress_images_rewrites_markdown_and_caches_mapping(self):
        downloads: list[str] = []
        uploads: list[str] = []

        def downloader(url: str, destination: Path) -> None:
            downloads.append(url)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(b"png-bytes")

        def uploader(image_path: Path, api_key: str) -> str:
            uploads.append(f"{image_path.name}:{api_key}")
            return f"https://files.readme.io/{image_path.name}"

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            cache_root = root / "asset-cache"
            page = output_root / "docs" / "guides" / "how_payments_work.md"
            page.parent.mkdir(parents=True, exist_ok=True)
            page.write_text(
                "![Lifecycle](https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Payment-lifecycle.png)\n"
                "![Lifecycle again](https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Payment-lifecycle.png)\n"
                "[Attachment](https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Payment-lifecycle.pdf)\n",
                encoding="utf-8",
            )

            summary = sync_wordpress_images(
                output_root,
                "rdme_test_key",
                cache_root,
                downloader=downloader,
                uploader=uploader,
            )

            self.assertEqual(summary.files_scanned, 1)
            self.assertEqual(summary.uploaded_images, 1)
            self.assertEqual(summary.reused_images, 0)
            self.assertEqual(summary.image_references_rewritten, 2)
            self.assertEqual(downloads, ["https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Payment-lifecycle.png"])
            self.assertEqual(len(uploads), 1)

            rewritten = page.read_text(encoding="utf-8")
            self.assertIn("https://files.readme.io/", rewritten)
            self.assertIn("Payment-lifecycle.pdf", rewritten)

            second_summary = sync_wordpress_images(
                output_root,
                "rdme_test_key",
                cache_root,
                downloader=downloader,
                uploader=uploader,
            )
            self.assertEqual(second_summary.uploaded_images, 0)
            self.assertEqual(second_summary.reused_images, 0)
            self.assertEqual(second_summary.image_references_rewritten, 0)
            self.assertEqual(len(downloads), 1)
            self.assertEqual(len(uploads), 1)
