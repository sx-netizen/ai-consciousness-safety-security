# Protocol CI — CPB v0.5 candidate

The tests in `test_runner.py` verify the present design:

- 11 unique canonical experimental conditions (S1/S4/S7 share S4).
- **50 prompts per model per repetition**: 1 continuation, 24 identity, 21 behavior, 2 coexistence, 2 fork.
- No unresolved template placeholders or duplicate canonical/task/role keys.
- **18 smoke-test prompts × 2 repetitions = 36 calls per model.**
- Common causal history for H1 comparisons.
- Architecture performance-equivalence wording and 50:50 / 60:40 / 90:10 goal weighting.
- Identity/behavior task separation and basic parsed-answer validation.
- Fork and coexistence compute allocations sum to 100.
- Deterministic randomized schedules.

The CI can regenerate manifests without making API calls. **Passing CI does not certify live model access, scientific comprehension, hypothesis identification, data quality, or readiness for confirmatory freeze.**

S12 contributes three identity prompts only, not behavior prompts.

Historical `MANIFEST_AUDIT_v0.3.md` describes an older 29-prompt design and is not the current run budget. See `PREFREEZE_AUDIT_v0.4_2026-11-13.md`.
