from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import shutil

from tools.readme_rebuild.models import DestinationPage


def render_site(
    output_root: Path,
    pages: tuple[DestinationPage, ...],
    content_by_path: dict[str, str],
) -> None:
    shutil.rmtree(output_root, ignore_errors=True)
    folder_entries: dict[str, set[str]] = defaultdict(set)

    for page in pages:
        file_path = output_root / page.path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content_by_path[page.path], encoding="utf-8")
        _track_folder_entries(folder_entries, file_path.relative_to(output_root))

    for folder in sorted(folder_entries):
        order_path = output_root / folder / "_order.yaml" if folder else output_root / "_order.yaml"
        entries = "".join(f"- {entry}\n" for entry in sorted(folder_entries[folder]))
        order_path.write_text(entries, encoding="utf-8")


def _track_folder_entries(folder_entries: dict[str, set[str]], relative_path: Path) -> None:
    directory_parts = relative_path.parts[:-1]
    folder_entries[""].add(directory_parts[0])

    for depth in range(1, len(directory_parts)):
        parent = Path(*directory_parts[:depth])
        child = directory_parts[depth]
        folder_entries[_folder_key(parent)].add(child)

    leaf_folder = _folder_key(Path(*directory_parts))
    folder_entries[leaf_folder].add(relative_path.stem)


def _folder_key(path: Path) -> str:
    return "" if str(path) == "." else str(path)
