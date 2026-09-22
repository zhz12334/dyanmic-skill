# Structural-Dynamics Paper Reproduction Report v4.0-rc5

## Executive provenance summary — mandatory

### Reproduction mode
- active mode: M1 / M2
- M1 -> M2 transition: yes/no
- transition reason (if any):

### Critical theory/formula source statistics
| Source class | Count | Percentage | Blocking items |
|---|---:|---:|---:|
| PAPER_DIRECT | | | |
| PAPER_DERIVED | | | |
| CITED_REFERENCE_DIRECT | | | |
| CITATION_LINEAGE_DERIVED | | | |
| RELATED_THESIS_OR_PAPER | | | |
| AUTHORITATIVE_EXTERNAL_SOURCE | | | |
| REPRODUCTION_DERIVED | | | |
| ASSUMED | | | |
| UNRESOLVED | | | |

### Critical parameter source statistics
| Source class | Count | Percentage | Blocking items |
|---|---:|---:|---:|
| PAPER_DIRECT | | | |
| PAPER_DERIVED | | | |
| CITED_REFERENCE_DIRECT | | | |
| CITATION_LINEAGE_DERIVED | | | |
| RELATED_THESIS_OR_PAPER | | | |
| AUTHORITATIVE_EXTERNAL_SOURCE | | | |
| TRANSFERRED_PRIOR_OR_BOUND_ONLY | | | |
| REPRODUCTION_DERIVED | | | |
| ASSUMED | | | |
| INVERSE_IDENTIFIED | | | |
| NUMERICAL_VERIFICATION_SETTING | | | |
| UNRESOLVED | | | |

### Provenance risk summary
- explicit assumptions:
- inverse-identified parameters:
- unresolved critical theory items:
- unresolved critical parameters:
- claims limited by provenance uncertainty:

### Pre-implementation reproducibility probability — mandatory and frozen
- assessment version/date:
- active mode at assessment: M1 / M2
- central estimated probability: **__%**
- plausible range: **__% – __%**
- evidence confidence: HIGH / MEDIUM / LOW
- hard cap/block applied:
- top strengths:
- top risks:
- unresolved items dominating forecast:

> This is the probability that was reported before implementation. Do not rewrite it after seeing reproduction results.

---

## 1. Paper identity, evidence availability and M1/M2 mode

## 2. Whole-paper / cross-chapter evidence scan
- chapter registry summary:
- cross-chapter evidence recovered:
- unresolved cross-chapter conflicts:
- reference-use closure summary:

## 3. Claim–Evidence–Artifact Graph summary

## 3. Paper Evidence Matrix

## 4. Preliminary target characterization
- extractability:
- expected digitization uncertainty:
- proposed calibration/validation roles:
- tolerance basis:

## 5. Theory and Formula Provenance Matrix — mandatory

For every claim-relevant formula/theoretical relation show:

| ID | Formula/theory | Model role | Target-paper location | Source class | Exact source | Derivation/transfer note | Claims | Implementation status |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Explicitly distinguish equations taken from the target paper from equations recovered from cited references, upstream lineage, related work, authoritative external theory, reproduction-team derivation, assumptions and unresolved interpretations.

## 6. Equation/Algorithm Registry, dependency graph and active variants
- numbered/operative formulas triaged:
- critical active formulas:
- direct implementations:
- proven-equivalent implementations:
- blocked/ambiguous formulas:
- inactive/non-claim formulas and reasons:

## 7. Theory/citation-lineage research and evidence conflicts

## 7A. Same-author / same-group literature cross-evidence — mandatory

Summarize mapped publications, model/system inheritance, parameter/formula corroboration, conflicts and non-transferable sources.

| Item | Target-paper status | Related source | Relationship | Related value/relation | Transferability | Adopted role | Conflict |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 8. Model-structure reconstruction and freeze decision

### Physics/model dependency DAG and module freeze

### Figure/result dependency graph, anchor roles and batch plan

## 9. Model/FE/solver/protocol fidelity registry

## 10. Parameter Provenance Matrix — mandatory

| Parameter | Final value/range | Unit | P/T/L/H/C/N/R | Source class | Exact source/location | Initial/prior | Bounds | Can optimize | Identification basis | Identifiability/UQ | Claims | Status |
|---|---:|---|---|---|---|---|---:|---|---|---|---|---|---|
| | | | | | | | | | | | | | |

