# Figure / Result Dependency and Batch Planning

## Purpose

Reproduce long theses by minimal physical validation units, not by consecutive figure number.

## Result roles

A result may be classified as:
- `ANCHOR` — high-information target used to establish a model module;
- `SATELLITE` — downstream/derived target tested after its anchor passes;
- `REGRESSION_ONLY` — previously accepted target rerun to prevent drift;
- `CALIBRATION_CANDIDATE`;
- `VALIDATION_CANDIDATE`.

## Anchor selection

Select anchors using:
- direct relation to upstream physics;
- observability/sensitivity;
- low ambiguity;
- quantitative data quality;
- analytic/scalar/frequency checkpoints;
- ability to discriminate competing model interpretations.

Do not hard-code a fixed number of anchors.

## Batch rule

Default: introduce no more than one new physical mechanism per batch unless the source paper inseparably couples multiple mechanisms.

Useful default sizes (configurable):
- new mechanism: 1–3 high-information results;
- same-model parameter sweep: 3–6 results;
- derived quantities: 4–8 results;
- time/FFT/orbit/Poincare from one state solution: one grouped validation unit.

## Batch contents

Each batch records:
- prerequisites;
- model modules;
- new physical mechanism;
- anchor results;
- satellite results;
- regression results;
- calibration/validation roles;
- acceptance gate;
- expected artifacts.

## Hard rule

Do not tune a satellite while its upstream anchor is failing.


## RC2: publication location vs validation target

Track separately:
- `introduced_by_modules` — modules needed to generate the result as published;
- `validates_modules` — upstream modules the evidence can constrain/validate.

A healthy curve embedded in a later fault chapter may be used as an upstream anchor without enabling the fault model. Do not equate chapter order with module order.

## RC2: result/evidence class

Distinguish at least `METHOD_SCHEMATIC`, `MODEL_RESULT`, `PARAMETER_SWEEP`, `EXPERIMENT_SETUP`, `VALIDATION_ANCHOR`, and `BORROWED_VALIDATION`. Schematics are not numerical targets.

## RC2: per-target comparison protocol

Freeze numbering direction, coordinate frame, sign convention, sensor axis, normalization, preprocessing and unit transform in the figure/result registry before scoring.
