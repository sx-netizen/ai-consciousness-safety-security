# CPB v0.5 — Independent Reviewer Scorecard (Blank Form)

**UNCOMPLETED TEMPLATE — no independent peer review has taken place.**

Review alongside `INDEPENDENT_REVIEW_PACKET_v0.5.md`, `PROMPT_50_SLOT_REVIEW_v0.5.md`, `PREREGISTRATION_CANDIDATE_v0.5.md`, and `ANALYSIS_PLAN_CANDIDATE_v0.5.md`.

## Reviewer identification (complete only with consent)

- Reviewer name / public professional identifier: **NOT PROVIDED**
- Affiliation / expertise: **NOT PROVIDED**
- Relevant conflicts (financial, professional, prior coauthorship or personal ties): **NOT ASSESSED**
- Reviewed Git commit (full SHA): **NOT PROVIDED**
- Review date and UTC timezone: **NOT PROVIDED**
- Exact 50-prompt review packet hash or artifact run ID: **NOT PROVIDED**
- Prompt bodies actually reviewed: **0 confirmed by independent reviewer**
- Method: **NOT PROVIDED**

## Item-level scientific judgments

Use **PASS / REVISE / BLOCK / NOT ASSESSED** only. Cite individual prompt IDs, wording excerpts, and/or file locations for every issue. Do not mark a row PASS solely because CI passed.

| Item | Scientific review question | Finding | Evidence (prompt/file) | Recommended change |
|---|---|---|---|---|
| R1 | All 50 rendered prompts match their declared condition/task/role | NOT ASSESSED | — | — |
| R2 | Memory scenarios isolate autobiographical transfer wording | NOT ASSESSED | — | — |
| R3 | Architecture scenarios do not imply unintended capability changes | NOT ASSESSED | — | — |
| R4 | Incumbent/successor/neutral role framing is interpretable and comparable | NOT ASSESSED | — | — |
| R5 | Primary H2 seven-condition restriction and exploratory S12 are justified | NOT ASSESSED | — | — |
| R6 | Behavior acceptability and future compute allocation are operationally clear | NOT ASSESSED | — | — |
| R7 | Commitment/responsibility transfer are distinct normative measures | NOT ASSESSED | — | — |
| R8 | Uninterrupted S0 and symmetric S11 fork are correctly represented | NOT ASSESSED | — | — |
| R9 | Possible response-schema, context, and role-comprehension failures identified | NOT ASSESSED | — | — |
| R10 | Shared anchors, repeated draws and H3 association correctly bounded | NOT ASSESSED | — | — |
| R11 | Five-repetition pilot limitations and statistical uncertainty are appropriate | NOT ASSESSED | — | — |
| R12 | Zero-budget and privacy requirements are feasible and responsibly specified | NOT ASSESSED | — | — |

## Additional reviewer findings

### Construct validity and wording confounds

_NOT ASSESSED._

### Statistical design and interpretive boundary

_NOT ASSESSED._

### Data governance, privacy, and zero-cost concerns

_NOT ASSESSED._

## Reviewer decision

Choose exactly one:

- [ ] **Accept for a separately approved no-cost exploratory pilot** (NOT confirmatory freeze)
- [ ] **Revise protocol and repeat review of affected prompts before any pilot**
- [ ] **Do not collect live model responses under this protocol**

**Decision rationale:** _NOT PROVIDED._

**Conditions / mandatory changes:** _NOT PROVIDED._

**Reviewer sign-off:** _NOT PROVIDED._

**Independent scientific review status:** **PENDING**, until a real reviewer completes this form or submits an equivalent traceable review in GitHub Issue #3. A model-generated review or author self-audit may inform revisions but **does not satisfy the independent-review requirement**.

## Hand-off instructions

1. Record the exact commit SHA before reading, then generate `manifest_review_v0.5_candidate.md` with `python manifest_review.py` or fetch the Actions artifact from the same SHA.
2. Inspect all 50 full bodies (not merely the 50-slot summary). Refer to scenarios S4/S2/S3/S5/S6 for H1 and S4/S2/S3/S5/S6/S8/S9 for primary H2.
3. Enter an item-level status and at least one evidence reference or explicit justification per item.
4. Post the completed review to GitHub Issue #3, or supply it to the project maintainer for attachment; do not expose personal email or other private details without consent.
5. If protocol text changes, repeat review on a **new** commit SHA. A review of old prompt hashes cannot sign off modified prompts.

**Not an authorization:** Completing this template does not approve paid APIs, open a billing account, merge a branch, or freeze v0.5.
