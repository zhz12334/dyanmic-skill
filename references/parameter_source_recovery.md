# Parameter Source Recovery and Citation-Lineage Strategy

## Purpose

Recover missing or ambiguous reproduction parameters from the paper's evidence ecosystem before introducing assumptions or inverse identification. This process is mandatory for nontrivial missing physical/model parameters.

This skill assumes no usable author source code. Parameter recovery therefore relies on literature/data provenance rather than hidden implementation artifacts.

## Recovery ladder

### R0 — Target paper whole-paper / cross-chapter closure
Search the entire paper before declaring the item missing: current section, earlier/later chapters, captions, appendices, supplementary material, notation/symbol lists, table notes, case definitions, validation/experiment chapters, summaries, errata, and exact surrounding text. Link reused/overridden/contradictory definitions through `cross_chapter_evidence_links.csv`.

Set `cross_chapter_search_complete=true` only after this scan. `missing in the local chapter` is not sufficient for H/C promotion.

### R1 — Citation-context tracing
For the missing item, identify citations attached to its equation, definition, constitutive law, damping model, boundary condition, material property, load, numerical scheme, or experimental protocol. Search those references specifically for the missing quantity and its definition.

### R2 — Upstream lineage
If R1 says a value/model was adopted from an earlier work, follow the chain. Record each hop. Stop when:
- the original/authoritative definition is found;
- the chain becomes physically non-transferable;
- no further source is accessible;
- additional hops no longer improve provenance.

Never copy a number across a citation chain without checking its meaning at each hop.

### R3 — Mandatory author/model-family literature cross-evidence
Search the authors' theses/dissertations, prior/later papers, conference versions, technical reports, institutional repositories, and same-group papers using the same apparatus/model. This step is mandatory for every claim-critical missing/ambiguous theory item or parameter, not merely a fallback.

Create/update `author_group_literature_map.csv` and `cross_parameter_validation.csv` following `references/author_group_cross_evidence.md`. Use these related publications to triangulate definitions, values, operating conditions and inheritance links. A same-group value is not automatically transferable; apply the transferability gate and register conflicts explicitly.

### R4 — Supplementary non-code data and parameter records
Inspect released data tables, parameter spreadsheets, input datasets, case tables, metadata, appendices and data dictionaries when available. Distinguish explicit target-case values from generic/default reference values.

### R5 — Authoritative generic sources
For generic quantities, consult standards, handbooks, material databases, and official solver/manual documentation. These can supply values or defensible ranges when the parameter is not target-paper-specific.

### R6 — Analogous literature
Use similar models only to form an initial guess, prior distribution, lower/upper bound, order-of-magnitude check, or sensitivity range unless the transferability gate is passed.

### R7 — Hypothesis / inverse identification
If the item remains unresolved:
1. register H with explicit basis and uncertainty;
2. assess sensitivity and physical identifiability;
3. determine whether using target-paper outputs for identification changes mode M1 -> M2;
4. promote H -> C only if justified;
5. calibrate within literature/physics-informed bounds;
6. report the result as an identified/equivalent reproduction parameter, not an author parameter.

## Literature Transferability Gate

Score each candidate source against:

1. **Definition equivalence** — same physical quantity and semantics.
2. **Unit/nondimensional equivalence** — same scale or transparent conversion.
3. **Model-form equivalence** — same governing law or compatible reduction.
4. **Topology/DOF equivalence** — same structural role/location.
5. **Material/interface equivalence** — same constitutive/contact/joint meaning.
6. **Operating-condition equivalence** — compatible preload, speed, amplitude, frequency, temperature, etc., where relevant.
7. **Experiment/postprocess equivalence** — same measured/derived quantity and processing definition.
8. **Target-paper consistency** — no contradiction with explicit target-paper evidence or resolved source lineage.

Decision:
- strong equivalence -> `FIXED_LITERATURE_VALUE` (type L);
- relationship known but case value must be calculated -> `DERIVED_FROM_SOURCE` (L/T as appropriate);
- partial equivalence -> `PRIOR_OR_BOUND_ONLY`;
- coding/formulation insight only -> `IMPLEMENTATION_CLUE_ONLY`;
- incompatible -> `REJECTED_NONTRANSFERABLE`.

## Evidence confidence

Suggested confidence labels:
- `A`: target supplement/data record or direct cited source explicitly specifying the case;
- `B`: same author/model family with strong transferability;
- `C`: authoritative generic source with compatible conditions;
- `D`: analogous source usable only as prior/bound;
- `E`: provisional hypothesis.

Confidence is not a substitute for transferability; record both.

## Evidence conflict rule

If credible sources disagree, create an entry in `evidence_conflict_register.csv` and follow `references/evidence_conflict.md`. Do not silently select the value that best fits the paper output.

## Recursive search discipline

Citation tracing should be targeted, not unbounded literature review. Search only branches that can plausibly resolve a defined missing item. Maintain a trace table and stop when the source is recovered, the branch becomes non-transferable, or further tracing is unlikely to change the modeling decision.

## Reporting language

Use:
- "Recovered from Ref. X and adopted as L after transferability checks."
- "Ref. X provides only a plausible range; used as a bound for C, not as the paper's value."
- "No transferable source value was found; the parameter was identified from calibration targets and is an equivalent reproduction parameter."


## Reference-closure status

For every claim-critical unresolved item record one status:
- `CLOSED_IN_TARGET_PAPER`;
- `CLOSED_BY_DIRECT_REFERENCE`;
- `CLOSED_BY_UPSTREAM_LINEAGE`;
- `CLOSED_BY_AUTHOR_FAMILY`;
- `CLOSED_BY_AUTHORITATIVE_GENERIC_SOURCE`;
- `PRIOR_BOUND_ONLY`;
- `UNRESOLVED`.

`REFERENCE_CLOSED` means the required search path has been completed, not that every value has been recovered. An item can remain `UNRESOLVED` and still have a closed search path; it must then remain explicit H/blocking or become C only under M2 eligibility rules.
