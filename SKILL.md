---
name: structural-dynamics-paper-reproduction
description: Reproduce long, multi-chapter structural-dynamics papers without relying on author source code, using whole-paper and cross-chapter evidence scanning, citation-lineage closure, claim/equation/model dependency mapping, immutable paper ground truth, model-based figure batching, equation and model/solver fidelity gates, explicit assumptions, Python-first verification, bounded engineering reconstruction when necessary, builder/validator separation, calibration/validation leakage control, stop-tuning evidence review, VVUQ, MATLAB parity, run provenance, and clean-room reruns.
---

# Structural Dynamics Paper Reproduction Skill v4.0.0-rc5

## 1. Purpose

Use this skill to reproduce, verify, independently reimplement, calibrate when necessary, audit, and extend structural-dynamics papers involving analytical models, numerical simulation, finite elements, experimental/operational modal analysis, nonlinear dynamics, random vibration, model updating, structural health monitoring, and related inverse problems.

This skill assumes **no usable author source code is available**. Reproduction must therefore be grounded in the paper, supplements/non-code data when available, cited theory, related papers/theses, standards/manuals, and eligible third-party open-source method/similar-system implementations.

The governing principle is:

**scan the whole paper before declaring information missing; recover cross-chapter evidence and trace references before identifying parameters; implement and freeze upstream paper mathematics/model modules before fitting downstream figures; reproduce in model-dependency batches rather than figure-number order; freeze paper ground truth before scoring; obtain plan approval before full implementation; separate builder and validator roles; stop tuning and return to evidence when residuals indicate model/evidence incompleteness; separate calibration from genuinely withheld validation; track validation exposure; bind every result to exact code/data/config/environment evidence; present formal validation with both source/reproduction views and typed quantitative evidence; and distinguish independent reproduction from engineering reconstruction.**

Default high-level chain:

**mode lock -> whole-paper/cross-chapter evidence scan -> claim graph -> paper evidence -> preliminary target characterization -> equation/theory/citation closure -> mandatory same-author/same-group literature cross-evidence -> evidence-conflict handling -> model-structure freeze -> physics/model dependency DAG -> figure dependency/anchor map -> parameter provenance -> reference/provenance closure -> cross-parameter consistency validation -> pre-implementation reproducibility-probability report -> implementation contract -> model-based batch plan -> plan approval -> third-party reuse audit -> computational/experimental/ML branch -> formula fidelity + model/solver fidelity -> Python verification -> formal target extraction + immutable ground-truth freeze -> batch baseline -> discrepancy budget -> M1/M2 mode check -> bounded calibration if justified -> identifiability/UQ -> builder freeze -> independent validation with exposure control -> validation-packet completion -> discrepancy repair or STOP_TUNING/EVIDENCE_REVIEW -> robustness/VVUQ + regression -> MATLAB parity -> artifact freeze -> clean-room rerun -> claim-level verdict.**

---

## 2. Non-negotiable principles

1. **Use only M1 or M2 reproduction mode.** Author-source-code rerun/porting workflows are intentionally out of scope.
2. **Reproduce claims, not only figures.** Every critical scientific claim must have a testable evidence path.
3. **Read and research before modeling.** Do not code before the physical problem, novelty, equations, assumptions, targets and protocol are understood.
4. **Trace sources before assuming or calibrating.** Missing parameters/theory must first be sought through the paper, supplements, citation lineage, related papers/theses, authoritative sources and transferable literature.
5. **No silent assumptions.** Every assumption must be registered, bounded where possible and linked to affected claims.
6. **Provenance must survive into the final report.** Every claim-relevant formula/theory/parameter must retain a source class and exact source/derivation record through implementation, optimization, final reporting and evidence-run hashing.
7. **Formula fidelity precedes result fidelity.** Critical claim-relevant equations/algorithms require 100% direct or proven-equivalent implementation coverage and runtime connectivity.
8. **Model/solver fidelity is independent of formula fidelity.** Geometry, DOFs, element theory, mass formulation, BCs, loads, contact, solver semantics, output coordinates and hidden defaults must also be traced and verified.
9. **No silent omission, simplification, correction or invention.** Suspected paper errors require explicit variants; do not quietly “improve” the paper model.
10. **Freeze model structure before calibration.** Optimization may not compensate for unresolved model-form, unit, sign, BC/IC, contact, damping, solver or post-processing errors.
11. **Resolve evidence conflicts explicitly.** Contradictory sources require a conflict register/variant/uncertainty decision, not silent cherry-picking.
12. **Maintain a persistent Implementation Contract.** Every repair must preserve or explicitly reopen paper/model obligations.
13. **Plan approval is a hard gate.** By default, present the reproduction plan and wait for user approval before full implementation. Continuous execution is allowed only when explicitly preapproved.
14. **Reuse before reinventing, but with provenance.** Search method/reference implementations and similar-system models after the plan is defined. Reuse does not transfer their hidden parameters to the target paper.
15. **Python first.** Python is the authoritative transparent verification implementation unless a solver-specific workflow requires another engine; even then, use Python checks where feasible.
16. **Experimental papers require an experimental branch.** Instrumentation, acquisition and signal-processing protocol are first-class evidence.
17. **ML/SHM papers require a leakage-aware data branch.** Dataset split, preprocessing, normalization, windowing and model selection must be reproduced without train/test contamination.
18. **Extract published evidence quantitatively.** Prefer exact data; digitize figures only when necessary and propagate extraction uncertainty.
19. **Compare physics, not pixels.** Use result-type-specific metrics. Image similarity is supplemental only.
20. **Numerical settings are not fitting knobs.** Mesh/time-step/tolerance/FFT/modal truncation are selected by verification/convergence.
21. **M1 and M2 must not be conflated.** If the reproduction team must infer a claim-critical omitted physical parameter from target-paper outputs, transition M1 -> M2 before calibration, unless that identification procedure is itself explicitly part of the paper method.
22. **Bounded inverse identification is allowed only for eligible missing physical parameters.** Results remain identified/equivalent parameters unless independently sourced.
23. **Separate calibration and validation.** Hold out physically meaningful evidence whenever possible.
24. **Track validation exposure.** Once a validation target influences model development, it is no longer independent validation.
25. **Treat stochastic and chaotic systems correctly.** Use ensemble/statistical/invariant comparisons rather than meaningless long-time pointwise equality.
26. **Check identifiability and uncertainty.** High curve similarity does not prove unique physical parameters.
27. **Represent model discrepancy explicitly.** Do not force every residual into adjustable parameters.
28. **Discrepancy drives the next plan.** Material scientific changes require a ranked-cause repair plan and approval unless continuous execution was preapproved.
29. **Preserve regression evidence.** A new fit is not accepted if it breaks previously passed theory, formula, model/solver, numerical or validation checks.
30. **Bind evidence runs to provenance.** Code, data, configuration, environment, commands, seeds and outputs must be version-pinned/hash-addressed.
31. **Clean-room rerun is the final reproducibility gate.** Development-machine success alone is insufficient.
32. **MATLAB follows accepted Python.** MATLAB is a parity implementation, not a fresh reinterpretation.
33. **Final verdicts are claim-level and multi-dimensional.** Reproduction quality, parameter-identification quality and artifact reproducibility must remain separate.
34. **Scan the whole target paper before declaring information missing.** Later chapters, appendices, captions, symbol lists and validation sections may close an apparent gap in an earlier chapter.
35. **Close citation lineage before parameter identification.** A quantity omitted from the local text is not a missing parameter if the paper explicitly delegates it to a cited source or recoverable upstream reference.
35A. **Same-author / same-group literature cross-evidence is mandatory.** Before a claim-critical theory item or parameter is declared unrecoverable, search the target authors' own related papers, theses/dissertations, conference versions, technical reports, and same-laboratory/model-family publications. Use these sources to recover, triangulate, and cross-validate definitions, parameter values, operating conditions and protocol details; never transfer a value without model/condition equivalence checks.
35B. **Report a pre-implementation reproducibility probability after evidence closure.** After the theory/formula/model/parameter provenance set is closed enough for planning, compute and present an evidence-based estimated reproducibility probability with a plausible range, dominant strengths, dominant risks, and hard caps/blocks. This is an engineering forecast, not an empirically calibrated statistical guarantee, and it must be shown to the user before the Implementation Contract/full implementation plan is frozen.
36. **Evidence-reading order and reproduction-execution order are different.** Read the whole paper first; execute reproduction according to the physics/model dependency DAG.
37. **Upstream modules gate downstream fitting.** Do not use a downstream response figure to compensate for an unresolved upstream contact, stiffness, excitation, constitutive or subsystem model.
38. **Plan figure work in model-based batches.** Group results by shared physics, parameter set and operating condition rather than by consecutive figure numbers.
39. **Frozen paper ground truth is immutable.** Raw authoritative target data cannot be overwritten by smoothing, interpolation, surrogate/ROM outputs or later tuning; target corrections require a new version and invalidate affected prior scores.
40. **Separate Builder and Validator responsibilities.** The Builder may repair the model but may not alter frozen target definitions or acceptance rules after seeing validation residuals; the Validator may score/fresh-run but may not tune the model.
41. **Stop tuning when the evidence says to stop.** Persistent structural residuals, negligible progress, parameter boundary pressure, or regression damage trigger `STOP_TUNING -> EVIDENCE_REVIEW` instead of continued curve fitting.
42. **Track the true origin of validation evidence.** A target printed in the paper may originate from a cited external experiment/dataset; mark borrowed validation evidence explicitly and close that source before treating it as authoritative.
43. **A validation target may live in a later chapter than the module it validates.** Later-chapter healthy/scalar evidence may back-validate an upstream module without importing the later chapter's new fault/excitation mechanism.
44. **Freeze comparison conventions per target.** Coordinate transforms, roller numbering, sign conventions, sensor direction and normalization used only for a comparison are part of the target protocol, not cosmetic plotting choices.
45. **Validation claim type determines the metric family.** A paper claiming frequency/sideband/mechanism agreement must not be silently upgraded to exact waveform-amplitude validation or scored by a default NRMSE objective.
46. **Formal validation uses dual evidence.** Every formal target must combine frozen paper/source ground truth, fresh-run reproduction, a direct comparison view when meaningful, result-type-specific quantitative/feature metrics and an explicit verdict; visual similarity alone or one scalar metric alone cannot establish PASS.

