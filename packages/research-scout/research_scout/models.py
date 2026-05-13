from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class PaperCandidate:
    source: str
    title: str
    url: str
    year: int | None = None
    doi: str | None = None
    abstract: str = ""
    authors: tuple[str, ...] = ()
    venue: str | None = None
    citation_count: int | None = None
    is_open_access: bool | None = None
    raw_text: str = ""
    observed_at: datetime = field(default_factory=utc_now)
    id: str | None = None


@dataclass(frozen=True, slots=True)
class ResearchCriteria:
    criteria_id: str
    query: str
    required_terms: tuple[str, ...] = ()
    optional_terms: tuple[str, ...] = ()
    excluded_terms: tuple[str, ...] = ()
    min_year: int | None = None
    require_open_access: bool = False
    min_citation_count: int | None = None
    preferred_methods: tuple[str, ...] = ()
    preferred_sources: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class MatchResult:
    criteria_id: str
    matched: bool
    reasons: tuple[str, ...]
    required_hits: tuple[str, ...] = ()
    optional_hits: tuple[str, ...] = ()
    method_hits: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ScoredPaper:
    candidate: PaperCandidate
    match: MatchResult
    score: float
    review_flags: tuple[str, ...] = ()
