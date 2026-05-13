# Kastel Research Scout

Criteria-driven research paper scouting for Kastel Stack.

This package adapts the useful shape of a market-scanner pipeline to evidence discovery:

```text
sources -> candidate records -> normalization -> criteria matching -> scoring -> digest
```

It is intended for human-supervised evidence workflows, not automated literature judgement.
The scout can collect or ingest paper candidates, rank them against an explicit criteria
profile, and produce review-ready observations for a Kastel lane.

## What It Does

- Normalizes paper records from common JSON-style payloads.
- Deduplicates candidates by DOI, URL, or stable title fingerprint.
- Matches candidates against explicit research criteria.
- Scores candidates by criteria fit and review affordances.
- Renders a compact digest for human review.

## Run Tests

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## Example Criteria

See `config/sample-criteria.json`.
