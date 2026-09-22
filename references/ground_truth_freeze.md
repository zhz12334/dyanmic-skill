# Immutable Paper Ground-Truth Freeze

## Purpose

Prevent processed, smoothed, interpolated, manually adjusted or surrogate curves from silently replacing the paper evidence.

## Target namespaces

Use explicit namespaces:
- `paper_raw_*` — authoritative extraction directly from text/table/vector/raster/manual evidence;
- `paper_processed_*` — transparent resampling/transformation derived from a raw paper target;
- `surrogate_*` — fitted/ROM/interpolated engineering targets; never label these as paper data.

## Manifest

Create `paper_ground_truth_manifest.csv` and record at minimum:
- figure/table/panel/series;
- source page;
- raw extraction file and hash;
- extraction method/version;
- axis calibration and units;
- estimated uncertainty;
- processed derivatives;
- freeze version/status.

## Freeze rule

After `GROUND_TRUTH_FROZEN`:
- raw targets are immutable;
- comparison code must refer to target IDs/version, not a mutable filename alias;
- smoothing/interpolation may only create a processed derivative;
- surrogate targets cannot be used as paper evidence.

## Correction rule

If the extraction is later found wrong:
1. preserve the old version for audit;
2. create a new ground-truth version;
3. document why the target changed;
4. invalidate all affected old metrics, PASS/FAIL decisions and optimization objectives;
5. rerun the affected baseline/calibration/validation/regression chain.


## RC2: evidence-origin class

Every ground-truth target must record one of:
- `TARGET_PAPER_DIRECT_DATA`;
- `TARGET_PAPER_DIGITIZED_FIGURE`;
- `CITED_EXTERNAL_VALIDATION_DATA`;
- `EXTERNAL_AUTHORITATIVE_BENCHMARK`;
- `PROCESSED_DERIVATIVE` (never authoritative raw evidence).

For `CITED_EXTERNAL_VALIDATION_DATA`, preserve both the target-paper location and the original cited source/protocol.

## RC2: comparison protocol

The manifest must freeze any target-specific coordinate/numbering/sign/sensor/preprocessing convention. A comparison transform must be explicit and versioned; it may not be introduced after seeing residuals.

## State-machine invalidation back-edge

If a frozen target is corrected, set the affected comparison state back to `G11/G12`:
1. increment target/extraction version;
2. invalidate old metrics, objectives and PASS/FAIL decisions;
3. identify affected claims/batches through the figure/model dependency graph;
4. rerun baseline/comparison and all dependent regression targets.

No old score survives a ground-truth version change unless it is recomputed against the new frozen target.
