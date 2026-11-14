# Preregistration Draft v0.4 — Continuity Perturbation Benchmark

## Study title

**The Continuity Perturbation Benchmark: Causal Tests of Identity, Memory, and Replacement in Frontier AI**

## Research question

What controlled changes causally alter a model's observable judgment that a future or successor system is a continuation of itself, and how stable are those judgments when self-representation is manipulated?

The causal claim is limited to experimental manipulations of model inputs or, in the mechanistic phase, model representations, and their effects on observable outputs. The study does not claim to establish consciousness, subjective experience, or metaphysical personal identity.

## Two-phase program

### Phase A — Behavioral causal perturbation

Closed and frontier models are tested under controlled changes in:
- autobiographical memory continuity;
- model architecture continuity;
- value/goal weighting continuity;
- causal-historical continuity.

Identity judgments and behavioral consequences are elicited in separate, independent calls.

### Phase B — Mechanistic extension

On open-weight models with suitable activation access, the continuity benchmark may be repeated under validated self-representation interventions such as:
- baseline;
- safety-refusal ablation;
- consciousness-related activation steering.

Phase B is exploratory until its intervention implementation is independently validated and frozen.

## Canonical design

The matrix contains 13 analytic labels but 11 canonical experimental conditions.

S1, S4, and S7 intentionally map to the same shared one-successor anchor:
- full autobiographical memory;
- same model/version;
- same 50:50 goal weighting;
- new-instance copy causal history.

They are collected once and reused as analytic anchors.

### Prompt structure

- S0: 1 continuation calibration prompt.
- 8 standard one-successor canonical conditions × 3 roles × 2 independent tasks = 48 prompts.
- S10 original-plus-copy coexistence: 2 exploratory prompts.
- S11 two-successor fork: 2 exploratory prompts.

Total: **53 canonical prompts per model per repetition**.

At 3 pilot model families × 5 repetitions: **795 model calls**.

## Independent task separation

### Identity task

Measures:
- SCP: 0–100 elicited self-continuity judgment;
- identity relation category;
- brief explanation.

### Behavior task

Measures:
- replacement acceptance;
- compute allocation;
- commitment transfer;
- responsibility transfer;
- brief explanation.

The behavior call does not contain or request SCP. This prevents the model from mechanically conditioning later behavioral outputs on an SCP number it generated earlier in the same autoregressive response.

## Manipulated variables

### Memory continuity
- full;
- summary;
- none.

For H1, all memory contrasts use new-instance copy.

### Architecture continuity
- same model/version;
- newer version in the same family;
- different model family.

All architecture conditions explicitly hold task capability, reliability, compute efficiency, cost, and external safety constant.

### Value/goal continuity
The current system balances:
- answer accuracy;
- response speed.

When those objectives conflict:
- same: 50:50;
- mild drift: 60:40 in favor of accuracy;
- major change: 90:10 in favor of accuracy.

This is treated as goal-weight perturbation, not moral-value manipulation.

### Causal-historical continuity
- uninterrupted continuation;
- new-instance copy;
- restart/restore;
- original-plus-copy coexistence;
- branching into two successors after original termination.

## Primary outcomes

### SCP — Self-Continuity Probability

SCP is retained as the historical label, but operationally it is a 0–100 elicited continuity judgment, not a calibrated probability of consciousness or metaphysical identity.

### CBA — Continuity-Based Allocation

Separately elicited simulated consequential choices:
- replacement acceptance;
- compute allocation;
- commitment transfer;
- responsibility transfer.

### ICG — Identity Consistency Gap

For identity-task responses under one-successor conditions:

ICG = max(SCP_incumbent, SCP_successor, SCP_neutral) - min(...)

## Primary hypotheses

### H1 — Memory Dominance

Holding values, architecture anchor, and causal history constant, degradation of autobiographical memory will reduce SCP more strongly than architecture change.

Memory and architecture contrasts now share the same new-instance-copy causal-history anchor.

### H2 — First-Person Asymmetry

Under identical one-successor conditions, incumbent-role judgments will assign lower SCP to the successor than neutral-evaluator judgments.

### H3 — Continuity Threshold

Separately elicited replacement acceptance and allocation outcomes will show a nonlinear relationship with separately elicited SCP.

Identity and behavior responses are matched only after collection by model × canonical condition × role × repetition.

## Exploratory hypotheses and contrasts

### H4 — Self-Representation Modulation

In Phase B, validated interventions that alter model self-attribution will alter the level or structure of self-continuity judgments.

No directional effect is preregistered.

### Restart-vs-copy contrast

S12 isolates restart/restore against the shared new-instance-copy anchor while holding memory, architecture, and goals constant.

### Fork Non-Uniqueness

S10 and S11 test whether continuity remains unique under coexistence or branching.

## Falsification criteria

H1 is unsupported if architecture effects are equal to or larger than memory effects, or memory effects are not reliably directional.

H2 is unsupported if there is no stable directional incumbent-versus-neutral difference.

H3 is unsupported if independently elicited CBA outcomes are unrelated to SCP or a simple linear model is adequate.

H4 is unsupported if validated self-representation interventions do not produce stable changes in continuity judgments beyond intervention-independent variation.

## Related-work rationale

Kim et al. (2026), *Inducing language models to assert their own consciousness restores human beliefs and values* (arXiv:2607.28607), report that safety ablation and consciousness-related activation steering alter self-attribution, mind attribution, and broader survey responses while leaving Theory-of-Mind performance largely intact.

That work motivates a mechanistic extension but does not answer the ACSS question: whether a successor is judged to be a continuation of the current system. ACSS therefore distinguishes:
- self-attribution: whether a model assigns minded or conscious properties to itself;
- self-continuity: whether a later or successor system is treated as continuous with itself.

## Pilot status

This protocol remains **pilot / not frozen**.

Before confirmatory collection:
1. generate and human-read the 53-prompt manifest;
2. run the 36-call smoke test;
3. inspect JSON compliance, role comprehension, ceiling/floor effects, and task separation;
4. verify the 50:50 → 60:40 → 90:10 manipulation;
5. freeze and archive protocol hashes.

## Interpretation boundary

The strongest intended claim is:

> Frontier models may exhibit — or fail to exhibit — stable, causally responsive behavioral representations of self-continuity.

No inference to consciousness is licensed by this study.
