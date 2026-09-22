# Source-Faithful and Corrected Variant Policy

## Why variants are needed
Published structural-dynamics papers may contain OCR errors, typographical errors, ambiguous signs, incomplete nondimensionalization, inconsistent notation, or equations that conflict with a cited source or later derivation. Reproduction must distinguish what was published from what the reproducer believes is correct.

## Variant types

### `PAPER_FAITHFUL`
Implements the target paper/supplement as written or as conservatively reconstructed from its own notation.

### `SOURCE_LINEAGE_VARIANT`
Implements the formulation recovered from the cited original source when the target paper appears to have abbreviated or corrupted it.

### `CORRECTED_INTERPRETATION`
Implements a separately justified correction/interpretation proposed by the reproducer.

### `VERIFICATION_SIMPLIFICATION`
A reduced/linearized/minimal model used only for verification; it must never be scored as the full paper reproduction unless the paper claim itself uses that model.

## Rules
1. Never silently replace `PAPER_FAITHFUL` by a corrected variant.
2. Each variant gets a separate ID, equation mapping, tests, and results.
3. Calibration parameters are not automatically transferable between variants.
4. Claim verdicts must state the variant used.
5. If only the corrected variant matches the published result, report that fact explicitly; do not claim the paper equation itself was reproduced.
6. If the paper-faithful branch is impossible because the expression is incomplete, mark the exact gap and do not fabricate missing algebra.
