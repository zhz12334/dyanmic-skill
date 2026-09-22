# Evidence and Artifact Availability Policy

## Purpose

This skill assumes no usable author source code. Availability assessment therefore focuses on the literature/data ecosystem that can support an independent implementation or engineering reconstruction.

Do not confuse "not located" with "does not exist". Record only evidence-supported availability states.

## Availability statuses

- `AVAILABLE` — located and accessible.
- `NOT_FOUND_AFTER_DOCUMENTED_SEARCH` — not located after the documented search plan.
- `KNOWN_PRIVATE` — evidence indicates the item exists but is not public.
- `INACCESSIBLE` — location is known but access/download is unavailable.
- `UNKNOWN` — availability has not yet been established.
- `NOT_APPLICABLE` — item type is irrelevant to this paper.

## Required Evidence Availability Matrix

At Phase 0 create `artifact_availability_matrix.csv` for at least:

- target paper PDF/version;
- supplementary material/appendices/errata;
- raw or processed research data, if separately released;
- parameter tables/input data published outside the paper;
- author thesis/dissertation;
- author/group prior/later papers relevant to the same model/apparatus;
- equation-local and upstream cited sources;
- third-party method/reference implementations;
- similar-system third-party implementations;
- solver examples/templates/manuals;
- standards/handbooks/material databases;
- benchmark/analytical reference data.

Record search evidence, identifier/URL when known, date checked, relevance and intended evidentiary role.

## Third-party code-source classes

### `METHOD_REFERENCE_CODE`
Independent implementation of a method/theory used by the paper, such as Newmark-beta, ERA, SSI-COV, a finite element formulation, contact law or standard numerical algorithm.

May be used for equation interpretation, unit tests, algorithm checks and implementation comparison when licensing/provenance permit. It must not silently redefine the target paper's model or parameters.

### `SIMILAR_SYSTEM_CODE`
Third-party implementation of a structurally similar but different problem.

May inform architecture, solver setup, diagnostics and plausible priors/bounds. Its parameters and hidden defaults are not target-paper evidence unless they independently pass source-lineage and transferability checks.

### `SOLVER_EXAMPLE_OR_TEMPLATE`
Official solver/manual example used to verify syntax or solver semantics, such as element formulation, contact definition, base excitation, damping implementation or output extraction.

Use as implementation evidence, not as a source of target-paper case parameters unless independently justified.

## Reuse audit

For every external implementation record:
- source class;
- URL/repository/reference;
- version/commit when available;
- license;
- similarity dimensions;
- exact reusable components;
- hidden-default risks;
- parameter-value transferability status;
- decision: `ADOPT/ADAPT/REFERENCE_ONLY/REJECT/NONE_FOUND`.

Absence of third-party code never blocks reproduction. It only changes whether implementation starts from a vetted reference or from the approved model specification.