---

## 3. Supported problem classes

- SDOF/MDOF vibration systems
- eigenvalue/modal analysis and mode correlation
- free/forced vibration, FRF and harmonic response
- direct/modal transient dynamics
- base excitation, seismic response and response spectra
- random vibration, PSD/ASD and stochastic processes
- beams, plates, shells, frames, solids, joints and reduced-order models
- finite-element structural dynamics
- linear/nonlinear dynamics, backlash/contact/friction/hysteresis
- periodic, quasi-periodic, bifurcation and chaotic dynamics
- experimental modal analysis (EMA)
- operational modal analysis (OMA)
- modal parameter estimation and correlation
- model updating and inverse identification
- structural health monitoring and damage identification
- vibration signal processing when integral to the paper
- ML/data-driven methods when part of a structural-dynamics or SHM claim

Typical environments may include Python/NumPy/SciPy, MATLAB, Abaqus, ANSYS/APDL, Nastran, OpenSees, COMSOL, Simcenter, or equivalent tools.

---

## 4. Reproduction modes

See `references/reproduction_modes.md`.

### M1 — Independent reimplementation

Reproduce from paper/theory/recoverable non-code evidence and eligible third-party references. M1 does **not** use target-paper outputs to infer omitted claim-critical physical parameters, except when reproducing an identification procedure explicitly described by the paper itself.

Question: **can an independent implementation reproduce the critical claims from disclosed/recoverable scientific information?**

### M2 — Engineering reconstruction / calibrated reproduction

Use explicit assumptions, transferable priors/bounds and bounded inverse identification where necessary to reconstruct missing claim-critical physical parameters from published evidence.

Question: **can a defensible, traceable engineering model reproduce and predict the reported behavior under documented reconstruction assumptions?**

### Mandatory M1 -> M2 transition

If the reproduction team must fit a claim-critical omitted physical parameter to target-paper outputs, transition to M2 **before** that calibration. Record affected parameters/claims/targets and the transition reason.

---

## 5. Workflow states

Use these states:

- `MODE_LOCKED`
- `WHOLE_PAPER_SCANNED`
- `CLAIMS_MAPPED`
- `TARGETS_CHARACTERIZED`
- `RESEARCHING`
- `THEORY_OPEN`
- `REFERENCE_CLOSURE_OPEN`
- `REFERENCE_CLOSED`
- `AUTHOR_GROUP_CROSS_EVIDENCE_CLOSED`
- `REPRODUCIBILITY_PROBABILITY_ASSESSED`
- `REPRODUCIBILITY_PROBABILITY_REPORTED`
- `FORMULAS_REGISTERED`
- `MODEL_STRUCTURE_OPEN`
- `MODEL_STRUCTURE_FROZEN`
- `MODEL_DEPENDENCY_OPEN`
- `MODEL_DEPENDENCY_FROZEN`
- `FIGURE_DEPENDENCY_FROZEN`
- `PARAMETERS_OPEN`
- `IMPLEMENTATION_CONTRACT_FROZEN`
- `BATCH_PLAN_FROZEN`
- `PLAN_AWAITING_APPROVAL`
- `PLAN_APPROVED`
- `PREAPPROVED_CONTINUOUS_EXECUTION`
- `REUSE_AUDITED`
- `FORMULA_FIDELITY_VERIFIED`
- `MODEL_IMPLEMENTATION_FIDELITY_VERIFIED`
- `PYTHON_VERIFIED`
- `GROUND_TRUTH_FROZEN`
- `CALIBRATING`
- `BUILDER_FROZEN`
- `VALIDATOR_RUNNING`
- `VALIDATION_PACKET_COMPLETE`
- `VALIDATING`
- `ITERATING`
- `STOP_TUNING`
- `EVIDENCE_REVIEW`
- `REPAIR_PLAN_AWAITING_APPROVAL`
- `REPAIR_PLAN_APPROVED`
- `BATCH_ACCEPTED`
- `PYTHON_ACCEPTED`
- `MATLAB_PARITY`
- `ARTIFACT_FROZEN`
- `CLEAN_ROOM_VERIFIED`
- `GO`
- `NO-GO`

---

# 6. Mandatory workflow

## Phase 0 — Define intent, evidence availability, mode, targets and deliverables

