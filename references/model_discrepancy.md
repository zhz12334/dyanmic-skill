# Model Discrepancy Budget

Treat observed mismatch as multiple components, not a single parameter-fitting residual.

Conceptual decomposition:

`y_paper = y_model(theta) + delta_model + eps_measurement + eps_digitization + eps_stochastic + eps_numerical + eps_rounding`

## Rules
- estimate/bound components when possible;
- keep numerical error from convergence studies;
- retain digitization uncertainty;
- use experimental repeatability/coherence/noise information;
- use ensemble uncertainty for stochastic outputs;
- do not let calibrated parameters absorb known systematic model-form errors without explicit model-discrepancy treatment.
