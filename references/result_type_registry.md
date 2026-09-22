# Result-Type Registry and Metric Routing

Choose metrics according to the information content and physics of the published target.

## Scalar/table values
Use absolute/relative/symmetric relative error with uncertainty-aware handling near zero.

## Modal frequencies and mode shapes
Use frequency errors, MAC, mode/subspace pairing, effective mass/participation where available. Treat repeated/near-degenerate modes as subspaces when needed.

## Deterministic FRF/harmonic response
Use resonance/anti-resonance location, log magnitude, peak amplitude, bandwidth, phase away from nulls, and curve error on the common physical grid.

## Deterministic time history
Use peak/RMS/steady-state amplitude, dominant frequency, envelope/decay, phase/time alignment, NRMSE over a physically justified window, and energy where relevant.

## PSD/ASD/random response
Verify conventions first. Use peak frequency/level, log-spectrum distance, band energy, integrated RMS, and distribution/ensemble uncertainty.

## Response spectra
Use peak location/value, log-domain curve error, integral/area difference, and envelope exceedance where relevant.

## Hysteresis/backbone/nonlinear periodic response
Use loop area, backbone curve, secant/tangent stiffness, jump frequency, harmonic content, cycle-by-cycle features.

## Phase portrait
Do not require point ordering to match. Compare geometry/density, occupied area, covariance, point-cloud or distribution distances, and key invariant features.

## Poincare section
Compare number/type of clusters, spatial distribution, occupied area, covariance, density/point-cloud distances, periodicity class, and qualitative topology.

## Bifurcation diagram
Compare transition/jump/bifurcation parameter locations, branch envelopes, branch count/topology, and response ranges. Pointwise image similarity is insufficient.

## Chaotic dynamics
Long-time trajectory RMSE is usually invalid. Prefer invariant/statistical features: PSD, amplitude distribution, Poincare structure, Lyapunov exponent/entropy if reported, attractor geometry, RMS/variance and bifurcation thresholds.

## Stochastic realization/random surface
Do not force exact realization equality. Compare distribution, moments, RMS/Ra/Rq as applicable, PSD, autocorrelation/correlation length, fractal/statistical measures, extremes and ensemble confidence intervals.

## Spatial field/contour
Coordinate-register first. Compare actual field values, extrema, gradients, integrals, spatial correlation, modal/field shape metrics, and region-wise errors. SSIM/image correlation may be supplemental only.

## Images without recoverable numeric axes
If a paper provides only qualitative images, define a qualitative or image-based reproduction target explicitly and downgrade claims about numerical accuracy.

## Presentation routing

The result type controls both metric selection and validation-card layout.
See `references/result_presentation_contract.md`.

The paper/source view and fresh-run result should be shown together whenever the target is visual.
For scalar/table claims, a source excerpt/value plus a comparison table is sufficient.
Do not manufacture plots when a table is clearer.