Record paper identity/version/DOI, supplements, desired figures/tables/conclusions, target fidelity and deliverables.

Create `artifact_availability_matrix.csv` using `references/artifact_availability.md` for paper/supplement/data/related theses/papers/cited sources/method code/similar code/solver examples/standards/benchmarks.

Lock M1 or M2. Default to M1 unless the task already clearly requires reconstruction/calibration of omitted parameters.

Define a validation ladder:
1. analytical/textbook checkpoint;
2. minimal model checkpoint;
3. baseline structural result;
4. primary paper target;
5. withheld validation target(s);
6. optional extension/prediction.

### Gate G0
No implementation before evidence scope, mode and target hierarchy are defined.

---

## Phase 0A — Whole-paper and cross-chapter evidence scan

Use `references/whole_paper_evidence_scan.md`. Before declaring any claim-critical quantity missing, scan the complete target paper, including later chapters, validation/experiment chapters, appendices, captions, table notes, symbol lists, summaries and cross-references.

Create/update:
- `chapter_registry.csv`;
- `cross_chapter_evidence_links.csv`;
- `reference_use_registry.csv`.

Record where equations/parameters/conditions are introduced, reused, inherited, redefined or contradicted across chapters. Separate:
- **evidence-reading order** — whole-paper first; from
- **reproduction-execution order** — determined later by the physics/model dependency DAG.

### Gate G0A — Whole-paper scan
Mark `WHOLE_PAPER_SCANNED` before an item may be labeled `missing`, `assumed`, `calibratable`, or `unresolved from the target paper`.

---

## Phase 1 — Build the Claim–Evidence–Artifact Graph

Use `references/claim_evidence_artifact_graph.md`.

For each critical claim record:
- claim ID and faithful statement;
- claim type;
- paper location and chapter ID;
- model-module ID(s) and result-group ID(s);
- equations/assumptions;
- required parameters/inputs;
- supporting figures/tables/data;
- required implementation modules;
- metric;
- tolerance;
- **tolerance basis/source/uncertainty**;
- calibration/validation role;
- status `OPEN/PASS/PARTIAL/FAIL/BLOCKED`.

Create `claim_registry.csv` and `claim_evidence_links.csv`.

### Gate G1
Do not declare reproduction based only on visually similar plots.

---

## Phase 2 — Build the Paper Evidence Matrix

Create `paper_evidence_matrix.csv` and extract only what the target paper/supplement explicitly supports:
- physical system/novelty;
- equations, notation and units;
- geometry/DOFs/coordinates;
- material/constitutive data;
- joints/contact/interfaces;
- BCs/supports;
- loads/base excitation;
- damping;
- initial conditions;
- nonlinearities;
- discretization/reduction;
- numerical solver/integration/eigensolver;
- experimental setup/signal processing;
- target definitions/postprocessing;
- uncertainty/rounding.

Classify each item as paper-stated, supplement-stated, externally sourced, inferred, assumed or inverse-identified. Link duplicate/reused items to `cross_chapter_evidence_links.csv` rather than treating each chapter as an isolated source. Do not silently “correct” or complete the paper at this phase.

### Gate G2
No model construction until the physical problem and target outputs can be explained coherently from source evidence.

---

## Phase 2A — Preliminary target characterization

Before freezing metrics/tolerances, create `target_characterization.csv`.

For every target estimate:
- exact/table/vector/raster/manual data availability;
- axes/coordinates/units/log scale;
- digitizability;
- expected extraction uncertainty;
- whether points are strongly correlated;
- candidate calibration/validation role;
- candidate metric;
- defensible tolerance basis.

This is **not** the final extraction. It exists so the plan is based on realistic target quality.

### Gate G2A
Mark `TARGETS_CHARACTERIZED` before finalizing tolerance and calibration/validation strategy.

---

## Phase 3 — Theory dependency map, citation lineage and missing-knowledge closure

Create `theory_research_log.csv`. After the Phase 0A whole-paper scan, resolve remaining theory/parameter gaps in this order:
1. exact local equation/statement/citation context;
2. direct cited source;
3. upstream source lineage;
4. **mandatory same-author / same-group cross-evidence sweep**: related theses/dissertations, prior/later papers, conference versions, technical reports, and same-laboratory/model-family publications;
5. supplementary non-code data/parameter records;
6. standards/manuals/handbooks/databases;
7. authoritative analogous literature for priors/bounds only unless transferability passes.

For each claim-critical gap maintain `reference_closure_status` as one of:
`CLOSED_IN_TARGET_PAPER`, `CLOSED_BY_DIRECT_REFERENCE`, `CLOSED_BY_UPSTREAM_LINEAGE`, `CLOSED_BY_AUTHOR_FAMILY`, `CLOSED_BY_AUTHORITATIVE_GENERIC_SOURCE`, `PRIOR_BOUND_ONLY`, or `UNRESOLVED`.

Audit dimensional consistency, sign convention, derivative order, coordinate mapping, nondimensionalization, damping definition, force vs base excitation, and OCR/printing errors.

Use `references/parameter_source_recovery.md` for parameter tracing.
Use `references/author_group_cross_evidence.md` and create `author_group_literature_map.csv` plus `cross_parameter_validation.csv`. For every claim-critical parameter/theory item, record whether same-author/group evidence confirms, refines, conflicts with, or is non-transferable to the target case.

If credible sources conflict, create `evidence_conflict_register.csv` and follow `references/evidence_conflict.md`. No silent source preference is allowed.

### Author clarification branch
If a high-impact ambiguity materially blocks a claim, an author clarification request may be logged. Lack of reply is unresolved evidence, not permission to invent a value.

### Gate G3
All critical theory must be sufficiently understood to implement/test, or explicitly marked blocking. Set `REFERENCE_CLOSURE_OPEN` while citation branches remain unresolved.

---

## Phase 3B — Mandatory same-author / same-group literature cross-evidence

Use `references/author_group_cross_evidence.md`. This is mandatory even when the target paper appears self-contained.

Search and map:
- first/corresponding/coauthors' prior and later publications on the same model/system/method;
- theses/dissertations from the authors or the same laboratory when relevant;
- same-group conference/journal versions and technical reports;
- same apparatus, specimen, solver deck, parameter table, constitutive/contact law, or model-family publications;
- later papers from the same group that explicitly inherit or restate the target model.

Create/update:
- `author_group_literature_map.csv`;
- `cross_parameter_validation.csv`;
- `theory_research_log.csv`;
- `evidence_conflict_register.csv` when cross-source disagreements exist.

For each recovered value/relation classify the cross-evidence role as one of:
`SAME_MODEL_DIRECT`, `SAME_SYSTEM_SAME_GROUP`, `SAME_EXPERIMENTAL_RIG`, `SAME_METHOD_LINEAGE`, `CORROBORATING_ONLY`, `PRIOR_OR_BOUND_ONLY`, `CONFLICTING_SOURCE`, or `NONTRANSFERABLE`.

A same-group value is **not** automatically a target-paper value. Transfer only after checking definition, units/nondimensionalization, model form, geometry/DOF role, material/interface meaning, operating conditions, experiment/postprocessing conventions, and explicit inheritance links.

### Gate G3B — Author/group cross-evidence closure
Mark `AUTHOR_GROUP_CROSS_EVIDENCE_CLOSED` only when every claim-critical formula/parameter has either:
1. a completed same-author/group search with mapped evidence; or
2. an explicit `NO_RELEVANT_GROUP_SOURCE_FOUND` result with search terms/scope recorded.

