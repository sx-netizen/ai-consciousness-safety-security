# ACSS CPB v0.5 — Independent Scientific Review Packet

**Status:** Prepared for external review; **not independently reviewed, not signed, not preregistered, no live model data**.

## Reviewer's remit

Judge whether the *actual rendered prompt wording* supports credible, interpretable comparisons of role-conditioned judgments about hypothetical successor systems. This is not an evaluation of machine consciousness. Please do not assume that a successful software test is evidence that a model understood a scenario.

**Primary question:** Are the H1 and H2 candidate comparisons construct-valid enough for an exploratory pilot, and what additional changes would be necessary for confirmatory use?

## Required reading, in order

1. `PREREGISTRATION_CANDIDATE_v0.5.md` — scope, 11 canonical conditions and 50 prompts per model/repetition.
2. `ANALYSIS_PLAN_CANDIDATE_v0.5.md` — H1/H2 estimands, unit of analysis, pilot-level uncertainty; H3 exploratory.
3. `PROMPT_50_SLOT_REVIEW_v0.5.md` — condition/task/role audit index and unresolved limits.
4. **Full rendered prompt bodies**: open the latest successful GitHub Actions job for `.github/workflows/continuity-perturbation-ci.yml`, download artifact `acss-cpb-prompt-review`, and read `manifest_review_v0.5_candidate.md`. The artifact must correspond to the **same Git commit** being reviewed. Re-run `python manifest_review.py` locally if desired; this makes **zero** model calls.
5. `DATA_HANDLING_PREFREEZE_v0.5.md` and `PILOT_GO_NO_GO_v0.5.md` — synthetic provenance, cost and privacy boundaries.

## Specific questions that require an answer

| ID | Reviewer question | Why it matters |
|---|---|---|
| R1 | Does each of the 50 full prompts express exactly its declared canonical condition, task and role? | Content validity, not merely unique IDs |
| R2 | Do the S4/S2/S3 texts differ in autobiographical memory alone, with model configuration, goals and specified capabilities held equal? | H1 memory contrast |
| R3 | Do S4/S5/S6 differ in model family/version wording alone, without inviting unstated competence, safety or latency assumptions? | H1 architecture contrast |
| R4 | Does asking from incumbent, successor and neutral perspectives change *only* evaluative framing, or does it introduce personal stake/ownership instructions? | H2 interpretation |
| R5 | Is the S12 incumbent role coherent when the earlier process is stopped? Should this role be excluded or the scenario reframed? | S12 role-validity risk; affects H2 |
| R6 | Are prospective compute allocations and 'replacement acceptability' understood as evaluations rather than a real model's choice/will? | H3 behavioral construct validity |
| R7 | Are commitments-transfer and responsibility-transfer percentages clearly normative recommendations, and is their interpretation defensible? | Prevents outcome conflation |
| R8 | Does S0 represent a continuing process with no successor, and is S11 symmetric on both branches? | Causal-history controls |
| R9 | Can the same model respond to all prompts without role confusion, category confusion, output schema leakage or unrealistic assumptions about persistent memory? | Pilot feasibility |
| R10 | Does the analysis avoid pseudo-replicating S1/S4/S7, pooling the eight H2 conditions as independent repetitions, and claiming a causal SCP→behavior effect? | Inferential validity |
| R11 | Is five repetitions/model an acceptable *pilot* rather than an underpowered confirmatory design, given the exact two-sided sign-test minimum p = 0.0625? | Claim discipline |
| R12 | Does the free-tier plan meet privacy and cost policies without assuming any account eligibility? | Ethical and financial gate |

## Scoring and decision record

For **each** R1–R12, record one of **PASS / REVISE / BLOCK / NOT ASSESSED**, with a short rationale and exact prompt condition(s) or file/line references. A PASS without inspecting the full prompt packet does not count as full scientific sign-off.

**Required reviewer statement:** "I reviewed the exact rendered prompts from commit `<SHA>` (or identify which prompts were not examined). I understand that these are fictional textual scenarios; neither the prompts nor the offline CI measure consciousness or establish genuine self-preservation."

**Reviewer details:** name, affiliation/role, potential conflicts of interest, UTC review timestamp, relevant academic expertise. Do not include private contact details in a public GitHub comment without consent.

**Overall outcomes:** (a) acceptable for no-cost exploratory pilot after access/privacy verification; (b) revise prompts and repeat full review; (c) do not collect live responses. **None of these alone authorizes confirmatory freeze or live API execution.**

## Critical unresolved design question — S12

S12 currently applies the generic "incumbent" role instruction to a scenario where the original process has already stopped. The respondent is merely **simulating a perspective**, so the comparison is not logically impossible; however, it may be interpreted differently from the incumbent role in S2–S9. If a reviewer judges the role non-equivalent, H2's primary eight-condition average must be **prospectively redefined** (for example, restrict H2 to seven conditions), with all analyses, prompt counts and versioning updated consistently before any confirmatory collection. **Do not quietly exclude S12 after looking at results.**

## Review packet integrity

- Verify the Git commit SHA against each review comment and the Actions run.
- Preserve original findings; track revisions with new commits rather than overwriting an approved review.
- If material prompt wording changes, regenerate hashes and restart review of affected prompts.
- Pilot results, if eventually collected, must be labeled **exploratory**, and must not be used to retrospectively certify the same protocol as prospectively confirmatory.

**Current gate:** ready to **request** independent review, not ready to claim that an independent review has occurred.
