# ML/SHM Reproduction Branch

Use this branch only when machine learning/data-driven inference is part of a structural-dynamics or SHM claim.

## Required dataset protocol registry

Create `dataset_protocol_register.csv` and record:
- dataset version/hash and acquisition unit;
- specimen/asset/run/condition identifiers;
- label provenance;
- train/validation/test split unit and rule;
- windowing/segmentation timing relative to split;
- normalization/statistics fit scope;
- feature extraction fit scope;
- augmentation;
- class balancing/sampling;
- cross-validation grouping;
- hyperparameter-tuning evidence set;
- checkpoint/early-stopping selection rule;
- seeds and repeat count;
- metric aggregation and confidence intervals.

## Leakage hard rules

Avoid information leakage across physically correlated units. Prefer splitting at the independent experimental/asset/run/specimen level **before** transformations that can share information across partitions.

At minimum audit:
- windows from the same continuous record appearing in train and test;
- normalization fitted using validation/test data;
- feature selection using target/test labels;
- target-domain statistics used in a claimed domain-generalization setting;
- augmentation before group split that creates near-duplicates across partitions;
- hyperparameter tuning on the final test set;
- checkpoint selection using test performance;
- repeated-run reporting that selects the best seed without disclosure.

## ML claim fidelity

Register loss, architecture-critical equations, preprocessing, split protocol, evaluation metrics and selection rules in the Implementation Contract. A high test score with protocol leakage is a reproduction failure for the claimed evaluation protocol.
