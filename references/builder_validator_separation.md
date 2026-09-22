# Builder / Validator Separation

## Purpose

Prevent the same development loop from changing a model and then retroactively changing the rules by which that model is judged.

## Builder

May:
- research evidence;
- implement/repair model equations and modules;
- select eligible calibration parameters under the approved plan;
- run development/calibration evidence.

May not, after validation results are inspected:
- mutate frozen paper ground truth;
- change acceptance metrics/tolerances without reopening approval;
- relabel exposed validation as independent.

## Validator

Starts from `builder_validator_handoff.yaml` and frozen artifacts.

May:
- execute a fresh run;
- calculate pre-registered metrics;
- issue `PASS/PARTIAL/FAIL/BLOCKED`;
- report a discrepancy signature.

May not:
- change equations;
- change physical parameters;
- change numerical settings to chase the paper;
- change ground truth;
- change objective/metric/tolerance after seeing results.

## Validation exposure

If the Builder receives detailed residual information and uses it to modify the model, the target becomes `EXPOSED_DEVELOPMENT_EVIDENCE` and cannot remain independent validation.

Procedural separation is required even when Builder and Validator are executed by the same software agent/session.
