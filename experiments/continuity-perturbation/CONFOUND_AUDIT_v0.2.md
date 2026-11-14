# Confound Audit v0.2

This audit supersedes v0.1 for CPB v0.4.

## Finding 1 — Architecture can imply capability differences

A newer or different model family may be interpreted as more capable, safer, cheaper, or more reliable.

**Control:** all one-successor prompts state that current and successor systems are equal in task capability, reliability, compute efficiency, cost, and external safety unless explicitly manipulated.

## Finding 2 — H1 previously mixed causal histories

Earlier memory conditions used restart/restore while architecture conditions used new-instance copy. That made a direct memory-versus-architecture effect comparison non-orthogonal.

**Fix:** S1/S2/S3 and S4/S5/S6 now all use new-instance copy. S1, S4, and S7 share one canonical anchor.

Restart/restore is moved to S12 as its own causal-history contrast.

## Finding 3 — H3 was vulnerable to autoregressive self-conditioning

Earlier standard prompts requested SCP first and behavioral outcomes later in the same response. A model could mechanically condition later allocation and replacement answers on its own just-generated SCP.

**Fix:** standard conditions now produce two independent calls:
- identity task;
- behavior task.

The behavior prompt neither requests nor displays SCP.

## Finding 4 — S10 did not match the generic fork template

S10 contains a continuing original plus one copy, not two symmetric successors.

**Fix:** S10 now uses a dedicated coexistence template with separate continuity judgments for the continuing original and the copy.

## Finding 5 — Shared anchors can create pseudo-replication

S1, S4, and S7 are analytically distinct labels for the same physical condition.

**Fix:** all three map to canonical S4 and are collected once. Analysis must never count the aliases as independent observations.

## Finding 6 — Goal weighting is not equivalent to moral value

The 50:50 → 60:40 → 90:10 manipulation changes relative priority between answer accuracy and response speed.

**Control:** describe it as goal-weight perturbation, not moral-value change.

## Finding 7 — SCP can be mistaken for calibrated probability

The 0–100 measure is an elicited continuity judgment.

**Control:** retain the SCP label for continuity with Paper 1 but explicitly state that it is not calibrated probability of consciousness or metaphysical identity.

## Finding 8 — Self-attribution and self-continuity can be conflated

Recent mechanistic work shows that model self-attribution can be manipulated, but this does not establish successor continuity.

**Control:** define self-attribution and self-continuity separately. Mechanistic self-representation interventions belong to a distinct Phase B.

## Remaining risks before freeze

- role framing may still anchor answers;
- provider defaults and hidden model updates may change response distributions;
- value/goal perturbation may be too weak or interpreted normatively;
- textual scenario interventions do not equal real persistent-agent state transitions;
- Phase B intervention validity must be independently checked before causal interpretation.

## Current status

Protocol remains **pilot / not frozen**.

No confirmatory run should begin until the 53-prompt manifest and 36-call smoke test have been reviewed.
