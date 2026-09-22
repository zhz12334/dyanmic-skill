# Calibration, Validation and Exposure Strategy

## Core rule
Calibration demonstrates that unknown parameters can be chosen to match selected evidence. Validation tests whether the accepted model predicts evidence not used in fitting **or in development decisions**.

Use `references/validation_exposure.md` and `validation_exposure_log.csv`.

## Preferred withholding dimensions

1. Different figure/panel.
2. Different operating speed/frequency/load.
3. Different forcing amplitude.
4. Different mode range.
5. Different measurement location/channel.
6. Different specimen/experiment.
7. Different time/frequency region only when the physics supports such partitioning.

Prefer holdouts that are physically distinct, not merely resampled points from the same curve.

## Weak validation patterns

- random points from the same smooth curve when all are strongly correlated;
- fitting a figure and validating on the same figure after resampling;
- tuning using every operating condition and then calling those same conditions validation;
- changing the model after inspecting a validation residual and continuing to call the same target independent validation.

## Validation exposure

If a withheld target influences model structure, parameter choices/bounds, objective design, tolerance choice, calibration membership or model-variant selection, reclassify it as `EXPOSED_DEVELOPMENT_EVIDENCE`.

Choose a new holdout when possible. If none remains, downgrade the final claim.

## No independent validation available

If the publication exposes only enough information for calibration/development:
- say independent validation is unavailable;
- classify the result as calibration-only or development-supported reproduction rather than predictive validation;
- strengthen sensitivity/identifiability/robustness checks;
- do not overstate predictive capability.

## Validation failure

Do not immediately add validation outputs to the objective. Diagnose first. If redesigning calibration is necessary, version the manifest, log exposure, obtain plan/repair approval when required, and rerun transparently.

## Validation packet completion

After the Validator scores a target, create the formal Validation Packet defined in `references/result_presentation_contract.md`.

A target may not be finalized as PASS/PARTIAL until:
- its frozen source target is identified;
- the fresh-run result is bound to run provenance;
- result-type-appropriate visual/comparison evidence is exported;
- typed metrics are recorded;
- the acceptance rule and verdict are explicit.

Set `VALIDATION_PACKET_COMPLETE`.
