from research_scout.criteria_loader import criteria_from_dict
from research_scout.dedupe import dedupe_candidates
from research_scout.jobs.digest import render_research_digest
from research_scout.models import PaperCandidate
from research_scout.normalize import normalize_candidates
from research_scout.scoring.relevance import score_candidates
from research_scout.sources.base import papers_from_payload


def _criteria():
    return criteria_from_dict(
        {
            "criteria_id": "wm-transfer",
            "query": "working memory transfer",
            "required_terms": ["working memory", "training"],
            "optional_terms": ["far transfer", "reasoning"],
            "excluded_terms": ["animal study"],
            "min_year": 2010,
            "preferred_methods": ["randomized", "active control"],
            "preferred_sources": ["openalex"],
        }
    )


def test_scores_matching_research_candidate() -> None:
    candidate = PaperCandidate(
        source="openalex",
        title="Working memory training improves reasoning in a randomized active control trial",
        url="https://example.test/paper",
        year=2021,
        abstract="A far transfer study of working memory training.",
        citation_count=120,
        is_open_access=True,
    )

    scored = score_candidates([candidate], _criteria())

    assert scored[0].score > 80
    assert scored[0].match.matched
    assert "working memory" in scored[0].match.required_hits


def test_rejects_excluded_candidate() -> None:
    candidate = PaperCandidate(
        source="openalex",
        title="Working memory training in an animal study",
        url="https://example.test/paper",
        year=2021,
        abstract="Animal study with training.",
    )

    scored = score_candidates([candidate], _criteria())

    assert scored[0].score == 0
    assert not scored[0].match.matched


def test_payload_normalization_and_dedupe() -> None:
    payload = {
        "results": [
            {
                "display_name": "Working memory training and far transfer",
                "doi": "10.1234/ABC",
                "publication_year": 2022,
                "abstract": "A randomized study of working memory training.",
                "cited_by_count": 10,
                "open_access": {"is_oa": True},
            },
            {
                "title": ["Working memory training and far transfer"],
                "DOI": "10.1234/abc",
                "year": 2022,
            },
        ]
    }

    candidates = normalize_candidates(papers_from_payload(payload, "openalex"))
    unique = dedupe_candidates(candidates)

    assert len(unique) == 1
    assert unique[0].doi == "10.1234/abc"


def test_digest_includes_review_flags() -> None:
    candidate = PaperCandidate(
        source="openalex",
        title="Working memory training improves reasoning",
        url="https://example.test/paper",
        year=2021,
        abstract="A working memory training study.",
    )

    digest = render_research_digest(_criteria(), score_candidates([candidate], _criteria()))

    assert "Research Scout Digest" in digest
    assert "access check needed" in digest
