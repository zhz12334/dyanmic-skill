# Model, FE/Deck, Solver and Protocol Fidelity

## Purpose

Formula fidelity alone is insufficient. A program can reproduce every equation symbolically while implementing the wrong geometry, element, mesh, mass formulation, contact, solver, loading, measurement coordinate or post-processing protocol.

Create `model_implementation_registry.csv` and trace every claim-relevant non-formula implementation obligation.

## Registry classes

At minimum audit, when applicable:
- geometry and topology;
- coordinate systems and DOFs;
- element family/formulation/order;
- mesh topology/density and convergence role;
- lumped vs consistent mass;
- material assignment and orientation;
- joint/contact/interface formulation;
- contact enforcement, penalty/constraint settings and friction semantics;
- constraint equations, rigid links, MPCs and coupling;
- boundary/support realization;
- load/base excitation realization;
- damping realization;
- initial state/preload/equilibrium step;
- numerical integration/eigensolver/nonlinear solver family;
- iteration and convergence semantics;
- reduced integration/hourglass controls when relevant;
- modal truncation/reduction basis;
- output location, interpolation and coordinate transform;
- sensor/measurement channel mapping;
- filtering/windowing/post-processing realization;
- unit system and solver defaults that can affect claims.

## Evidence states

Each item must be one of:
- `PAPER_FAITHFUL`;
- `SOURCE_LINEAGE_SUPPORTED`;
- `VERIFIED_EQUIVALENT`;
- `EXPLICIT_HYPOTHESIS`;
- `NUMERICALLY_VERIFIED_CHOICE`;
- `AMBIGUOUS`;
- `BLOCKED`.

## Hard failures

Treat as P0/P1 fidelity findings when claim-relevant:
- wrong element/kinematic theory;
- wrong DOF or coordinate sign;
- wrong mass formulation where dynamics changes materially;
- BC/support drift;
- excitation type drift (force vs base excitation, etc.);
- contact/joint model substitution;
- solver-family substitution that changes the modeled physics without evidence;
- output coordinate/location drift;
- hidden solver defaults materially affecting results;
- mesh/time-step chosen to fit instead of verify convergence.

## Runtime trace

For critical entries show:
`paper/model obligation -> implementation setting/file/API/deck entry -> runtime evidence -> claim output`.

## Gate

`MODEL_IMPLEMENTATION_FIDELITY_VERIFIED` requires:
- no open P0/P1 non-formula fidelity findings;
- every claim-critical registry item resolved or explicitly blocking;
- numerical settings justified by solution verification rather than fit;
- all implementation hypotheses linked to the Assumption Register.
