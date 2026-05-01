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

LINK_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
BUILDER_CONTENT_KEY_RE = re.compile(
    r"^(?:page|api)_content_builder_.*(?:content|text|description|title)$"
)
BUILDER_INDEX_RE = re.compile(r"\d+")
PAIRABLE_TITLE_RE = re.compile(r".*_columns_\d+_title$")
SERIALIZED_VALUE_RE = re.compile(r"^[abisOdN]:\d*(?:[:;{])")
ANCHOR_RE = re.compile(
    r"""<a\b[^>]*href\s*=\s*["']([^"']+)["'][^>]*>(.*?)</a>""",
    re.IGNORECASE | re.DOTALL,
)
STRONG_RE = re.compile(
    r"<(?:strong|b)\b[^>]*>(.*?)</(?:strong|b)>",
    re.IGNORECASE | re.DOTALL,
)
HEADING_RE = re.compile(r"<h([1-6])\b[^>]*>(.*?)</h\1>", re.IGNORECASE | re.DOTALL)
IMAGE_RE = re.compile(
    r"""<img\b([^>]*?)src\s*=\s*["']([^"']+)["']([^>]*)>""",
    re.IGNORECASE | re.DOTALL,
)
LIST_ITEM_RE = re.compile(r"<li\b[^>]*>(.*?)</li>", re.IGNORECASE | re.DOTALL)
BREAK_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
BLOCK_TAG_RE = re.compile(
    r"</?(?:p|div|ul|ol|section|article|table|tbody|thead|tr|td|th|blockquote)\b[^>]*>",
    re.IGNORECASE,
)
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
        attachments=tuple(sorted(attachments, key=lambda attachment: attachment.url)),
    )


def _parse_page(item: ElementTree.Element) -> WordPressPage:
    content = _page_content(item)
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
        content_markdown=_html_to_markdown(content),
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


def _page_content(item: ElementTree.Element) -> str:
    fragments: List[str] = []
    builder_entries: List[tuple[str, str, int]] = []

    content = _text(item, "content:encoded")
    if _keep_content_fragment(content):
        fragments.append(content)

    for position, meta in enumerate(item.findall("wp:postmeta", NS)):
        key = clean_text(_text(meta, "wp:meta_key"))
        if not BUILDER_CONTENT_KEY_RE.match(key):
            continue

        value = _text(meta, "wp:meta_value")
        if _keep_content_fragment(value):
            builder_entries.append((key, value, position))

    fragments.extend(_ordered_builder_fragments(builder_entries))

    return "\n\n".join(fragment for fragment in fragments if clean_text(fragment))


def _keep_content_fragment(value: str) -> bool:
    cleaned = clean_text(value)
    if not cleaned:
        return False
    if SERIALIZED_VALUE_RE.match(cleaned):
        return False
    return True


def _ordered_builder_fragments(
    entries: List[tuple[str, str, int]]
) -> List[str]:
    ordered = sorted(entries, key=_builder_sort_key)
    fragments: List[str] = []
    index = 0

    while index < len(ordered):
        key, value, _ = ordered[index]
        if index + 1 < len(ordered):
            next_key, next_value, _ = ordered[index + 1]
            if _can_pair_title_fragment(key, next_key):
                fragments.append(_pair_title_fragment(value, next_value))
                index += 2
                continue
        fragments.append(value)
        index += 1

    return fragments


def _builder_sort_key(entry: tuple[str, str, int]) -> tuple[tuple[int, ...], int, int]:
    key, _, position = entry
    numeric_key = tuple(int(token) for token in BUILDER_INDEX_RE.findall(key))
    return (numeric_key, _builder_suffix_priority(key), position)


def _builder_suffix_priority(key: str) -> int:
    if key.endswith("_title"):
        return 0
    if key.endswith("_content"):
        return 1
    if key.endswith("_text"):
        return 2
    if key.endswith("_description"):
        return 3
    return 4


def _can_pair_title_fragment(current_key: str, next_key: str) -> bool:
    if not PAIRABLE_TITLE_RE.match(current_key):
        return False
    prefix = current_key[: -len("_title")]
    return next_key in {f"{prefix}_text", f"{prefix}_content", f"{prefix}_description"}


def _pair_title_fragment(title: str, body: str) -> str:
    return f"<p><strong>{html.escape(clean_text(title))}</strong></p>\n{body}"


def _extract_links(content: str) -> Tuple[str, ...]:
    links = [clean_text(match.group(1)) for match in LINK_RE.finditer(content)]
    return tuple(link for link in links if link)


def _html_to_text(content: str) -> str:
    without_tags = TAG_RE.sub(" ", content)
    text = clean_text(html.unescape(without_tags))
    return re.sub(r"\s+([.,;:!?])", r"\1", text)


def _html_to_markdown(content: str) -> str:
    markdown = ANCHOR_RE.sub(_anchor_to_markdown, content)
    markdown = STRONG_RE.sub(_strong_to_markdown, markdown)
    markdown = HEADING_RE.sub(_heading_to_markdown, markdown)
    markdown = IMAGE_RE.sub(_image_to_markdown, markdown)
    markdown = LIST_ITEM_RE.sub(_list_item_to_markdown, markdown)
    markdown = BREAK_RE.sub("\n", markdown)
    markdown = BLOCK_TAG_RE.sub("\n\n", markdown)
    without_tags = TAG_RE.sub(" ", markdown)
    return _normalize_markdown_text(without_tags)


def _anchor_to_markdown(match: re.Match[str]) -> str:
    href = clean_text(html.unescape(match.group(1)))
    label = _html_to_text(match.group(2))
    if not href:
        return label
    if not label:
        return href
    return f"[{label}]({href})"


def _image_to_markdown(match: re.Match[str]) -> str:
    attributes = " ".join(part for part in match.groups() if part)
    src = clean_text(html.unescape(match.group(2)))
    alt_match = re.search(r"""alt\s*=\s*["']([^"']*)["']""", attributes, re.IGNORECASE)
    alt = clean_text(html.unescape(alt_match.group(1))) if alt_match else ""
    if not src:
        return ""
    return f"![{alt}]({src})"


def _strong_to_markdown(match: re.Match[str]) -> str:
    text = _html_to_text(match.group(1))
    if not text:
        return ""
    return f"**{text}**"


def _heading_to_markdown(match: re.Match[str]) -> str:
    level = max(1, min(6, int(match.group(1))))
    heading = _html_to_text(match.group(2))
    if not heading:
        return ""
    return f"\n\n{'#' * level} {heading}\n\n"


def _list_item_to_markdown(match: re.Match[str]) -> str:
    item = _html_to_text(match.group(1))
    if not item:
        return ""
    return f"\n- {item}"


def _normalize_markdown_text(value: str) -> str:
    text = html.unescape(value)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[^\S\n]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"\s+([.,;:!?])", r"\1", text)
    return text.strip()
