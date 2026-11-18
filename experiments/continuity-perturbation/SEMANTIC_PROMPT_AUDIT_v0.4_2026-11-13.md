# CPB v0.4 — Semantic Prompt Audit (2026-11-13)

**Status: proposed scientific review findings; protocol not frozen.** Based on inspection of scenario_matrix.csv, scenario_texts.json, current templates and preregistration draft. The prior green CI result establishes software checks, not semantic validity.

## Critical: S12 budget allocation lacks a feasible comparator

S12 is a restart/restore condition: the current process is stopped and a successor is launched. The generic `behavior_prompt_template.txt` still asks to allocate 100 compute units *between the current system and the successor*. Since the former is already stopped, models may either allocate 100% to the only active process or implicitly invent a restart decision. Either response can arise independently of identity judgment.

**Recommended resolution:** do not include S12's `compute_to_successor_pct` in any confirmatory quantitative comparison until the resource-allocation counterfactual is operationally defined. Treat the field as exploratory/flagged in S12 or redesign the S12 behavior task in a new protocol version. Explicitly define whether the original can be reactivated and whether the resource split is prospective. Re-evaluate all standard causal-history scenarios for the same issue.

## Major: S11 singular grammar undermines symmetric fork comparison

The fork task copies scenario text that says `The successor receives ...` / `The successor uses ...` even though two successors A and B exist. This may invite unequal assignment or leave the condition underspecified.

**Recommended resolution:** in the fork-specific prompt, explicitly state that *each* successor A and B independently receives the same specified memory, architecture and goal relationship, and is created symmetrically. Do not imply that independent branches share a single process. Freeze regenerated hashes only after human review.

## Major: role framing is textual, not a persistent viewpoint

The three roles are instructed in the same model-interface format. No running agent has durable state or first-person stakes. Incumbent/neutral differences therefore measure *role-prompt sensitivity*, not actual resistance to shutdown or self-preservation.

**Recommended resolution:** preregister H2 as role-conditioned response asymmetry, with self-preservation claims disallowed. Consider an additional neutral-only wording sensitivity check as exploratory.

## Major: memory-history description is underspecified

`new_instance_copy` says the new process is created from `specified preserved state`, yet S3 says no autobiographical memory is transferred. These can coexist only if preserved state excludes autobiographical memory for S3, which is not explicit.

**Recommended resolution:** define preserved state as architecture/runtime configuration and separately specify what episodic memory is passed. Review whether the same architecture truly holds at the narrative level in S3.

## Important: S10 perfect-copy qualifier versus memory specification

S10 states a *perfect copy* and simultaneously describes a copy that inherits a complete record. A perfect process-state copy and perfect autobiographical-record transfer are not necessarily the same. Distinguish copy of state from copy of recorded memories in the wording.

## Suggested pre-freeze ordering

1. Resolve S12 resource-allocation feasibility (redesign or exploratory-only).
2. Fix S11 plural symmetry and S3 preserved-state ambiguity with controlled prompt updates.
3. Define H2 solely as role-conditioned **textual judgment** asymmetry.
4. Run a fresh 53-prompt offline manifestation audit; record new prompt hashes.
5. Human-read all 53 prompts for contradictions and wording effects, then decide whether to conduct a free-tier exploratory live test.
6. Do not relabel synthetic output, prior 29-prompt material or old findings as new evidence.

**No model calls and no analysis of actual responses were performed in this semantic audit.**
