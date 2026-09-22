# Discrepancy Diagnosis and Correction Strategy

This guide ranks hypotheses; it does not prove causality.

## Universal first checks

Before calibrating parameters, check in order:
1. paper/source transcription and OCR;
2. unit and coordinate conventions;
3. response/output definition;
4. equation/model-form consistency;
5. boundary/load/initial-condition interpretation;
6. numerical convergence;
7. postprocessing/normalization;
8. only then uncertain physical parameters.

## Modal signatures

### All frequencies shifted by similar ratio
Check unit, mass/density, stiffness scale, dimensions, global BC, added mass. Use `f ~ sqrt(k/m)` scaling diagnostically before tuning.

### Low modes match, high modes drift
Check theory choice, rotary inertia/shear deformation, mesh/order, mass formulation, local detail and truncation.

### Isolated mode mismatch
Check mode pairing, local joint stiffness/mass, symmetry breaking, sensor/DOF mapping and repeated modes.

## FRF signatures

### Resonance location correct, peak wrong
Check damping, force normalization, FRF definition, participation and excitation/response DOFs.

### Constant magnitude scale error
Check units, gain/calibration, displacement/velocity/acceleration conversion and spectral convention.

### Resonance locations shifted
Check mass/stiffness/BC before damping.

### Anti-resonance mismatch
Check DOF placement, residues, omitted modes/static correction and local connection modeling.

## Time-history signatures

### Period correct, decay wrong
Check damping mapping.

### Constant time/phase offset
Check trigger/time origin, initial condition, load start, processing delay and phase convention.

### Correct timing, wrong amplitude
Check input amplitude, response coordinate, damping and nonlinear parameters.

### Drift/instability
Check integrator, timestep, rigid modes, baseline correction and numerical damping.

## PSD signatures

### Shape correct, RMS scale wrong
Check PSD/ASD, one-/two-sided, Hz/rad/s, bandwidth and calibration.

### Peaks shifted
Check structural mass/stiffness/BC.

### Broadband slope wrong
Check excitation PSD/filtering, damping frequency dependence and preprocessing.

## Nonlinear signatures

### Small-amplitude match, large-amplitude divergence
Check nonlinear stiffness/contact/material law/amplitude-dependent damping.

### Backbone close, hysteresis width wrong
Check dissipation/hysteretic parameters before elastic stiffness.

### Jump/bifurcation location wrong
Check nonlinear coefficients, forcing amplitude, sweep/continuation protocol.

## Chaotic/phase-space signatures

### Pointwise trajectories diverge but spectra/attractor statistics agree
Do not force trajectory matching; treat as potentially successful invariant reproduction.

### Attractor size/energy wrong but topology similar
Check excitation scale, damping, nonlinear coefficients and normalization.

### Poincare periodicity class differs
Check sampling phase, forcing period definition, transient discard length, integration accuracy, parameter regime and model form.

## Stochastic signatures

### One realization differs but statistical moments/PSD agree
Do not tune the seed. Treat as expected realization variability.

### Distribution/PSD consistently shifted
Check stochastic process definition, mapping, scale parameter, correlation structure and sampling bandwidth.

## Calibration-related signatures

### Excellent calibration, poor validation
Suspect overfitting, missing operating-condition dependence, wrong model form, non-identifiability or calibration targets that are not sufficiently informative.

### Multiple parameter sets yield same score
Classify non-unique. Add complementary evidence or reduce C parameter set.

### Optimum hits bounds
Check bounds, parameter sensitivity and model-form inadequacy; do not silently widen bounds without evidence.

## Iteration decision template

- Observed signature:
- Magnitude:
- Result type:
- Top hypothesis 1/evidence:
- Top hypothesis 2/evidence:
- Top hypothesis 3/evidence:
- Discriminating test:
- Allowed factor group:
- Expected effect:
- Rollback condition:
- Verification checks to rerun:
- Calibration required again? Yes/No
- Validation metrics to rerun:


## Persistent residual / stop-tuning rule

A stable, structured residual that survives legitimate solver changes and scientifically meaningful parameter tests is evidence about the model/evidence, not permission for unlimited fitting.

Track:
- primary error improvement ratio;
- regression damage to frozen anchors;
- parameter-bound pressure;
- whether a numerical setting is being abused as a fitting knob;
- whether independent numerical backends retain the same residual signature.

When an approved trigger fires, use `references/stop_tuning_evidence_review.md` and enter `STOP_TUNING -> EVIDENCE_REVIEW` before any further calibration.
