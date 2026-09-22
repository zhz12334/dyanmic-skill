# Theory & Parameter Provenance Policy — v3.3

## Purpose

Every claim-relevant formula, theoretical relation, parameter, assumption and numerical setting must retain an explicit provenance trail from discovery through implementation to the final reproduction report.

The final report must make it possible for a reviewer to answer, without opening the source code:

1. Which equations/theoretical relations came directly from the target paper?
2. Which were uniquely derived from the target paper?
3. Which were recovered from references cited by the target paper?
4. Which required upstream citation-lineage tracing, related theses/papers, or external authoritative sources?
5. Which values are only transferred priors/bounds from analogous literature?
6. Which quantities were assumed by the reproduction team?
7. Which quantities were inverse-identified from target-paper outputs?
8. Which settings were selected only by numerical verification/convergence?
9. Which critical items remain unresolved?

## Unified provenance source classes

Use one of the following source classes for every claim-relevant theory/formula/parameter item:

- `PAPER_DIRECT` — explicitly stated in the target paper or its non-code supplement.
- `PAPER_DERIVED` — uniquely derivable from target-paper equations/data without fitting target outputs.
- `CITED_REFERENCE_DIRECT` — explicitly provided by a reference cited by the target paper for the same model role.
- `CITATION_LINEAGE_DERIVED` — recovered by following the cited source upstream and deriving/transforming the value or relation with documented steps.
- `RELATED_THESIS_OR_PAPER` — recovered from a related thesis, prior/later paper, or model-family publication and shown transferable.
- `AUTHORITATIVE_EXTERNAL_SOURCE` — standard, handbook, material database, solver manual, textbook, or other authoritative source used to fill theory/engineering data.
- `TRANSFERRED_PRIOR_OR_BOUND_ONLY` — analogous literature used only to define an initial value, prior, or admissible bound; not treated as target-paper truth.
- `REPRODUCTION_DERIVED` — derived by the reproduction team from already justified quantities/relations; derivation must be shown.
- `ASSUMED` — not recoverable from evidence; explicitly introduced as a reproduction hypothesis with rationale and affected claims.
- `INVERSE_IDENTIFIED` — estimated by fitting/calibrating to target-paper outputs under an approved M2 workflow; never reported as an author-supplied value.
- `NUMERICAL_VERIFICATION_SETTING` — mesh, time step, tolerance, quadrature, FFT length, modal truncation, etc. chosen by verification/convergence rather than fitting.
- `UNRESOLVED` — provenance/value/definition is not defensibly resolved.

For experimental or ML branches, measurement/calibration/database-derived values should still map to the closest class above and include an explicit evidence role in notes.

## Source class is not the same as parameter type

Parameter type (`P/T/L/H/C/N/R`) describes how the reproduction workflow treats a quantity. Provenance class describes where the information came from.

Examples:

- target paper gives `E = 210 GPa`: type `P`, source class `PAPER_DIRECT`.
- target paper gives geometry and density and mass is uniquely calculated: type `T`, source class `PAPER_DERIVED` or `REPRODUCTION_DERIVED` depending on where the derivation is stated.
- cited reference gives a transferable contact-law exponent: type `L`, source class `CITED_REFERENCE_DIRECT`.
- analogous paper gives damping range `[0.01,0.04]`: type `H` or candidate `C`, source class `TRANSFERRED_PRIOR_OR_BOUND_ONLY`.
- damping is fitted to Figure 6: type `C`, source class `INVERSE_IDENTIFIED`.
- time step is selected by convergence: type `N`, source class `NUMERICAL_VERIFICATION_SETTING`.

## Theory/formula provenance requirements

For every critical theory/formula item record:

- theory/formula ID and linked equation ID when applicable;
- faithful expression or relation;
- role in the model;
- target-paper location/context;
- source class;
- exact source citation and source location (page/equation/table/section when available);
- derivation/translation/transfer step, if any;
- affected claims;
- implementation status and model variant;
- confidence/status and unresolved ambiguity.

A formula copied from external theory without disclosure is a provenance failure even if mathematically correct.

## Same-author / same-group cross-evidence requirement

Before final provenance closure, every claim-critical formula/theory/parameter must be checked against the mapped publication family of the target authors/research group when relevant sources exist. Record corroboration, inheritance, conflicts and non-transferability in `author_group_literature_map.csv` and `cross_parameter_validation.csv`. This cross-evidence is part of provenance, not optional background reading.

## Parameter provenance requirements

For every claim-relevant parameter record:

- parameter ID/symbol/description;
- final value (or distribution/range) and unit;
- workflow type (`P/T/L/H/C/N/R`);
- provenance source class;
- exact source citation/location or source-trace ID;
- initial/prior value and admissible bounds when applicable;
- whether optimization is allowed;
- calibration target/objective/method if inverse-identified;
- identifiability class and uncertainty/confidence interval where applicable;
- affected claims;
- final status.

For every `INVERSE_IDENTIFIED` parameter the final report must explicitly state:

> This value is an equivalent parameter identified by this reproduction from published target outputs; it is not a parameter value disclosed by the target-paper authors.

## Assumptions

Every `ASSUMED` item must appear in the Assumption Register and final report with:

- why the item was required;
- what searches failed to recover it;
- chosen value/relation;
- physical rationale/bounds;
- sensitivity/robustness treatment;
- affected claims;
- closure status (`CLOSED_BY_SOURCE`, `CALIBRATED_EQUIVALENT`, `ACCEPTED_UNCERTAINTY`, `NON_IDENTIFIABLE`, `BLOCKING`).

## Final-report provenance summary

The final report must include, near the beginning, a provenance executive summary containing at least:

- count of critical theory/formula items by source class;
- count of critical parameters by source class;
- count of `ASSUMED`, `INVERSE_IDENTIFIED`, `NUMERICAL_VERIFICATION_SETTING`, and `UNRESOLVED` items;
- M1/M2 mode and any M1->M2 transition caused by inverse identification;
- unresolved provenance items that limit claims.

It must then contain four mandatory detailed tables:

1. **Theory/Formula Provenance Matrix**.
2. **Parameter Provenance Matrix**.
3. **Assumption and Inverse-Identification Matrix**.
4. **Unresolved Provenance Items**.

Do not hide provenance only in appendices or CSV files. The final human-readable report itself must summarize it.

## Provenance freeze and run binding

Before an evidence-producing final run:

- freeze the theory/formula provenance register;
- freeze the parameter provenance summary;
- freeze assumptions and inverse-identification records;
- hash the frozen provenance snapshot;
- bind the snapshot hash into `run_manifest.yaml`.

If a parameter source, formula source, assumption, or inverse-identification status changes, invalidate affected evidence runs and rerun the relevant gates.

## Hard gate

A final `GO` is forbidden if any claim-critical formula or parameter lacks one of:

- a defensible provenance class and source/derivation record;
- an explicit `ASSUMED` treatment;
- an explicit `INVERSE_IDENTIFIED` treatment under M2;
- an explicit `UNRESOLVED`/blocking declaration.

Unknown provenance may be reported; it may not be silently converted into certainty.
