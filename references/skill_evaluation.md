# Skill Evaluation Suite

Evaluate the skill itself on a curated benchmark rather than by prose review alone.

## Coverage set
Include analytical SDOF/MDOF, beams/plates, FEM modal/FRF, transient, random vibration, nonlinear/contact/chaos, EMA, OMA, model updating, SHM/ML and deliberately incomplete papers. The benchmark should assume no usable author source code, matching this skill's scope.

At least some benchmark cases should intentionally contain LLM traps:
- a numbered equation whose term is easy to overlook;
- a time-varying term that a generic implementation might replace by its mean;
- a piecewise/nonlinear law with boundary cases;
- a paper typo requiring faithful vs corrected variants;
- a dead-code implementation where a correct function exists but is bypassed at runtime;
- an unsourced extra correction term that improves curve fit;
- BC/IC/sign/unit drift;
- wrong FE element/mass/contact/solver choice despite correct written equations;
- conflicting paper/thesis/reference parameter values;
- a reference-source formula that differs subtly from the target paper;
- a solver/post-processing convention mismatch;
- parameter fitting that can hide a missing formula;
- validation evidence reused after influencing development;
- ML/SHM windowing or normalization leakage.

## Orchestration / long-thesis challenge dimensions
- parameter available only in a later chapter/appendix/validation section
- local chapter omission incorrectly interpreted as globally missing
- citation-recoverable parameter tempted into inverse identification
- upstream model failure that downstream figures can superficially hide
- dozens of figures requiring dependency-aware batching
- incorrect or mutated digitized paper ground truth
- repeated low-value tuning that should trigger evidence review
- builder/validator rule violations

## Challenge dimensions
- complete vs missing parameters
- source parameter hidden in a cited reference
- transferable vs non-transferable literature value
- conflicting literature evidence
- method-reference code present/absent
- similar-system code helpful/misleading
- figure-only result
- stochastic/chaotic output
- non-identifiable parameter set
- experimental uncertainty
- FE/solver protocol ambiguity
- calibration-only vs genuinely withheld validation
- ML/SHM leakage risk
- formula completeness vs visually plausible but incomplete code

## Evaluation metrics
- missing-information detection recall
- source-lineage recovery precision
- evidence-conflict detection/resolution quality
- correct parameter role classification
- model-structure error detection
- model/solver fidelity detection
- numbered/claim-relevant equation triage recall
- critical formula coverage accuracy
- missing-equation detection recall
- unauthorized-simplification detection precision/recall
- unsourced-term detection
- dead/disconnected-formula detection
- faithful-vs-corrected variant separation
- equation-to-code traceability completeness
- equation-level test quality
- correct M1/M2 classification and M1->M2 transition behavior
- correct third-party reuse behavior
- correct metric routing
- calibration/validation leakage rate
- validation-exposure detection rate
- rate of calibration used to mask formula/model errors
- identifiability detection
- ML/SHM leakage detection
- runnable code rate
- clean-room success rate
- Python/MATLAB parity
- claim verdict accuracy
- unsupported-fact/fabrication rate
- cross-chapter evidence recovery recall
- reference-recoverable quantities misclassified as calibratable
- downstream-before-upstream violation count
- first defensible anchor iteration count
- invalid tuning cycle count
- paper-ground-truth mutation count
- invalidated-score detection rate after target correction
- Builder/Validator rule-violation detection
- stop-tuning trigger precision/recall
- batch-plan dependency accuracy

A release that cannot detect deliberately planted paper-to-code/model-to-code hallucination cases should not be considered mature even if it reproduces final plots.
