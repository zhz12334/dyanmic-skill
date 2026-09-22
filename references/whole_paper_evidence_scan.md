# Whole-Paper and Cross-Chapter Evidence Scan

## Purpose

Prevent a local chapter omission from being misclassified as a genuinely missing parameter/model detail.

## Mandatory scope

Before declaring a claim-critical item missing, inspect the complete target paper:
- all chapters, including later application/validation chapters;
- figure/table captions and notes;
- nomenclature/symbol lists;
- appendices;
- experiment/setup sections;
- summaries/conclusions that restate methods or conditions;
- equations reused by reference to earlier sections;
- parameter tables that are inherited across chapters.

## Outputs

Create:
- `chapter_registry.csv`;
- `cross_chapter_evidence_links.csv`;
- `reference_use_registry.csv`.

## Cross-chapter relation types

Use at least:
- `INTRODUCES`;
- `REUSES`;
- `SPECIALIZES`;
- `OVERRIDES`;
- `VALIDATES`;
- `CONTRADICTS`;
- `PROVIDES_MISSING_VALUE`;
- `PROVIDES_OPERATING_CONDITION`;
- `PROVIDES_NUMERICAL_PROTOCOL`.

## Hard rule

`missing in this section` is not equivalent to `missing from the paper`.

An item may enter H/C only after the whole-paper search is complete and, when applicable, citation-lineage closure is complete.

## Reading order vs execution order

The evidence-reading plan is whole-paper-first. The reproduction execution plan is created later from the physics/model dependency DAG. A later chapter may close an earlier parameter gap without becoming an earlier reproduction target.


## RC2: back-propagating later-chapter evidence

When a later chapter provides geometry, operating conditions, experimental settings or a healthy numerical result needed to instantiate/validate an earlier module, record the relation and back-propagate the evidence before implementation. This does **not** change execution order or activate the later chapter's new physics.

## RC2: borrowed validation evidence

If the target paper reproduces or reuses experimental/data evidence from a cited source, classify it as `BORROWED_VALIDATION_DATA`. The target-paper figure location and the true experimental/data origin must both remain in provenance. Critical borrowed evidence requires direct-source closure before final validation.
