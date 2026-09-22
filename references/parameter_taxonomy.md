# Parameter Provenance and Calibration Taxonomy

Every parameter or numerical setting must receive exactly one primary type.

## P — Paper-fixed
Explicitly supplied by the paper/supplement/non-code released data for the reproduced case.

Default rule: freeze. Do not optimize merely to improve agreement.

## T — Theory-derived
Determined from a stated theoretical relationship using fixed inputs.

Default rule: derive transparently and freeze. If alternative conventions exist, resolve the convention before calibration.

## L — Literature-completed
Missing in the target paper but defensibly recovered through a documented source lineage: citation-attached references, upstream method/source papers, author theses/related papers, supplementary non-code data, standards/manuals, or other authoritative directly transferable material.

Default rule: treat as sourced, not as a free fitting knob. Sensitivity may still be studied. A value is not type L merely because a similar paper used it. It must pass the Literature Transferability Gate in `parameter_source_recovery.md`.

Recommended literature roles:
- `L_DIRECT`: the target paper explicitly points to the source for this parameter/model choice and the value/definition is recoverable;
- `L_LINEAGE`: recovered from a clearly continuous author/model/reference lineage with compatible definition and conditions;
- `L_DERIVED`: source gives an equation/relationship from which the value is transparently derived.

Values from analogous but non-equivalent studies are **not** L by default; classify their use as `PRIOR_OR_BOUND_ONLY` for an H/C parameter.

## C — Calibratable missing physical parameter
A genuinely missing/uncertain physical/model parameter that remains after reasonable source recovery—including citation-lineage tracing, author-related literature, supplementary non-code data, standards/manuals, and transferable literature search—and is eligible for inverse identification.

Requirements:
- physical meaning is clear;
- bounds/prior are defensible;
- target outputs are sensitive to it;
- it is not compensating for known model-form error;
- calibration evidence is sufficient relative to parameter dimension.

Examples can include joint stiffness, equivalent boundary flexibility, damping parameters, contact coefficients, unreported preload, or uncertain material property only when the paper does not fix them.

## N — Numerical setting
Mesh size, time step, solver tolerance, FFT length, frequency step, quadrature order, integration tolerance, iteration tolerance, etc.

Rule: determine through numerical verification/convergence. Never fit N settings to paper curves.

## R — Random/nuisance variable
Random seed, realization, noise draw, initial random phase, stochastic field realization, and other variables whose individual value is not a stable physical parameter.

Rule: prefer ensemble/statistical treatment. Do not claim an optimized seed as physical identification.

## H — Reproduction hypothesis
An explicit modeling assumption introduced because disclosure is incomplete and external evidence is insufficient.

Examples: zero initial displacement, assumed sensor orientation, assumed load start phase, mapping between a spatial stochastic profile and time.

H may later become:
- L if a source is found;
- C if it is a physical uncertain parameter suitable for calibration;
- accepted uncertainty if not identifiable;
- blocking if it can reverse the conclusion.

## Promotion rule H -> C
Only promote a hypothesis to calibratable status after model structure is frozen and a sensitivity/identifiability rationale exists.

## Reporting rule
Always distinguish:
- published parameter;
- sourced completion;
- provisional assumption;
- calibrated equivalent parameter.