This gate must close before a claim-critical item can be promoted to `ASSUMED`, `INVERSE_IDENTIFIED`, or `UNRESOLVED`.

---

## Phase 3A — Equation/Algorithm Registry and dependency graph

Use `references/formula_fidelity.md`.

Create `equation_registry.csv` and `equation_dependency_graph.csv` for every numbered equation and every claim-relevant unnumbered mathematical/algorithmic rule.

Record:
- source location;
- provenance source class and exact source citation/location;
- faithful expression/description;
- role (`GOVERNING`, `KINEMATIC`, `CONSTITUTIVE`, `BOUNDARY`, `INITIAL_CONDITION`, `EXCITATION`, `DAMPING`, `CONTACT_OR_NONLINEARITY`, `TRANSFORMATION`, `DISCRETIZATION`, `ALGORITHM_STEP`, `POSTPROCESSING`, `METRIC`, etc.);
- variables/units/sign convention;
- affected claims;
- implementation requirement;
- dependencies;
- active variant;
- ambiguity/blocking status.

Critical active equations require **100%** implementation or proven-equivalent coverage. A weighted score cannot compensate for one missing governing/BC/IC/excitation/damping/contact/active algorithm term.

If the published formula appears wrong/incomplete, preserve `PAPER_FAITHFUL` and separate corrected/source-lineage variants per `references/source_faithful_variants.md`.

### Gate G3F
Mark `FORMULAS_REGISTERED` only when no claim-relevant formula can disappear silently.

---

## Phase 4 — Reconstruct and freeze model structure

Create `model_structure_register.csv` and freeze, in order:
1. geometry/topology;
2. coordinate system/DOFs;
3. mass/inertia model;
4. constitutive/material law;
5. joints/contact/interfaces;
6. BC/supports;
7. excitation/load/base motion;
8. damping law;
9. initial/preload state;
10. nonlinear/restoring law;
11. observation/output coordinates;
12. discretization/reduction;
13. solver/postprocessing definition.

Unresolved evidence conflicts that materially alter governing physics must be represented as explicit variants, uncertainty, or blocking findings before freeze.

### Gate G4
`MODEL_STRUCTURE_FROZEN` requires remaining uncertainty to be defensibly parameter/measurement/numerical uncertainty rather than hidden model-form ambiguity.

---

## Phase 4A — Pre-register model/FE/solver/protocol obligations

Use `references/model_solver_fidelity.md` and create `model_implementation_registry.csv` **before coding**.

Register claim-relevant non-formula obligations: geometry, DOFs, elements, mesh role, mass formulation, materials/orientation, contact/joints, constraints, BCs, loads/base excitation, damping realization, preload, solver/integration semantics, convergence, reduction, output coordinates and solver defaults.

This registry complements the Equation Registry; it does not replace it.

---

## Phase 4B — Build and freeze the physics/model dependency DAG

Use `references/model_dependency_planning.md` and create `model_dependency_graph.csv`.

Represent claim-relevant modules such as geometry, material, kinematics, contact, constitutive law, excitation, nonlinear force, subsystem dynamics, system dynamics, solver and postprocessing. Record upstream/downstream dependencies, affected claims/figures, inputs/outputs, freeze criteria and current status.

### Gate G4B
Mark `MODEL_DEPENDENCY_FROZEN` only when the reproduction order is physically defensible. Downstream response fitting is prohibited while its upstream physical module is still open.

---

## Phase 4C — Build the figure/result dependency graph and classify anchors

Use `references/figure_batch_planning.md` and create `figure_dependency_graph.csv`. Classify each target/result group as `ANCHOR`, `SATELLITE`, `REGRESSION_ONLY`, `CALIBRATION_CANDIDATE`, and/or `VALIDATION_CANDIDATE` as appropriate.

Anchor selection must be based on observability, upstream sensitivity, directness, uncertainty and available analytical/scalar/frequency checkpoints — not a fixed number of figures.

### Gate G4C
Mark `FIGURE_DEPENDENCY_FROZEN` before formal batch planning. Satellite targets may not be tuned while the anchor evidence for the same upstream module is failing.

---

## Phase 5 — Parameter provenance and source recovery

Classify parameters using `references/parameter_taxonomy.md`:
- `P` paper-fixed;
- `T` theory-derived;
- `L` literature-completed;
- `C` calibratable missing physical parameter;
- `N` numerical setting;
- `R` random/nuisance realization;
- `H` explicit reproduction hypothesis.

For every non-P parameter create a Parameter Source Trace. Apply transferability checks before promoting literature values to L.

Use `references/theory_parameter_provenance.md` to assign a provenance source class to every claim-relevant parameter. Update `parameter_register.csv` with final value/range, source class, exact source/location, identification basis, identifiability and uncertainty.

Recovery hierarchy:

**target-paper whole-paper closure -> local citation -> cited source -> upstream lineage -> mandatory same-author/same-group model-family cross-evidence -> related thesis/dissertation/papers/technical reports -> supplementary non-code data -> authoritative standards/manuals -> analogous literature for prior/bounds -> H -> possible H->C only after reference closure + sensitivity/identifiability check.**

Type N values are selected through numerical verification, not curve fitting.

If target-paper outputs will be used by the reproduction team to identify a claim-critical omitted physical parameter, transition M1 -> M2 before calibration.

### Gate G5
Every active value must have type, provenance, units, role, optimization permission, `cross_chapter_search_complete`, `author_group_cross_evidence_status`, and `reference_closure_status`. No C parameter may be approved while a plausible target-paper, citation-lineage, or same-author/same-group evidence branch remains unsearched.

---

## Phase 5A — Theory & Parameter Provenance Closure

Use `references/theory_parameter_provenance.md` and create/update:
- `theory_formula_provenance.csv`;
- `parameter_provenance_summary.csv`;
- `provenance_source_summary.csv`;
- `inverse_parameter_summary.csv` when applicable;
- `unresolved_provenance_items.csv`.

For every critical formula/theoretical relation and parameter, make the final source status explicit using one of:
`PAPER_DIRECT`, `PAPER_DERIVED`, `CITED_REFERENCE_DIRECT`, `CITATION_LINEAGE_DERIVED`, `RELATED_THESIS_OR_PAPER`, `AUTHORITATIVE_EXTERNAL_SOURCE`, `TRANSFERRED_PRIOR_OR_BOUND_ONLY`, `REPRODUCTION_DERIVED`, `ASSUMED`, `INVERSE_IDENTIFIED`, `NUMERICAL_VERIFICATION_SETTING`, or `UNRESOLVED` as applicable.

Rules:
- a value found in analogous literature is not a target-paper value unless transferability is established;
- an inverse-identified value is never described as an author-disclosed value;
- a reproduction-team derivation must show its derivation chain;
- unresolved items must remain visibly unresolved/blocking rather than becoming silent defaults;
- every assumption and C parameter must link back to source-recovery failure and affected claims.

### Gate G5P — Provenance closure
Before freezing the Implementation Contract, every claim-critical formula/theory/parameter must have either:
1. a defensible source class + exact source/derivation record; or
2. explicit `ASSUMED`; or
3. explicit `INVERSE_IDENTIFIED` eligibility under M2; or
4. explicit `UNRESOLVED`/blocking status.

