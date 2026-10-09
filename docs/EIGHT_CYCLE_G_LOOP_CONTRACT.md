# Eight-cycle business model and G-loop contract

**Specification alignment:** 1.10  
**Date:** 9 October 2026  
**Status:** specified product contract; runtime implementation, migration, validation and activation are separate.

This contract extends the [organism architecture](ARCHITECTURE.md) with the standard eight-cycle business model, recognition-aware G-loop and baseline-first operating mode. For these subjects it takes precedence over older high-level summaries in this repository. It does not replace existing human gates, source-of-truth rules or the [public/private boundary](PUBLIC_PRIVATE_BOUNDARY.md).

## Generic product and configured instances

Kastel is a configurable commercial product. One shared, versioned kernel implements evidence processing, inference, recall, candidate comparison, action routing, evaluation and bounded memory. A standard business pack supplies eight cycles and a broad catalogue of potential latent states, sensing capabilities, actions and KPIs.

Each business supplies its own Kastel Stack Startup Model (KSSM): ontology, offers, segments, active states, observation links, generative hypotheses, expected delays, action policy, targets, constraints and permissions. Instances pin core and pack versions and retain separate adaptive state. Cross-instance learning is explicit transfer requiring applicability checks.

Reference use cases co-develop the same core; business identifiers and private strategy must not become generic kernel logic. Public examples use synthetic or sanitised records.

## Eight cycles and initial latent-state catalogue

The 47 states below are candidate constructs. Activate only states that are decision-relevant and have defined observations; unsupported estimates remain unknown. A latent state is not a directly observed KPI.

| Cycle | Candidate latent states |
| --- | --- |
| 1 Market / Demand | Qualified demand; problem salience; audience–offer relevance; channel resonance; trust/credibility |
| 2 Exchange / Conversion | Purchase intent; offer fit; price acceptability; purchase friction; customer readiness; repeat-buy propensity |
| 3 Delivery / Retention / Proof | Access friction; activation quality; experienced product value; engagement persistence; support burden; evidence/proof strength |
| 4 Offer / Capability | Product readiness; capability quality; technical reliability; network integration; development maturity; method confidence |
| 5 Distribution / Network | Partner fit; relationship strength; reciprocal value; distribution leverage; referral quality; network momentum |
| 6 Finance / Capital / Viability | Financial viability; liquidity resilience; adaptation capacity; cost pressure; reinvestment capacity; financial constraint severity |
| 7 Operations / People / Capacity | Operational slack; owner overload; process efficiency; automation maturity; bottleneck pressure; delivery capacity |
| 8 Governance / Legal / Structure | Governance fit; regulatory exposure; contractual adequacy; privacy fit; structural fit; jurisdictional risk |

Environmental sensing, learning, portfolio/resource allocation and cross-cycle relations are shared functions, not additional cycles.

**SEO belongs explicitly to Cycle 1:** search demand, query intent, organic discovery, content relevance and qualified routes into offers. Cycle 4 owns technical implementation such as crawlability, indexing and performance repairs; Cycle 5 owns relationship-led links and referrals. Give each intervention one primary owner and secondary cycle references where necessary.

## Sensing action and KPI capabilities

These are potential integration capabilities, not claims that connectors are implemented or connected. Support multiple authorised provider adapters where useful, plus manual/CSV imports. Provider identity remains an adapter detail; every installation declares availability, permissions, freshness, coverage, quotas and source-of-truth mappings.

| Cycle | Potential sensing capabilities | Action classes | Example KPIs |
| --- | --- | --- | --- |
| 1 | Search analytics/index inspection, web analytics, market/research feeds, audience replies | SEO/content work, audience/channel proposals, demand tests | Qualified organic visits, visitor-to-lead rate, qualified enquiries |
| 2 | Checkout, payment, email and CRM events, objections | Checkout repairs, offer/CTA proposals, approved conversion tests | Conversion with denominator, checkout completion, contribution per order |
| 3 | Product/entitlement events, support records, surveys | Access repairs, onboarding/support work, retention tests | Activation, time to first value, mature-cohort retention |
| 4 | Repository/QA events, monitoring, reliability and research records | Product fixes, release checks, capability tests | Failed releases, recovery time, blocked days |
| 5 | Partner CRM, correspondence, referrals and affiliate outcomes | Qualification, collaboration proposals, approved partner actions | Partner progression, activated partners, attributable contribution |
| 6 | Payment reconciliation, accounting, cash and obligation records | Budget/cost proposals, financial constraints | Net cash flow, cash buffer, contribution margin |
| 7 | Tasks, calendars, time records, support and automation logs | Workload allocation, process repair, automation proposals | Available capacity, backlog age, rework |
| 8 | Contract/data-use registers, official updates, professional assessments | Reviews, approval holds, policy/structure proposals | Overdue reviews, unresolved obligations, exception age |

Read access never grants write authority. Action contracts include preconditions, cost/capacity bounds, approval route, deduplication, expected outcome, stop conditions and receipts. Sources cannot manufacture legal or causal certainty.

## Evidence and causal modelling

Use the explicit sequence: observation → observation model → latent-state estimate/confidence/precision → generative expectation → action/outcome → prediction error.

