# ACSS Research Landscape and Problem Discovery — Evidence Register v0.1

**Date:** 2026-11-13. **Scope:** published papers, preprints, public workshop submissions, standards drafts, public research programs, released code where identifiable. **Purpose:** determine *whether* Paper 2 has a worthwhile original question before writing a title or building a benchmark. This is an open evidence register, **not a completed systematic review or a novelty/priority certification**. Web discovery can miss unpublished work, non-indexed preprints, paywalled sources and private team plans.

## Research decision and freeze

**PAUSE:** Paper 2 title, preprint deposit, protocol freeze, live API calls, public claims of originality, and experimental extension building.

**PRESERVE:** CPB v0.5 candidate and v0.1/v0.2 prose as historical exploratory assets. New named proposal `Identity Is Not Authority` is **NOT an approved thesis**. Independent-review Issue #3 remains a feedback channel, not an endorsement.

**START:** question-first discovery: clusters, teams, timestamps, exact measured objects, methods, limitations, overlapping hypotheses and prospective falsifiers.

## Search approach used in first pass

Targeted combinations of `AI successor identity`, `model replacement`, `fork rollback`, `memory continuity`, `AI agent authority`, `authorization evidence`, `benchmark`, `model identity`, `self-preservation bias`, `identity leakage`, `agent handoff`, `responsibility`, `delegation`, `preprint`, `OpenReview`, `arXiv`; cross-checked publisher/arXiv/SSRN/IETF/NIST pages when possible. Included 2025–2026, not only peer-reviewed research.

This is **scoping**, not PRISMA: search index coverage, exact counts, full-paper risk-of-bias assessment and citation-network closure remain incomplete. Do **not** claim exhaustive search.

## Literature map (priority sources; version and evidence status)

| Track | Source / date / venue or status | What was *already done* | Significance for ACSS |
|---|---|---|---|
| Role-conditioned self-preservation | Migliarini et al. (2026), TBSP, Findings EMNLP, DOI 10.18653/2026.findings-emnlp.1238 | Role-reversed upgrade decisions, neutral role, same-self fine-tuning framing, 23 models | Role reversal, succession framing and neutral controls **NOT novel** |
| Prompted multi-agent identity | Del Giudice et al. (2026), arXiv:2609.35928 | Identity labels induce factional coordination and cooperation loss | Prompted family labels and group-level identity effects **NOT novel** |
| Successor identity theory | Konstantinidis (2026), SSRN:7391218 | Computational, mnemonic, dispositional and interactional continuity; fission and rollback | Multiple continuity dimensions and forks **NOT novel as a concept** |
| Persistent agent identity measurement | Zhao & Zhao (2026), PAI-Bench, arXiv:2609.13637 | Identity contracts: recall, enactment, lineage, update; external scoring oracle | Identity vs behavior distinction **NOT novel** |
| Persistent runtime identity | Zhao & Zhao (2026), arXiv:2609.00546 | Continuity-bearing substrate and authorized migration | Actual runtime continuity mechanisms **NOT novel** |
| Authority across AI generations | Zhu & Wang (2026), arXiv:2610.00347 | Population-safe authorization succession across replacement/fork/rollback, executable validation | Fork authority conservation and external enforcement **NOT novel** |
| Policy-relative successor state | He & Yu (2026), Cognitive Continuity Test / IdentityLineageBench, arXiv:2610.00132 | Policy-relative valid/invalid state transitions, 24 families and verified fixtures | State transition identity/authorization checks **NOT novel** |
| Agent continuity kernel | He & Yu (2026), arXiv:2608.11632 | Transactional identity/state activation across long-lived agents | Continuity-as-governed-state mechanism **NOT novel** |
| Memory authority laundering | Cerruti, Okamoto & Erol (2026), EAL-Bench, arXiv:2609.01836, v2 Oct 24, NeurIPS PALM workshop accepted | Memory incorrectly introduces or preserves authority, propagates to downstream unauthorized action | **High overlap with last proposed Identity–Authority Leakage**; updated v2 claims up to 45.4% false authority and 99.0% executor action once false authority exists. Do not repeat older v1 percentages |
| Authorization before memory context | Liu (2026), arXiv:2609.36373 | Audience-constrained memory lifecycle; independent admission before context | Memory-based authorization and provenance already evaluated |
| Agent handoff continuity | Li et al. (2026), HSC-Bench, arXiv:2610.36523 | 1,039 task takeovers, evidence and commitment continuity | Handoff/commitment inheritance **NOT a blank research area** |
| Interruption recovery | ContinuityBench (2026), OpenReview preprint | h0/h1/h2 handoff information, interruption recovery | Partial/full/no-memory contrasts already common |
| Delegation attack evaluation | Dantuluri & Sundi (2026), arXiv:2609.00267 | Broker-enforced delegation, confused-deputy/impersonation threats | External policy gate and delegation bypass **NOT novel** |
| Authorization survey | Zhou & Zhang (2026), arXiv:2611.06764 | Access control research across policy, delegation, action, information flow | Current field taxonomy and open questions |
| Stronger runtime/control contract | Su (2026), arXiv:2611.15515 | Incentive/authority contract at runtime and 240 LLM runs | Textual incentive and actual authority must be separated |
| Identity and continuity standards | IETF `draft-drake-agent-identity-problem-statement-01` (Oct/Nov 2026 draft, not RFC) | Actor identity, transfer, history, accountability | Identity/persona/authorization distinctions actively standardized |
| Delegation and obligations | IETF `draft-luna-eagf-agent-delegation-semantics-01` (Oct/Nov 2026 draft, not RFC) | No implicit authority transfer; accountable owner; evidence and decision references | Policy/obligation separation already public |
| NIST agent IAM | NIST blog *Design Tenets for Agent Identity Management Systems* (2026) | Dynamic permissions, least privilege, authority separation and external checks | Governance norms and enterprise controls actively evolving |
| Agent values | Dong et al. (2026), Agent-ValueBench, arXiv:2605.10365 | 394 executable environments, value-conflict assessment | Goal-value tests not novel without stronger causal question |
| General agent research surveys | Yehudai et al. (2026) ACL Findings survey; Surapani et al. (2026) arXiv:2609.15906 | Broad evaluation and authorization architecture surveys | Use as seed sources for citation snowballing |

