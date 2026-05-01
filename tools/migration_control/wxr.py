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
SERIALIZED_VALUE_RE = re.compile(r"^[abisOdN]:\d*(?:[:;{])")
ANCHOR_RE = re.compile(
    r"""<a\b[^>]*href\s*=\s*["']([^"']+)["'][^>]*>(.*?)</a>""",
    re.IGNORECASE | re.DOTALL,
)
IMAGE_RE = re.compile(
    r"""<img\b([^>]*?)src\s*=\s*["']([^"']+)["']([^>]*)>""",
    re.IGNORECASE | re.DOTALL,
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

    content = _text(item, "content:encoded")
    if _keep_content_fragment(content):
        fragments.append(content)

    for meta in item.findall("wp:postmeta", NS):
        key = clean_text(_text(meta, "wp:meta_key"))
        if not BUILDER_CONTENT_KEY_RE.match(key):
            continue

        value = _text(meta, "wp:meta_value")
        if _keep_content_fragment(value):
            fragments.append(value)

    return "\n\n".join(fragment for fragment in fragments if clean_text(fragment))


def _keep_content_fragment(value: str) -> bool:
    cleaned = clean_text(value)
    if not cleaned:
        return False
    if SERIALIZED_VALUE_RE.match(cleaned):
        return False
    return True


def _extract_links(content: str) -> Tuple[str, ...]:
    links = [clean_text(match.group(1)) for match in LINK_RE.finditer(content)]
    return tuple(link for link in links if link)


def _html_to_text(content: str) -> str:
    without_tags = TAG_RE.sub(" ", content)
    text = clean_text(html.unescape(without_tags))
    return re.sub(r"\s+([.,;:!?])", r"\1", text)


def _html_to_markdown(content: str) -> str:
    markdown = ANCHOR_RE.sub(_anchor_to_markdown, content)
    markdown = IMAGE_RE.sub(_image_to_markdown, markdown)
    without_tags = TAG_RE.sub(" ", markdown)
    text = clean_text(html.unescape(without_tags))
    return re.sub(r"\s+([.,;:!?])", r"\1", text)


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
