# Structural-Dynamics Comparison Metrics

These are metric-design rules, not universal pass/fail limits.

## General principles

1. Compare like with like: response quantity, coordinate, unit, normalization, reference DOF, time/frequency domain, processing convention.
2. Prefer physical features plus curve/field metrics rather than one global score.
3. Account for digitization, experimental, stochastic and numerical uncertainty.
4. Never extrapolate outside common support for scoring.
5. Preserve exact formula/implementation of every metric.
6. A composite objective ranks candidates; it does not erase critical component failures.

## Scalars

Relative error:

`e_rel = abs(y_model-y_ref)/max(abs(y_ref), eps)`

Near zero also report absolute or symmetric error.

## Modes

- per-mode frequency error;
- mean/RMS/max frequency error;
- MAC matrix;
- frequency + MAC mode pairing;
- subspace angle/correlation for repeated modes;
- effective mass/participation error when reported.

## FRFs

- resonance/anti-resonance frequency error;
- peak amplitude error;
- dB magnitude error;
- half-power bandwidth/damping difference;
- log-magnitude NRMSE;
- phase MAE/circular error away from nulls;
- curve correlation/shape error on common grid.

## Time histories

- peak/peak-time;
- RMS/steady-state amplitude;
- RMSE/NRMSE over justified window;
- dominant frequency;
- decay envelope/log decrement;
- cross-correlation and lag for diagnosis;
- energy/integral where meaningful.

Do not silently shift time traces merely to improve final score.

## PSD/ASD

Before metrics verify PSD vs ASD, one-/two-sided convention, Hz vs rad/s, windowing and bandwidth.

Use:
- peak frequency/level;
- log-spectrum distance;
- band-energy error;
- integrated RMS;
- spectral correlation;
- ensemble confidence where stochastic.

## Nonlinear periodic/hysteretic response

Use:
- peak response;
- harmonic content;
- loop area/energy dissipation;
- backbone curve;
- secant/tangent stiffness;
- jump/bifurcation location;
- cycle-level phase/energy features.

## Phase-space and Poincare results

Use distributional/geometric metrics rather than ordered pointwise error:
- occupied area;
- covariance;
- density distance;
- Wasserstein distance;
- Chamfer/Hausdorff distance when robustly defined;
- cluster count/periodicity;
- topological/qualitative class.

## Chaotic results

Long-time trajectory RMSE should normally not be primary. Use:
- spectral distribution;
- amplitude distribution;
- RMS/variance;
- attractor/Poincare geometry;
- bifurcation thresholds;
- Lyapunov/entropy when paper reports them.

## Stochastic/random-surface results

Use ensemble/statistical metrics:
- mean/std/moments;
- empirical distribution distance;
- RMS/Ra/Rq as appropriate;
- PSD;
- autocorrelation/correlation length;
- fractal/statistical descriptors;
- extremes/quantiles.

## Spatial fields

After coordinate registration use:
- field RMSE/NRMSE;
- spatial correlation;
- extrema/location errors;
- gradient errors;
- region-wise/integral errors;
- MAC-like shape metrics where appropriate.

SSIM may be reported only as supplemental when raster image reproduction itself matters.

## Tolerance-normalized composite objective

For component metric `m_i`, target tolerance/uncertainty scale `s_i`:

`r_i = m_i / max(s_i, eps)`

A robust weighted aggregate may be:

`J = sum(w_i * rho(r_i)) / sum(w_i)`

where `rho` is a documented robust loss. Keep every `m_i` visible.

## Uncertainty-aware acceptance

Where independent reference and numerical/digitization uncertainties are available, a combined uncertainty scale may be used. Do not claim exact reproduction beyond the precision of the source evidence.


## RC2: validation-claim type

Before selecting metrics, classify the claim, for example:
- `AMPLITUDE_WAVEFORM`;
- `FREQUENCY_FEATURE`;
- `SIDEBAND_MECHANISM`;
- `TREND_MONOTONICITY`;
- `LOAD_DISTRIBUTION`;
- `TOPOLOGY_ORBIT`;
- `STATISTICAL_INDICATOR`;
- `QUALITATIVE_MECHANISM`.

The metric family must test the paper's actual claim. Do not impose amplitude NRMSE on a source that only claims frequency/sideband agreement.

## Result presentation

Metric computation and result presentation are separate obligations.

Use `references/result_presentation_contract.md`.

For each formal target, preserve:
- frozen paper/source view;
- fresh-run reproduction;
- direct comparison view when meaningful;
- typed component metrics;
- explicit verdict.

A visually convincing plot without typed metrics is not sufficient for PASS.
A strong global metric without physically correct visual/topological features is not sufficient for PASS.
