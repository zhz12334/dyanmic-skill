# v4.0.0-rc1 Static / Design Validation Summary

## Scope

This RC is an incremental orchestration upgrade of v3.3.0, not a rewrite.

## Preserved v3.3 core

Verified present after patch:
- M1/M2 and transition semantics;
- claim/evidence architecture;
- parameter/source provenance;
- formula fidelity and hallucination audit;
- model/solver fidelity;
- calibration/validation exposure control;
- identifiability/UQ/VVUQ;
- Python-first / MATLAB parity;
- run provenance / clean-room rerun.

## New orchestration layer

Verified added:
- whole-paper/cross-chapter gate;
- reference-closure status/gate;
- model dependency DAG;
- figure dependency / anchor roles;
- batch planner;
- ground-truth manifest/freeze;
- Builder/Validator handoff;
- stop-tuning/evidence-review decision.

## Bearing failure-replay expectations

The new workflow should block or invalidate the historical failure modes:
1. scoring before authoritative paper target freeze;
2. surrogate/processed targets being relabeled as paper curves;
3. parameter identification before whole-paper/reference closure;
4. prolonged tuning after persistent pressure/film structural mismatch;
5. downstream fitting while upstream model interpretation remains open;
6. builder self-scoring without a frozen handoff;
7. target correction without automatic old-score invalidation.

## Rotor desktop-benchmark expectations

The new workflow should:
- read all chapters before marking parameters missing;
- trace Hertz exponent/fatigue life/crack-opening rules through their cited references;
- reproduce Chapter-2 bearing foundation before Chapter-3/4 fault dynamics;
- select high-information model-validation anchors before broad parameter sweeps;
- treat source inconsistencies as explicit evidence conflicts, not silent corrections.

## RC status

`READY_FOR_PROCESS_BENCHMARK`, not `FINAL_V4_RELEASE`.

Required before final v4.0.0:
1. bearing failure replay;
2. rotor desktop dependency/batch benchmark;
3. gear-domain regression benchmark;
4. revise any rule that overfits one domain or creates unnecessary process burden.
