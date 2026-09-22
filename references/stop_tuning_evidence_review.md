# Stop-Tuning and Evidence-Review Policy

## Purpose

Prevent long curve-fitting loops when the dominant error is missing/ambiguous evidence, model form or algorithm semantics rather than an eligible physical parameter.

## Default trigger

Enter `STOP_TUNING` when any approved trigger fires. Recommended default triggers:
- two scientifically meaningful repair iterations produce <10% improvement in the frozen primary error;
- improvement in one target materially damages frozen anchors/regression targets;
- physical calibration parameters repeatedly hit implausible/prior bounds;
- numerical settings are being adjusted to improve figure agreement instead of convergence;
- independent legitimate solver/backends retain the same structured residual;
- residual topology strongly indicates a missing model/evidence item.

The 10% threshold is a configurable engineering heuristic, not a universal law. Freeze any alternative threshold before viewing the relevant residuals.

## Evidence-review order

When triggered, review:
1. target-paper cross-chapter evidence;
2. direct citation context;
3. cited source and upstream lineage;
4. original variable/parameter definitions;
5. units, scales, coordinate and nondimensional conventions;
6. model/constitutive/contact/excitation semantics;
7. numerical algorithm semantics and boundary/initial treatment;
8. explicit source-faithful variants.

Only after this review may parameter identification reopen.

## Required output

Create `stop_tuning_decision.csv` with improvement, regression damage, bound pressure, numerical-knob pressure, multi-solver residual evidence, decision and next evidence branch.

## Exit rules from EVIDENCE_REVIEW

`EVIDENCE_REVIEW` is not an open-ended research loop. It must exit through one of:

- `REOPEN_WITH_NEW_EVIDENCE`: recovered evidence changes a formula, parameter, model, unit, boundary condition or numerical-algorithm contract; reopen the affected upstream gate and rerun dependency regression.
- `APPROVED_M2_TRANSITION`: evidence remains incomplete, but a bounded/physically defensible calibration plan is explicitly approved; resume through G14.
- `ROLLBACK_AND_RETRY`: a candidate repair damaged frozen anchors; restore the last accepted Builder baseline and test a different evidence-based hypothesis.
- `TERMINAL_BLOCKED`: evidence remains insufficient/inconsistent and no defensible M2 route exists; terminate the affected claim at G25 as `BLOCKED` / `Not reproducible from disclosed/recoverable information`.

Never return from `EVIDENCE_REVIEW` to parameter tuning merely because the target still mismatches.
