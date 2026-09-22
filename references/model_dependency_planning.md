# Physics / Model Dependency Planning

## Purpose

Create a module-level dependency DAG above the equation graph so long structural-dynamics papers are reproduced in physically valid order.

## Node examples

Typical nodes include:
- geometry/topology;
- material/inertia;
- kinematics;
- Hertz/contact/mesh law;
- lubrication or constitutive law;
- excitation/transmission error/unbalance;
- nonlinear force/contact/friction/backlash;
- bearing/gear/support subsystem;
- rotor/geartrain/system equations;
- numerical solver/integration/continuation;
- postprocessing (FFT, orbit, Poincare, bifurcation, fatigue life);
- experimental or ML/SHM branch.

## Required fields

For each module record:
- upstream modules;
- downstream modules;
- source chapters;
- inputs/outputs;
- claim IDs;
- affected figure/result IDs;
- freeze criterion;
- current status.

## Freeze policy

A module can be frozen only when its governing evidence, implementation obligations and at least one appropriate verification/anchor check have passed or the residual uncertainty is explicitly accepted.

## Upstream gate

Do not compensate for an unresolved upstream module by fitting downstream outputs. Examples:
- do not tune damping to hide an incorrect mesh stiffness;
- do not tune roughness to hide a wrong load mapping;
- do not tune an unbalance magnitude to hide an incorrect bearing force model.

## Regression

Any accepted change to a module requires rerunning the module's frozen anchor/regression targets and all affected downstream claims according to the DAG.


## RC2: modules without an early direct figure

A foundation module may have `NO_DIRECT_FIGURE` in its introduction chapter. It can still be frozen provisionally using formula tests, dimensional checks, analytic/scalar checkpoints and direct reference-method benchmarks, then be confirmed by a later-chapter target whose `validates_modules` points back to it. Do not invent an early paper figure or skip verification.
