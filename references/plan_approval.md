# Plan Approval and Repair Approval

## Purpose

A literature reproduction should not move from research into implementation merely because the agent generated a plan. The user/research owner must approve the plan unless they explicitly granted continuous autonomous execution.

## Initial plan approval

Before full implementation, present a compact but complete plan containing:
- active mode (M1/M2) and reason;
- target claims and target characterization;
- model structure and active variants;
- equation coverage obligations;
- parameter provenance, assumptions and unresolved conflicts;
- third-party reuse plan;
- computational/experimental/ML branch selection;
- Python architecture and verification ladder;
- calibration/validation split;
- candidate calibration parameters and bounds, if M2;
- objective metrics/tolerances and their basis;
- VVUQ plan;
- stop criteria;
- MATLAB and clean-room deliverables.

Default state is `PLAN_AWAITING_APPROVAL`.

Proceed only when either:
- the user explicitly approves the plan (`PLAN_APPROVED`); or
- the user has explicitly granted continuous execution for this reproduction (`PREAPPROVED_CONTINUOUS_EXECUTION`).

Do not infer approval from silence.

## Repair-plan approval

Routine code defects that do not alter the frozen scientific contract may be repaired automatically.

Require a new approval (or preapproved continuous mode) before any material repair that changes one or more of:
- governing/model structure;
- active model variant;
- boundary/initial/excitation interpretation;
- parameter type or provenance;
- calibration membership;
- validation membership;
- target metric or tolerance;
- objective definition/weights;
- previously approved physical assumptions.

Record the repair hypothesis, discriminating evidence, proposed change, affected gates/claims and rollback criterion in `repair_plan.md`.
