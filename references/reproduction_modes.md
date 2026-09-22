# Reproduction Modes for Literature-Only Structural-Dynamics Reproduction

This skill assumes the target paper does **not** provide author source code as a usable reproduction artifact. Source-code rerun/porting workflows are intentionally out of scope. The reproduction evidence base is the paper, supplements/non-code data when available, cited theory, related literature/theses, standards/manuals, and eligible third-party open-source implementations.

## M1 — Independent reimplementation

Implement independently from the paper, cited/reference theory, disclosed numerical/experimental protocol, recoverable parameter evidence, and eligible third-party method/reference implementations.

M1 is appropriate when the critical paper claims can be tested without using the paper's own target outputs to infer omitted claim-critical physical parameters.

Allowed completion sources include:
- paper/supplement/errata;
- citation lineage;
- author theses and related papers;
- authoritative standards/manuals/databases;
- transferable literature values;
- third-party method/reference code and similar-system code with provenance.

### M1 calibration boundary

M1 may reproduce a parameter-identification procedure **if that identification procedure is explicitly part of the paper's disclosed method**.

However, if the reproduction team itself must fit an omitted claim-critical physical parameter to the target paper's figures/tables/curves in order to match the result, the work is no longer pure M1. Transition to M2 (or record M2 as the primary final mode) before calibration.

Non-claim-critical nuisance choices may be explored under sensitivity analysis, but must remain explicit and may not be used to hide model-form errors.

## M2 — Engineering reconstruction / calibrated reproduction

Use all recoverable non-code evidence, explicit assumptions, transferable priors/bounds, and bounded inverse identification where justified to construct a traceable engineering-equivalent model.

M2 is appropriate when:
- the paper omits important physical parameters;
- those parameters cannot be recovered from source lineage;
- the missing quantities materially affect target claims; and
- the reproduction therefore uses published target evidence to identify equivalent parameters.

Final wording must distinguish:
- reproduced paper behavior/claims;
- reconstructed or calibrated parameters;
- independently documented values;
- non-identifiable or assumption-dependent quantities.

Never present an M2-identified value as the author's original hidden parameter unless an independent source establishes that fact.

## Mode transition rule

Start in M1 when feasible. Transition M1 -> M2 if any claim-critical hidden physical parameter is newly inferred from target-paper outputs by the reproduction team.

The transition is **not** triggered when faithfully implementing a calibration/identification procedure explicitly described by the paper itself.

Record the transition reason, affected claims, parameters, targets and date in the mode manifest and iteration log.

## Third-party code-source classes

- `METHOD_REFERENCE_CODE` — independent implementation of a method/theory used by the paper.
- `SIMILAR_SYSTEM_CODE` — third-party implementation of a structurally similar but different system.
- `SOLVER_EXAMPLE_OR_TEMPLATE` — official solver/manual example used only to verify element, contact, loading, API or numerical syntax/semantics.

Third-party code may accelerate implementation, but its hidden defaults and parameter values are not target-paper evidence unless separately recovered through provenance/transferability checks.

## Mode manifest fields

- primary_mode: `M1` or `M2`
- initial_mode
- mode_transition_history
- calibration_allowed
- paper_described_identification_procedure
- reproduction_team_inverse_identification_used
- target_outputs_used_for_missing_parameter_identification
- expected_final_claim
- third_party_code_policy
- final_mode_justification
