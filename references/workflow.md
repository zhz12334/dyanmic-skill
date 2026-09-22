# Structural-Dynamics Paper Reproduction State Machine — v4.0.0-rc4

```text
G0   Evidence availability + lock M1/M2 + target hierarchy
 |
 v
G0A  WHOLE-PAPER / CROSS-CHAPTER evidence scan
 |
 v
G1   Claim–Evidence–Artifact Graph
 |
 v
G2   Paper Evidence Matrix
 |
 v
G2A  Preliminary target characterization
 |
 v
G3   Theory/citation closure + evidence-conflict register
G3B  Same-author/same-group literature cross-evidence closed
 |
 v
G3F  Equation/Algorithm Registry + equation dependency graph
 |
 v
G4   Model-structure reconstruction/freeze
 |
 v
G4A  Model/FE/solver/protocol obligations registered
 |
 v
G4B  Physics/model dependency DAG frozen
 |
 v
G4C  Figure/result dependency + anchor roles frozen
 |
 v
G5   Parameter provenance + source recovery + M1/M2 boundary check
 |
 v
G5P  Theory/formula + parameter provenance closure
G5B  Cross-parameter consistency / inheritance validation closed
G5Q  Pre-implementation reproducibility probability assessed
G5U  Reproducibility probability reported to user
 |
 v
G5R  REFERENCE_CLOSED (search path closed; unresolved items may remain explicit)
 |
 v
G6   Persistent Implementation Contract frozen
 |
 v
G7B  Model-based figure/result batch plan frozen
 |
 v
G7   PLAN APPROVAL
 |    user approval OR explicit preapproved continuous execution
 v
G8   Third-party method/similar-system/solver-example reuse audit
 |
 v
G9   Select computational / experimental / ML-SHM branch(es)
 |
 v
G9F  Formula-to-code fidelity + hallucination audit
 |
 v
G9M  Model/FE/solver/protocol implementation fidelity
 |
 v
G10  Python code + solution verification
 |
 v
G11  Formal target extraction + uncertainty
 |
 v
G11F GROUND_TRUTH_FROZEN
 |    |
 |    +-- frozen target later corrected -> version target -> invalidate affected metrics/verdicts/objectives
 |                                      -> reopen G11/G12 and rerun affected comparisons
 v
G12  Active-batch baseline + upstream regression set
 |
 +-- gross physics/fidelity failure -> affected upstream gate
 |
 v
G13  Model-discrepancy budget
 |
 v
G14  Calibration eligibility + approved C set + mandatory M1->M2 transition if needed
 |
 +-- no calibration needed -> G17/G18 as applicable
 |
 v
G15  Physics-aware objective frozen
 |
 v
G16  Bounded inverse identification / paper-described identification
 |
 v
G17  Sensitivity + identifiability + UQ
 |
 v
G18  BUILDER_FROZEN -> Validator fresh run -> withheld validation + exposure logging
 |
 v
G18P Validation Packet: source view + fresh-run view + typed comparison + metrics + verdict
 |
 v
G18F VALIDATION_PACKET_COMPLETE
 |
 +-- pass -> G21
 |
 +-- fail -> G19 discrepancy repair
 |           |
 |           +-- repair improves active target but damages frozen anchor/regression
 |           |      -> ROLLBACK to last accepted Builder baseline
 |           |
 |           +-- evidence/model signal or low progress -> STOP_TUNING -> EVIDENCE_REVIEW
 |           |      |
 |           |      +-- new/recovered evidence changes an upstream contract -> reopen affected G3/G4/G5/G9 gate
 |           |      |
 |           |      +-- evidence exhausted but a scientifically justified M2 transition is approved -> G14
 |           |      |
 |           |      +-- evidence exhausted and no defensible M2 path exists -> G25 claim verdict = BLOCKED /
 |           |             Not reproducible from disclosed/recoverable information
 |           |
 |           +-- justified repair -> rerun G9F/G9M/G10 + regression + revalidation
 v
G20  Result-type policy overlay for stochastic/nonlinear/chaotic/spatial outputs
 |
 v
G21  Robustness + VVUQ + dependency-aware claim/anchor regression
 |
 v
G22  MATLAB parity
 |
 v
G23  Run provenance + artifact freeze
 |
 v
G24  CLEAN-ROOM fresh-environment rerun
 |
 v
G25  Claim-level verdict + evidence bundle
```

