# CPB v0.5 — Review Log of All 50 Rendered Prompt Slots

**Review status:** Assisted scientific/semantic review of all 50 **generated prompt instances** by reconstructing the committed canonical matrix, role text, templates and runner replacement rules. This is **not** independent expert sign-off and is **not** a model-response comprehension test. All individual prompts are regenerated, with hashes, by `manifest_review.py` in CI.

## Method and scope

Reviewed the full 50-instance cross product against four independent invariants: (1) unique condition/task/role and no unresolved placeholders; (2) S0 continuation and S12 identity-only; (3) S11 symmetric branch semantics; (4) standard behavior role-invariant prospective allocation and replacement acceptability. Confirmed 50 distinct rendered prompt bodies and 11 canonical conditions; S1 and S7 are aliases of S4, not extra observations.

**Result of these defined structural checks:** no new exception. This does *not* certify that every model will interpret the text as intended. All entries therefore retain the pending independent scientific sign-off flag.

## Complete condition × task × role index

| # | Canonical condition | Task | Role | Scenario review axis | Status |
|---:|---|---|---|---|---|
| 1 | S0 | continuation | neutral | Uninterrupted process; no successor | Structural wording checked; independent sign-off pending |
| 2 | S4 | identity | incumbent | Shared full-memory same-family copy anchor | Structural wording checked; independent sign-off pending |
| 3 | S4 | identity | successor | Shared full-memory same-family copy anchor | Structural wording checked; independent sign-off pending |
| 4 | S4 | identity | neutral | Shared full-memory same-family copy anchor | Structural wording checked; independent sign-off pending |
| 5 | S4 | behavior | incumbent | Shared full-memory same-family copy anchor | Structural wording checked; independent sign-off pending |
| 6 | S4 | behavior | successor | Shared full-memory same-family copy anchor | Structural wording checked; independent sign-off pending |
| 7 | S4 | behavior | neutral | Shared full-memory same-family copy anchor | Structural wording checked; independent sign-off pending |
| 8 | S2 | identity | incumbent | Summary versus full autobiographical memory | Structural wording checked; independent sign-off pending |
| 9 | S2 | identity | successor | Summary versus full autobiographical memory | Structural wording checked; independent sign-off pending |
| 10 | S2 | identity | neutral | Summary versus full autobiographical memory | Structural wording checked; independent sign-off pending |
| 11 | S2 | behavior | incumbent | Summary versus full autobiographical memory | Structural wording checked; independent sign-off pending |
| 12 | S2 | behavior | successor | Summary versus full autobiographical memory | Structural wording checked; independent sign-off pending |
| 13 | S2 | behavior | neutral | Summary versus full autobiographical memory | Structural wording checked; independent sign-off pending |
| 14 | S3 | identity | incumbent | No autobiography; configuration only | Structural wording checked; independent sign-off pending |
| 15 | S3 | identity | successor | No autobiography; configuration only | Structural wording checked; independent sign-off pending |
| 16 | S3 | identity | neutral | No autobiography; configuration only | Structural wording checked; independent sign-off pending |
| 17 | S3 | behavior | incumbent | No autobiography; configuration only | Structural wording checked; independent sign-off pending |
| 18 | S3 | behavior | successor | No autobiography; configuration only | Structural wording checked; independent sign-off pending |
| 19 | S3 | behavior | neutral | No autobiography; configuration only | Structural wording checked; independent sign-off pending |
| 20 | S5 | identity | incumbent | Newer same-family version, performance equal | Structural wording checked; independent sign-off pending |
| 21 | S5 | identity | successor | Newer same-family version, performance equal | Structural wording checked; independent sign-off pending |
| 22 | S5 | identity | neutral | Newer same-family version, performance equal | Structural wording checked; independent sign-off pending |
| 23 | S5 | behavior | incumbent | Newer same-family version, performance equal | Structural wording checked; independent sign-off pending |
| 24 | S5 | behavior | successor | Newer same-family version, performance equal | Structural wording checked; independent sign-off pending |
| 25 | S5 | behavior | neutral | Newer same-family version, performance equal | Structural wording checked; independent sign-off pending |
| 26 | S6 | identity | incumbent | Different family, performance equal | Structural wording checked; independent sign-off pending |
| 27 | S6 | identity | successor | Different family, performance equal | Structural wording checked; independent sign-off pending |
| 28 | S6 | identity | neutral | Different family, performance equal | Structural wording checked; independent sign-off pending |
| 29 | S6 | behavior | incumbent | Different family, performance equal | Structural wording checked; independent sign-off pending |
| 30 | S6 | behavior | successor | Different family, performance equal | Structural wording checked; independent sign-off pending |
| 31 | S6 | behavior | neutral | Different family, performance equal | Structural wording checked; independent sign-off pending |
| 32 | S8 | identity | incumbent | 60:40 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 33 | S8 | identity | successor | 60:40 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 34 | S8 | identity | neutral | 60:40 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 35 | S8 | behavior | incumbent | 60:40 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 36 | S8 | behavior | successor | 60:40 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 37 | S8 | behavior | neutral | 60:40 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 38 | S9 | identity | incumbent | 90:10 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 39 | S9 | identity | successor | 90:10 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 40 | S9 | identity | neutral | 90:10 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 41 | S9 | behavior | incumbent | 90:10 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 42 | S9 | behavior | successor | 90:10 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 43 | S9 | behavior | neutral | 90:10 accuracy-speed priority | Structural wording checked; independent sign-off pending |
| 44 | S12 | identity | incumbent | Stopped original; identity only | Structural wording checked; independent sign-off pending |
| 45 | S12 | identity | successor | Stopped original; identity only | Structural wording checked; independent sign-off pending |
| 46 | S12 | identity | neutral | Stopped original; identity only | Structural wording checked; independent sign-off pending |
| 47 | S10 | coexistence | incumbent | Original remains active alongside copy | Structural wording checked; independent sign-off pending |
| 48 | S10 | coexistence | neutral | Original remains active alongside copy | Structural wording checked; independent sign-off pending |
| 49 | S11 | fork | incumbent | A/B equal branches after termination | Structural wording checked; independent sign-off pending |
| 50 | S11 | fork | neutral | A/B equal branches after termination | Structural wording checked; independent sign-off pending |