Do not label a literature prior as a paper value. Do not label an inverse-identified value as an author-disclosed parameter.

## 11. Assumptions and Inverse-Identification Matrix — mandatory

### 11.1 Explicit assumptions
| Item | Why missing | Searches completed | Assumption | Rationale/bounds | Sensitivity | Affected claims | Closure status |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### 11.2 Inverse-identified parameters
| Parameter | Initial value | Bounds | Calibration targets | Objective | Optimizer | Identified value | Identifiability | Uncertainty/CI | Validation result |
|---|---:|---|---|---|---|---:|---|---|---|
| | | | | | | | | | |

For each inverse-identified parameter state explicitly: **this is an equivalent parameter identified by this reproduction from published target outputs; it is not a parameter value disclosed by the target-paper authors.**

## 12. Unresolved Provenance Items — mandatory

| Item | Kind | Missing/conflicting evidence | Actions already taken | Current treatment | Impact on claims | Blocking? |
|---|---|---|---|---|---|---|
| | | | | | | |

## 12A. Pre-implementation reproducibility probability assessment — mandatory

Reproduce the frozen factor table exactly as reported before coding.

| Factor | Weight | Low | Base | High | Evidence basis | Main risk |
|---|---:|---:|---:|---:|---|---|
| Theory/formula closure and consistency | 0.16 | | | | | |
| Parameter closure and provenance | 0.16 | | | | | |
| Model structure / BC / IC / loads / damping completeness | 0.14 | | | | | |
| Same-author/same-group cross-evidence convergence | 0.12 | | | | | |
| Numerical/solver/protocol completeness | 0.10 | | | | | |
| Target-data extractability and ground-truth quality | 0.08 | | | | | |
| Identifiability / calibration burden | 0.08 | | | | | |
| Independent validation evidence availability | 0.06 | | | | | |
| Evidence consistency / unresolved-conflict risk | 0.05 | | | | | |
| Computational/experimental tractability | 0.05 | | | | | |

- raw weighted estimate:
- hard caps/blocks:
- final central estimate/range:
- recommended next action at the time:

### Forecast vs final outcome
- pre-implementation forecast:
- final reproduction classification:
- main reasons the outcome matched/diverged from the forecast:

## 13. Persistent Implementation Contract and provenance freeze
- implementation contract hash:
- theory/formula provenance snapshot hash:
- parameter provenance snapshot hash:
- unresolved-provenance snapshot hash:

## 14. Reproduction plan and approval state

## 15. Third-party open-source reuse audit

## 16. Formula-to-Code Traceability and Paper-to-Code Hallucination Audit
- critical formula coverage:
- equation-level test pass rate:
- runtime-path coverage:
- open P0/P1/P2 findings:
- unauthorized simplifications:
- unsourced terms:
- faithful/corrected variant conclusions:

## 17. Computational branch verification

## 18. Experimental branch reconstruction/quality checks (if applicable)

## 19. ML/SHM data protocol and leakage audit (if applicable)

## 20. Formal paper-target extraction, immutable ground-truth manifest and digitization uncertainty

## 21. Baseline comparison

## 22. VVUQ matrix and model-discrepancy budget

## 23. M1/M2 mode transition decision and approved C parameters

## 24. Calibration objective and optimization results

## 25. Sensitivity, identifiability and uncertainty

## 26. Builder freeze, Validator handoff, withheld validation/prediction and exposure log

## 27. Discrepancy-driven iteration history, stop-tuning/evidence-review decisions and repair approvals

## 28. Robustness and assumption closure

## 29. Python–MATLAB parity

## 30. Run provenance and artifact hashes

## 31. Clean-room rerun

## 32. Validation presentation packets and batch/regression dashboards
- per-target Validation Cards:
- validation metric files:
- batch validation summary:
- dependency-aware final regression dashboard:
- incomplete validation packets / reasons:

## 33. Claim-level verdict table

## 34. Final classifications
- reproduction quality:
- parameter-identification quality:
- artifact reproducibility quality:
- formula fidelity quality:
- model/FE/solver/protocol fidelity quality:
- experimental/ML protocol fidelity quality where applicable:

## 35. Remaining limitations and blocked claims

## 36. Final provenance disclosure statement
Summarize in plain language what proportion of the implemented theory and parameter set came from the target paper, what came from its references/other literature, what was assumed, what was inverse-identified, what was selected numerically, and what remains unresolved. This statement must be readable without consulting CSV appendices.
