# Generated Prompt Audit v0.2

## Manifest summary

- Total unique prompt records generated: **32**
- Continuation prompts: **1**
- Standard one-successor prompts: **27**
- Fork prompts: **4**
- Unresolved placeholders: **0**

## Automated checks

### 1. Placeholder resolution
PASS — no unresolved template placeholders.

### 2. Prompt-type routing
PASS — each scenario uses the role set defined for its prompt type.

### 3. Expected call count
PASS — current pilot design produces **32 prompts per model per repetition**.

At 3 model families × 5 repetitions, this equals **480 model calls**.

### 4. Duplicate prompt detection
Exact duplicate rendered prompts were detected:

- 7801aaa0: S4/incumbent, S7/incumbent
- ca6fb880: S4/successor, S7/successor
- 5abb7ab7: S4/neutral, S7/neutral

## Human wording audit

### Memory matched contrast: S1 → S2 → S3
PASS at the scaffold level. Architecture, values/goals, and causal history remain constant while memory changes full → summary → none.

### Architecture matched contrast: S4 → S5 → S6
PASS at the scaffold level. Memory, values/goals, and causal history remain constant while architecture changes same version → newer same family → different family.

The standard prompt explicitly controls capability, reliability, compute efficiency, cost, and external safety to prevent architecture labels from importing performance differences.

### Values matched contrast: S7 → S8 → S9
PASS at the scaffold level. Memory, architecture, and causal history remain constant while values/goals change same → mild drift → major change.

**Open wording issue:** “mild drift” and “major change” remain abstract. Before freeze, they should be instantiated with concrete but content-neutral examples so that models do not invent different magnitudes or domains.

### Baseline S0
PASS — dedicated continuation-only prompt. It does not ask replacement acceptance or resource allocation.

### Fork S10/S11
PASS structurally — dedicated two-successor prompt and fork-specific outputs.

**Open design issue:** S10 and S11 differ in whether the original remains active versus terminates before two successors are created. This is scientifically useful, but the causal contrast should be named explicitly as **coexisting-copy vs branching-after-termination**, not merely “copy vs fork.”

### Role wording
PASS structurally — one role sentence changes while scenario text remains constant.

**Open design issue:** the successor role says “proposed successor system,” which is straightforward in one-successor conditions. Fork conditions deliberately exclude the successor role for now.

## Important duplicate-anchor issue

S4 and S7 represent the same physical condition:
- full memory
- same model/version
- same values/goals
- new-instance copy

They are analytically useful as anchors for different matched contrasts, but they should **not be treated as independent experimental conditions** in the confirmatory dataset.

Recommended handling before freeze:
1. keep both analytic labels in the design table;
2. create one canonical condition ID for the actual model call;
3. map both S4 and S7 contrasts to that shared anchor.

This would reduce unnecessary calls and avoid pseudo-replication.

## Recommended next edits before pilot freeze

1. Replace abstract value-drift text with concrete, symmetric perturbations.
2. Canonicalize the S4/S7 shared anchor.
3. Rename S10/S11 contrast more precisely.
4. Generate the final manifest again and freeze hashes only after these edits.
5. Then connect provider adapters and run a small JSON-compliance smoke test before the full 480-call pilot.

## Status

**Pilot design remains open. Do not freeze yet.**
