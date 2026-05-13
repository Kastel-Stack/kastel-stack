from __future__ import annotations

from research_scout.matching.criteria import match_candidate
from research_scout.models import PaperCandidate, ResearchCriteria, ScoredPaper


def _review_flags(candidate: PaperCandidate) -> tuple[str, ...]:
    flags: list[str] = []
    if not candidate.abstract:
        flags.append("missing abstract")
    if candidate.is_open_access is not True:
        flags.append("access check needed")
    if candidate.citation_count is None:
        flags.append("citation count unknown")
    if candidate.year is None:
        flags.append("year unknown")
    return tuple(flags)


def score_candidate(candidate: PaperCandidate, criteria: ResearchCriteria) -> ScoredPaper:
    match = match_candidate(candidate, criteria)
    if not match.matched:
        return ScoredPaper(candidate=candidate, match=match, score=0.0, review_flags=_review_flags(candidate))

    score = 50.0
    score += 10.0 * len(match.required_hits)
    score += 4.0 * len(match.optional_hits)
    score += 5.0 * len(match.method_hits)

    if criteria.preferred_sources and candidate.source in criteria.preferred_sources:
        score += 6.0
    if candidate.is_open_access is True:
        score += 5.0
    if candidate.citation_count is not None:
        score += min(12.0, candidate.citation_count / 25.0)
    if candidate.year is not None and criteria.min_year is not None:
        score += min(8.0, max(0, candidate.year - criteria.min_year) * 0.5)

    return ScoredPaper(
        candidate=candidate,
        match=match,
        score=round(score, 2),
        review_flags=_review_flags(candidate),
    )


def score_candidates(candidates: list[PaperCandidate], criteria: ResearchCriteria) -> list[ScoredPaper]:
    scored = [score_candidate(candidate, criteria) for candidate in candidates]
    return sorted(scored, key=lambda item: item.score, reverse=True)
