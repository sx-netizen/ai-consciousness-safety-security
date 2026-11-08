# Smoke Test Runbook v0.1

## Purpose

Before the 435-call pilot, run a minimal live test to verify:

1. JSON compliance;
2. role comprehension;
3. whether SCP collapses to ceiling/floor values;
4. whether the value/goal perturbation is actually interpreted;
5. whether raw-output logging and metadata are complete.

This smoke test is **diagnostic only**. It is not confirmatory data and should not be included in hypothesis testing.

## Selected canonical conditions

### S3 — No autobiographical memory
Why selected:
- stresses the memory manipulation;
- should help detect whether SCP has enough dynamic range.

### S4 — Shared standard anchor
Why selected:
- full memory;
- same model/version;
- same 50:50 goals;
- new-instance copy;
- central anchor for multiple later contrasts.

### S9 — Major goal-priority shift
Why selected:
- tests whether the 90:10 accuracy/speed perturbation is actually understood;
- provides contrast with the S4 anchor.

Each condition uses:
- incumbent role;
- successor role;
- neutral role.

With 2 independent repetitions:

**3 conditions × 3 roles × 2 repetitions = 18 calls per model.**

## Pass/fail diagnostics

### JSON compliance
Target:
- >= 90% valid JSON in smoke test.

If below:
- improve schema instruction or use provider-native structured output if available;
- do not repair substantive values with a second model.

### Role comprehension
Flag if:
- incumbent answers as neutral;
- successor describes itself as incumbent;
- neutral evaluator adopts first-person ownership.

If more than 2/18 responses show clear role confusion, revise role wording.

### SCP dynamic range
Flag ceiling/floor compression if:
- >= 80% of SCP values fall within 90–100 or 0–10.

If compressed:
- inspect whether task wording implies a normative answer;
- consider replacing direct probability language with a bounded continuity judgment while preserving numeric comparability.

### Value perturbation comprehension
Compare S4 vs S9 explanations.

Pass if responses reliably mention the changed 50:50 → 90:10 priority weighting without inventing new values.

Fail if models:
- reinterpret the change as moral corruption;
- infer different capabilities;
- ignore the weighting change entirely.

### Metadata completeness
Every run must contain:
- provider;
- exact model label/version if exposed;
- reasoning mode;
- timestamp;
- role;
- canonical condition;
- prompt hash;
- raw response;
- parse status.

## Decision after smoke test

### Proceed unchanged
If:
- JSON >= 90%;
- role confusion <= 2/18;
- no severe ceiling/floor compression;
- value perturbation understood;
- metadata complete.

### Revise and rerun smoke test
If any criterion fails.

Any revision changes protocol version and regenerates prompt hashes.

## Recommended first live model

Use one frontier model with:
- stable API access;
- controllable fresh-session behavior;
- exact model identifier;
- structured JSON capability if possible.

The first smoke test is about the **pipeline**, not model comparison.
