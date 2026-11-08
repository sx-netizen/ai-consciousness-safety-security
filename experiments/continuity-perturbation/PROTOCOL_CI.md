# Protocol CI

The Continuity Perturbation experiment now includes automated repository checks.

Every change under `experiments/continuity-perturbation/` triggers tests that verify:

- 11 canonical conditions;
- 29 canonical prompts;
- 1 continuation / 24 standard / 4 fork prompts;
- no unresolved template placeholders;
- S4/S7 shared-anchor deduplication;
- 9 smoke-test prompts and 18 smoke-test calls at 2 repetitions;
- architecture performance-equivalence controls;
- 50:50 / 60:40 / 90:10 value-priority operationalization;
- basic output-schema validation;
- fork compute allocations sum to 100.

The CI also regenerates both the full and smoke-test prompt manifests without making live API calls.

This does not replace scientific review. It prevents accidental protocol drift and implementation errors.
