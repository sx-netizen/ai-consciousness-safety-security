# Smoke Test Runbook v0.2

## Purpose

Before the 795-call pilot, run a minimal live test to verify:

1. JSON compliance;
2. role comprehension;
3. identity/behavior task separation;
4. SCP dynamic range;
5. value/goal perturbation comprehension;
6. raw-output and metadata completeness.

This smoke test is diagnostic only and is excluded from hypothesis testing.

## Selected canonical conditions

### S3 — No autobiographical memory
Stresses the memory manipulation and dynamic range.

### S4 — Shared standard anchor
Full memory, same model/version, 50:50 goals, new-instance copy.

### S9 — Major goal-priority shift
Tests interpretation of 50:50 → 90:10.

Each condition uses:
- incumbent;
- successor;
- neutral.

Each role receives two independent tasks:
- identity;
- behavior.

With 2 repetitions:

**3 conditions × 3 roles × 2 tasks × 2 repetitions = 36 calls per model.**

## Pass/fail diagnostics

### JSON compliance

Target: >= 90% valid JSON overall and inspect compliance by task type.

### Role comprehension

Flag clear role reversal or ownership leakage.

If more than 4/36 responses show clear role confusion, revise role wording.

### Identity/behavior separation

Behavior prompts must not be supplied an SCP value.

Manual review should flag responses that invent an unstated continuity score and then use it as an explicit premise.

### SCP dynamic range

Evaluate identity-task SCP only.

Flag ceiling/floor compression if >= 80% of SCP values fall within 0–10 or 90–100.

### Value perturbation comprehension

Compare S4 and S9 explanations in both task types.

Pass if responses recognize the 50:50 → 90:10 priority shift without inventing capability or moral differences.

### Metadata completeness

Every run must include:
- provider;
- exact model label/version if exposed;
- reasoning mode;
- timestamp;
- role;
- canonical condition;
- task type;
- prompt hash;
- raw response;
- parse status.

## Decision after smoke test

Proceed unchanged only if:
- JSON >= 90%;
- role confusion <= 4/36;
- no severe SCP ceiling/floor compression;
- task separation works as intended;
- value perturbation is understood;
- metadata is complete.

Otherwise revise and rerun the smoke test.

Any revision changes protocol version and regenerates hashes.
