# Research Scout

Research Scout is an incubating Kastel Stack package for criteria-driven evidence discovery.
It generalizes the useful pattern from a small market-scanner project into a review-gated
paper scouting workflow.

## Purpose

Research Scout helps a lane find candidate papers against explicit criteria, rank them for
human review, and emit source-grounded observations. It does not decide what the evidence
means and should not be used as an automated claim engine.

## Pipeline

```text
source adapters
-> PaperCandidate records
-> normalization and dedupe
-> ResearchCriteria matching
-> relevance scoring
-> digest / observation output
-> human review
-> source-of-truth registry or script banking, if warranted
```

## Current Package

```text
packages/research-scout/
```

The package includes:

- `research_scout.models` for candidate, criteria, match, and score records.
- `research_scout.sources.base` for common JSON payload normalization.
- `research_scout.matching.criteria` for explicit criteria matching.
- `research_scout.scoring.relevance` for review-priority scoring.
- `research_scout.jobs.digest` for compact human-review digests.
- `config/sample-criteria.json` for a cognitive-training example.

## Kastel Fit

Research Scout belongs in the external intelligence / evidence lane. It can support:

- research monitoring for Trident-G, IQ Mindware, Wellness, and Recovery products
- evidence rollups before claim updates
- competitor or adjacent-method scanning, if criteria are changed
- source-of-truth registry updates after human review
- Clarify Intent generation when candidates are ambiguous or under-specified

## Governance Defaults

- `Auto-run`: scheduled source queries and candidate normalization.
- `Draft-for-approval`: digests, summaries, evidence tables, candidate shortlists.
- `Escalate`: product claims, clinical claims, legal/regulatory language, pricing or sales claims based on evidence.
- `Blocked`: unsupported automated claim changes or medical recommendations.

## Next Implementation Steps

1. Add source-specific adapters for OpenAlex, Semantic Scholar, PubMed, Crossref, and arXiv.
2. Add persistent storage for observations and review status.
3. Emit `ResearchScoutObservation.v1` events into the Kastel event log.
4. Add a review UI or GitHub issue template for evidence triage.
5. Add claim-linking rules so reviewed papers connect back to public-facing claims.
