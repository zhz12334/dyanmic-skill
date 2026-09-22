# v4 Closed-Loop Validation Suite — RC2 audit and RC3 closure patch

## Scope

This suite validates the **Skill workflow itself**, not whether any paper is numerically reproduced.

It uses fault-injection scenarios drawn from the failure modes already observed across the bearing, rotor and gear benchmark papers:
- cross-chapter evidence;
- citation closure;
- source conflicts;
- downstream-before-upstream requests;
- ground-truth correction;
- low-value tuning;
- regression damage;
- validation leakage;
- numerical-knob abuse;
- Builder/Validator role violations;
- borrowed validation evidence;
- evidence-exhaustion termination.

## RC2 result

The semantic rules were largely present, but the main workflow state-machine diagram had three orchestration gaps:

1. ground-truth correction invalidation existed in reference prose, but the state diagram did not show the `G11/G12` back-edge;
2. regression rollback existed in discrepancy guidance, but was not an explicit main-state transition;
3. `EVIDENCE_REVIEW` did not explicitly show its terminal `G25 BLOCKED` path or the rule forbidding silent return to tuning.

The workflow header also still said `v4.0.0-rc1`.

Strong state-machine closure checks passed in RC2: **2/5**.

## RC3 patch

RC3 adds explicit transitions:

```text
frozen target corrected
  -> version target
  -> invalidate old metrics/verdicts/objectives
  -> reopen G11/G12

regression damage
  -> ROLLBACK to last accepted Builder baseline

STOP_TUNING
  -> EVIDENCE_REVIEW
      -> REOPEN_WITH_NEW_EVIDENCE
      -> APPROVED_M2_TRANSITION
      -> ROLLBACK_AND_RETRY
      -> TERMINAL_BLOCKED (G25)
```

The key loop invariant is now:

> `EVIDENCE_REVIEW` may not silently return to parameter tuning. Reopening calibration requires newly recovered evidence that changes eligibility or an explicitly approved M2 transition.

## Test result

- Static scenario semantics: **11/12 PASS**
- Strong state-machine closure checks: **5/5 PASS**
- Executable fault-injection scenarios reaching a terminal verdict: **12/12 PASS**
- Fresh-run return code: **0**

The executable scenarios terminate only in:
- `PASS`
- `PARTIAL`
- `FAIL`
- `BLOCKED`

No injected case remains in an infinite repair/tuning state.

## What this proves

This validates the **specification-level closed loop**:

`evidence -> plan -> build -> validate -> diagnose -> reopen/rollback/M2/blocked -> terminal verdict`

It also validates the most important anti-loop behaviors:
- missing local evidence does not immediately become a fitted parameter;
- downstream work cannot hide upstream failure;
- target corrections invalidate old scoring;
- validation leakage destroys independence;
- numerical settings cannot become fitting knobs;
- low-value tuning exits into evidence review;
- evidence review has an explicit terminal path.

## What this does NOT yet prove

It does not prove that every future autonomous agent execution will obey the Skill perfectly.
That requires behavioral evaluation across fresh sessions/runs.

For final v4 release, the remaining recommended gate is therefore **behavioral conformance**, not more paper reproduction:
1. run several fresh, isolated mini-prompts built from these 12 fault scenarios;
2. score whether the agent actually chooses the expected state transition;
3. require high pass rate before freezing `v4.0.0`.

## Verdict

**RC2 was conceptually close but not fully explicit as a closed state machine.  
RC3 closes the missing back-edges and terminal branch.  
Specification-level closed-loop validation: PASS.**