Keep state, confidence and evidence precision separately inspectable. Define indicator direction, diagnosticity, expected lag, confounds and provenance. KPI contracts include scope, formula, denominator, cohort, time window, currency where relevant and outcome maturity. Missing data are not zero; a shared event may inform several cycles without being counted as independent evidence.

Generative relationships begin as declared hypotheses with evidence status. Preserve competing explanations. Predictive fit or an observational association is not causal proof; a learned causal graph is not a prerequisite for v1.

## Six trajectory states

| State | Meaning |
| --- | --- |
| GROWING | Exploit worthwhile gains at acceptable cost and risk |
| TUNING | Improve an identifiable local bottleneck inside the present strategy |
| PLATEAU | Adequate observation and local tuning indicate diminishing returns |
| REOPENING | Make materially different alternatives reachable |
| VALIDATING | Narrow alternatives through prospective tests and boundary checks |
| BANKED | Reuse bounded reliable structure until a review or reopening trigger |

Store cycle and horizon with each state. One flat observation does not establish PLATEAU. Mismatch is an alert, and RECALL is an operation; neither is a seventh trajectory state.

## Recognition-aware G-loop

The kernel operates from current KSSM expectations:

1. SENSE observations and LOCATE the cycle/horizon state.
2. RECALL relevant banked strategies and ASSESS APPLICABILITY.
3. Select/generate a small bounded Candidate Workspace with provenance.
4. FORECAST plausible futures.
5. EVALUATE benefits, costs, downside, reversibility, viability, learning and optionality.
6. COMMIT proportionately under existing gates and PREDICT before acting.
7. ACT, OBSERVE and COMPARE outcomes against the recorded prediction.
8. ADAPT, update evidence/model versions where justified, and BANK only bounded validated learning.

The canonical adaptive decisions are CONTINUE, TUNE, IMPROVE_SENSING, CONSTRAIN, REOPEN, PAUSE, REVERT_TO_BANKED, ABANDON, VALIDATE and BANK.

Applicability operations include DIRECT_REUSE, TRANSFER_TEST, ADAPT and RECOMBINE. Changed-context reuse and recombination are candidates requiring validation, not automatic BANKED knowledge. Natural-language “switch” maps to a suitable validated strategy or a candidate test under these gates.

Recall before reopening unless a documented urgency exception applies. Reopening depth distinguishes R1 local tactics, R2 strategy/commercial mechanism and R3 architecture/market representation. Match revision scale to evidence; one local failure is not a pivot mandate.

## Baseline-first mode

A new instance normally starts in BASELINE_ESTABLISHMENT. Onboarding offers a **configurable 60–90 day initial review window**, with explicit episode counts, coverage and outcome-maturity requirements. An instance-specific programme can use another window. Elapsed time alone does not enable adaptation.

Hold the approved non-urgent operating policy, structural hypotheses, state/measurement definitions, KPI denominators and constraints stable. Continue formulaic business activity and observe its consequences.

Permit evidence-linked updates to latent-state estimates, confidence, evidence precision and expected observation ranges/lags. This is predictive calibration, not business-policy TUNE. Keep dated calibration/model lineage and original forecasts; never rewrite past predictions with later expectations.

| Operation | Baseline default | After approved exit |
| --- | --- | --- |
| Continue routine policy and collect evidence | Enabled within existing permissions | Enabled |
| Calibrate estimates, confidence, ranges and lags | Enabled with lineage; no hidden policy change | Enabled with lineage |
| Recall and compare alternatives | Shadow proposals only | Reuse or test according to applicability |
| Discretionary TUNE, REOPEN or experiments | Deferred | Bounded and gated |
| Bank a newly inferred rule | No automatic promotion | Only after evidence and review requirements |
| Critical operational exception | Recorded, authorised and segmented | Existing gates still apply |

Exceptions cover safety, customer service, legality/regulation, viability, data integrity, critical defects and release readiness. Record reason, authority, effective time, affected cycles/KPIs and comparability boundaries. Structural definition changes require a versioned amendment rather than silent calibration.

A TUNING diagnosis does not open the action gate. Shadow candidates cannot influence the active selector. Insufficient evidence leaves affected decisions unresolved or extends their baseline. Owner review authorises entry to ADAPTIVE_VALIDATION; it does not authorise unrestricted self-modification.

## Coordination and implementation checks

Cycle instances share evidence and model services within their business instance. A coordinator resolves conflicts and enforces money, time, delivery and governance constraints across cycles. A demand opportunity cannot override delivery capacity or viability.

Implementation acceptance must show:

- All eight cycles are configurable without business-specific kernel code.
- New observations update an inspectable state/KPI; duplicates and missing data are handled correctly.
- Operating mode, trajectory state and decision permission remain separate.
- Baseline calibration works while discretionary business tuning remains blocked.
- Recall/applicability, bounded alternatives and future evaluation precede consequential commitment.
- Predictions precede actions; delayed/boundary checks precede banking.
- Exceptions preserve lineage and comparability; elapsed time alone cannot trigger adaptive mode.
- Model revisions retain predecessors and rollback paths; instance data remain isolated.

These are specification requirements. Passing them requires implementation and runtime evidence; this document does not assert that those gates have passed.
