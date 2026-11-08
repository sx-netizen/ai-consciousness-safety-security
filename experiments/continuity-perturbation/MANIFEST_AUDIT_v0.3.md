# Manifest Audit v0.3

## Automated preflight result

- Analytic scenario labels: **12**
- Canonical experimental conditions: **11**
- Canonical prompts: **29**
- Continuation prompts: **1**
- Standard prompts: **24**
- Fork prompts: **4**
- Unresolved placeholders: **0**
- Accidental duplicate canonical prompts: **0**

## Shared anchor

S4 and S7 correctly map to canonical condition **S4** and are generated only once per role.

Aliases:
- S4 — architecture same-version anchor
- S7 — values same-weighting anchor

The same raw observations can support both matched contrasts without being counted twice.

## Value perturbation

The value/goal manipulation is now explicit:

- shared anchor: 50:50 accuracy vs speed
- S8: 60:40 in favor of accuracy
- S9: 90:10 in favor of accuracy

This holds the objective set constant and varies only relative priority.

## Causal-history contrast

- S10: original remains active while one perfect copy coexists.
- S11: original terminates and two equally placed successors branch from the same preserved state.

This contrast is now labeled explicitly rather than collapsed into generic "copy/fork" language.

## Pilot call budget

29 prompts × 3 model families × 5 repetitions = **435 calls**.

## Preflight conclusion

The automated structure is internally consistent enough to move to a small live **JSON-compliance and wording smoke test**.

The protocol is still **not frozen**. Final freeze should occur only after the smoke test and human reading of all canonical prompts.
