# Figure and Curve Digitization Protocol

## Objective

Convert paper-only plots into traceable machine-readable target data without overstating precision.

## Priority

Exact table/text values > supplementary data > official result files > vector extraction > raster digitization > manual read-off.

## Axis calibration

For each axis record at least two trusted tick-value anchors for linear axes and suitable anchors for logarithmic axes. Verify whether scientific multipliers such as `x10^3` apply.

For log axes, fit pixel position to log(value), not value directly.

## Curve extraction

- Extract each identifiable series separately.
- Record legend mapping and marker style.
- Preserve raw extracted points.
- Never smooth raw points in-place.
- If smoothing/resampling is needed for comparison, save it as a separate processed artifact with parameters recorded.
- Do not fabricate values under labels, legends, or occluded regions.

## Uncertainty estimate

Estimate extraction uncertainty using one or more of:

- repeat extraction by two calibrations;
- one-pixel data sensitivity;
- repeated digitization;
- marker/line thickness converted to data units;
- paper rounding precision.

The acceptance gate should not demand smaller error than the reference can support.

## Curve alignment

Use only the shared domain for global curve metrics. Preserve native grids for peak detection. Record the interpolation method and direction when resampling is used.

## Special cases

### Mode shapes
Sign is arbitrary. Normalize and align signs before pointwise comparison. If only sparse plotted points exist, compare MAC on common coordinates.

### FRF dB plots
Determine whether the ordinate is amplitude, power, mobility, receptance, accelerance, or another FRF before converting dB.

### PSD plots
Confirm PSD/ASD and one-/two-sided conventions before digitization-to-RMS comparisons.

### Image contours
Do not infer precise field values from a color contour unless a readable color bar exists. If a contour is the only evidence, classify the comparison as qualitative/semi-quantitative unless robust color mapping is possible.


## Ground-truth freeze and namespaces

After formal extraction create `paper_ground_truth_manifest.csv` and follow `references/ground_truth_freeze.md`.

Use distinct namespaces:
- `paper_raw_*` for authoritative extracted paper evidence;
- `paper_processed_*` for derived/resampled paper evidence;
- `surrogate_*` for fitted/ROM/engineering reconstructions.

A processed/surrogate curve must never overwrite or be renamed as the authoritative paper target. If a frozen extraction is corrected, increment the target version and invalidate affected prior metrics/verdicts.
