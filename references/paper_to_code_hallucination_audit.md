# Paper-to-Code Hallucination Audit

## Purpose
Detect common LLM-generated reproduction failures where the code sounds plausible but does not implement the paper faithfully.

## Mandatory audit categories

### `MISSING_EQUATION`
A required paper/source-lineage equation or operative rule has no faithful implementation.

### `EXTRA_UNSOURCED_TERM`
A claim-relevant term, force, damping component, regularizer, nonlinear term, correction factor, or heuristic appears in code without an allowed source/variant declaration.

### `UNAUTHORIZED_SIMPLIFICATION`
The model was simplified beyond what the paper/source/approved verification branch permits.

### `PARAMETER_INVENTION`
A value is presented as paper-used/published although it is actually assumed, literature-prior, inferred, or calibrated.

### `WRONG_EQUATION_MAPPING`
A code symbol is claimed to implement an equation but represents a different mathematical quantity or convention.

### `DISCONNECTED_IMPLEMENTATION`
The equation exists in code but is not on the runtime path that generates the reproduced result.

### `UNIT_MISMATCH`
Implementation units differ from the paper/model without an explicit conversion.

### `SIGN_OR_COORDINATE_ERROR`
Sign, direction, coordinate, phase, or reference-frame conventions drift from the paper.

### `INDEX_OR_DOF_ERROR`
Mode, node, DOF, channel, component, or tensor indexing is inconsistent with the paper.

### `BOUNDARY_CONDITION_DRIFT`
Supports/constraints/periodicity/interface conditions differ from the selected faithful model.

### `INITIAL_CONDITION_DRIFT`
Initial state is changed silently or chosen by tuning rather than registered assumption/source.

### `SOLVER_SUBSTITUTION_DRIFT`
A different solver/integration/eigensolver method changes the scientific behavior without verification/equivalence evidence.

### `POSTPROCESSING_DRIFT`
Scaling, normalization, filtering, windowing, coordinate transform, spectral convention, averaging, or metric differs silently.

### `METRIC_DRIFT`
The code optimizes/scores a different quantity from the paper claim or frozen objective.

### `DEAD_OR_SHADOWED_FORMULA`
The intended equation is overridden by a constant, default, alternative branch, cache, surrogate, or stale intermediate.

### `PAPER_CORRECTION_NOT_DISCLOSED`
The implementation silently fixes a suspected paper typo/bug instead of separating a corrected/interpreted variant.

### `CLAIM_SCOPE_DRIFT`
A result generated from a simplified/alternate model is presented as reproducing a stronger paper claim than it actually supports.

## Audit procedure
1. Compare Equation Registry to the Implementation Contract.
2. Compare each critical equation to code traceability.
3. Inspect dependency/runtime evidence.
4. Check parameters and source types against code/config values.
5. Check BC/IC/excitation/damping and units.
6. Check solver and post-processing protocols.
7. Search for constants/terms not represented in the contract.
8. Run equation-level and integration tests.
9. Run controlled ablations/perturbations for critical submodels.
10. Record every finding in `hallucination_audit.csv` with severity and closure evidence.

## Severity
- `P0`: fabricated/scientifically invalid implementation or result provenance; stop immediately.
- `P1`: critical claim can change materially; must close before scoring reproduction.
- `P2`: traceability/documentation weakness unlikely to change current conclusion but must be recorded.

## Closure rule
A finding is closed only by code/test/evidence change or an explicit scientifically justified scope downgrade. Natural-language reassurance alone does not close a finding.
