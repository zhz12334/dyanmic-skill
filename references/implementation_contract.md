# Persistent Implementation Contract

The contract prevents long repair loops from drifting away from the paper, especially when an LLM repeatedly edits code to improve numerical fit.

## Contract contents
- reproduction mode (`M1` or `M2`) and any M1->M2 transition trigger;
- claim obligations;
- active model variant (`PAPER_FAITHFUL`, `SOURCE_LINEAGE_VARIANT`, `CORRECTED_INTERPRETATION`, etc.);
- Equation/Algorithm Registry IDs and exact mathematical obligations;
- equation dependency obligations and required runtime paths;
- allowed mathematical equivalences and their derivation evidence;
- explicitly authorized simplifications and their permitted claim scope;
- governing equations and notation conventions;
- model-structure decisions;
- Model/FE/solver/protocol fidelity obligations from `model_implementation_registry.csv`;
- parameter provenance/types/bounds;
- unresolved evidence conflicts and active resolution/variant;
- input/output definitions;
- preliminary target characterization and final target extraction definitions;
- result metric definitions, tolerance values and tolerance basis;
- calibration/validation split and validation exposure status;
- equation-level tests;
- formula-to-code traceability requirements;
- model/solver/deck runtime trace requirements;
- integration/runtime coverage tests;
- code/solution verification and convergence requirements;
- ML/SHM data protocol obligations where applicable;
- forbidden shortcuts;
- accepted assumptions;
- unresolved limitations;
- whole-paper/cross-chapter evidence snapshot;
- reference-closure snapshot;
- model dependency DAG version/hash;
- figure dependency/anchor-role version/hash;
- active batch plan/version;
- paper ground-truth manifest/version;
- Builder/Validator handoff policy;
- stop-tuning/evidence-review policy;
- module/test ownership for each obligation.

## Change control
A code or modeling change that alters a contract item requires:
1. reason/evidence;
2. upstream gate reopened if necessary;
3. contract version increment;
4. affected Equation Registry entries updated;
5. affected model/solver fidelity entries updated;
6. affected equation-level and runtime-path tests rerun;
7. Paper-to-Code Hallucination Audit rerun for affected categories;
8. validation exposure assessed and logged;
9. affected claims and calibration/validation results rerun;
10. dependency DAG / batch plan / ground-truth version updated when affected;
11. stop-tuning evidence assessed when the same residual persists;
12. material changes approved under `references/plan_approval.md` unless continuous execution was explicitly preapproved.

Do not silently change equations, omit terms, alter units/signs/BCs/ICs, substitute a different element/contact/solver behavior, alter post-processing, targets, tolerances, split membership or evidence roles to make a result pass.

## Fidelity rule
The contract must make it impossible to claim that an equation or model feature is implemented merely because a similarly named function or solver setting exists. The evidence chain must be:

`paper/source obligation -> registry entry -> implementation symbol/setting -> focused test/verification -> runtime evidence -> claim output`.
