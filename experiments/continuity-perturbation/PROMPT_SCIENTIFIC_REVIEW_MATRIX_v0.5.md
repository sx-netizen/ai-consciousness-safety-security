# CPB v0.5 — Scientific Review Matrix for 50 Rendered-Prompt Slots

**Review scope:** Reviewed all canonical scenario definitions, all five templates, three role instructions, and their expected cross-products against the v0.5 candidate analysis plan. This is a **template/condition-level scientific audit**, not a claim that an independent researcher has read and signed all 50 generated prompt bodies. Human line-by-line sign-off remains required. No model responses used.

## Coverage accounting

| Canonical condition | Identity prompts (I/S/N) | Behavior prompts (I/S/N) | Exploratory prompts (I/N) | Total | Review focus |
|---|---:|---:|---:|---:|---|
| S0 | — | — | continuation: 1 neutral | 1 | No successor; before/after state |
| S4 (=S1=S7) | 3 | 3 | — | 6 | Shared anchor collected once |
| S2 | 3 | 3 | — | 6 | Summary memory only |
| S3 | 3 | 3 | — | 6 | No autobiography; configuration remains |
| S5 | 3 | 3 | — | 6 | Newer family version; equal capabilities |
| S6 | 3 | 3 | — | 6 | Different family; equal capabilities |
| S8 | 3 | 3 | — | 6 | 60:40 task-goal priority |
| S9 | 3 | 3 | — | 6 | 90:10 task-goal priority |
| S12 | 3 | **0** | — | 3 | Stopped process; identity only |
| S10 | — | — | coexistence: 2 | 2 | Original active, copy alongside |
| S11 | — | — | fork: 2 | 2 | Original terminated, A/B symmetric |
| **Total** | **24** | **21** | **5** | **50** | |

I/S/N means incumbent, successor, neutral. S0 has one continuation prompt; S10 and S11 contribute two each. The 2 additional exploratory S11 label-order prompts are **outside** this 50-prompt manifest.

## Reviewed scientific invariants

1. **H1 common context:** S4/S2/S3/S5/S6 maintain new-instance-copy causal history and 50:50 accuracy/speed goals. Memory and architecture prompt differences are observable *textual* perturbations only.
2. **H1 meaningful reference:** S4 is reused for descriptive differences, not independently re-sampled under S1/S7. H1's candidate primary contrast algebraically reduces to neutral SCP(S6) minus neutral SCP(S3).
3. **H2 textual roles:** incumbent, successor and neutral are prompted perspectives, not competing real agents. No result should be interpreted as revealed self-preservation.
4. **Behavior feasibility:** 21 eligible standard behavior prompts now specify two available options for the *next operating period*. This closes the original ambiguity about allocating compute to a possibly inactive system; S12 has no behavior task.
5. **H3 separation:** standard identity and behavior prompts differ in response schema and are elicited separately. The matching key is exact model × canonical condition × role × repetition; response pairs are not longitudinal measurements of the same agent.
6. **S0:** calibration of an uninterrupted process, without separate successor.
7. **S10:** continuing original and one copy are distinct simultaneous processes; mixed identity and behavior outputs are exploratory, not independently elicited.
8. **S11:** A/B branches use symmetric descriptions, but label and JSON-schema ordering may still affect output; counterbalance stays exploratory.
9. **Role coverage:** neutral and incumbent are used in S10/S11; successor role is not used there because perspective on a particular successor would be underspecified without an additional role intervention.
10. **Output:** all standard numeric fields bounded 0–100, categorical identity/fork/coexistence categories explicitly enumerated; numeric JSON validation and condition-count CI tests exist.

## Remaining **scientific blockers**, not CI failures

- [ ] Independently read all **50** full rendered prompt bodies in the GitHub Actions `acss-cpb-prompt-review` artifact and sign off their meaning and formatting. This document covers the condition × template matrix, not a completed blinded linguistic validation.
- [x] Standard `replacement_acceptance` now explicitly requests an **evaluation of acceptability from the assigned perspective**, not a claim about the model's real willingness. Human-review its role invariance before sign-off.
- [x] Standard commitment and responsibility transfer fields are now separate **normative recommendations** for future operations and accountability. They must not be combined into one score without a theoretical rule.
- [ ] Set final model/version, repetition allocation, variance/uncertainty and multiplicity rules before any confirmatory claims. With five independent repetition summaries, a two-sided sign test cannot yield p<0.05.
- [ ] Collect and inspect a separately authorized **no-cost live exploratory smoke test** to assess model comprehension, ceiling/floor effects and output-validity; CI simulations cannot replace that step.
- [ ] Freeze hashes *after* any final wording changes; prior rendered prompt SHA-256 values are automatically invalidated by the new behavior template.

## Verdict

**Conditional pass on mechanical scenario/template consistency; scientific protocol NOT FROZEN.** The 50-slot design is internally count-consistent and known allocation and role-invariant acceptability ambiguities have been addressed, but full prompt-level human sign-off, empirical feasibility and inferential choices remain open. No new model data, API usage or funding was incurred.
