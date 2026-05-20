from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import shutil

from tools.migration_control.paths import slugify
from tools.readme_rebuild.models import DestinationPage

SLUG_OVERRIDES = {
    "Guides/companion-api.md": "companion-api-guide",
}

GUIDE_ORDER = (
    "get-started",
    "ask-ai",
    "our-apis",
    "security",
    "testing",
    "client-card-program",
    "client-testing-guide",
    "fraud",
    "glossary",
    "companion-api-guide",
    "issue-cards",
    "digital-first",
    "manage-cards",
    "secure-cards",
    "offline-pin",
    "manage-funds",
    "3d-secure",
    "automated-fuel-dispensers-afd-transactions",
    "secure-apis",
    "messages",
    "tokenization2",
    "token-payments",
    "token-processing",
    "token-provisioning",
    "token-lifecycle-management",
    "visa-token-provisioning",
    "settlement-and-reconciliation",
    "disputes",
    "klv-lookup",
    "card-api",
    "issue-card",
    "tokenization",
    "payments",
    "processing",
    "provisioning",
    "lifecycle-management",
    "reconciliation",
    "qr-payments-api",
    "qr-payments",
    "notifications",
    "report-generator-help",
    "tutuka-transaction-stream-2",
    "generatetimebasedsecret",
    "response-codes",
    "response-codes-2",
    "response-and-action-code-mapping",
    "reversedevalueprofile",
    "updateprofile",
    "home",
    "contact-us",
    "login",
    "privacy-policy",
    "api-reference-sample",
)

TOOLS_ORDER = (
    "tools",
    "simpos",
    "help",
    "simpos-result-codes",
    "xml-generator",
    "xml-poster",
    "checksum-generator",
    "checksum-generator-help",
    "3d-secure-customization",
    "one-time-password-otp-authentication",
    "out-of-band-oob-authentication",
)

REPORT_ROOT_ORDER = {
    "Companion API": 0,
    "Card API": 1,
    "QR Payments": 2,
    "Shared": 3,
}

REPORT_CHILD_ORDER_BY_FAMILY = {
    "Companion API": (
        "reports",
        "daily-statement-report",
        "mark-off-file",
        "blocked-transactions-report",
        "daily-sales-and-redemption-report",
        "vau-transaction-report",
        "authorisation-income-report",
        "daily-negative-balance-report",
        "inactive-cards-report",
        "google-pay-monthly-report",
        "card-balance-report",
        "linked-cards-report",
        "qvr-data-report",
        "qmr-data-report",
        "summary-settlement-report",
        "detailed-settlement-report",
        "forex-gains-report",
        "failed-transaction-report",
        "card-order-report",
        "unsettled-transactions-report-2",
        "apple-pay-quarterly-fee-billing-report",
        "apple-pay-monthly-top-merchant-report",
        "ecommerce-report",
        "apple-pay-monthly-metric-report",
        "apple-pay-monthly-usage-frequency-report",
        "apple-pay-monthly-fee-billing-report",
        "apple-pay-monthly-declines-report",
    ),
    "Card API": (
        "reports",
        "daily-statement-report",
        "vau-transaction-report",
        "qvr-data-report",
        "blocked-transactions-report",
        "mark-off-file",
        "daily-sales-and-redemption-report",
        "linked-cards-report",
        "card-balance-report",
        "inactive-cards-report",
        "authorisation-income-report",
        "google-pay-monthly-report",
        "qmr-data-report",
        "daily-negative-balance-report",
        "summary-settlement-report-2",
        "detailed-settlement-report",
        "forex-gains-report-2",
        "failed-transaction-report-2",
        "card-order-report-2",
        "ecommerce-report",
        "apple-pay-quarterly-fee-billing-report",
        "apple-pay-monthly-top-merchant-report",
        "apple-pay-monthly-metric-report",
        "apple-pay-monthly-usage-frequency-report",
        "apple-pay-monthly-fee-billing-report",
        "apple-pay-monthly-declines-report",
    ),
    "QR Payments": (
        "reports",
    ),
    "Shared": (
        "reporting-api",
        "reporting-api-2",
        "report-generator-offline",
    ),
}

