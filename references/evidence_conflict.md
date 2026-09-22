# Evidence Conflict Resolution

## Purpose

Papers, theses, cited sources, supplements, standards and related work can disagree. Never resolve conflicts silently by choosing whichever value gives the best match.

Create `evidence_conflict_register.csv` whenever two credible sources disagree on a claim-relevant quantity, equation, model definition, protocol or result.

## Conflict fields

Record:
- conflict ID;
- item/equation/parameter/claim affected;
- each source and exact statement/value;
- source role and provenance strength;
- definition/unit/model-form comparability;
- possible reasons for disagreement;
- affected claims;
- proposed resolution;
- whether multiple model variants are required;
- status and closure evidence.

## Resolution principles

There is no universal source hierarchy. Use context:
- errata/corrections can supersede original text;
- the target paper defines the published scientific claim;
- cited original theory can clarify definitions/derivations;
- thesis/related work can provide omitted detail but must pass transferability checks;
- standards/manuals can define generic quantities but not author-specific hidden values.

Possible decisions:
- `TARGET_PAPER_FAITHFUL`;
- `ERRATUM_SUPERSEDES`;
- `SOURCE_LINEAGE_VARIANT`;
- `MULTI_VARIANT_REQUIRED`;
- `TREAT_AS_UNCERTAINTY`;
- `UNRESOLVED_BLOCKING`;
- `UNRESOLVED_NONBLOCKING`.

If the conflict changes governing physics or a critical parameter, reopen the model/parameter gate. Do not use inverse optimization to conceal unresolved contradictory evidence.