## Hard rules

1. Use M1/M2 only; author-code rerun/porting is out of scope.
2. Whole-paper scanning precedes any declaration that a claim-critical item is missing.
3. Target-paper cross-chapter evidence and citation lineage must close before H/C promotion.
4. Evidence-reading order is whole-paper-first; reproduction order follows the physics/model dependency DAG.
5. Claims are mapped before coding.
6. Critical equations and operative rules require complete formula-fidelity registration/runtime coverage.
7. Model/FE/solver/protocol fidelity is a separate gate from formula fidelity.
8. Evidence conflicts are explicit; no silent correction/cherry-picking.
9. Upstream modules gate downstream fitting.
10. Figures/results are executed in model-based batches; satellite tuning is prohibited while anchors fail.
11. Ground truth is versioned and immutable after freeze; processed/surrogate targets cannot masquerade as paper data.
12. Every critical theory/formula/parameter carries provenance into the final report.
13. Same-author/same-group publications are mandatory cross-evidence for claim-critical theory and parameters; no missing-item declaration is complete before this search is closed.
14. After provenance and group-cross-evidence closure, report a pre-implementation reproducibility probability and plausible range before implementation/plan freeze.
13. Numerical settings are verification knobs, not fitting knobs.
14. Plan and batch execution require approval or explicit continuous-execution preapproval.
15. Third-party code is audited; its hidden/default parameters do not become target-paper truth.
16. Calibration cannot compensate for missing/disconnected formulas or model/solver drift.
17. Builder/Validator responsibilities are separated procedurally.
18. Validation evidence is independent only until it influences development; exposure must be logged.
19. Random/chaotic outputs use statistical/invariant comparisons.
20. High fit does not imply unique physical parameters.
21. Repair is discrepancy-driven and dependency-aware; accepted changes rerun affected anchors/regression targets.
22. Stop-tuning triggers force evidence review rather than indefinite parameter fitting.
23. Every evidence run is bound to exact artifacts/environment.
24. Final independent reproducibility requires a clean-room rerun.

## Closed-loop termination invariant

Every repair/evidence-review branch must end in exactly one of four outcomes:

1. **REOPEN_WITH_NEW_EVIDENCE** — reopen the affected upstream gate because new/recovered evidence changes the scientific contract;
2. **APPROVED_M2_TRANSITION** — move through G14 with the M1->M2 boundary explicitly updated;
3. **ROLLBACK_AND_RETRY** — reject the candidate repair and return to the last accepted Builder baseline with a new, justified hypothesis;
4. **TERMINAL_BLOCKED** — issue the G25 `BLOCKED` / `Not reproducible from disclosed/recoverable information` verdict.

`EVIDENCE_REVIEW` must not silently return to parameter tuning. Reopening calibration requires either newly recovered evidence that changes parameter eligibility or an explicitly approved M2 transition. This rule prevents infinite curve-fitting loops.


## Result-presentation gate

`G18P/G18F` is mandatory for formal validation targets.

A formal PASS/PARTIAL cannot be issued from:
- visual similarity alone;
- one aggregate metric alone;
- a reproduction plot without the frozen source target;
- a source target without a fresh-run provenance link.

The packet structure is defined in `references/result_presentation_contract.md`.

For scalar/table claims, the source value/excerpt + reproduced value + metric table satisfies the source/reproduction view requirement; an unnecessary plot is not required.
