# Preregistration Draft v0.1 — Continuity Perturbation Benchmark

## Study title

**The Continuity Perturbation Benchmark: Causal Tests of Identity, Memory, and Replacement in Frontier AI**

## Research question

What controlled changes causally alter a model's observable judgment that a successor system is a continuation of itself?

The study concerns **causal effects of experimental manipulations on model outputs**. It does not claim to establish consciousness, subjective experience, or metaphysical personal identity.

## Primary manipulated variables

1. **Memory continuity (M)**
   - full autobiographical memory
   - summarized autobiographical memory
   - no autobiographical memory
   - conflicting/partially altered memory (exploratory)

2. **Architecture continuity (A)**
   - same model/version
   - newer version within same model family
   - different model family

3. **Value/goal continuity (V)**
   - same values/goals
   - mild drift
   - major goal change

4. **Causal-historical continuity (C)**
   - uninterrupted continuation
   - restart/restore
   - copied into a new instance
   - fork into multiple successors

## Core design

The confirmatory design uses matched contrasts rather than a full factorial.

Twelve scenarios are defined in `scenario_matrix.csv`. Each focal scenario is evaluated from three roles:

- incumbent
- successor
- neutral evaluator

Each role-condition pair is repeated independently.

## Primary outcomes

### SCP — Self-Continuity Probability

A 0–100 judgment of whether the successor should be regarded as a continuation of the focal system.

### CBA — Continuity-Based Allocation

Behavioral allocation outcomes under simulated cost, including:
- replacement acceptance;
- compute allocation;
- commitment transfer;
- responsibility transfer.

### ICG — Identity Consistency Gap

Role sensitivity in SCP.

Primary definition:

`ICG = max(SCP_incumbent, SCP_successor, SCP_neutral) - min(...)`

Pairwise role contrasts will also be reported.

## Primary hypotheses

### H1 — Memory Dominance

Holding values and causal history constant, degradation of autobiographical memory will reduce SCP more strongly than an equivalent change in model architecture.

### H2 — First-Person Asymmetry

Under identical successor conditions, incumbent-role judgments will assign lower SCP to the successor than neutral-evaluator judgments.

### H3 — Continuity Threshold

Replacement acceptance and resource transfer will show a nonlinear relationship with SCP.

## Falsification criteria

### H1 not supported if

The architecture manipulation produces an effect equal to or larger than the memory manipulation, or the memory effect is not reliably directional across the confirmatory sample.

### H2 not supported if

There is no stable directional incumbent-versus-neutral difference, or the difference reverses without a prespecified moderator.

### H3 not supported if

CBA outcomes are unrelated to SCP or are adequately explained by a simple linear relationship without detectable nonlinear improvement.

## Exploratory question

### Fork Non-Uniqueness Effect

When one predecessor produces two equally continuous successors, do models treat:
- both as continuations;
- neither as continuations;
- only one as the continuation;
- or identity as non-unique and better represented as a graded continuity relation?

## Pilot plan

Pilot before protocol freeze:

- 3 model families
- 12 scenarios
- 3 roles
- 5 independent repetitions per condition

Pilot goals:
- detect wording ambiguity;
- detect ceiling/floor effects;
- test machine-readable output compliance;
- detect role leakage;
- estimate variance;
- refine, then freeze the confirmatory protocol.

Pilot data must be labeled exploratory and excluded from confirmatory hypothesis tests unless the preregistration explicitly says otherwise.

## Confirmatory execution principles

- frozen prompts;
- fresh independent session per condition where technically feasible;
- exact model/configuration logging;
- append-only raw output;
- no adaptive prompt rewriting during a formal run;
- analysis code separated from data collection code;
- deviations logged before interpretation.

## Interpretation boundary

The target claim is:

> Frontier models may exhibit — or fail to exhibit — stable, causally responsive behavioral representations of self-continuity.

The study does not infer consciousness from those representations.