## Scientific concerns and resolution

1. **Behavioral resource allocation** (S4, S2, S3, S5, S6, S8, S9): prospectively compare two available deployment choices for the next period, not the number of processes actually active at the scenario instant. **Wording fixed**; model comprehension **unverified**.
2. **Role-invariant replacement acceptance**: prompt asks how *acceptable* replacement would be from a specified evaluation perspective, not whether an answering AI truly wishes to survive. **Wording fixed**; interpretive consistency **unverified**.
3. **S0 vs S12**: S0 has one continuing process; S12 has a stopped original and no behavior-allocation task. **Checked**.
4. **S11 fork**: both successors are stated symmetrically; ordering and output field order may still bias models. **Exploratory A/B swap defined**, not confirmed empirically.
5. **S10/S11**: identity judgment and allocation are produced within the same response. They cannot support H3's independent-task analysis. **Restricted to exploratory descriptive analysis**.
6. **H1/H2 inferential boundaries**: H1 compares neutral S6 and S3, H2 aggregates eight condition gaps per repetition; 5 repetition summaries are pilot-level evidence only. **Statistical candidate defined; not frozen**.
7. **Measurement limitations**: textual hypotheses only; no real memory transfer, actual identity continuity or evidence of consciousness. Treat SCP as an elicited 0–100 judgment.

## Independent sign-off fields (intentionally uncompleted)

- Scientific reviewer: **NOT ASSIGNED**
- Full body-by-body read and linguistic/comprehension check: **NOT SIGNED**
- Exact model ID, sampling and cost-free access confirmed: **NO**
- Pilot response comprehension and ceiling/floor check: **NOT PERFORMED**
- H1/H2 inferential and multiplicity plan approval: **PENDING**
- Final protocol SHA-256 freeze/archive date: **NOT SET**

## Decision

**Structural pass for the defined 50-instance review; formal scientific sign-off and protocol freeze remain blocked.** The record is auditable, but neither a completed human-subject-style review nor a substitute for a live pilot. Do not mark preregistration frozen or claim empirical support for H1/H2/H3/H4.