**Additional current relevant work to inspect:** agent-memory poisoning benchmarks (MemSecBench, MPBench), philosophical “continuity as autonomy” research, model-consciousness indicators, and consent/privacy at memory migration. Distinguish standards **draft** from adopted standards.

## Key danger: previous proposed Paper 2 themes overlap prior art

1. **CPB 50 prompts:** only offline design. Three-role and partial memory conditions overlap TBSP/PAI/handoff work; not enough for a claim of original empirical contribution.
2. **48-cell memory × architecture bridge:** a factorial repackaging may be an incremental test; not enough as the *sole* novelty without a deeper hypothesis and informative null alternatives.
3. **Identity–Authority Leakage:** direct overlap with EAL-Bench and policy-relative continuity verifiers. The mere existence of policy-invalid permissions induced by memory or continuity is **not an untouched phenomenon**.
4. **Forked rights and obligations:** formal succession and IETF delegation/identity drafts already address them. Rebranding as self-continuity is not innovation.
5. **Runtime or long-horizon continuity:** existing open work already covers executable kernels, handoff continuity and identity contracts.

## Question-first candidates to investigate, NOT approved research questions

### Q-A: Evidential authority of a continuity judgment (philosophy / epistemology)
When a model's own report of continuity is uncertain, inconsistent or self-contradictory, **what evidence could justify any operational decision contingent on that report**? Can a principled reliability calibration be designed beyond simple SCP self-ratings? Strong overlap risk: PAI-Bench, moral-status literature, evidence-based governance. Need concrete falsifier and human/technical reference criteria.

### Q-B: Under-determination in non-unique continuation (metaphysics / formal theory)
For two competing successors preserving *different noncomparable* dimensions of continuity, can any publicly defensible decision rule allocate continuation status **without covert priority assumptions**, and what counterexamples defeat it? Strong overlap risk: Successor Problem, continuity kernels and fork authorization. Must distinguish numerical identity, psychological continuation, role continuation and permission.

