## 4.0.0-rc5

Added mandatory same-author/same-group literature cross-evidence and a pre-implementation reproducibility-probability checkpoint.

- requires systematic search of target authors' and research group's related papers, theses/dissertations, conference versions, technical reports and same-model/same-rig publications for every claim-critical theory/parameter gap;
- adds `author_group_literature_map.csv` and `cross_parameter_validation.csv` with inheritance/transferability/conflict roles;
- prevents H/C/UNRESOLVED promotion before author/group cross-evidence closure;
- adds an evidence-based pre-implementation reproducibility probability (central estimate + plausible range) after theory/formula/model/parameter provenance closure and before Implementation Contract/full planning;
- probability factors include theory, parameters, model structure, group-cross-evidence convergence, numerical protocol, target quality, identifiability, validation availability, evidence consistency and tractability;
- adds conservative hard caps for unresolved governing equations, non-identifiable critical parameters, physics-changing conflicts, poor target extractability and weak validation;
- freezes the original probability report and requires final report comparison against actual outcome without retroactive rewriting;
- binds group-cross-evidence and probability-report snapshots into the Implementation Contract and run provenance.

# v4.0.0-rc4

- Added a mandatory Result Presentation Contract for every formal validation target.
- Formal validation now uses dual evidence: paper/source ground truth + fresh-run reproduction + typed comparison + quantitative/feature metrics + explicit verdict.
- Added `VALIDATION_PACKET_COMPLETE` gate; PASS/PARTIAL cannot be finalized from visual similarity alone or metrics alone.
- Added result-type-specific display rules for time history, FFT/spectrum, orbit/phase portrait, Poincare, bifurcation, scalar/table, field/contour and stochastic targets.
- Added validation-card, metric, batch-summary and regression-dashboard templates.
- Added explicit phase/alignment governance: alignment must be predeclared and cannot be silently optimized to reduce error.
- Extended closed-loop fault-injection suite with presentation-completeness and metric-family mismatch tests.
- Updated reproduction-report template and final evidence bundle to include validation packets and dashboards.

# v4.0.0-rc3

- Added explicit closed-loop exits from `EVIDENCE_REVIEW`: reopen with new evidence, approved M2 transition, rollback/retry, or terminal BLOCKED.
- Added explicit ground-truth correction back-edge to G11/G12 with metric/verdict invalidation.
- Added explicit regression-damage rollback path to the main state-machine diagram.
- Added a closed-loop termination invariant preventing silent return from evidence review to tuning.
- Added executable closed-loop fault-injection validation suite.
- Corrected workflow release-candidate header.

# Changelog

## 4.0.0-rc2

Regression-driven refinement after Level-A process tests on two gear-domain theses (high-speed EMU gearbox-bearing system; planetary-gear fault dynamics).

Added/strengthened:
- explicit provenance for `CITED_EXTERNAL_VALIDATION_DATA` / borrowed validation evidence;
- distinction between modules that introduce/generate a result and upstream modules the result validates;
- later-chapter healthy/scalar evidence may back-validate an earlier module without activating the later chapter's new mechanism;
- per-target comparison protocol for numbering direction, coordinate/sign/sensor/normalization conventions;
- validation-claim typing and metric-family routing (frequency/sideband/mechanism claims are not silently scored as amplitude-waveform NRMSE);
- explicit support for foundation modules with `NO_DIRECT_FIGURE`, using formula/scalar/reference checkpoints before later integrated anchors.

No new calibration freedom was introduced. M1/M2, provenance, formula/model fidelity, VVUQ, MATLAB parity and clean-room semantics remain unchanged.

## 4.0.0-rc1

Release candidate focused on execution orchestration for long, multi-chapter structural-dynamics papers. v3.3 provenance, M1/M2, formula/model fidelity, VVUQ, MATLAB parity and clean-room semantics are preserved.

Added:
- mandatory whole-paper/cross-chapter evidence scan before declaring claim-critical information missing;
- explicit reference-closure status and gate before H/C promotion;
- physics/model dependency DAG and upstream-module gate;
- figure/result dependency graph with Anchor/Satellite/Regression roles;
- model-based figure batch planning instead of consecutive-figure execution;
- immutable/versioned paper ground-truth manifest and raw/processed/surrogate namespaces;
- Builder/Validator procedural separation and handoff manifest;
- configurable `STOP_TUNING -> EVIDENCE_REVIEW` policy;
- dependency-aware regression over frozen anchors/modules;
- orchestration benchmark metrics for the skill itself;
- nine new evidence/governance templates and six new reference modules.

Changed:
- parameter recovery now explicitly requires whole-paper closure before external citation closure and identification;
- Implementation Contract binds dependency graphs, batch plan, ground-truth version, Builder/Validator policy and stop-tuning policy;
- paper-target corrections invalidate affected prior scores/verdicts;
- baseline and repair loops are batch- and dependency-aware.

