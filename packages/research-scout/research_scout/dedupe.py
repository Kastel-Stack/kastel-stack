from __future__ import annotations

import hashlib
import re

from research_scout.models import PaperCandidate


SPACE_RE = re.compile(r"\s+")
PUNCT_RE = re.compile(r"[^a-z0-9 ]+")


def title_fingerprint(title: str) -> str:
    normalized = PUNCT_RE.sub(" ", title.lower())
    normalized = SPACE_RE.sub(" ", normalized).strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def candidate_key(candidate: PaperCandidate) -> str:
    if candidate.doi:
        return f"doi:{candidate.doi.lower().strip()}"
    if candidate.url:
        return f"url:{candidate.url.lower().strip()}"
    return f"title:{title_fingerprint(candidate.title)}"


def dedupe_candidates(candidates: list[PaperCandidate]) -> list[PaperCandidate]:
    seen: set[str] = set()
    unique: list[PaperCandidate] = []
    for candidate in candidates:
        key = candidate_key(candidate)
        if key in seen:
            continue
        seen.add(key)
        unique.append(candidate)
    return unique
