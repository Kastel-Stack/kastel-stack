# Script Banking

Kastel does not bank one-off wins as permanent truth.

It banks portable operating patterns that have evidence, context, boundary conditions, delayed review and validation metadata.

## Rule

```text
Do not bank a win.
Bank a portable operating pattern.
```

## Validation Ladder

| Status | Meaning |
| --- | --- |
| Observed | Worked once in one node, not delayed-reviewed. |
| Delayed checked | Reviewed after a defined delay and still interpretable. |
| Replicated | Tested by more than one node or more than one context. |
| Cross-context validated | Survived a changed wrapper, segment, channel, timing, node or local context. |
| Banked | Safe, documented, bounded, reusable and approved for wider adaptation. |
| Retired | Unsafe, obsolete, misleading, context-bound or no longer useful. |

Observed scripts may be stored locally.

Network-shared scripts must carry validation metadata.

Banked scripts require delayed review and at least one portability signal.

## Required Metadata

Every script should carry:

- script name
- node type
- original context
- action type
- source-of-truth outcome
- expected result
- observed result
- delayed reviews completed
- tested-by-node count
- contexts tested
- known failure modes
- boundary conditions
- last reviewed date
- confidence level
- shareability level
- validation status

## Validation Badges

User-facing apps and commons views should expose simple badges:

- Observed
- Delayed checked
- Tested by N nodes
- Cross-context validated
- Banked
- Retired

These badges let Light Nodes use the commons without inspecting the full evidence trail every time.

## Network Memory

A node may contribute a redacted script to network memory when:

- it is safe to share
- it does not expose private customer data
- it does not expose sensitive partner information
- it has a clear context of use
- it includes failure modes
- it has survived at least one delayed review
- it is adaptable rather than prescriptive
- it carries validation metadata

Network memory should support local adaptation, not enforce uniformity.
