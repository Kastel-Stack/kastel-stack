from __future__ import annotations

from datetime import datetime, timezone

from research_scout.models import ResearchCriteria, ScoredPaper


def render_research_digest(
    criteria: ResearchCriteria,
    scored: list[ScoredPaper],
    as_of: datetime | None = None,
    limit: int = 10,
) -> str:
    timestamp = (as_of or datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"Research Scout Digest ({timestamp})",
        f"Criteria: {criteria.criteria_id}",
        f"Query: {criteria.query}",
        "",
    ]
    matches = [item for item in scored if item.score > 0]
    if not matches:
        lines.append("No criteria-matching papers found in this run.")
        return "\n".join(lines)

    for idx, item in enumerate(matches[:limit], start=1):
        candidate = item.candidate
        lines.extend(
            [
                f"{idx}. {candidate.title}",
                f"   Score: {item.score:.2f}",
                f"   Source: {candidate.source}",
                f"   Year: {candidate.year or 'unknown'}",
                f"   Venue: {candidate.venue or 'unknown'}",
                f"   Citations: {candidate.citation_count if candidate.citation_count is not None else 'unknown'}",
                f"   Open access: {candidate.is_open_access if candidate.is_open_access is not None else 'unknown'}",
                f"   Hits: {', '.join(item.match.required_hits + item.match.optional_hits + item.match.method_hits) or 'none'}",
                f"   Review flags: {', '.join(item.review_flags) or 'none'}",
                f"   Link: {candidate.url}",
                "",
            ]
        )
    return "\n".join(lines).rstrip()
