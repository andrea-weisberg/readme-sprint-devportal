from __future__ import annotations

from tools.readme_rebuild.models import Classification, SourcePage


def classify_page(page: SourcePage) -> Classification:
    url = page.source_url.lower()
    title = page.title.lower()

    if "/tools/" in url:
        return Classification("Tools", "Tools", "tool utility url")
    if "/api-reference/" in url or "/chargeback-api/" in url or "/profile-api-reference/" in url:
        return Classification("API Reference", _api_family_for_url(url) or "Shared", "reference path")
    if "/reports/" in url or "report" in title:
        return Classification("Reports", _api_family_for_url(url) or "Shared", "report url or title")
    return Classification("Guides", "Shared", "default shared guide")


def _api_family_for_url(url: str) -> str:
    if "/card-api/" in url:
        return "Card API"
    if "/companion-api/" in url:
        return "Companion API"
    if "/qr-payments-api/" in url:
        return "QR Payments"
    if "/chargeback-api/" in url:
        return "Chargeback API"
    if "/profile-api-reference/" in url:
        return "Profile API Reference"
    return ""