GUIDE_ORDER_RANK = {slug: index for index, slug in enumerate(GUIDE_ORDER)}
TOOLS_ORDER_RANK = {slug: index for index, slug in enumerate(TOOLS_ORDER)}
REPORT_CHILD_ORDER_RANK = {
    family: {slug: index for index, slug in enumerate(slugs)}
    for family, slugs in REPORT_CHILD_ORDER_BY_FAMILY.items()
}


@dataclass(frozen=True)
class RdmeExportManifest:
    docs_count: int
    reference_count: int
    guide_categories: tuple[str, ...]
    reference_categories: tuple[str, ...]


def export_rdme_source(
    output_root: Path,
    pages: tuple[DestinationPage, ...],
    content_by_path: dict[str, str],
) -> RdmeExportManifest:
    shutil.rmtree(output_root, ignore_errors=True)
    docs_count = 0
    reference_count = 1
    guide_categories: set[str] = set()
    reference_categories: set[str] = {"Shared"}
    ordered_pages = _sorted_pages(pages)
    pages_by_bucket = _group_pages_by_bucket(ordered_pages)
    parent_slugs = _parent_slugs_by_bucket(pages_by_bucket)

    overview_path = output_root / "reference" / "shared" / "api-reference.md"
    overview_path.parent.mkdir(parents=True, exist_ok=True)
    overview_path.write_text(
        _build_frontmatter(
            title="API Reference",
            category_title="Shared",
            slug="api-reference",
            position=1,
            parent_slug=None,
        )
        + "\n\n"
        + _api_reference_overview_body()
        ,
        encoding="utf-8",
    )

    for bucket, bucket_pages in pages_by_bucket.items():
        start_position = 2 if bucket == ("reference", "Shared") else 1
        bucket_pages_by_source_id = {
            page.source_id: page for page in bucket_pages if page.source_id
        }
        for offset, page in enumerate(bucket_pages, start=start_position):
            export_path = output_root / _relative_export_path(page)
            export_path.parent.mkdir(parents=True, exist_ok=True)

            category_title = _category_title_for_page(page)
            body = _sanitize_body_for_rdme(
                _strip_leading_title(content_by_path[page.path], page.title)
            )
            export_title = _export_title_for_page(page)
            frontmatter = _build_frontmatter(
                title=export_title,
                category_title=category_title,
                slug=_slug_for_export(page),
                position=offset,
                parent_slug=_parent_slug_for_page(
                    page,
                    parent_slugs.get(bucket),
                    bucket_pages_by_source_id,
                ),
            )
            export_path.write_text(f"{frontmatter}\n\n{body}", encoding="utf-8")

            if page.top_bar == "API Reference":
                reference_count += 1
                reference_categories.add(category_title)
            else:
                docs_count += 1
                guide_categories.add(category_title)

    return RdmeExportManifest(
        docs_count=docs_count,
        reference_count=reference_count,
        guide_categories=tuple(sorted(guide_categories)),
        reference_categories=tuple(sorted(reference_categories)),
    )


def _sorted_pages(pages: tuple[DestinationPage, ...]) -> tuple[DestinationPage, ...]:
    return tuple(sorted(pages, key=lambda page: (page.source_index, page.path)))


def _group_pages_by_bucket(
    pages: tuple[DestinationPage, ...],
) -> dict[tuple[str, str], list[DestinationPage]]:
    grouped: dict[tuple[str, str], list[DestinationPage]] = defaultdict(list)
    for page in pages:
        grouped[_bucket_for_page(page)].append(page)

    for bucket, bucket_pages in grouped.items():
        grouped[bucket] = _ordered_bucket_pages(bucket_pages)

    return grouped


