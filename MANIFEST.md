# Package Manifest — v4.0.0-rc5

## Core
- `SKILL.md` — mandatory workflow, gates and final classifications
- `VERSION` — package version
- `CHANGELOG.md` — change history

## Core reference modules
- `references/reproduction_modes.md` — literature-only M1/M2 reproduction modes and transition rule
- `references/artifact_availability.md` — non-code evidence availability and third-party code-source classes
- `references/claim_evidence_artifact_graph.md` — claim-level reproduction model
- `references/plan_approval.md` — mandatory initial-plan and material-repair approval rules
- `references/formula_fidelity.md` — equation registry, dependency graph, formula coverage, tests and runtime fidelity
- `references/paper_to_code_hallucination_audit.md` — LLM paper-to-code hallucination categories and closure rules
- `references/model_solver_fidelity.md` — geometry/FE/deck/solver/protocol fidelity gate
- `references/evidence_conflict.md` — contradictory-source handling
- `references/source_faithful_variants.md` — paper-faithful vs source-lineage/corrected/verification variant policy
- `references/implementation_contract.md` — persistent scientific obligations and change control
- `references/vvuq_framework.md` — verification/validation/calibration/UQ/prediction
- `references/experimental_reproduction.md` — experimental branch
- `references/ml_shm_reproduction.md` — ML/SHM data-split/preprocessing/leakage branch
- `references/model_discrepancy.md` — discrepancy-budget rules
- `references/validation_strategy.md` — calibration/validation split
- `references/validation_exposure.md` — validation leakage/exposure lifecycle
- `references/run_provenance.md` — evidence/run hash binding
- `references/clean_room_reproduction.md` — fresh-environment rerun gate
- `references/skill_evaluation.md` — benchmark for the skill itself
- `references/parameter_taxonomy.md` — P/T/L/C/N/R/H taxonomy
- `references/theory_parameter_provenance.md` — unified source classes, provenance closure, final-report disclosure and run binding
- `references/parameter_source_recovery.md` — citation-lineage recovery and transferability
- `references/author_group_cross_evidence.md` — mandatory same-author/same-group literature mapping, parameter triangulation and transferability/conflict checks
- `references/reproducibility_probability.md` — pre-implementation evidence-based reproducibility probability assessment
- `references/inverse_identification.md` — bounded calibration
- `references/result_type_registry.md` — metric routing by result type
- `references/comparison_metrics.md` — physical comparison metrics
- `references/discrepancy_strategy.md` — mismatch diagnosis
- `references/figure_digitization.md` — figure/data extraction
- `references/checklists.md` — engineering checks
- `references/equations.md` — equation references
- `references/workflow.md` — state machine

- `references/whole_paper_evidence_scan.md` — mandatory whole-paper/cross-chapter scan before missing-item declaration
- `references/model_dependency_planning.md` — physics/model module DAG and upstream freeze rules
- `references/figure_batch_planning.md` — result dependencies, anchors/satellites and model-based batches
- `references/ground_truth_freeze.md` — immutable/versioned paper ground truth
- `references/builder_validator_separation.md` — procedural development/evaluation separation
- `references/stop_tuning_evidence_review.md` — stop-tuning triggers and evidence-return policy

## Evidence templates
- `templates/chapter_registry.csv`
- `templates/cross_chapter_evidence_links.csv`
- `templates/reference_use_registry.csv`
- `templates/model_dependency_graph.csv`
- `templates/figure_dependency_graph.csv`
- `templates/figure_batch_plan.csv`
- `templates/paper_ground_truth_manifest.csv`
- `templates/builder_validator_handoff.yaml`
- `templates/stop_tuning_decision.csv`
- `templates/artifact_availability_matrix.csv`
- `templates/reproduction_mode_manifest.md`
- `templates/paper_evidence_matrix.csv`
- `templates/claim_registry.csv`
- `templates/claim_evidence_links.csv`
- `templates/target_characterization.csv`
- `templates/theory_research_log.csv`
- `templates/theory_formula_provenance.csv`
- `templates/parameter_provenance_summary.csv`
- `templates/provenance_source_summary.csv`
- `templates/inverse_parameter_summary.csv`
- `templates/unresolved_provenance_items.csv`
- `templates/evidence_conflict_register.csv`
- `templates/equation_registry.csv`
- `templates/equation_dependency_graph.csv`
- `templates/equation_code_traceability.csv`
- `templates/formula_test_registry.csv`
- `templates/hallucination_audit.csv`
- `templates/model_variant_manifest.csv`
- `templates/model_structure_register.csv`
- `templates/model_implementation_registry.csv`
- `templates/implementation_contract.yaml`
- `templates/parameter_register.csv`
- `templates/parameter_source_trace.csv`
- `templates/author_group_literature_map.csv`
- `templates/cross_parameter_validation.csv`
- `templates/reproducibility_probability_assessment.csv`
- `templates/reproducibility_probability_report.md`
- `templates/assumption_register.csv`
- `templates/plan_approval.md`
- `templates/repair_plan.md`
- `templates/open_source_reuse_audit.csv`
- `templates/calibration_validation_manifest.csv`
- `templates/validation_exposure_log.csv`
- `templates/vvuq_matrix.csv`
- `templates/model_discrepancy_budget.csv`
- `templates/experimental_protocol_register.csv`
- `templates/dataset_protocol_register.csv`
- `templates/author_clarification_log.csv`
- `templates/paper_data_extraction_register.csv`
- `templates/baseline_comparison.csv`
- `templates/optimization_run_log.csv`
- `templates/identifiability_report.csv`
- `templates/iteration_log.csv`
- `templates/metric_history.csv`
- `templates/run_manifest.yaml`
- `templates/artifact_inventory.csv`
- `templates/clean_room_rerun.md`
- `templates/claim_verdict.csv`
- `templates/reproduction_report.md`

## Validation evidence
- `RC5_EVIDENCE_PROBABILITY_VALIDATION.md` — RC5 design validation for author/group cross-evidence and pre-implementation probability
- `RC5_STATIC_LINT.json` — RC5 static package lint
- `RC1_VALIDATION.md` — original RC1 static/design validation status
- `RC2_REGRESSION_NOTE.md` — regression-derived RC2 rationale
- `RC2_STATIC_LINT.json` — RC2 static package lint
- `RC1_STATIC_LINT.json` — static package lint
- `validation/RC1_BENCHMARK_REPLAY.md` — bearing failure replay + rotor desktop benchmark

## RC4 result-presentation additions
- `references/result_presentation_contract.md`
- `templates/validation_card.md`
- `templates/validation_metrics.csv`
- `templates/validation_packet_manifest.csv`
- `templates/batch_validation_summary.csv`
- `templates/regression_dashboard.csv`
- `validation/presentation/validation_card_layout_example.png`

## RC5 evidence-closure additions
- Mandatory same-author/same-group publication cross-evidence before missing/assumed/inverse-identified classification.
- Mandatory pre-implementation reproducibility probability report after provenance closure and before Implementation Contract/full plan.