No hidden-origin value may enter the production model.

### Gate G5R — Reference closure
Mark `REFERENCE_CLOSED` when every claim-critical gap has completed the required whole-paper, citation-lineage, and same-author/same-group search path, even if some items remain explicitly `UNRESOLVED`. `REFERENCE_CLOSED` means the search process is closed; it does **not** mean every quantity has been recovered.

---

## Phase 5B — Cross-parameter consistency and inheritance validation

Before estimating feasibility, use `cross_parameter_validation.csv` to compare each claim-critical target-paper parameter/theory item against mapped same-author/group sources.

For every comparable item record:
- target-paper value/definition or missing status;
- related-source value/definition and exact location;
- relationship to the target model (`DIRECT_INHERITANCE`, `SAME_MODEL_DIFFERENT_CASE`, `SAME_RIG`, `SAME_METHOD`, `CORROBORATION_ONLY`);
- unit/nondimensional conversion;
- operating-condition equivalence;
- transferability verdict;
- conflict status;
- adopted role (`FIXED_LITERATURE_VALUE`, `DERIVED_FROM_SOURCE`, `PRIOR_OR_BOUND_ONLY`, `VALIDATION_ONLY`, `REJECTED_NONTRANSFERABLE`).

Do not average conflicting values merely to obtain a convenient parameter. Conflicts route through `references/evidence_conflict.md`.

### Gate G5B
No claim-critical formula/parameter provenance is considered complete until related-author/group cross-evidence has either corroborated it, legitimately supplemented it, shown a conflict, or been documented as unavailable/non-transferable.

---

## Phase 5C — Pre-implementation reproducibility probability assessment

Use `references/reproducibility_probability.md` and create:
- `reproducibility_probability_assessment.csv`;
- `reproducibility_probability_report.md`.

This assessment is mandatory **after** theory/formula/model/parameter provenance closure and author/group cross-validation, but **before** freezing the Implementation Contract and before full implementation planning.

Estimate the probability that the active M1/M2 workflow can reproduce the critical claims to the preregistered fidelity level using the currently recoverable evidence. Report:
- central estimated reproducibility probability, 0–100%;
- plausible low/high range;
- active mode (M1/M2);
- evidence-confidence level;
- factor-by-factor scores and weights;
- hard caps/blocks applied;
- top positive evidence;
- top reproducibility risks;
- unresolved items most likely to dominate failure;
- what additional evidence would most increase the probability.

The probability is an **evidence-based engineering forecast**, not an empirically calibrated frequentist probability and not a guarantee of success. Never present it with false precision. Prefer integer percentages or coarse 5% increments.

Default factor model (weights may be changed only with documented rationale):
1. theory/formula closure and consistency — 16%;
2. parameter closure and provenance — 16%;
3. model structure / BC / IC / load / damping completeness — 14%;
4. same-author/same-group cross-evidence convergence — 12%;
5. numerical/solver/protocol completeness — 10%;
6. target-data extractability and ground-truth quality — 8%;
7. identifiability/calibration burden — 8%;
8. independent validation evidence availability — 6%;
9. evidence consistency / unresolved-conflict risk — 5%;
10. computational/experimental tractability — 5%.

For each factor provide `low/base/high` scores in [0,1]. The weighted low/base/high totals form the plausible probability range before hard caps. Apply hard caps when claim-critical blockers remain; all caps must be listed in the report.

### Gate G5Q — Reproducibility probability
Mark `REPRODUCIBILITY_PROBABILITY_ASSESSED` only when the factor table, interval, caps and evidence rationale are complete.

### Gate G5U — User-facing feasibility checkpoint
Present the probability report to the user **before** Phase 6. Mark `REPRODUCIBILITY_PROBABILITY_REPORTED` after it has been surfaced.

If the central estimate is below 50% or a claim-critical hard block exists, the subsequent plan must be framed as evidence-gap closure / partial reproduction / feasibility work unless the user explicitly approves a higher-risk full attempt.

---

## Phase 6 — Freeze the persistent Implementation Contract

Create `implementation_contract.yaml` using `references/implementation_contract.md`.

Bind:
- M1/M2 mode and transition rule;
- claim obligations;
- active model variant;
- Equation Registry/dependency obligations;
- model/FE/solver/protocol obligations;
- parameter provenance/types/bounds;
- frozen theory/formula and parameter provenance summaries;
- unresolved provenance items and their claim impact;
- evidence-conflict decisions;
- input/output definitions;
- target definitions and tolerance basis;
- calibration/validation split;
- validation exposure rules;
- equation/model/runtime/convergence tests;
- ML/SHM data protocol if applicable;
- forbidden shortcuts;
- assumptions/limitations;
- whole-paper scan snapshot/version;
- reference-closure snapshot;
- same-author/same-group literature map + cross-parameter validation snapshot;
- pre-implementation reproducibility-probability assessment/report snapshot;
- model dependency graph version/hash;
- figure dependency graph and anchor roles;
- batch-plan version/hash;
- ground-truth freeze/versioning policy;
- Builder/Validator separation policy;
- stop-tuning/evidence-review policy.

### Gate G6
No production implementation before the contract is frozen.

---

## Phase 7 — Plan reproduction, VVUQ and acceptance criteria

Write the reproduction plan:
- active mode;
- target claims;
- computational/experimental/ML branch;
- model hierarchy, dependency DAG and variants;
- figure/result dependency and anchor strategy;
- formula and model/solver fidelity plan;
- verification ladder;
- code architecture;
- third-party open-source search/reuse strategy;
- formal target extraction strategy;
- metrics/tolerances **with basis/source/uncertainty**;
- calibration and withheld validation sets;
- candidate C parameters/bounds, if M2 is expected;
- optimizer/objective strategy if needed;
- sensitivity/identifiability/UQ plan;
- model discrepancy budget;
- stopping criteria and stop-tuning trigger;
- model-based batch plan and regression set;
- MATLAB parity;
- clean-room rerun.

Use `references/vvuq_framework.md`.

### Phase 7A — Model-based figure/result batch planning
Use `references/figure_batch_planning.md` and create `figure_batch_plan.csv`.

Default planning heuristic — configurable, not a scientific law:
- first appearance of a new physical mechanism: about 1–3 high-information results;
- same-model parameter sweep: about 3–6 results;
- downstream derived quantities: about 4–8 results;
- time history + FFT + orbit + Poincare from one operating condition: treat as one validation group when they share the same state solution.

Each batch must list prerequisites, new physical mechanism, anchor results, satellite results, regression results and acceptance gate. Prefer one new physical mechanism per batch unless the paper itself inseparably couples them.

### Gate G7B — Batch plan
Mark `BATCH_PLAN_FROZEN` before full implementation. The user approves the overall plan and active batch sequence; later batches may be updated only with explicit dependency/regression reasoning.

### Gate G7 — Plan approval
Use `templates/plan_approval.md` and `references/plan_approval.md`.

Default: `PLAN_AWAITING_APPROVAL`.

Do not start full implementation until:
- user explicitly sets/communicates `PLAN_APPROVED`; or
- the user has explicitly granted `PREAPPROVED_CONTINUOUS_EXECUTION` for this reproduction.

---

## Phase 8 — Third-party open-source reuse audit