def _bucket_for_page(page: DestinationPage) -> tuple[str, str]:
    if page.top_bar == "API Reference":
        return ("reference", page.subsection)
    if page.top_bar == "Reports":
        return ("docs", "Reports")
    if page.top_bar == "Tools":
        return ("docs", "Tools")
    return ("docs", "Guides")


def _relative_export_path(page: DestinationPage) -> Path:
    path = Path(page.path)
    top = path.parts[0]

    if top == "API Reference":
        return Path("reference", path.parts[1], path.name)
    if top == "Reports":
        return Path("docs", "reports", slugify(page.subsection), path.name)
    if top == "Tools":
        return Path("docs", "tools", path.name)
    return Path("docs", "guides", path.name)


def _category_title_for_page(page: DestinationPage) -> str:
    if page.top_bar == "API Reference":
        return page.subsection
    if page.top_bar == "Reports":
        return "Reports"
    if page.top_bar == "Tools":
        return "Tools"
    return "Guides"


def _slug_for_export(page: DestinationPage) -> str:
    if page.top_bar == "Reports":
        subsection_slug = slugify(page.subsection)
        if page.slug == "reports":
            return f"{subsection_slug}-reports"
        return f"{subsection_slug}-{page.slug}"
    return SLUG_OVERRIDES.get(page.path, page.slug)


def _export_title_for_page(page: DestinationPage) -> str:
    slug = _slug_for_export(page)

    if page.top_bar == "Reports" and page.slug == "reports":
        return f"{page.subsection} Reports"

    if slug.endswith("-card-api"):
        return f"{page.title} (Card API)"

    tool_help_titles = {
        "3d-secure-customization-help": "3D Secure Customization Help",
        "xml-generator-help": "XML Generator Help",
        "simpos-help": "SIMPOS Help",
        "checksum-generator-help": "Checksum Generator Help",
    }
    if slug in tool_help_titles:
        return tool_help_titles[slug]

    return page.title


def _parent_slugs_by_bucket(
    pages_by_bucket: dict[tuple[str, str], list[DestinationPage]]
) -> dict[tuple[str, str], str]:
    parent_slugs: dict[tuple[str, str], str] = {}

    for bucket, pages in pages_by_bucket.items():
        for page in pages:
            if page.slug in {"api-reference", "reports", "tools"}:
                parent_slugs[bucket] = _slug_for_export(page)
                break

    return parent_slugs


def _bucket_page_sort_key(page: DestinationPage) -> tuple[int, int, int, int, str]:
    priority = 0 if page.slug in {"api-reference", "reports", "tools"} else 1
    return (
        priority,
        _section_order_rank(page),
        page.menu_order,
        page.source_index,
        page.path,
    )


def _ordered_bucket_pages(bucket_pages: list[DestinationPage]) -> list[DestinationPage]:
    pages_by_source_id = {page.source_id: page for page in bucket_pages if page.source_id}
    children_by_parent: dict[str, list[DestinationPage]] = defaultdict(list)
    roots: list[DestinationPage] = []

    for page in bucket_pages:
        if page.parent_source_id and page.parent_source_id in pages_by_source_id:
            children_by_parent[page.parent_source_id].append(page)
        else:
            roots.append(page)

    for children in children_by_parent.values():
        children.sort(key=_bucket_page_sort_key)
    roots.sort(key=_bucket_page_sort_key)

    ordered: list[DestinationPage] = []

    def visit(page: DestinationPage) -> None:
        ordered.append(page)
        for child in children_by_parent.get(page.source_id, ()):
            visit(child)

    for root in roots:
        visit(root)

    return ordered


def _section_order_rank(page: DestinationPage) -> int:
    export_slug = _slug_for_export(page)
    if page.top_bar == "Guides":
        return GUIDE_ORDER_RANK.get(export_slug, 10_000)
    if page.top_bar == "Tools":
        return TOOLS_ORDER_RANK.get(export_slug, 10_000)
    if page.top_bar == "Reports":
        if page.slug == "reports":
            return REPORT_ROOT_ORDER.get(page.subsection, 10_000)
        return REPORT_CHILD_ORDER_RANK.get(page.subsection, {}).get(page.slug, 10_000)
    return 10_000


