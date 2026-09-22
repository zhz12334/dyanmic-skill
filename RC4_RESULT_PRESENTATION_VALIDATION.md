# v4.0.0-rc4 — Result Presentation Contract

RC4 adds the missing final validation-output layer.

Every formal validation target now combines:
1. frozen paper/source ground truth;
2. fresh-run reproduction;
3. direct comparison view when meaningful;
4. result-type-specific quantitative/feature metrics;
5. explicit PASS/PARTIAL/FAIL/BLOCKED verdict.

State: `VALIDATION_PACKET_COMPLETE`.

Visual similarity alone cannot establish PASS.
A single global metric alone cannot establish PASS.

Result-specific display/metric rules are defined for:
- scalar/table;
- curves;
- time history;
- FFT/spectrum/sidebands;
- orbit/phase portrait;
- Poincare;
- bifurcation;
- stochastic/random response;
- field/contour.

New artifacts:
- `validation_card.md`
- `validation_metrics.csv`
- `validation_packet_manifest.csv`
- `batch_validation_summary.csv`
- `regression_dashboard.csv`

Closed-loop suite extended from 12 to 14 scenarios:
- CL13: incomplete validation packet blocks formal PASS/PARTIAL;
- CL14: metric-family mismatch is rejected before verdict.

Fresh-run return code: 0
Executed cases: 14/14
Static lint: PASS

Release status: RC4 remains a release candidate. The remaining gate is behavioral conformance in fresh sessions, not more paper reproduction.
