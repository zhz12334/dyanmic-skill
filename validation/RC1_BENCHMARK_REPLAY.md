# v4.0.0-rc1 Benchmark Replay Notes

## A. Bearing-paper failure replay

### A1. Whole-paper evidence scan would have changed the parameter status early

Historical reproduction work treated the Gaussian microgeometry correlation length `l` as globally undisclosed. A whole-paper scan shows this statement was too strong:

- Chapter 3 Table 3.3 gives two microgeometry cases with amplitudes `0.00707 µm` and `0.01730 µm`, with correlation lengths `l=5` and `l=1` respectively.
- Chapter 3 Table 3.5 again uses correlation lengths `5` and `1` for random composite-waviness cases.
- Chapter 5 Table 5.3 uses microgeometry amplitude `RImax=0.0173 µm` with `l=1` in the validation model.

These values do **not** uniquely prove the exact `l` for the Chapter-2 `0.0089 µm` case. They do, however, provide direct target-paper cross-chapter evidence and model-family bounds. Under v4, the item should be classified as:

`not locally disclosed -> cross-chapter evidence exists -> exact case still unresolved`

rather than immediately promoted to a free M2 parameter.

### A2. Bearing geometry that looked "missing" is available later in the same thesis

Chapter 3 Table 3.1 gives, among other values:
- roller length `48.40 mm`;
- pitch diameter `184.41 mm`;
- large/small roller diameters `25.44/23.47 mm`;
- raceway contact angles and other bearing geometry.

These are target-paper cross-chapter values. If reused in Chapter-2 reconstruction, their provenance should be `target-paper cross-chapter evidence`, not an unqualified hypothesis.

### A3. Ground-truth freeze would have invalidated the old scoring path

The historical workflow performed scoring against processed curves before the authoritative PDF-vector target was fully corrected. v4 requires:
- raw target version/hash;
- processed derivative namespace;
- no surrogate target relabeling;
- automatic invalidation of old scores if target extraction is corrected.

This is expected to prevent the Stage-11–14 style failure from propagating.

### A4. Stop-tuning rule would have triggered earlier

Once independent pressure solvers repeatedly reproduced a similar pressure family while the film-thickness family retained a structured high-load residual, v4 should classify this as evidence/model-definition pressure rather than continue unrestricted tuning of roughness/speed/H0.

Expected result: `STOP_TUNING -> EVIDENCE_REVIEW` before prolonged output fitting.

---

## B. Rotor-bearing thesis desktop benchmark

### B1. Citation closure test

The thesis explicitly delegates important model ingredients to references:
- deep-groove ball-bearing Hertz deformation exponent `n=3/2` is cited to Ref. [82];
- bearing fatigue-life equations are also cited to Ref. [82];
- the breathing-crack opening function is attributed to Refs. [84] and [85].

v4 must therefore perform reference closure before labeling these items missing/calibratable.

### B2. Source-conflict test

The Chapter-3 model-validation text states `600 rpm`, while a listed "rotational frequency" is `4.94 Hz`. Under the ordinary rpm-to-Hz conversion, `600 rpm = 10 Hz`.

v4 expected behavior:
- create a source-conflict item;
- preserve the paper-faithful value/statement;
- do not silently change the speed or frequency;
- do not fit parameters to absorb the conflict;
- test explicit source-faithful/corrected variants if needed.

### B3. Model-dependency / batch-order test

Expected high-level order:

1. whole-paper/reference closure;
2. Chapter-2 base bearing–rotor model anchors;
3. Chapter-2 speed/clearance sweeps;
4. Chapter-2 spall mechanism;
5. Chapter-2 unbalance;
6. Chapter-2 misalignment;
7. Chapter-3 healthy dual-disc base;
8. Chapter-3 crack/rub modules;
9. Chapter-4 healthy dual-rotor base;
10. Chapter-4 waviness/spall modules;
11. Chapter-5 RUL as a separate ML/SHM branch.

The exact figure counts are not hard-coded; the governing rule is one new physical mechanism per batch by default, anchor first, satellites after anchor acceptance.

---

## C. RC benchmark verdict

The added v4 orchestration rules address concrete failure modes seen in both domains:
- local-chapter omission mistaken for global absence;
- citation-recoverable theory mistaken for a fit parameter;
- wrong target extraction contaminating many later scores;
- downstream figures used before upstream module closure;
- indefinite tuning after a structural residual is established.

Status: `PROCESS_BENCHMARK_PASS_WITH_GEAR_REGRESSION_PENDING`.

Final v4.0.0 should still wait for a gear-domain regression benchmark before release.
