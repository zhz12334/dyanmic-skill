# Validation Exposure and Leakage Control

## Core rule

Withheld validation evidence is independent only until it influences model design, parameter selection, objective design, tolerance choice or calibration strategy.

Create `validation_exposure_log.csv` for every withheld target.

## States

- `WITHHELD_UNSEEN` — not inspected for development decisions.
- `EVALUATED_ONCE` — evaluated after freeze; still valid if no development decision uses the residual pattern.
- `EXPOSED_DEVELOPMENT_EVIDENCE` — used to modify model/parameters/objective/assumptions; no longer independent validation.
- `RETIRED` — no longer eligible as validation.
- `FINAL_HOLDOUT` — reserved for final prediction only.

## Exposure events

Validation becomes development evidence if its result is used to:
- add/remove a physical term;
- alter model structure or BC/IC/excitation interpretation;
- change parameter bounds/types;
- add it or a correlated portion to the calibration objective;
- change metric/weight/tolerance based on observed residuals;
- select among model variants because one matches that validation target better.

Routine bug fixes that are independently demonstrated by formula/unit/runtime tests need not consume validation evidence, but record the event if the validation target was inspected.

## After exposure

1. reclassify the target;
2. version the calibration/validation manifest;
3. choose a new holdout if the paper provides one;
4. rerun from the appropriate gate;
5. if no independent evidence remains, downgrade the final classification to calibration/development-supported reproduction rather than predictive validation.


## Builder / Validator handoff

Before first withheld-validation scoring, freeze `builder_validator_handoff.yaml` as described in `references/builder_validator_separation.md`.

If the Validator reports detailed residuals and the Builder uses them to modify equations, parameters, objectives, assumptions or processing, change the target state to `EXPOSED_DEVELOPMENT_EVIDENCE`. Procedural Builder/Validator separation does not preserve independence after such exposure.
