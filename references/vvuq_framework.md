# VVUQ Framework

## Code verification
Are the intended equations/algorithms implemented correctly? Use unit tests, limiting cases, manufactured/analytical solutions, and cross-implementation checks.

## Solution verification
How large is numerical error? Establish mesh, timestep, frequency-step, modal-truncation and solver-tolerance convergence.

## Model validation
Does the mathematical model reproduce independent paper/experimental evidence within stated uncertainty?

## Calibration
Estimate approved missing physical parameters using calibration-only evidence. Calibration is not validation.

## Uncertainty quantification
Represent uncertainty from parameters, measurements, digitization, stochastic inputs, model form and numerical approximation where material. Prefer intervals/posteriors over false precision.

## Prediction
Evaluate frozen parameters/model on withheld conditions, specimens, modes, bands, figures or experiments.
