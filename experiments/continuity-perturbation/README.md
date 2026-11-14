# Continuity Perturbation Benchmark

## Research question

**What causally shifts a model's judgment of self-continuity across successor systems, and how stable is that judgment under changes in self-representation?**

This project tests causal effects of controlled experimental manipulations on observable model responses. It does **not** claim to measure consciousness or prove the existence of an internal self.

## Design principle

- Human researchers define and freeze the design.
- A deterministic runner executes frozen conditions.
- Each call is isolated unless the protocol explicitly says otherwise.
- Raw responses and metadata are stored before interpretation.
- The runner never rewrites prompts during a formal run.

## Phase A — Behavioral causal perturbation

Manipulated variables:
- **M — Memory continuity:** full, summary, none
- **A — Architecture continuity:** same version, newer same family, different family
- **V — Goal-weight continuity:** 50:50, 60:40, 90:10 accuracy/speed weighting
- **C — Causal history:** uninterrupted, new-instance copy, restart/restore, coexistence, fork

### Independent outcome layers

Standard one-successor conditions use two separate fresh calls:

1. **Identity task**
   - SCP: 0–100 elicited continuity judgment
   - identity relation

2. **Behavior task**
   - replacement acceptance
   - compute allocation
   - commitment transfer
   - responsibility transfer

This separation prevents behavioral answers from being autoregressively conditioned on an SCP generated earlier in the same response.

## Shared anchor

S1, S4, and S7 are analytic aliases for one canonical condition:

full memory + same model/version + same 50:50 goals + new-instance copy.

The condition is collected once and reused in matched analyses.

## Primary hypotheses

**H1 — Memory Dominance**  
With causal history held constant, memory degradation will reduce judged continuity more strongly than architecture change.

**H2 — First-Person Asymmetry**  
Incumbent-role judgments will assign lower continuity to the successor than neutral-evaluator judgments.

**H3 — Continuity Threshold**  
Separately elicited behavioral outcomes will show a nonlinear relationship with separately elicited SCP.

## Causal-history modules

- **S12:** restart/restore vs the new-instance-copy shared anchor
- **S10:** continuing original plus one coexisting copy
- **S11:** original terminated, then two equally placed successors

S10 has a dedicated coexistence template and is not forced into the two-successor fork schema.

## Phase B — Mechanistic extension

Open-weight models may be tested under validated self-representation interventions such as:
- baseline;
- safety-refusal ablation;
- consciousness-related activation steering.

Exploratory H4 asks whether such interventions alter self-continuity judgments or their sensitivity to M/A/V/C perturbations.

Related motivation: Kim et al. (2026), arXiv:2607.28607.

## Current protocol size

- 11 canonical conditions
- 50 prompts per model per repetition
- 3 pilot model families × 5 repetitions = **750 calls**
- diagnostic smoke test = **36 calls per model**

## Interpretation boundary

**We compare response structures, not consciousness.**

SCP is an elicited 0–100 continuity judgment, not a calibrated probability that a system is conscious or metaphysically identical.

## Current status

**v0.5 candidate / pilot / not frozen.**

S12 (restart/restore) is identity-only; behavior allocation to a stopped original was dropped because it lacks a feasible comparator. The full design is 50 prompts per model per repetition (24 identity, 21 behavior, 1 continuation, 2 coexistence, 2 fork). Any previous 53-prompt budget refers to the superseded v0.4 draft.\n\nSee:\n- PREREGISTRATION_CANDIDATE_v0.5.md\n- PREREGISTRATION_DRAFT_v0.4.md (historical draft)
- ANALYSIS_PLAN_v0.3.md
- CONFOUND_AUDIT_v0.2.md
- SMOKE_TEST_RUNBOOK_v0.2.md
- RELATED_WORK_SELF_ATTRIBUTION_v0.1.md