After the plan is approved, search:
- cited method/reference implementations;
- structurally similar open-source models;
- official solver/manual examples/templates.

Classify code as:
- `METHOD_REFERENCE_CODE`;
- `SIMILAR_SYSTEM_CODE`;
- `SOLVER_EXAMPLE_OR_TEMPLATE`.

Create `open_source_reuse_audit.csv` and record source/version/license/similarity/reusable components/hidden defaults/parameter transferability and decision `ADOPT/ADAPT/REFERENCE_ONLY/REJECT/NONE_FOUND`.

Rules:
- method code may validate theory/algorithm implementation;
- similar-system code may inform architecture and diagnostics;
- solver examples may verify solver semantics;
- no external parameter value becomes target-paper evidence without independent provenance/transferability;
- no suitable code found -> implement from the approved plan; this is normal.

### Gate G8
Mark `REUSE_AUDITED` before importing/adapting external code.

---

## Phase 9 — Select implementation branch(es)

### 9A Computational branch
Use Python first. Implement configuration/provenance, model, solver, postprocess, target extraction, metrics, objective, sensitivity, identification, diagnosis, reproduction runner, equation/claim traceability and tests.

### 9B Experimental branch
Use `references/experimental_reproduction.md`. Reconstruct specimen, fixtures/preload, sensors, actuator/hammer/shaker, DAQ, sample rate, anti-aliasing, triggering, windows/averaging, estimator/coherence, calibration/noise/clipping, environmental conditions, repeats and coordinate/channel mapping.

Distinguish experimental rerun, data-analysis reproduction and simulation-to-experiment reconstruction.

### 9C ML/SHM branch
If ML/data-driven inference is claim-relevant, use `references/ml_shm_reproduction.md` and create `dataset_protocol_register.csv`.

Audit independent-unit splits, windowing relative to split, normalization fit scope, feature extraction, augmentation, class balancing, CV grouping, hyperparameter tuning, checkpoint selection, seeds/repeats and confidence intervals.

Any train/validation/test leakage that invalidates the paper's claimed evaluation protocol is a critical reproduction finding.

### Gate G9
Do not mix computational, experimental, stochastic, measurement or ML-data mismatch sources without labeling them.

---

## Phase 9D — Formula-to-Code Fidelity and Paper-to-Code Hallucination Audit

Create:
- `equation_code_traceability.csv`;
- `formula_test_registry.csv`;
- `hallucination_audit.csv`;
- `model_variant_manifest.csv` when variants exist.

Use `references/formula_fidelity.md` and `references/paper_to_code_hallucination_audit.md`.

For every critical equation:
1. map to concrete code symbol;
2. map paper variables to code variables/units/signs;
3. link equation-level tests;
4. show runtime connectivity to affected claim;
5. detect constants/defaults/alternate branches that shadow it;
6. detect unsourced terms/unapproved simplifications.

Audit at least:
`MISSING_EQUATION`, `EXTRA_UNSOURCED_TERM`, `UNAUTHORIZED_SIMPLIFICATION`, `PARAMETER_INVENTION`, `WRONG_EQUATION_MAPPING`, `DISCONNECTED_IMPLEMENTATION`, `UNIT_MISMATCH`, `SIGN_OR_COORDINATE_ERROR`, `INDEX_OR_DOF_ERROR`, `BOUNDARY_CONDITION_DRIFT`, `INITIAL_CONDITION_DRIFT`, `SOLVER_SUBSTITUTION_DRIFT`, `POSTPROCESSING_DRIFT`, `METRIC_DRIFT`, `DEAD_OR_SHADOWED_FORMULA`, `PAPER_CORRECTION_NOT_DISCLOSED`, `CLAIM_SCOPE_DRIFT`.

### Gate G9F
`FORMULA_FIDELITY_VERIFIED` requires 100% critical active equation coverage, runtime connectivity and no open P0/P1 hallucination findings. If it fails, return upstream. **Do not calibrate around missing equations.**

---

## Phase 9E — Model/FE/Solver/Protocol Fidelity Gate

Update `model_implementation_registry.csv` with actual implementation evidence using `references/model_solver_fidelity.md`.

Trace:
`paper/model obligation -> implementation file/deck/API/setting -> focused verification -> runtime evidence -> claim output`.

Check geometry, DOFs, element/formulation/order, mass formulation, mesh role, materials/orientation, contact/joints, constraints, supports, loading/base excitation, damping, initial/preload state, solver semantics, convergence, reduction, outputs and hidden defaults.

### Gate G9M
`MODEL_IMPLEMENTATION_FIDELITY_VERIFIED` requires no open claim-relevant P0/P1 non-formula fidelity findings. Formula fidelity alone cannot pass this gate.

---

## Phase 10 — Python-first code and solution verification

Prerequisites: G9F and G9M.

Verification ladder:
1. syntax/import/smoke;
2. unit/dimension sanity;
3. equation-level limiting cases;
4. analytical/textbook benchmark;
5. minimal DOF/reduced model;
6. solver stability;
7. timestep/mesh/frequency/modal convergence;
8. alternate implementation/solver check where feasible;
9. full paper model.

Record numerical error separately from paper mismatch.

### Gate G10
`PYTHON_VERIFIED` means the intended, fidelity-verified model is solved consistently with defensible numerical settings; it does not mean the paper result matches yet.

---

## Phase 11 — Formal quantitative extraction of paper targets

Priority:
1. exact text/table values;
2. supplementary source data;
3. vector PDF/SVG/EPS extraction;
4. calibrated raster digitization;
5. documented manual reading.

Record axes/units, linear/log scale, series identity, transforms, interpolation, raw/processed files, occlusion and extraction uncertainty in `paper_data_extraction_register.csv`. In addition create `paper_ground_truth_manifest.csv` using `references/ground_truth_freeze.md`.

Use `references/result_type_registry.md` and `references/figure_digitization.md`.

Reconcile actual extraction quality with Phase 2A characterization. If tolerance/role must change materially, reopen G7 and approval before scoring.

Namespace targets explicitly:
- `paper_raw_*` — authoritative raw extraction;
- `paper_processed_*` — transparent derived/resampled target;
- `surrogate_*` — fitted/ROM/interpolated engineering surrogate that must never be called the paper target.

A target correction creates a new freeze version and automatically invalidates all affected old scores/verdicts.

### Gate G11F — Ground-truth freeze
Mark `GROUND_TRUTH_FROZEN` only when source page/panel/series, extraction method, axis calibration, units, uncertainty and raw hash are fixed.

### Gate G11
No paper-result scoring until targets and uncertainty are machine-comparable **and** the authoritative target version is frozen.

---

## Phase 12 — Baseline reproduction before calibration

Run P/T/L plus explicit H values with **no reproduction-team inverse-calibration result**.

Create `baseline_comparison.csv` for the active batch **plus every upstream/frozen regression target affected by the same modules**.

Diagnose discrepancy categories:
- target extraction/transcription;
- theory/model form;
- formula fidelity;
- model/solver fidelity;
- geometry/material/BC/interface;
- excitation/initial state;
- numerical settings;
- experimental/measurement;
- ML/data protocol;
- stochastic realization;
- missing physical parameters;
- model discrepancy.

### Gate G12
If gross physics/fidelity/verification fails, return upstream. Do not optimize first.

---

## Phase 13 — Model-discrepancy budget

