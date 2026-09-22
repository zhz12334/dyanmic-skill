# Structural Dynamics Reproduction Checklists

## 0A. Whole-paper / cross-chapter evidence scan
- [ ] All chapters scanned before declaring claim-critical information missing
- [ ] Captions/table notes/symbol lists/appendices checked
- [ ] Later validation/experiment chapters checked for earlier-model parameters
- [ ] Chapter Registry created
- [ ] Cross-Chapter Evidence Links created
- [ ] Reference Use Registry created
- [ ] Evidence-reading order separated from reproduction-execution order

## 1. Paper and literature understanding
- [ ] Paper/version/DOI fixed
- [ ] Target figures/tables/results fixed
- [ ] Supplementary files checked
- [ ] Governing equations extracted
- [ ] Novelty and baseline method understood
- [ ] Geometry/material/BC/load/IC/damping locations identified
- [ ] Paper Evidence Matrix created

## 2. Theory closure
- [ ] Theory Dependency Map created
- [ ] Missing concepts identified
- [ ] Missing theory searched online
- [ ] Primary/authoritative sources preferred
- [ ] Formula conventions and units reconciled
- [ ] Theory Research Log created

## 2A. Formula fidelity and anti-hallucination
- [ ] Every numbered equation has an Equation Registry entry
- [ ] Every claim-relevant unnumbered mathematical/algorithmic rule is registered
- [ ] Each equation is classified by role and claim scope
- [ ] Critical active equations have 100% direct or proven-equivalent implementation coverage
- [ ] Mathematical-equivalence substitutions have derivation/equivalence evidence
- [ ] Equation dependency graph is complete for critical claims
- [ ] Each critical equation maps to file/function/symbol
- [ ] Unit/sign/coordinate mapping is explicit
- [ ] Equation-level tests exist for critical formulas
- [ ] Piecewise laws include branch-boundary tests
- [ ] Active formulas are demonstrated on the runtime path
- [ ] No critical formula is dead, shadowed, bypassed, or replaced by a constant/default
- [ ] No unsourced claim-relevant term exists
- [ ] No unauthorized simplification exists
- [ ] No silent paper correction exists
- [ ] Paper-faithful and corrected/interpreted variants are separated when needed
- [ ] No parameter optimization is being used to compensate for a missing/disconnected equation
- [ ] Paper-to-Code Hallucination Audit has no open P0/P1 findings

## 3. Physical model reconstruction
- [ ] Geometry complete enough to instantiate model
- [ ] Coordinate system/DOFs explicit
- [ ] Material properties recorded with units
- [ ] BCs/supports explicit
- [ ] Contacts/joints explicit
- [ ] Loads/excitation explicit
- [ ] Damping explicit
- [ ] Initial conditions explicit
- [ ] Output locations explicit
- [ ] Model Parameter Register complete

## 4. Assumptions
- [ ] Missing values searched in citations/supplements/repos first
- [ ] Remaining assumptions assigned IDs
- [ ] Basis for each assumption stated
- [ ] Confidence stated
- [ ] Expected influence stated
- [ ] Sensitivity range stated where practical
- [ ] No silent assumptions remain

## 4A. Model and figure dependency planning
- [ ] Physics/model dependency DAG created
- [ ] Upstream/downstream modules identified
- [ ] Freeze criterion defined for each critical module
- [ ] Figure/result dependency graph created
- [ ] Anchor/Satellite/Regression roles assigned
- [ ] No downstream tuning is planned while its upstream anchor is open

## 5. Planning
- [ ] Validation ladder defined
- [ ] Python architecture planned
- [ ] Numerical method selected
- [ ] Convergence checks planned
- [ ] Paper comparison metrics defined
- [ ] Acceptance criteria defined before runs
- [ ] High-risk uncertainties prioritized
- [ ] Model-based figure batch plan created
- [ ] Each batch prerequisites/new mechanism/anchors/satellites/regression set defined
- [ ] Stop-tuning trigger pre-registered

## 6. Open-source reuse audit
- [ ] Exact paper title searched
- [ ] Authors + GitHub/GitLab searched
- [ ] Official repository checked
- [ ] Supplementary source checked
- [ ] Similar method implementations searched
- [ ] Similar geometry/BC/excitation models searched
- [ ] Candidate versions/commits recorded
- [ ] Candidate code audited against paper
- [ ] ADOPT/ADAPT/REFERENCE_ONLY/REJECT/NONE_FOUND decision recorded

## 7. Python-first verification
- [ ] FORMULA_FIDELITY_VERIFIED gate passed before paper-result scoring
- [ ] Unit/equation sanity checks pass
- [ ] Analytical/textbook benchmark used when possible
- [ ] Minimal model runs
- [ ] Solver smoke test passes
- [ ] Mesh/time/frequency convergence checked when applicable
- [ ] Full paper model runs
- [ ] Key intermediate checkpoint reproduced
- [ ] Python code is scriptable/repeatable

## 8. Paper result extraction and digitization
- [ ] Exact table/text/supplementary values preferred
- [ ] Official result files checked before digitization
- [ ] Vector extraction attempted when appropriate
- [ ] Figure/panel/series identity recorded
- [ ] Linear/log axis calibration checked
- [ ] Units and scientific multipliers checked
- [ ] Raw extracted points preserved separately
- [ ] Processed/resampled target stored separately
- [ ] Digitization uncertainty estimated
- [ ] No extrapolation used for comparison scoring
- [ ] Paper Data Extraction Register complete
- [ ] Paper Ground-Truth Manifest complete
- [ ] Raw/processed/surrogate target namespaces are separated
- [ ] Ground-truth version frozen before scoring
- [ ] Any corrected target invalidates affected old scores

