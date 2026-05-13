from __future__ import annotations

import re

from research_scout.dedupe import title_fingerprint
from research_scout.models import PaperCandidate


SPACE_RE = re.compile(r"\s+")


def compact_text(text: str) -> str:
    return SPACE_RE.sub(" ", text).strip()


def normalize_candidate(candidate: PaperCandidate) -> PaperCandidate:
    title = compact_text(candidate.title)
    abstract = compact_text(candidate.abstract)
    raw_text = compact_text(" ".join(part for part in (title, abstract, candidate.raw_text) if part))
    candidate.title = title
    candidate.abstract = abstract
    candidate.raw_text = raw_text
    if candidate.doi:
        candidate.doi = candidate.doi.lower().strip()
    if not candidate.id:
        candidate.id = candidate.doi or title_fingerprint(title)
    return candidate


def normalize_candidates(candidates: list[PaperCandidate]) -> list[PaperCandidate]:
    return [normalize_candidate(candidate) for candidate in candidates if candidate.title and candidate.url]
