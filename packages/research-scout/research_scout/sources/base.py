from __future__ import annotations

import json
import time
from typing import Any, Iterable
from urllib.error import URLError
from urllib.request import Request, urlopen

from research_scout.models import PaperCandidate


def fetch_json(url: str, timeout_s: int = 20, retries: int = 2, backoff_s: float = 1.5) -> dict[str, Any]:
    request = Request(
        url=url,
        headers={
            "User-Agent": "KastelResearchScout/0.1 (+human-supervised-evidence-scout)",
            "Accept": "application/json",
        },
    )
    for attempt in range(retries + 1):
        try:
            with urlopen(request, timeout=timeout_s) as response:
                return json.loads(response.read().decode("utf-8", errors="ignore"))
        except (URLError, json.JSONDecodeError):
            if attempt >= retries:
                raise
            time.sleep(backoff_s * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}")


def records_from_payload(payload: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for key in ("results", "items", "data", "works"):
        value = payload.get(key)
        if isinstance(value, list):
            return value
    message = payload.get("message")
    if isinstance(message, dict) and isinstance(message.get("items"), list):
        return message["items"]
    return ()


def _first_string(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    if isinstance(value, list):
        for item in value:
            found = _first_string(item)
            if found:
                return found
    return None


def _authors(record: dict[str, Any]) -> tuple[str, ...]:
    authors = record.get("authors") or record.get("author") or record.get("authorships") or ()
    names: list[str] = []
    if isinstance(authors, list):
        for author in authors:
            if isinstance(author, str):
                names.append(author)
            elif isinstance(author, dict):
                name = author.get("name")
                if not name and isinstance(author.get("author"), dict):
                    name = author["author"].get("display_name")
                if name:
                    names.append(str(name))
    return tuple(names)


def paper_from_record(record: dict[str, Any], source: str) -> PaperCandidate | None:
    title = _first_string(record.get("title") or record.get("display_name"))
    url = _first_string(record.get("url") or record.get("URL") or record.get("landing_page_url"))
    doi = _first_string(record.get("doi") or record.get("DOI"))
    if not url and doi:
        url = f"https://doi.org/{doi.removeprefix('https://doi.org/')}"
    if not title or not url:
        return None

    abstract = _first_string(record.get("abstract") or record.get("abstractText")) or ""
    venue = _first_string(record.get("venue") or record.get("container-title") or record.get("publicationVenue"))
    year = record.get("year") or record.get("publication_year") or record.get("published")
    citation_count = record.get("citation_count") or record.get("cited_by_count") or record.get("is-referenced-by-count")
    is_open_access = record.get("is_open_access")
    if is_open_access is None and isinstance(record.get("open_access"), dict):
        is_open_access = record["open_access"].get("is_oa")

    return PaperCandidate(
        source=source,
        title=title,
        url=url,
        year=int(year) if isinstance(year, int | str) and str(year).isdigit() else None,
        doi=doi,
        abstract=abstract,
        authors=_authors(record),
        venue=venue,
        citation_count=int(citation_count) if isinstance(citation_count, int | str) and str(citation_count).isdigit() else None,
        is_open_access=bool(is_open_access) if is_open_access is not None else None,
        raw_text=json.dumps(record, sort_keys=True),
    )


def papers_from_payload(payload: dict[str, Any], source: str) -> list[PaperCandidate]:
    candidates: list[PaperCandidate] = []
    for record in records_from_payload(payload):
        if not isinstance(record, dict):
            continue
        candidate = paper_from_record(record, source)
        if candidate:
            candidates.append(candidate)
    return candidates
