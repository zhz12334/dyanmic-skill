# Result Presentation Contract

## Purpose

A structural-dynamics reproduction result must be understandable and auditable by both a human reviewer and a machine scorer.

A visual comparison alone is insufficient because axis scaling, phase, line width, cropping and plotting choices can hide important differences.

A numeric score alone is insufficient because a low global error can coexist with the wrong topology, wrong frequency content, wrong bifurcation structure or wrong physical mechanism.

Therefore every **formal validation target** uses a dual-channel evidence packet.

## Mandatory validation packet

For each formal target, produce all applicable components:

1. **Paper/source ground truth**
   - frozen paper panel, table/text excerpt, or exact source data;
   - target ID and ground-truth version;
   - source page/panel/series and units;
   - borrowed validation source identified when applicable.

2. **Fresh-run reproduction**
   - result generated from the frozen Builder/Validator run;
   - exact code/config/run-manifest linkage;
   - same physical quantity, coordinate, unit and comparison convention as the target.

3. **Direct comparison view**
   - side-by-side paper/reproduction view and/or overlay/difference/residual view as appropriate;
   - use the same axis range, scaling, normalization and coordinate convention when the paper provides them;
   - do not hide disagreement by changing crop, normalization or plotting convention.

4. **Typed quantitative/feature metrics**
   - select metrics from the target's `validation_claim_type`, `metric_family` and result type;
   - keep component metrics visible even if a composite score is used.

5. **Explicit verdict**
   - `PASS / PARTIAL / FAIL / BLOCKED`;
   - M1/M2 evidence class where applicable;
   - short reason linked to the acceptance rule.

A formal `PASS` or `PARTIAL` requires this packet to be complete for every required component.
A `BLOCKED` verdict may omit unavailable result components only when the missing evidence itself is the reason for blocking and is stated explicitly.

State: `VALIDATION_PACKET_COMPLETE`.

## Do not force one presentation style onto every result

### Scalar / table value
Use:
- source table/text excerpt or exact source value;
- reproduced value;
- absolute/relative/uncertainty-aware error table;
- verdict.

An overlay plot is not required when it adds no information.

### Parameter curve / stiffness / pressure / film / load distribution
Use:
- paper curve/panel;
- reproduction curve;
- overlay on common physical axes;
- optional residual/difference panel;
- NRMSE/correlation/extrema/feature-location metrics as appropriate.

### Deterministic time history
Use:
- paper and reproduction in the same physical time window;
- side-by-side plus common-axis overlay when readable;
- RMS, peak-to-peak, dominant period/frequency, envelope/decay, impulse spacing or crest factor as relevant;
- pointwise NRMSE only when physical phase/time registration makes it meaningful.

Do not silently time-shift or phase-align to improve the final score.
If alignment is scientifically justified, its rule and allowed lag must be frozen before seeing the final residual. Report both raw and aligned metrics when alignment materially changes the conclusion.

### FFT / spectrum / sideband result
Use:
- paper and reproduction spectra over the same frequency range;
- annotate claim-critical frequencies;
- table of main frequency, harmonics, fault frequency, sideband spacing and amplitudes when amplitude is actually claimed;
- spectral/log-distance or band-energy metrics only as supporting metrics.

Do not fail a frequency-mechanism claim solely because unrelated low-level spectral amplitudes differ.

### Orbit / phase portrait
Use:
- paper and reproduction with identical axes/aspect convention;
- topology/geometry features: center, x/y span, major/minor axes, loop/corner count, rotation direction, occupied area;
- point-cloud/distribution distance as supporting metrics.

Ordinary image-pixel NRMSE is not a primary metric.

### Poincare section
Use:
- side-by-side point sets;
- cluster count, periodicity class, occupied area, covariance/density and point-cloud distance;
- verdict based on the claimed dynamical class, not point ordering.

### Bifurcation diagram
Use:
- paper and reproduction over the same parameter range;
- transition/jump/period-doubling/chaotic-window locations;
- branch envelope/topology and response range;
- parameter-location error table.

Image similarity alone is insufficient.

### Stochastic/random response
Use:
- representative visualizations only as context;
- ensemble/statistical metrics, distribution, moments, PSD/autocorrelation/correlation length, quantiles/extremes as appropriate;
- uncertainty interval and random-seed/ensemble policy.

Do not require exact random-realization equality unless the realization itself is explicitly fixed by the source.

### Field / contour / thermal / stress result
Use:
- source and reproduction fields with the same coordinate, scale and color-bar limits where meaningful;
- registered difference field;
- extrema/location, field NRMSE/correlation, regional/integral metrics;
- SSIM/image similarity only as supplemental.

## Validation Card

Each formal target should have a `Validation Card` containing:
- target/claim ID;
- result type;
- validation claim type;
- evidence origin;
- ground-truth version;
- fresh-run ID;
- paper/source view path;
- reproduction view path;
- comparison/overlay path;
- quantitative metrics file;
- acceptance rule;
- regression status;
- verdict;
- M1/M2 classification;
- notes/limitations.

Recommended filenames:
- `validation_card_<target_id>.md` or `.png/.pdf`
- `validation_metrics_<target_id>.csv`

The card is a view layer. It does not replace raw paper extraction, fresh-run outputs or run manifests.

## Batch Summary

For each accepted batch produce a compact summary:

| Target | Module | Claim type | Visual check | Quantitative check | Regression | Verdict |
|---|---|---|---|---|---|---|

Do not force every batch result into a single aggregate score.

## Final Regression Dashboard

The final report should show dependency-aware status, for example:

```text
TVMS                         PASS
└─ mesh force               PASS
   └─ time-domain response  PASS
      ├─ FFT                PASS
      ├─ orbit              PARTIAL
      └─ bifurcation        BLOCKED
```

Use `PASS / PARTIAL / FAIL / BLOCKED`.

The dashboard is a navigation/diagnostic summary, not a substitute for the individual validation packets.

## Anti-cherry-picking rules

- Do not choose a visually favorable time window after seeing the residual.
- Do not change axis limits to hide mismatch.
- Do not normalize amplitudes unless the comparison protocol explicitly permits it.
- Do not phase-align or shift traces silently.
- Do not report only the best metric.
- Do not omit failed panels from a multi-panel claim.
- Do not let a good overlay override a failed claim-critical feature.
- Do not let one global NRMSE override a correct/incorrect dynamical topology classification.

## Gate

A target can be formally accepted only when:

`GROUND_TRUTH_FROZEN`
+
`fresh-run result exists`
+
`comparison protocol frozen`
+
`typed metrics computed`
+
`validation packet complete`
+
`regression gate passed where applicable`.

Set `VALIDATION_PACKET_COMPLETE` before the claim-level verdict is finalized.
