# Same-Author / Same-Group Literature Cross-Evidence Strategy

## Purpose

Before a claim-critical formula, model choice or parameter is declared unavailable, the reproduction must search the target authors' own related publications and the same research group's model-family literature. This source family is often the strongest non-code evidence for details omitted from a target article.

This is a **mandatory evidence-recovery and cross-validation step**, not an optional literature review.

## Search scope

Search, as relevant:

1. first/corresponding/coauthors' prior papers on the same system/model/method;
2. later papers that inherit, refine, restate or validate the target model;
3. theses/dissertations by the authors or same laboratory;
4. conference/journal versions and technical reports;
5. same-group papers using the same apparatus, specimen, geometry, parameter table, solver setup, contact/constitutive law or experiment rig;
6. papers from the same project/grant/model family when the link is explicit.

Do not rely only on title similarity. Search by model name, distinctive equation terms, apparatus name, specimen dimensions, solver method, parameter symbols, figure labels and cited foundational sources.

## Required artifacts

Create:

- `author_group_literature_map.csv` — map publications to the target model/system/method lineage;
- `cross_parameter_validation.csv` — parameter/theory cross-checks across sources;
- update `theory_research_log.csv` and `evidence_conflict_register.csv` as needed.

## Cross-evidence roles

Classify each related source as:

- `SAME_MODEL_DIRECT` — explicit inheritance/reuse of the same mathematical/physical model;
- `SAME_SYSTEM_SAME_GROUP` — same physical system/specimen/assembly but possibly different study question;
- `SAME_EXPERIMENTAL_RIG` — same rig/fixture/sensors/DAQ/protocol lineage;
- `SAME_METHOD_LINEAGE` — same analytical/numerical method or constitutive/contact formulation;
- `CORROBORATING_ONLY` — independently supports definition/order/range but not transferable as the target value;
- `PRIOR_OR_BOUND_ONLY` — usable only as initial guess/prior/bound;
- `CONFLICTING_SOURCE` — credible but inconsistent with target-paper evidence;
- `NONTRANSFERABLE` — superficially related but physically incompatible.

## Parameter/theory transferability gate

A related-group value or formula may become target-model evidence only after checking:

1. parameter definition and physical meaning;
2. units and nondimensionalization;
3. governing model/formulation;
4. geometry, topology, DOF location and component identity;
5. material/contact/interface semantics;
6. operating condition, preload, speed, amplitude, temperature and frequency regime as relevant;
7. experiment/postprocessing conventions;
8. explicit statements of inheritance or reuse;
9. consistency with the target paper and citation lineage.

Decisions:

- `FIXED_LITERATURE_VALUE` — transferable, may become L;
- `DERIVED_FROM_SOURCE` — source relation is transferable but case value must be computed;
- `PRIOR_OR_BOUND_ONLY` — useful for H/C bounds only;
- `VALIDATION_ONLY` — useful as an independent or corroborating check but not a target parameter;
- `REJECTED_NONTRANSFERABLE` — do not use.

## Cross-validation logic

For each claim-critical formula/parameter:

- record the target-paper statement/value or missing status;
- list all same-author/group sources found;
- compare definitions, values and operating cases;
- determine whether sources converge, refine, conflict or are non-transferable;
- preserve disagreements explicitly;
- never choose the value that best fits the target figure merely because it improves reproduction.

Confidence increases when multiple independent same-group sources converge **and** transferability is strong. Repetition of the same inherited number across derivative papers is not independent evidence; mark source dependence.

## Conflict handling

If credible same-group sources disagree, do not average them automatically. Register the conflict and route it through `references/evidence_conflict.md`.

Possible outcomes include:

- paper-faithful variant;
- source-lineage variant;
- case-dependent values;
- uncertainty distribution/range;
- unresolved blocking conflict.

## Search closure

`AUTHOR_GROUP_CROSS_EVIDENCE_CLOSED` requires, for every claim-critical item:

- at least one mapped related source, or
- an explicit `NO_RELEVANT_GROUP_SOURCE_FOUND` result with search scope/terms and date recorded.

Only after this closure may the workflow promote a missing item to `ASSUMED`, `INVERSE_IDENTIFIED`, or `UNRESOLVED`.

## Reporting

The final report must state which formulas/parameters were:

- confirmed by same-author/group literature;
- recovered from same-author/group literature;
- only bounded by same-group literature;
- contradicted by same-group literature;
- unsupported after a documented group-literature search.
