from __future__ import annotations

from research_scout.models import MatchResult, PaperCandidate, ResearchCriteria


def _search_text(candidate: PaperCandidate) -> str:
    return " ".join(
        part
        for part in (
            candidate.title,
            candidate.abstract,
            candidate.venue or "",
            candidate.raw_text,
        )
        if part
    ).lower()


def _hits(terms: tuple[str, ...], text: str) -> tuple[str, ...]:
    return tuple(term for term in terms if term.lower() in text)


def match_candidate(candidate: PaperCandidate, criteria: ResearchCriteria) -> MatchResult:
    text = _search_text(candidate)
    reasons: list[str] = []

    excluded_hits = _hits(criteria.excluded_terms, text)
    if excluded_hits:
        return MatchResult(criteria.criteria_id, False, tuple(f"excluded term: {term}" for term in excluded_hits))

    required_hits = _hits(criteria.required_terms, text)
    missing_required = tuple(term for term in criteria.required_terms if term not in required_hits)
    if missing_required:
        reasons.append("missing required terms: " + ", ".join(missing_required))

    if criteria.min_year is not None and (candidate.year is None or candidate.year < criteria.min_year):
        reasons.append(f"year below minimum: {candidate.year or 'unknown'}")

    if criteria.require_open_access and candidate.is_open_access is not True:
        reasons.append("not confirmed open access")

    if (
        criteria.min_citation_count is not None
        and candidate.citation_count is not None
        and candidate.citation_count < criteria.min_citation_count
    ):
        reasons.append(f"citation count below minimum: {candidate.citation_count}")

    optional_hits = _hits(criteria.optional_terms, text)
    method_hits = _hits(criteria.preferred_methods, text)
    return MatchResult(
        criteria_id=criteria.criteria_id,
        matched=not reasons,
        reasons=tuple(reasons) if reasons else ("matched",),
        required_hits=required_hits,
        optional_hits=optional_hits,
        method_hits=method_hits,
    )


def match_candidates(candidates: list[PaperCandidate], criteria: ResearchCriteria) -> list[MatchResult]:
    return [match_candidate(candidate, criteria) for candidate in candidates]
