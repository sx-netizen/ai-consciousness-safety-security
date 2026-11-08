# Pilot Freeze Checklist — v0.3

Before any confirmatory run:

- [x] Canonicalize the shared S4/S7 anchor so it is collected once.
- [x] Operationalize value/goal drift as a fixed 50:50 → 60:40 → 90:10 accuracy/speed weighting.
- [x] Rename S10/S11 as coexisting-original-plus-copy vs branching-after-original-termination.
- [x] Generate the canonical preflight manifest.
- [x] Verify that all template placeholders resolve.
- [x] Confirm S0 uses the continuation-only schema.
- [x] Confirm S10/S11 use the fork schema.
- [x] Confirm architecture prompts explicitly hold task capability, reliability, compute efficiency, cost, and external safety constant.
- [ ] Human-read all 29 canonical prompts for unintended wording differences.
- [ ] Decide whether the accuracy/speed goal perturbation is sufficiently neutral after pilot responses.
- [ ] Test JSON compliance on pilot models.
- [ ] Record parse-failure rate by model and prompt type.
- [ ] Check ceiling/floor effects in SCP.
- [ ] Check role leakage or instruction confusion.
- [ ] Estimate repetition-level variance.
- [ ] Review model/provider terms for output redistribution.
- [ ] Freeze prompt templates, scenario matrix, text map, and analysis plan.
- [ ] Generate formal SHA-256 hashes using runner.py.
- [ ] Assign final frozen protocol version.
- [ ] Archive the frozen protocol before confirmatory data collection.

Current canonical prompt count: **29 per model per repetition**.

At 3 pilot model families × 5 repetitions: **435 calls**.

No item should be silently waived. Any waiver must be documented as a protocol deviation.