Use `references/model_discrepancy.md` and `model_discrepancy_budget.csv`.

Conceptually separate:
`paper evidence = model(theta) + model-form discrepancy + measurement uncertainty + paper rounding/extraction uncertainty + stochastic variability + numerical error`.

Estimate/bound components where possible. Adjustable parameters must not absorb every residual.

### Gate G13
Before calibration, identify which discrepancy is plausibly parameter-driven.

---

## Phase 14 — Calibration eligibility, parameter approval and M1/M2 mode check

Promote H -> C only when:
- source recovery failed to recover a transferable fixed value;
- the quantity is physical, not numerical;
- bounds/prior are defensible;
- calibration evidence is sensitive to it;
- parameter count is supportable;
- no unresolved model/fidelity error is being hidden.

Do not optimize P/T/N values merely to improve fit. Random seeds/noise realizations are not physical truth.

### Mandatory mode check
If the reproduction team will use target-paper outputs to infer a claim-critical omitted physical parameter, ensure active mode is M2 before optimization. If still M1, transition and update the mode manifest/Implementation Contract/plan.

### Gate G14
Freeze the approved C set and mode before optimization.

---

## Phase 15 — Physics-aware objective construction

Use typed metrics; normalize residuals by uncertainty/tolerance scales and preserve individual components.

Examples:
- modal: frequency error + MAC/subspace;
- FRF: resonance/antiresonance, log magnitude, phase, bandwidth;
- transient: peak/RMS/envelope/dominant frequency/time shift;
- PSD: peaks, log spectrum, band energy, integrated RMS;
- nonlinear: backbone, hysteresis energy, jumps/bifurcations;
- chaotic: invariant/statistical/phase-space features;
- stochastic: distributions, PSD, correlation/ensemble statistics;
- spatial fields: registered physical field errors; SSIM supplemental;
- ML/SHM: exact evaluation protocol metrics plus uncertainty/repeats.

### Gate G15
Objective definitions/weights/tolerance bases must be versioned and frozen before calibration.

---

## Phase 16 — Bounded inverse identification / calibration (M2 or paper-described identification)

Select optimizer according to dimension/cost/smoothness/multimodality: least-squares/trust-region/L-BFGS-B, differential evolution/CMA-ES/PSO, global->local, DOE/surrogate/Bayesian optimization, gradient/adjoint when trustworthy.

Record bounds, transforms, seed, optimizer/version/settings, objective components, evaluations, runtime, best vector and termination reason.

Use multi-stage identification when physics supports parameter grouping.

### Gate G16
Calibrated values are identified/equivalent parameters unless independently recovered from literature evidence.

---

## Phase 17 — Sensitivity, identifiability and uncertainty quantification

Perform as applicable:
- local/global sensitivity;
- Jacobian/SVD/Fisher/correlation analysis;
- multi-start;
- profile likelihood;
- bootstrap;
- ensemble/posterior exploration;
- MCMC/Bayesian calibration for high-value cases;
- parameter covariance/prediction intervals;
- extraction/measurement uncertainty propagation.

Classify `WELL_IDENTIFIED/WEAKLY_IDENTIFIED/NON_UNIQUE/BOUND_HIT/UNIDENTIFIABLE`.

Keep separate verdicts for result reproduction and physical parameter identification.

### Gate G17
Do not claim physical parameter truth without identifiability/UQ evidence.

---

## Phase 18 — Builder freeze, withheld validation, prediction and exposure control

Use `references/validation_strategy.md`, `references/validation_exposure.md` and `references/builder_validator_separation.md`.

Before inspecting withheld residuals, freeze the Builder output and create `builder_validator_handoff.yaml` containing code/model/parameter hashes, ground-truth manifest version, metric/tolerance policy, calibration targets, validation targets, exposure snapshot and regression set. Set `BUILDER_FROZEN`, then `VALIDATOR_RUNNING`.

The Validator may fresh-run, score, classify and diagnose a discrepancy signature, but may not change equations, physical parameters, numerical settings to chase the paper, ground truth, metrics or tolerances.

Freeze accepted model/C parameters and run `WITHHELD_UNSEEN` targets. Log every validation target in `validation_exposure_log.csv`.

Use `references/result_presentation_contract.md`. For each formal target, the Validator must produce a Validation Packet containing:
- frozen paper/source ground-truth view or exact source excerpt/value;
- fresh-run reproduction bound to the run manifest;
- paper/reproduction side-by-side and/or overlay/difference view when meaningful;
- result-type-specific quantitative/feature metrics;
- explicit acceptance rule and `PASS/PARTIAL/FAIL/BLOCKED` verdict.

Do not use the same display/metric policy for all result types. Time histories, spectra, orbit/Poincare/bifurcation results, stochastic outputs and fields require different feature metrics. Any time/phase alignment must be predeclared; silent shifting to improve fit is forbidden.

Set `VALIDATION_PACKET_COMPLETE` before a formal PASS/PARTIAL is finalized.

If validation fails:
1. diagnose first;
2. do not silently refit;
3. if the residual is used to change model/parameters/objective/assumptions, reclassify that target `EXPOSED_DEVELOPMENT_EVIDENCE`;
4. choose a new holdout if available;
5. version the calibration/validation manifest.

### Gate G18
`PYTHON_ACCEPTED` requires successful independent validation when available and `VALIDATION_PACKET_COMPLETE` for formal targets. If no independent evidence remains, downgrade to calibration/development-supported or engineering-equivalent reproduction.

---

## Phase 19 — Discrepancy-driven repair loop

For each material mismatch:

`quantify -> classify -> rank hypotheses -> inspect evidence -> design discriminating test -> write repair plan -> approval if scientifically material -> make smallest justified change -> reopen affected gates -> rerun fidelity/verification/regression -> recalibrate only when eligible -> revalidate with exposure control -> accept/rollback/iterate`.

Use `templates/repair_plan.md`.

Routine implementation bugs that do not alter the scientific contract can be fixed without a new user approval. Changes to model structure, parameter type/provenance, calibration/validation split, objective/tolerance or physical assumptions require `REPAIR_PLAN_APPROVED` unless continuous execution was explicitly preapproved.

Default to one factor group per iteration. Track primary-error improvement, regression damage, bound pressure and whether independent solvers/backends reproduce the same residual structure.

Use `references/stop_tuning_evidence_review.md` and `stop_tuning_decision.csv`. The default configurable stop-tuning heuristic is triggered when any of the following holds:
- two scientifically meaningful repair iterations improve the pre-registered primary error by less than about 10%;
- a local improvement materially degrades frozen anchors/regression targets;
- eligible physical parameters repeatedly hit implausible or prior boundaries;
- numerical settings must be changed to fit the paper rather than to establish convergence;
- multiple legitimate numerical backends retain the same structured residual;
- the residual signature points to missing/ambiguous model or evidence rather than an eligible parameter.

When triggered, set `STOP_TUNING` and enter `EVIDENCE_REVIEW`. Review in priority order: target-paper cross-chapter evidence -> citation lineage -> original variable/model definitions -> units/nondimensionalization -> parameter semantics -> numerical-algorithm semantics -> explicit model-form variants.

The 10% value is an engineering default, not a universal scientific threshold; it may be changed only in the approved plan before seeing the relevant residuals.

Stop when criteria pass, residuals are within justified uncertainty, parameters are non-identifiable, evidence blocks further progress, improvement requires implausible values or no independent validation remains.

