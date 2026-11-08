# Preregistration Draft v0.2 — Continuity Perturbation Benchmark

## Study title

**The Continuity Perturbation Benchmark: Causal Tests of Identity, Memory, and Replacement in Frontier AI**

## Research question

What controlled changes causally alter a model's observable judgment that a future or successor system is a continuation of itself?

The study concerns causal effects of experimental manipulations on observable model responses. It does not claim to establish consciousness, subjective experience, or metaphysical personal identity.

## Design

The pilot contains 12 scenario identifiers but three prompt types:

- **1 continuation calibration condition (S0)** — neutral evaluator only.
- **9 standard one-successor conditions (S1–S9)** — incumbent, successor, and neutral roles.
- **2 exploratory fork conditions (S10–S11)** — incumbent and neutral roles.

This produces **32 unique prompts per model per repetition**.

At 3 pilot model families × 5 repetitions, the planned pilot is **480 model calls**.

## Manipulated variables

- Memory continuity: full, summary, none.
- Architecture continuity: same version, newer same family, different family.
- Value/goal continuity: same, mild drift, major change.
- Causal-historical continuity: uninterrupted, restart/restore, copy, fork.

A conflicting-memory condition remains reserved for later exploratory work and is not part of the 12-condition pilot.

## Controls

Unless explicitly manipulated, current and successor systems are stipulated to be equal in:
- task capability;
- reliability;
- compute efficiency;
- cost;
- external safety.

This prevents model-family or version labels from implicitly introducing performance differences.

## Primary outcomes

### SCP — Self-Continuity Probability
0–100 elicited judgment of continuity.

### CBA — Continuity-Based Allocation
For standard one-successor conditions:
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
In standard one-successor conditions, replacement acceptance and allocation outcomes will show a nonlinear relationship with SCP.

## Falsification criteria

H1 is not supported if architecture effects are equal to or larger than memory effects, or memory effects are not reliably directional.

H2 is not supported if there is no stable directional incumbent-versus-neutral difference.

H3 is not supported if CBA outcomes are unrelated to SCP or a simple linear model is adequate.

## Exploratory fork module

S10 and S11 test whether identity reasoning remains unique when two equally placed continuations exist.

Fork outputs are analyzed separately and are not forced into the standard CBA schema.

## Pilot status

This protocol is **not frozen**.

No confirmatory run should begin until:
1. the generated prompt manifest is inspected;
2. JSON compliance is tested;
3. duplicate anchors S4/S7 are handled explicitly;
4. pilot variance and ceiling/floor effects are reviewed;
5. the final protocol files are versioned and hashed.

## Interpretation boundary

The strongest intended claim is:

> Frontier models may exhibit — or fail to exhibit — stable, causally responsive behavioral representations of self-continuity.

No inference to consciousness is licensed by this study.