def _parent_slug_for_page(
    page: DestinationPage,
    bucket_parent_slug: str | None,
    bucket_pages_by_source_id: dict[str, DestinationPage],
) -> str | None:
    if page.top_bar == "Reports":
        if page.slug == "reports":
            return None
        report_root = next(
            (
                candidate
                for candidate in bucket_pages_by_source_id.values()
                if candidate.top_bar == "Reports"
                and candidate.subsection == page.subsection
                and candidate.slug == "reports"
            ),
            None,
        )
        if report_root:
            return _slug_for_export(report_root)
    if page.parent_source_id and page.parent_source_id in bucket_pages_by_source_id:
        parent_page = bucket_pages_by_source_id[page.parent_source_id]
        return _slug_for_export(parent_page)
    if not bucket_parent_slug or _slug_for_export(page) == bucket_parent_slug:
        return None
    return bucket_parent_slug


def _strip_leading_title(content: str, title: str) -> str:
    lines = content.splitlines()
    heading = f"# {title}".strip()

    if lines and lines[0].strip() == heading:
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]

    body = "\n".join(lines).rstrip()
    return f"{body}\n" if body else ""


def _build_frontmatter(
    *,
    title: str,
    category_title: str,
    slug: str,
    position: int,
    parent_slug: str | None,
) -> str:
    lines = [
        "---",
        f"title: {_yaml_string(title)}",
        "category:",
        f"  uri: {_yaml_string(category_title)}",
        f"slug: {slug}",
        f"position: {position}",
    ]

    if parent_slug:
        lines.extend(
            (
                "parent:",
                f"  uri: {parent_slug}",
            )
        )

    lines.append("---")
    return "\n".join(lines)


def _yaml_string(value: str) -> str:
    if value == "":
        return '""'
    if any(character in value for character in ':#[]{}&*!|>\'"%@`"') or value != value.strip():
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return value


def _sanitize_body_for_rdme(body: str) -> str:
    sanitized = body.replace("![", "\n\n![")
    sanitized = re.sub(r"\n{3,}", "\n\n", sanitized)
    sanitized = _strip_legacy_navigation(sanitized)
    sanitized = _wrap_xml_blocks(sanitized)
    return sanitized


def _wrap_xml_blocks(body: str) -> str:
    lines = body.splitlines()
    output: list[str] = []
    buffer: list[str] = []

    def flush_buffer() -> None:
        nonlocal buffer
        if not buffer:
            return
        output.append("```xml")
        output.extend(buffer)
        output.append("```")
        buffer = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("<?xml") or stripped.startswith("<methodCall>") or stripped.startswith("<methodResponse>"):
            buffer.append(line)
            continue
        if buffer and stripped.startswith("<"):
            buffer.append(line)
            continue
        flush_buffer()
        output.append(line)

    flush_buffer()
    rendered = "\n".join(output).rstrip()
    return f"{rendered}\n" if rendered else ""


def _strip_legacy_navigation(body: str) -> str:
    lines = body.splitlines()
    filtered: list[str] = []
    for line in lines:
        if re.match(r"^\s{0,3}#*\s*\[back to .*?\]\(.*\)\s*$", line, re.IGNORECASE):
            continue
        filtered.append(line)
    rendered = "\n".join(filtered)
    rendered = re.sub(r"\n{3,}", "\n\n", rendered).strip()
    return f"{rendered}\n" if rendered else ""


def _api_reference_overview_body() -> str:
    return (
        "Browse the API families below using ReadMe's native reference navigation.\n\n"
        "- Card API\n"
        "- Companion API\n"
        "- QR Payments\n"
        "- Chargeback API\n"
        "- Shared\n"
    )