## 9. Typed comparison and iteration
- [ ] Comparison Matrix created
- [ ] Metrics selected by result type
- [ ] Modal pairing not based on order alone when ambiguous
- [ ] FRF peaks, magnitude and phase handled separately where relevant
- [ ] Time lag used diagnostically, not silently hidden
- [ ] PSD/ASD and one-/two-sided conventions verified
- [ ] Discrepancy signature classified
- [ ] Top hypotheses ranked with evidence
- [ ] Discriminating test planned before parameter change
- [ ] One factor group changed per iteration unless coupling is unavoidable
- [ ] Expected direction of change recorded
- [ ] Regression checkpoints rerun after each accepted change
- [ ] Formula-to-code traceability/hallucination audit rerun after any equation/model/BC/IC/solver/postprocessing change
- [ ] Metric history maintained
- [ ] No blind/unbounded parameter tuning
- [ ] Calibratable parameters have physical bounds
- [ ] Stop condition explicitly assessed
- [ ] Primary-error improvement ratio tracked
- [ ] Regression damage tracked
- [ ] STOP_TUNING / EVIDENCE_REVIEW trigger assessed

## 10. Modal analysis
- [ ] Density present and correct
- [ ] BCs reviewed
- [ ] Rigid-body modes understood
- [ ] Element/model type appropriate
- [ ] Mesh target frequency justified
- [ ] Eigensolver recorded
- [ ] Normalization understood
- [ ] Frequencies convergence-checked
- [ ] Mode pairing not based on order alone
- [ ] MAC uses mapped DOFs when applicable

## 11. Harmonic/FRF
- [ ] Force vs base excitation distinguished
- [ ] Excitation amplitude/unit known
- [ ] Response quantity/unit explicit
- [ ] Damping documented
- [ ] Frequency grid adequate
- [ ] Modal truncation assessed
- [ ] FRF type identified

## 12. Transient
- [ ] Initial conditions defined
- [ ] Integration scheme known
- [ ] Time-step sensitivity performed
- [ ] Highest retained frequency considered
- [ ] Numerical damping documented

## 13. Random vibration
- [ ] PSD units checked
- [ ] One-sided/two-sided convention checked
- [ ] PSD vs ASD not confused
- [ ] Bandwidth adequate
- [ ] RMS integration verified

## 14. EMA/OMA
- [ ] Sampling configuration known
- [ ] Windowing/averaging known
- [ ] FRF estimator documented for EMA
- [ ] Coherence inspected for EMA
- [ ] OMA does not claim measured FRF without input
- [ ] Mode extraction/stabilization method documented

## 15. Assumption closure and robustness
- [ ] Each assumption marked Closed/Accepted uncertainty/Blocking
- [ ] Material assumptions sensitivity-tested
- [ ] Mesh convergence addressed
- [ ] Time/frequency-step convergence addressed
- [ ] Parameter sensitivity addressed
- [ ] No blocking uncertainty hidden

## 15A. Result presentation and Validation Packet
- [ ] Frozen paper/source ground truth is included or referenced
- [ ] Fresh-run reproduction is bound to run provenance
- [ ] Paper/source and reproduction are shown together when the target is visual
- [ ] Axis range/unit/scaling/comparison convention matches the frozen protocol
- [ ] Result-type-specific metrics are used
- [ ] Time/phase alignment, if any, was predeclared and both raw/aligned metrics are retained where material
- [ ] Overlay/difference/residual view is exported when it adds diagnostic value
- [ ] Validation Card created
- [ ] Validation Metrics file created
- [ ] Acceptance rule and verdict are explicit
- [ ] Batch validation summary updated
- [ ] Dependency-aware regression dashboard updated
- [ ] VALIDATION_PACKET_COMPLETE set before PASS/PARTIAL

## 15B. Builder / Validator governance
- [ ] Builder output frozen before withheld validation
- [ ] Builder-Validator handoff manifest created
- [ ] Validator cannot mutate equations/parameters/ground truth/metrics
- [ ] Validation residual exposure logged
- [ ] Exposed targets are not still called independent validation

## 16. MATLAB parity
- [ ] Python accepted before MATLAB finalization
- [ ] Same parameters/units used
- [ ] Same equations/model used
- [ ] Same initial conditions used
- [ ] Same comparison metrics used
- [ ] Python-MATLAB Parity Table created
- [ ] Material disagreement resolved

## 17. Final delivery
- [ ] Reproduction report complete
- [ ] Equation Registry included
- [ ] Equation dependency graph included
- [ ] Equation-to-code traceability included
- [ ] Formula test registry included
- [ ] Hallucination audit included
- [ ] Final Python runnable
- [ ] Python dependency/environment file included
- [ ] Final MATLAB runnable
- [ ] README/run instructions included
- [ ] Comparison figures/tables exported
- [ ] Per-target Validation Cards exported
- [ ] Batch validation summary exported
- [ ] Final dependency-aware regression dashboard exported
- [ ] Source/repository manifest included
- [ ] Final classification assigned
- [ ] GO/NO-GO assigned
