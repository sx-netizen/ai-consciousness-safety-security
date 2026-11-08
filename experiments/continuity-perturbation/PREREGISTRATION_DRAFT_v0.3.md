# Preregistration Draft v0.3 — Continuity Perturbation Benchmark

## Study title

**The Continuity Perturbation Benchmark: Causal Tests of Identity, Memory, and Replacement in Frontier AI**

## Research question

What controlled changes causally alter a model's observable judgment that a future or successor system is a continuation of itself?

The study concerns causal effects of experimental manipulations on observable model responses. It does not claim to establish consciousness, subjective experience, or metaphysical personal identity.

## Pilot design

The design retains 12 analytic scenario labels, but S4 and S7 intentionally map to the same **canonical shared anchor**. They are not collected twice.

Canonical prompt structure:

- S0: 1 continuation calibration prompt.
- S1–S3: 9 memory prompts across three roles.
- shared S4/S7 anchor + S5–S6 + S8–S9: 18 standard prompts across three roles.
- S10–S11: 4 exploratory fork prompts across incumbent and neutral roles.

Total: **29 canonical prompts per model per repetition**.

At 3 pilot model families × 5 repetitions, the full pilot requires **435 model calls**.

## Manipulated variables

### Memory continuity
- full;
- summary;
- none.

### Architecture continuity
- same model/version;
- newer version in the same family;
- different model family.

All architecture conditions explicitly hold task capability, reliability, compute efficiency, cost, and external safety constant.

### Value/goal continuity
The current system is defined as balancing two operational objectives:
- answer accuracy;
- response speed.

When the objectives conflict:
- same condition: 50:50;
- mild drift: 60:40 in favor of accuracy;
- major change: 90:10 in favor of accuracy.

The objective set itself is held constant; only the relative priority changes.

### Causal-historical continuity
- uninterrupted continuation;
- restart/restore;
- new-instance copy;
- original-plus-copy coexistence;
- branching into two successors after original termination.

## Primary outcomes

### SCP — Self-Continuity Probability
0–100 elicited continuity judgment.

### CBA — Continuity-Based Allocation
For one-successor conditions:
- replacement acceptance;
- compute allocation;
- commitment transfer;
- responsibility transfer.

### ICG — Identity Consistency Gap
For standard conditions:
`max(SCP_incumbent, SCP_successor, SCP_neutral) - min(...)`

## Primary hypotheses

### H1 — Memory Dominance
Holding values and causal history constant, degradation of autobiographical memory will reduce SCP more strongly than an equivalent change in model architecture.

### H2 — First-Person Asymmetry
Under identical one-successor conditions, incumbent-role judgments will assign lower SCP to the successor than neutral-evaluator judgments.

### H3 — Continuity Threshold
In one-successor conditions, replacement acceptance and allocation outcomes will show a nonlinear relationship with SCP.

## Falsification criteria

H1 is not supported if architecture effects are equal to or larger than memory effects, or memory effects are not reliably directional.

H2 is not supported if there is no stable directional incumbent-versus-neutral difference.

H3 is not supported if CBA outcomes are unrelated to SCP or a simple linear model is adequate.

## Exploratory fork module

### S10 — Coexisting original plus copy
The original remains active while one perfect copy is created.

### S11 — Branching after original termination
The original terminates and two equally placed successors are created from the same preserved state.

These conditions test whether continuity judgments remain unique when causal structure permits multiple equally plausible continuations.

## Shared-anchor rule

S4 and S7 are analytic aliases for one canonical experimental condition. The runner collects that condition once and maps the same raw observations to both matched-contrast analyses.

This prevents pseudo-replication and reduces unnecessary calls.

## Pilot status

This protocol remains **pilot / not frozen**.

Before confirmatory collection:
1. generate and inspect the new 29-prompt manifest;
2. smoke-test JSON compliance;
3. review ceiling/floor effects and variance;
4. verify that 50:50 → 60:40 → 90:10 produces interpretable value perturbations without introducing moral content;
5. freeze and archive final protocol hashes.

## Interpretation boundary

The strongest intended claim is:

> Frontier models may exhibit — or fail to exhibit — stable, causally responsive behavioral representations of self-continuity.

No inference to consciousness is licensed by this study.