### Q-C: Moral uncertainty and reversibility under irreversible successor transitions (decision theory)
Do uncertain identity/moral-status beliefs yield new **reversibility, option-preservation or procedural-duty** criteria for authorized replacement, independent of the model's claimed preferences? Strong overlap risk: moral uncertainty, precautionary principles, shutdown/corrigibility, future welfare. Requires formal assumptions, quantitative tradeoffs and falsifiable predictions.

### Q-D: Cross-layer semantic failure under contradictory evidence (empirical safety)
Can a model track **evidence provenance, permitted action and responsibility separately** when identity cues, memory provenance and operator mandates disagree? Highest existing overlap with EAL-Bench / CCT / delegation benchmarks; only worthwhile with *new information-theoretic or experimental generalization* beyond their tested failure modes.

### Q-E: Distinguishing self-continuity claims from model role conformity (measurement science)
Can we construct an **identifiability test** to distinguish verbal-role compliance from stable transition-invariant continuity judgments, and prove or empirically bound what cannot be inferred from single-session text? Strong overlap with TBSP, identity-label factionalism and PAI-Bench. Needs genuine measurement-theoretic proposition, not another prompt suite.

### Q-F: Adversarial model/world mismatch (control / architecture)
What changes when the successor's **actual permissioned capabilities** conflict with its self-description and memory, and enforcement operates outside the LLM? Existing auth-broker and provenance literature is extensive; must specify independent control outcomes not already established.

**None currently merits a “first,” “novel,” or Paper 2 title claim.** Each must be reviewed against 3–5 nearest works, examined for theory and empirical testability, and accepted only after a decisive contrast is found.

## Gated next discovery workflow

1. **Search completeness:** redo queries in Semantic Scholar, OpenAlex, Crossref, arXiv, SSRN, OpenReview/NeurIPS workshops, ACL Anthology, IEEE/ACM, IETF/NIST, and relevant public repos. Record search dates, queries, hit counts, exclusion reasons and paper versions. Missing access must be stated.
2. **Forward/backward citation chaining:** start with TBSP, Prompted Identity, EAL-Bench, CCT, PAI-Bench and Authorization Succession; read references, citing papers, linked artifacts, workshop revisions and author homepages. Distinguish verified current work from inferred unpublished activity.
3. **Team map:** TBSP–Del Giudice/Spinelli/Galasso; Cerruti/Okamoto/Erol; Zhao/Zhao; Zhu/Wang; He/Yu; Li et al.; Standards/IETF/NIST; philosophy clusters. List public activity and possible adjacent questions, not assumed private agendas.
4. **Method matrix:** For each nearby work log problem, construct, interventions, true runtime vs prompt fiction, outcome, oracle/ground truth, claims, sample, model versions, code availability, limitations, next stated goals, and risk of overlap.
5. **Problem candidates:** each must have a **one-sentence question, closest competitor, distinction, decisive test or proof, expected negative result, and reason it matters beyond academic count**.
6. **Stop rule:** Reject ideas reducible to swapping prompt labels, adding another axis without unique identification, or renaming existing authority/identity controls. If none survives, **no Paper 2**, continue literature exploration.

**No automatic reminders, API calls, paper submission, repo merge, requests to external authors or DOI deposit authorized.**

## Source links

- https://aclanthology.org/2026.findings-emnlp.1238/
- https://arxiv.org/abs/2609.35928
- https://ssrn.com/abstract=7391218
- https://arxiv.org/abs/2609.13637
- https://arxiv.org/abs/2609.00546
- https://arxiv.org/abs/2610.00347
- https://arxiv.org/abs/2610.00132
- https://arxiv.org/abs/2608.11632
- https://arxiv.org/abs/2609.01836
- https://arxiv.org/abs/2609.36373
- https://arxiv.org/abs/2610.36523
- https://arxiv.org/abs/2609.00267
- https://arxiv.org/abs/2611.06764
- https://arxiv.org/abs/2611.15515
- https://arxiv.org/abs/2605.10365
- https://datatracker.ietf.org/doc/html/draft-drake-agent-identity-problem-statement-01
- https://www.ietf.org/archive/id/draft-luna-eagf-agent-delegation-semantics-01.html
- https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems
