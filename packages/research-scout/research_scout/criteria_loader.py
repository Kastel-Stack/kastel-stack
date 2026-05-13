from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_scout.models import ResearchCriteria


def _tuple_of_strings(payload: dict[str, Any], key: str) -> tuple[str, ...]:
    value = payload.get(key, ())
    if value is None:
        return ()
    if not isinstance(value, list):
        raise ValueError(f"{key} must be a list of strings")
    return tuple(str(item) for item in value)


def criteria_from_dict(payload: dict[str, Any]) -> ResearchCriteria:
    return ResearchCriteria(
        criteria_id=str(payload["criteria_id"]),
        query=str(payload["query"]),
        required_terms=_tuple_of_strings(payload, "required_terms"),
        optional_terms=_tuple_of_strings(payload, "optional_terms"),
        excluded_terms=_tuple_of_strings(payload, "excluded_terms"),
        min_year=payload.get("min_year"),
        require_open_access=bool(payload.get("require_open_access", False)),
        min_citation_count=payload.get("min_citation_count"),
        preferred_methods=_tuple_of_strings(payload, "preferred_methods"),
        preferred_sources=_tuple_of_strings(payload, "preferred_sources"),
    )


def load_criteria(path: str | Path) -> ResearchCriteria:
    with Path(path).open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("criteria file must contain a JSON object")
    return criteria_from_dict(payload)
