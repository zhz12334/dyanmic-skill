# Pre-Implementation Reproducibility Probability Assessment

## Purpose

After theory/formula/model/parameter provenance and same-author/group cross-evidence are closed enough for planning, estimate the probability that the active reproduction mode can reproduce the critical claims to the preregistered fidelity level.

This estimate must be presented **before full implementation** so the user can decide whether to proceed, gather more evidence, narrow the target, or accept a higher-risk reconstruction.

## Important interpretation

The reported value is an **evidence-based engineering forecast / subjective probability**, not an empirically calibrated frequentist probability and not a guarantee. Do not imply statistical calibration unless the skill has later been calibrated on a benchmark corpus.

Avoid false precision. Prefer integer percentages or 5% increments, plus a plausible interval.

## Required output

Report at least:

- active mode: M1 or M2;
- central estimated reproducibility probability (0–100%);
- plausible low/high range;
- evidence-confidence level (`HIGH`, `MEDIUM`, `LOW`);
- factor table with low/base/high ratings and weights;
- hard caps/blocks applied;
- strongest positive evidence;
- dominant failure risks;
- unresolved items most likely to dominate error;
- additional evidence/actions most likely to increase probability;
- whether the planned task should proceed as full reproduction, evidence-gap closure, partial reproduction, or high-risk reconstruction.

## Default factor model

Each factor is scored in [0,1] using low/base/high judgments. Default weights sum to 1.0:

| Factor | Weight | What to assess |
|---|---:|---|
| Theory/formula closure and consistency | 0.16 | governing equations, algorithms, transformations, source conflicts |
| Parameter closure and provenance | 0.16 | claim-critical values/ranges, units, source strength, unresolved parameters |
| Model structure / BC / IC / loads / damping completeness | 0.14 | physical implementation obligations and hidden model-form uncertainty |
| Same-author/same-group cross-evidence convergence | 0.12 | corroboration, inheritance, conflicts, model-family continuity |
| Numerical/solver/protocol completeness | 0.10 | integration, mesh, solver, convergence, experimental/ML protocol details |
| Target-data extractability and ground-truth quality | 0.08 | tables/raw values/vector figures/digitization uncertainty |
| Identifiability / calibration burden | 0.08 | number/sensitivity/correlation of missing parameters, M2 burden |
| Independent validation evidence availability | 0.06 | withheld operating cases, experiments, alternative metrics |
| Evidence consistency / unresolved-conflict risk | 0.05 | contradictions, OCR ambiguity, incompatible source variants |
| Computational/experimental tractability | 0.05 | cost, stiffness, chaos, stochastic burden, unavailable hardware/solver constraints |

If a factor is not applicable, redistribute its weight transparently; never silently delete it.

## Calculation

For factor i with weight w_i and low/base/high score s_i:

- `P_low_raw = 100 * sum(w_i * s_i_low)`
- `P_base_raw = 100 * sum(w_i * s_i_base)`
- `P_high_raw = 100 * sum(w_i * s_i_high)`

Then apply any documented hard cap to all three values. Round conservatively.

The interval is not a confidence interval in the statistical sense; it is a scenario/plausibility range reflecting evidence uncertainty.

## Suggested scoring anchors

- 1.00 — strong, directly evidenced, internally consistent, low residual ambiguity;
- 0.80 — mostly complete, minor noncritical ambiguity;
- 0.60 — usable but important uncertainty remains;
- 0.40 — substantial missing/ambiguous evidence likely to affect results;
- 0.20 — weak evidence, large reconstruction burden;
- 0.00 — unavailable/contradictory/blocking.

## Default hard caps

These are conservative defaults, not physical laws. If changed, document why.

- unresolved claim-critical governing equation / active algorithm / BC semantics -> maximum 35%;
- unresolved claim-critical physical parameter that is both influential and non-identifiable -> maximum 40%;
- unresolved source conflict that changes governing physics/model branch -> maximum 50%;
- paper target cannot be quantitatively extracted and no defensible feature-level target exists -> maximum 55%;
- M2 requires several strongly correlated claim-critical parameters with poor identifiability -> maximum 60%;
- no genuinely independent validation evidence remains -> maximum 80% for a full predictive-reproduction claim (calibration reproduction may still be higher under its narrower claim).

A hard **block** may be preferable to a cap when implementation would be scientifically meaningless.

## Mode interpretation

### M1
Probability concerns whether the critical claims can be reproduced from disclosed/recoverable scientific evidence without fitting omitted claim-critical physical parameters to target outputs.

### M2
Probability concerns whether a traceable calibrated reconstruction can reproduce and validate the critical claims under bounded assumptions. Identifiability and validation evidence should materially affect the estimate.

## User-facing format

Use a compact statement such as:

> Estimated reproducibility probability (M1): **75%**, plausible range **60–85%**. Evidence confidence: **MEDIUM**. Main strengths: governing equations and geometry are closed; three same-group papers corroborate damping/model definitions. Main risks: one contact parameter is only bounded, Figure 7 digitization uncertainty is high, and only one withheld operating condition remains.

Then show the factor table and any caps.

## Probability update discipline

The pre-implementation probability must be frozen and preserved. After implementation, the final report may compare forecast vs outcome but must not retroactively rewrite the original estimate.

If major new evidence is discovered before coding, create a **new version** of the assessment and show both old and new values with the evidence change that caused the update.

## Skill calibration over time

If the skill is later benchmarked across many papers, archive forecast/outcome pairs and calibrate the probability model empirically. Until then, label the probability as an engineering forecast.
