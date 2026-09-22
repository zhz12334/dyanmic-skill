# Formula-to-Code Fidelity Framework

## Purpose
Prevent paper-reproduction code from drifting away from the mathematics actually stated, derived, or legitimately recovered from the paper and its source lineage.

A visually similar result is not evidence of faithful reproduction if required equations, terms, boundary conditions, transformations, or post-processing definitions were omitted, replaced, or silently simplified.

## 1. Mandatory Equation / Algorithm Registry
Every numbered equation and every unnumbered operative mathematical rule that can affect a reproduced claim must be triaged. No equation may disappear silently.

Recommended fields:
- equation_id
- paper_location
- source_scope (`PAPER`, `SUPPLEMENT`, `CITED_SOURCE`, `AUTHOR_CLARIFICATION`, `INTERPRETED_VARIANT`)
- faithful_expression_or_description
- role
- variables_and_units
- claim_ids
- implementation_required
- implementation_status
- omission_or_equivalence_reason
- dependency_ids
- variant (`PAPER_FAITHFUL`, `CORRECTED_INTERPRETATION`, `REFERENCE_ONLY`)

Recommended roles:
- `GOVERNING`
- `KINEMATIC`
- `CONSTITUTIVE`
- `BOUNDARY`
- `INITIAL_CONDITION`
- `EXCITATION`
- `DAMPING`
- `CONTACT_OR_NONLINEARITY`
- `TRANSFORMATION_OR_NONDIMENSIONALIZATION`
- `DISCRETIZATION_OR_REDUCTION`
- `ALGORITHM_STEP`
- `POSTPROCESSING`
- `METRIC_OR_OBJECTIVE`
- `AUXILIARY_DERIVATION`
- `BACKGROUND_OR_ALTERNATIVE`

Implementation status:
- `IMPLEMENTED_DIRECT`
- `IMPLEMENTED_DERIVED_EQUIVALENT`
- `DOCUMENT_ONLY_NOT_ON_ACTIVE_BRANCH`
- `AMBIGUOUS`
- `BLOCKED`
- `NOT_APPLICABLE_TO_SELECTED_CLAIM`

`DOCUMENT_ONLY_NOT_ON_ACTIVE_BRANCH` or `NOT_APPLICABLE_TO_SELECTED_CLAIM` requires an explicit scientific reason. "Not needed" without a claim/dependency explanation is insufficient.

## 2. Critical Formula Coverage Gate
For equations classified as governing, constitutive, kinematic, BC/IC, excitation, damping, contact/nonlinearity, active transformations, active algorithm steps, or active post-processing definitions:

**required coverage = 100%**

Coverage means either:
1. direct faithful implementation, or
2. documented mathematical equivalence with derivation/tests.

A weighted fidelity score may be reported for diagnostics, but it must never override a missing critical formula hard failure.

## 3. Equation Dependency Graph
Construct an executable dependency graph such as:

`roughness model -> transmission error -> excitation -> governing ODE -> integrator -> response -> spectrum -> paper claim`

For each required equation confirm that its output reaches the claim-relevant computation path. A function that exists in source code but is never called is not implemented for reproduction purposes.

Possible dependency findings:
- `CONNECTED_ACTIVE`
- `CONNECTED_ONLY_IN_TEST`
- `DISCONNECTED_FORMULA`
- `SHADOWED_BY_CONSTANT_OR_DEFAULT`
- `BYPASSED_BY_ALTERNATE_BRANCH`
- `UNKNOWN_RUNTIME_PATH`

## 4. Formula-to-Code Traceability
Every critical equation must map to:
- file/module;
- function/class;
- code location or stable symbol;
- input/output variables;
- unit/sign convention;
- unit test(s);
- integration/runtime-path test(s);
- associated claim IDs.

Do not accept a natural-language assertion such as "Eq. (7) is implemented" without code and test evidence.

## 5. Equation-level Tests
Generate tests from mathematical properties, not merely final plot similarity.

Typical test types:
- exact special-point tests;
- branch/boundary tests for piecewise laws;
- zero-input / limiting-case tests;
- symmetry / reciprocity tests when applicable;
- dimensional and shape tests;
- periodicity tests;
- conservation/equilibrium checks;
- known analytical solution checks;
- coordinate/sign transformation checks;
- nondimensionalization round-trip checks;
- perturbation/sensitivity checks showing that an active term actually influences downstream results where physics predicts it should.

## 6. Unauthorized Simplification Rule
The implementation must not silently:
- remove nonlinear terms;
- replace time-varying coefficients by means/constants;
- drop coupling terms;
- linearize a paper-nonlinear model;
- omit damping/contact/friction/backlash/history effects;
- replace BCs or base excitation with a more convenient forcing form;
- change solver or post-processing definitions in a claim-relevant way;
- set a paper-defined stochastic/process term to zero;
- collapse multi-DOF dynamics without an approved reduced-model derivation.

A simplification is allowed only if it is:
1. explicitly in the target paper;
2. recovered from an accepted source in the model lineage;
3. used only for verification/benchmarking and excluded from final paper-claim scoring; or
4. explicitly approved as a new model variant, with affected claims separated.

Otherwise classify it `UNAUTHORIZED_MODEL_SIMPLIFICATION` and fail the fidelity gate.

## 7. Mathematical Equivalence Rule
An alternative form (e.g. second-order ODE -> first-order state-space) is allowed only when equivalence is documented.

Minimum evidence:
- mapping between paper variables and implementation state;
- derivation or symbolic/numerical equivalence argument;
- initial/boundary-condition mapping;
- unit/sign convention mapping;
- equivalence test on representative inputs.

Status is then `IMPLEMENTED_DERIVED_EQUIVALENT`, not simply `IMPLEMENTED_DIRECT`.

## 8. Source-faithful vs Corrected/Interpreted Variants
If a paper equation appears inconsistent, dimensionally invalid, typographically corrupted, or incompatible with its own preceding derivation, do not silently repair it.

Create distinct variants:
- `PAPER_FAITHFUL`: implementation of the published/recoverable expression as faithfully as possible;
- `CORRECTED_INTERPRETATION`: a separately justified interpretation/repair;
- optionally `SOURCE_LINEAGE_VARIANT`: form recovered from the cited original source.

Compare variants against analytical checks and published results. Report which variant reproduces which claims. Never rewrite the paper retroactively.

## 9. Runtime Coverage
Static code presence is insufficient. Demonstrate claim-relevant runtime use by one or more of:
- call-path instrumentation;
- coverage traces;
- dependency injection checks;
- controlled term perturbation/ablation;
- mock/assertion that the expected submodel is called;
- output-sensitivity tests.

If removing or perturbing a supposedly critical term leaves all dependent outputs unchanged, investigate whether the term is disconnected, shadowed, numerically negligible, or the dependency graph is wrong.

## 10. Fidelity Verdict
At minimum report:
- critical formula count;
- critical formulas faithfully/equivalently implemented;
- critical formulas blocked/ambiguous;
- unauthorized simplifications;
- disconnected formulas;
- unsourced extra terms;
- equation-level test pass rate;
- runtime coverage status.

Hard `NO-GO` conditions include:
- any omitted critical equation without justified branch exclusion;
- any unauthorized model simplification;
- any unsourced claim-relevant term intentionally added to make results fit;
- unresolved sign/unit/BC/IC drift affecting a critical claim;
- critical formula implemented only as dead/disconnected code.