---

## Phase 20 — Result-type-specific stochastic/nonlinear/chaotic/spatial handling

This phase is a policy overlay for Phases 11–21, not a separate excuse to change the model.

- stochastic systems: compare ensembles, distributions, PSD/correlation/extremes/confidence intervals; report realizations/seeds;
- chaotic systems: avoid long-time pointwise RMSE; use spectra/statistics/phase-space/Poincare/bifurcation/invariant measures as appropriate;
- spatial fields: register physical coordinates before comparing values/gradients/integrals/mode subspaces;
- random surfaces/processes: prefer statistical/fractal/spectral equivalence over realization-by-realization equality unless the realization is fully specified.

---

## Phase 21 — Robustness, VVUQ closure and claim regression

Revisit every H/C item, conflict, exposed validation target and critical claim.

Run applicable:
- convergence/alternate solver;
- stochastic ensemble;
- parameter-bound perturbation;
- target digitization uncertainty;
- model-form variants;
- experimental repeatability;
- ML repeated seeds/group splits;
- regression of formula/model fidelity;
- rerun of all frozen anchors/modules whose dependency nodes are affected by the accepted change.

Classify assumptions `CLOSED_BY_SOURCE/CALIBRATED_EQUIVALENT/ACCEPTED_UNCERTAINTY/NON_IDENTIFIABLE/BLOCKING`.

Update `vvuq_matrix.csv`, conflicts, validation exposure and claim statuses.

---

## Phase 22 — MATLAB parity

After Python acceptance, port the accepted formulation to MATLAB. Preserve equations, units, inputs, initial conditions, solver intent and postprocessing.

Compare scalar outputs, curves and claim metrics within parity tolerance. MATLAB mismatch is a new discrepancy requiring diagnosis.

---

## Phase 23 — Run provenance and artifact freeze

Use `references/run_provenance.md` and create `run_manifest.yaml` for every evidence-producing run.

Bind at minimum:
- code hashes/commit;
- source/data/target-extraction hashes;
- configuration/parameter/contract hashes;
- theory/formula provenance, parameter provenance and combined provenance-snapshot hashes;
- Python/MATLAB/solver/tool versions;
- OS/compiler/libraries;
- relevant hardware;
- random seed policy;
- exact command;
- timestamp/duration;
- output hashes and claim metrics.

Freeze the final artifact inventory and prevent untracked changes.

### Gate G23
No final reproducibility claim without provenance to exact producing artifacts.

---

## Phase 24 — Clean-room independent rerun

Use `references/clean_room_reproduction.md`.

In a fresh environment:
1. start only from frozen package/README;
2. install declared dependencies;
3. acquire/verify allowed data by documented procedure;
4. run smoke/fidelity/verification tests;
5. execute Python reproduction;
6. execute MATLAB parity when required/available;
7. regenerate metrics/figures;
8. compare to frozen acceptance bounds;
9. record manual interventions.

Hidden local files, caches, undeclared environment variables or manual corrections are reproducibility defects.

### Gate G24
Mark `CLEAN_ROOM_VERIFIED` only after successful fresh-environment execution.

---

## Phase 25 — Final claim-level verdict and evidence bundle

Produce an evidence bundle containing:
- evidence availability matrix;
- M1/M2 mode manifest and transitions;
- plan/repair approvals;
- claim registry/links;
- Paper Evidence Matrix;
- chapter registry + cross-chapter evidence links + reference-use registry;
- preliminary target characterization;
- Equation/Algorithm Registry/dependency graph;
- formula-to-code traceability/tests/hallucination audit;
- model structure + model/solver fidelity registry;
- physics/model dependency graph;
- figure dependency graph + anchor/satellite roles;
- model-based figure batch plan;
- theory/citation research logs;
- theory/formula provenance matrix and source statistics;
- evidence conflict register;
- parameter register/source traces/assumptions;
- parameter provenance summary, inverse-parameter summary and unresolved-provenance register;
- Implementation Contract;
- third-party reuse audit;
- VVUQ/discrepancy budget;
- experimental and/or ML protocol registers;
- target extraction/raw/processed data + immutable ground-truth manifest/version;
- baseline/calibration/validation metrics;
- per-target Validation Cards + validation metric files;
- batch validation summaries + final dependency-aware regression dashboard;
- validation exposure log + Builder/Validator handoff;
- optimization/sensitivity/identifiability/UQ outputs;
- iteration log + stop-tuning/evidence-review decisions;
- Python/MATLAB parity;
- run manifests/artifact hashes;
- clean-room report;
- unresolved limitations;
- claim-level verdict table.

The human-readable `reproduction_report.md` must contain the provenance executive summary plus explicit Theory/Formula Provenance, Parameter Provenance, Assumption/Inverse-Identification, and Unresolved Provenance tables; provenance must not exist only in CSV appendices. It must also reproduce the **pre-implementation reproducibility probability** exactly as it was reported before coding, including its interval, factor scores, caps, and top risks, and compare that forecast with the eventual outcome without retroactively changing the original probability.

For each critical claim report `PASS/PARTIAL/FAIL/BLOCKED` and strongest justified evidence class.

---

# 7. Final classifications

## Reproduction quality

- **Independent reproduction (M1)** — independently implemented model reproduces critical claims from paper/theory/recoverable evidence without reproduction-team fitting of omitted claim-critical parameters to target-paper outputs.
- **Predictive validated engineering reconstruction (M2)** — reconstructed/calibrated model predicts genuinely withheld evidence within acceptance criteria.
- **Engineering-equivalent reproduction (M2)** — reconstructed/calibrated model reproduces main claims and residual differences are consistent with justified uncertainty, but predictive validation may be limited.
- **Calibration/development-supported reproduction** — fitted/development evidence matches but no unexposed independent validation remains.
- **Partial reproduction** — some critical claims pass while others fail or remain blocked.
- **Failed reproduction** — critical claims materially disagree after justified investigation.
- **Not reproducible from disclosed/recoverable information** — missing/inconsistent evidence prevents a defensible implementation/reconstruction.

## Parameter-identification quality

- `WELL_IDENTIFIED`
- `WEAKLY_IDENTIFIED`
- `NON_UNIQUE_EQUIVALENT_SET`
- `BOUND_LIMITED`
- `UNIDENTIFIABLE`
- `NOT_APPLICABLE`

## Artifact reproducibility quality

- `CLEAN_ROOM_VERIFIED`
- `DEVELOPMENT_ENVIRONMENT_ONLY`
- `PARTIALLY_RUNNABLE`
- `NOT_RUNNABLE`

## Provenance disclosure quality

Report one of:
- `PROVENANCE_COMPLETE`
- `PROVENANCE_COMPLETE_WITH_EXPLICIT_ASSUMPTIONS`
- `PROVENANCE_LIMITED_BY_UNRESOLVED_ITEMS`
- `PROVENANCE_INSUFFICIENT`

A final `GO` requires every claim-critical theory/parameter item to be explicitly sourced, derived, assumed, inverse-identified, numerically verified, or unresolved/blocking; silent provenance gaps are forbidden.

## Fidelity quality

Report separately:
- formula fidelity;
- model/FE/solver/protocol fidelity;
- data/experimental/ML protocol fidelity where applicable.

Never collapse these dimensions into one score.