This is an RC, not yet the final v4.0.0 release. It is intended for bearing failure-replay, rotor-thesis desktop benchmarking and gear regression benchmarking before finalization.

## 3.3.0

Strengthened mandatory theory/formula/parameter provenance disclosure and final-report transparency.

Added:
- unified provenance source classes (`PAPER_DIRECT`, `PAPER_DERIVED`, `CITED_REFERENCE_DIRECT`, `CITATION_LINEAGE_DERIVED`, `RELATED_THESIS_OR_PAPER`, `AUTHORITATIVE_EXTERNAL_SOURCE`, `TRANSFERRED_PRIOR_OR_BOUND_ONLY`, `REPRODUCTION_DERIVED`, `ASSUMED`, `INVERSE_IDENTIFIED`, `NUMERICAL_VERIFICATION_SETTING`, `UNRESOLVED`);
- mandatory Phase 5A provenance-closure gate before the Implementation Contract;
- theory/formula provenance matrix, parameter provenance summary, source-count summary, inverse-parameter summary, and unresolved-provenance templates;
- explicit source-class/location fields in equation, theory-research, and parameter registers;
- mandatory human-readable provenance executive summary in the final reproduction report;
- required detailed report tables for theory/formulas, parameters, assumptions/inverse identification, and unresolved provenance;
- explicit disclosure that inverse-identified values are reproduction-equivalent values and not author-disclosed parameters;
- provenance snapshot hashes bound into evidence-producing run manifests;
- provenance disclosure quality as a separate final classification.

This release makes provenance a first-class output: a reviewer must be able to see exactly which theory and parameters came from the target paper, its references, other literature, reproduction-team derivation, assumptions, inverse identification, numerical verification, or remain unresolved.


## 3.2.0

Scope and logic consolidation for literature-only structural-dynamics reproduction (no usable author source code).

Changed:
- removed author-source-code rerun/porting/blinding logic from the active workflow; the skill now uses only `M1 Independent reimplementation` and `M2 Engineering reconstruction / calibrated reproduction`;
- added mandatory `M1 -> M2` transition when the reproduction team must infer a claim-critical omitted physical parameter from target-paper outputs (except when reproducing an identification procedure explicitly described by the paper);
- fixed the previous workflow/Phase-20 semantic conflict; G20 now consistently denotes result-type-specific stochastic/nonlinear/chaotic/spatial handling;
- added a hard initial `PLAN_APPROVED` gate and a separate material repair-plan approval gate, with an explicit continuous-execution opt-out only when the user preapproves it;
- added preliminary target characterization before tolerance/calibration-validation freeze, plus tolerance basis/source/uncertainty fields;
- added non-formula Model/FE/Deck/Solver/Protocol Fidelity with a dedicated registry and hard gate;
- added explicit Evidence Conflict Register and no-silent-cherry-picking policy;
- added Validation Exposure Ledger so validation evidence loses independent status once it influences development;
- added a dedicated ML/SHM data-protocol and leakage branch;
- added missing package templates: Paper Evidence Matrix, Theory Research Log, Model Structure Register, Model Implementation Registry, Open-Source Reuse Audit, Evidence Conflict Register, Validation Exposure Log, Target Characterization, Dataset Protocol Register, Plan Approval, and Repair Plan;
- updated parameter-source recovery to remove author-source-code dependence and emphasize citation/thesis/supplement/non-code data provenance;
- updated the Implementation Contract, report template, manifest and self-evaluation suite accordingly.

The central scientific rule remains: **prove paper/model fidelity before using similarity or calibration as evidence.**

## 3.1.0

Added a first-class Formula-to-Code Fidelity and anti-hallucination layer to prevent LLM implementations from silently drifting away from paper mathematics.

Added:
- mandatory Equation/Algorithm Registry for every numbered and claim-relevant operative formula;
- 100% hard coverage requirement for critical governing/constitutive/BC/IC/excitation/damping/nonlinear/active algorithm and post-processing equations;
- Equation Dependency Graph from paper equations through runtime computation to claim outputs;
- Equation-to-Code Traceability Matrix with file/function/symbol, variable/unit/sign mapping, tests and runtime evidence;
- equation-level test registry using limiting cases, branch boundaries, analytical properties, transformations and perturbation/ablation checks;
- runtime coverage rule so dead/disconnected/shadowed formulas do not count as implemented;
- Paper-to-Code Hallucination Audit covering missing equations, extra unsourced terms, unauthorized simplification, invented parameters, wrong mapping, unit/sign/DOF/BC/IC drift, solver/post-processing/metric drift, dead formulas and undisclosed paper corrections;
- strict ban on using parameter optimization to compensate for missing/disconnected formulas;
- separate `PAPER_FAITHFUL`, `SOURCE_LINEAGE_VARIANT`, `CORRECTED_INTERPRETATION`, and `VERIFICATION_SIMPLIFICATION` model variants;
- explicit rule that suspected paper errors must not be silently corrected;
- formula-fidelity regression after equation/model/BC/IC/solver/post-processing changes;
- new templates for equation registry, dependency graph, traceability, formula tests, hallucination findings and model variants;
- expanded clean evidence/report/self-evaluation expectations for formula fidelity.

