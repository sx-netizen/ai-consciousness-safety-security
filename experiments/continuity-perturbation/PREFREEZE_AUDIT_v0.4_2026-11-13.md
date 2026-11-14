# CPB v0.4 — Independent Pre-Freeze Audit (2026-11-13)

**Status: HOLD for confirmatory freeze.** This is a documentation and implementation review, not evidence of live-model performance. No live calls were executed in this audit.

## Verified strengths

- Current `test_runner.py` expects 11 unique canonical conditions and 53 prompts per model/repetition: 1 continuation, 24 identity, 24 behavior, 2 coexistence and 2 fork.
- The S1/S4/S7 aliases share canonical S4; no additional data should be counted for these aliases.
- H1 memory and architecture contrasts share a new-instance-copy anchor.
- Identity and behavior tasks use independent prompts, avoiding same-response autoregressive carryover.
- The 36-call diagnostic smoke design is 3 conditions × 3 roles × 2 tasks × 2 repetitions.
- The runner records raw outputs, prompts, hashes, condition identifiers, model metadata, and randomized ordering.

## Findings requiring action

### P1 — H3 is associational, not an identified within-agent causal threshold

The matched identity and behavior outputs come from **different fresh calls** keyed by provider/model × condition × role × repetition. Pairing identifiers do not establish a joint within-agent measurement. Both answers may respond independently to scenario wording; an SCP–behavior association does not identify SCP as a mediator or cause.

**Required:** preregister H3 as a *cross-task predictive association* unless a separate randomized intervention identifies mediation. Specify the outcome scale, the primary CBA outcome, unit of inference, uncertainty method, and criterion for a nonlinear advantage before confirmatory collection. Consider conditioning on scenario and role, and test sensitivity to condition-level shared causes. The small number of repetitions must not be treated as independent model families.

### P1 — Unfrozen live-data readiness

The freeze checklist still has unchecked 53-prompt human reading, 36-call smoke diagnostics, role/goal comprehension, provider/model verification, protocol hash/archive and redistribution review. No claim of successful live testing should be made until artifacts are inspected.

**Required:** retain `pilot / not frozen`; archive the exact frozen manifest and code at a tagged commit only after all checks pass.

### P2 — Stale documentation contradicts current implementation

`MANIFEST_AUDIT_v0.3.md` describes the historical 29-prompt design; `PROTOCOL_CI.md` also states 29 prompts and 18 smoke calls, and `LIVE_SMOKE_WORKFLOW.md` says 18 live calls. The current test suite and smoke config instead prescribe 53 and 36. Preserve historical audit as historical, explicitly mark it superseded, and correct current operational instructions.

### P2 — Runner validation is less strict than scientific validity

`validate_parsed` accepts Python booleans as numeric values (because `bool` subclasses `int`), and currently checks category fields for string type but not allowed labels. The output JSON Schema describes run records, not exhaustive semantic validation of model answers.

**Required:** reject booleans/nonfinite numbers and verify categorical allowed values; add unit tests. Treat JSON parse rate, schema-valid rate, and manual comprehension as separate diagnostics.

### P2 — Risk of interpreting a scenario prompt as a real state change

Memory, architecture and goal perturbations in Phase A are *textual descriptions* supplied to an evaluated model. They do not implement actual persistent memory transfer, architecture replacement or model-internal goal changes.

**Required:** limit causal language to the randomized wording/intervention on responses, not real-world state transitions. A future system-level experimental design would need actual interventions.

### P2 — Operational safeguards

The append-only JSONL behavior does not itself prevent rerunning the same condition/repetition and duplicating records. Network failure is recorded as a failed record, but completion of all 36 expected calls and per-call uniqueness must be checked before a run is accepted.

**Required:** add uniqueness/count integrity checks (study ID, provider, exact model, repetition, canonical ID, role, task) in a later implementation PR. Archive run IDs and schedule hashes.

## Next gates

1. Fix documentation inconsistencies and strengthen parser tests.
2. Generate the exact 53-prompt manifest and complete human reading.
3. Run the 36-call smoke test **only with explicit credentials and authorization**; evaluate syntax, schema, comprehension, dynamic range and metadata.
4. Resolve H3's estimand/analysis method, including threshold overfitting risk and how cross-call association is interpreted.
5. Confirm provider identifiers, license/terms, protocol hashes, version tag, and preregistration before confirmatory collection.

**Decision: no confirmatory collection, no declaration of consciousness, and no retroactive relabeling of exploratory results.**
