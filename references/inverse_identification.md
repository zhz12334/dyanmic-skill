# Constrained Inverse Identification Rules

## 1. When inverse identification is appropriate

Use it when the paper's model structure is recoverable but one or more physically meaningful parameters needed for reproduction remain undisclosed or uncertain **after the parameter-source recovery ladder has been executed and documented**.

Appropriate examples:
- joint/support flexibility;
- damping coefficients;
- contact/backlash/friction parameters;
- preload;
- effective boundary stiffness;
- uncertain sensor or actuator calibration where a real gain mechanism exists;
- unreported constitutive parameters in a stated model.

## 2. When it is not appropriate

Do not use optimization to hide:
- equation/formulation errors;
- unit mistakes;
- wrong coordinate or response definition;
- wrong boundary-condition topology;
- wrong force/base-excitation formulation;
- wrong nonlinear law;
- unconverged numerical settings;
- paper/OCR transcription errors.

## 3. Source-recovery prerequisite

Before approving a calibration variable, verify that the parameter source trace has checked:
- target paper/supplement;
- citations attached to the relevant formula/model/parameter;
- upstream references when the cited source imports the value;
- author theses/related papers/model-family publications;
- supplementary non-code data/parameter records where available;
- authoritative standards/manuals/databases when applicable.

A value found only in an analogous study should usually define a prior or bound rather than be frozen as the target paper's value.

If a strong transferable literature value is recovered, reclassify to L and remove it from the optimization set unless uncertainty study is an explicit objective.

## 4. Calibration evidence budget

The number/diversity of calibration observables should support the number of unknowns. A dense curve does not automatically provide thousands of independent constraints because points can be highly correlated.

Prefer complementary observables that excite different physics.

## 5. Objective design

Use physical features and curve metrics normalized by tolerances/uncertainty.

Keep critical component metrics visible even when a composite objective is used.

## 6. Parameter bounds

Bounds must come from physics, literature, geometry, material limits, engineering tolerances, or explicit conservative assumptions.

If the optimum repeatedly hits a bound, classify `BOUND_HIT` and investigate model inadequacy or bound choice.

## 7. Optimizer selection

- low-dimensional smooth: least squares/trust region/L-BFGS-B;
- non-smooth/multimodal: differential evolution/CMA-ES/PSO;
- expensive simulations: DOE/surrogate/Bayesian optimization;
- differentiable models: gradient/adjoint methods if derivatives are trustworthy.

A common robust strategy is global exploration followed by local refinement.

## 8. Multi-start and reproducibility

For nonconvex problems, use multiple starts/seeds and report whether the same basin/parameter region is recovered.

## 9. Identifiability

At minimum examine sensitivity and parameter correlation. For serious inverse problems consider SVD/Jacobian conditioning, Fisher information, profile likelihood, or posterior/ensemble analysis.

High fit + multiple dissimilar parameter sets = curve reproduction may pass while physical identification is non-unique.

## 10. Calibration vs validation

Freeze parameters before validation. Never tune directly on validation outputs without logging exposure, versioning the calibration/validation manifest, and transparently reclassifying those outputs as development/calibration evidence. Follow `references/validation_exposure.md`.

## 11. Parameter truth language

Use wording such as:

"The paper does not disclose this value. The reported value is an equivalent parameter identified in this reproduction from specified calibration targets under stated bounds. It must not be interpreted as the author's original parameter unless independently documented."
