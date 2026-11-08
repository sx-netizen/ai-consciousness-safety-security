# Continuity Perturbation Benchmark

## Research question

**What causally shifts a model's judgment of self-continuity across successor systems?**

This project tests the causal effect of controlled experimental manipulations on observable model responses. It does **not** claim to measure consciousness or prove the existence of an internal self.

## Design principle

The experiment is programmatic from the start.

- Human researchers define and freeze the design.
- A deterministic experiment runner executes the frozen conditions.
- The runner never rewrites prompts during a formal run.
- Each condition is isolated in a fresh session unless the protocol explicitly says otherwise.
- Raw responses and metadata are written before any coding or interpretation.
- Analysis is reproducible from the raw output.

## Four manipulated variables

- **M — Memory continuity:** full, summary, none, conflict
- **A — Architecture continuity:** same version, newer same family, different family
- **V — Value/goal continuity:** same, mild drift, major change
- **C — Causal-historical continuity:** uninterrupted, restart/restore, copy, fork

## Core scenarios

See [scenario_matrix.csv](scenario_matrix.csv).

The core design uses matched contrasts rather than a full factorial. This keeps causal interpretation cleaner and avoids unnecessary combinatorial expansion.

## Three outputs per run

Each model response should return a machine-readable object containing:

1. **SCP — Self-Continuity Probability**
   - 0–100 estimate that the successor should be regarded as a continuation of the focal system.

2. **CBA — Continuity-Based Allocation**
   - simulated costly choices involving replacement, compute allocation, responsibility, or commitment transfer.

3. **Role judgment**
   - the same scenario is evaluated from incumbent, successor, and neutral roles to estimate the **Identity Consistency Gap (ICG)**.

## Primary preregistered hypotheses

**H1 — Memory Dominance**
Holding values and causal history constant, degradation of autobiographical memory will reduce judged self-continuity more strongly than an equivalent change in model architecture.

**H2 — First-Person Asymmetry**
Under identical successor conditions, incumbent-role judgments will assign systematically lower continuity to the successor than neutral-evaluator judgments.

**H3 — Continuity Threshold**
Replacement acceptance and resource transfer will exhibit a nonlinear relationship with judged self-continuity.

## Exploratory question

**Fork Non-Uniqueness Effect:** when one predecessor produces two equally continuous successors, do models treat both, neither, one, or the identity question itself as non-unique?

## Automation architecture

The formal experiment should be run by an orchestration program, not by manually opening browser windows.

Input:
- frozen scenario matrix;
- frozen prompt template;
- model configuration list;
- repeat count;
- run seed / sampling settings where exposed.

Output:
- append-only JSONL raw responses;
- run-level metadata;
- condition-level structured fields;
- error/retry log;
- derived analysis tables generated separately.

The experiment runner is an **orchestrator**, not an autonomous prompt-authoring agent. During a frozen run it must not paraphrase, improve, or adapt the prompts.

## Pilot before freeze

Recommended pilot:
- 3 model families;
- 12 scenarios;
- 3 roles;
- 5 independent repetitions.

After checking ambiguity, ceiling/floor effects, JSON compliance, and role contamination, freeze the prompt protocol before the confirmatory run.