This release changes the order of evidence: **prove that the program implements the intended paper mathematics before using result similarity or parameter calibration as evidence.**

## 3.0.1

Corrected and generalized author-artifact handling:
- author code/data are now conditional evidence sources rather than universal workflow prerequisites;
- added an Artifact Availability Matrix with precise states (`AVAILABLE`, `AVAILABLE_BLINDED`, `NOT_FOUND_AFTER_DOCUMENTED_SEARCH`, `KNOWN_PRIVATE`, `INACCESSIBLE`, `UNKNOWN`, `NOT_APPLICABLE`);
- R1/R2 are explicitly artifact-dependent and can be `NOT_ELIGIBLE_FROM_AVAILABLE_ARTIFACTS`; R3/R4 do not require author code;
- R3 permits metadata-level availability discovery while keeping accessible author-code contents blinded until the independent implementation/tests/primary results are frozen;
- unavailable author code no longer blocks independent reproduction; the fallback evidence triangle is Paper <-> Theory <-> Independent Implementation plus analytical/benchmark/published-result checks;
- introduced code-source classes `AUTHOR_IMPLEMENTATION`, `METHOD_REFERENCE_CODE`, and `SIMILAR_SYSTEM_CODE`;
- Paper <-> Author Code discrepancy audit is conditional on author-code availability/access;
- added `references/artifact_availability.md` and `templates/artifact_availability_matrix.csv`;
- updated reproduction-mode manifest and workflow gates accordingly.

## 3.0.0

Major architecture upgrade from a reproduction workflow to a reproducible research agent workflow.

Added:
- R1/R2/R3/R4 reproduction-mode taxonomy and mode-specific reuse/blinding rules.
- Claim–Evidence–Artifact Graph and claim-level verdicts.
- Persistent Implementation Contract with change control.
- Formal VVUQ separation: code verification, solution verification, validation, calibration, UQ and prediction.
- Dedicated experimental-reproduction branch.
- Explicit model-discrepancy budget.
- Author-clarification branch for high-impact unresolved disclosure.
- Run provenance with code/data/config/environment/output binding.
- Artifact freeze and clean-room independent rerun gate.
- Skill self-evaluation benchmark framework.
- New templates for mode, claims, VVUQ, discrepancy, experiment, clarification, run manifests, artifacts and clean-room evidence.

Retained and strengthened:
- paper-first theory closure;
- citation-lineage parameter recovery;
- literature transferability checks;
- model-structure freeze;
- P/T/L/C/N/R/H parameter taxonomy;
- Python-first verification;
- figure/data digitization;
- bounded inverse identification;
- calibration-validation separation;
- stochastic/chaotic result handling;
- sensitivity/identifiability;
- discrepancy-driven iterative correction;
- MATLAB parity.

## 2.1.0

Added a mandatory parameter-source recovery strategy before inverse identification.

New behavior:
- trace missing/ambiguous parameters from the exact citation context in the target paper;
- open cited references and recursively follow upstream source lineage when necessary;
- search author theses, prior/later papers, same-group model-family publications, supplements, and official code/data;
- distinguish directly transferable literature values from analogous values that may only define priors/bounds;
- require a Literature Transferability Gate covering definition, units, model form, topology, material/interface meaning, operating conditions, experiment/postprocessing, and consistency with target-paper evidence;
- add Parameter Source Trace records and confidence levels;
- require source recovery to fail before an H parameter may be promoted to C for inverse identification;
- prevent optimization from replacing literature research when the missing value may already exist in the paper's reference lineage.

## 2.0.0

Major generalization from a curve-comparison workflow to a physics-constrained structural-dynamics reproduction and inverse-identification framework.

Added:
- hard model-structure freeze before calibration;
- parameter provenance taxonomy P/T/L/C/N/R/H;
- missing-information research hierarchy;
- explicit H -> C promotion rules;
- bounded inverse identification of eligible missing physical parameters;
- ban on fitting numerical settings;
- calibration vs independent validation manifests;
- baseline comparison before optimization;
- physics-aware multi-objective construction;
- optimizer selection by cost/smoothness/dimension;
- sensitivity and parameter-identifiability gates;
- separate reproduction-quality and physical-parameter-identification conclusions;
- stochastic/random-result handling;
- nonlinear/chaotic phase-space/Poincare/bifurcation comparison rules;
- spatial-field comparison rules;
- regression-protected discrepancy iteration;
- cross-operating-condition predictive validation;
- new templates for parameters, assumptions, calibration/validation, optimization, baseline comparison and identifiability.

The workflow remains paper-first, theory-grounded, reuse-first, Python-first and finishes with MATLAB parity.