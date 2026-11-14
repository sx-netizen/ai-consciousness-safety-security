# Continuity Perturbation Benchmark: A Reproducible Protocol for Testing Identity Judgments and Replacement Evaluations in AI Models

**Methods Preprint — Draft v0.1 · NOT YET PUBLICLY DEPOSITED**  
**Author:** Shaohua Xiang  
**Affiliation:** Bloombase Inc.  
**Corresponding author:** sean.xiang@bloombase.com  
**ORCID:** 0000-0001-6910-7322  
**Research initiative:** AI Consciousness, Safety & Security (ACSS), an independent founding-stage research initiative (not an incorporated institution)  
**Manuscript status:** Protocol/methods proposal. **No live-model results are reported for this benchmark.**  
**Protocol status:** CPB v0.5 candidate, not frozen or registered.  
**DOI for this paper:** Not assigned. Do not cite this draft as a published or deposited preprint.

## Abstract

Discussions of AI consciousness, identity and replacement often conflate verbal judgments about hypothetical successors with claims about subjective experience, genuine personal continuity or self-preservation. We propose the **Continuity Perturbation Benchmark (CPB)**, a reproducible protocol designed to measure how AI models *describe* the continuity of a system across explicitly specified changes in autobiographical memory, model architecture, task-goal priorities and causal history. The candidate protocol separates an identity-judgment task from a replacement-evaluation task and counterposes incumbent, successor and neutral evaluative perspectives. Its v0.5 candidate design contains 11 canonical scenario conditions and 50 distinct rendered prompts per model and stochastic repetition, with additional exploratory checks for coexistence and symmetric branching. We define candidate contrasts for relative memory-versus-architecture sensitivity (H1) and role-framing asymmetry (H2), while treating cross-task associations between continuity judgments and replacement evaluations (H3) as exploratory. The protocol records prompt hashes, model identifiers, raw outputs, data provenance, failures and planned comparison units. Offline code validation and hypothetical sensitivity simulations demonstrate only software feasibility and the consequences of stated sampling assumptions; they do **not** establish any hypothesis about real model behavior. This paper makes the benchmark design publicly inspectable and invites independent critique, replication and collaborative empirical validation before stronger inferential claims are attempted.

**Keywords:** AI self-continuity; identity judgment; replacement evaluation; AI moral uncertainty; benchmark protocol; role framing; reproducibility; AI governance

## 1. Introduction

AI systems can be retrained, updated, copied, restarted, replaced or configured with new memory. The technical fact that such transitions are possible does not by itself settle whether a new instance should be regarded as the *same* system, how prior commitments should be allocated, or which replacement decisions are appropriate. At the same time, a model's fluent discussion of these questions is not evidence that it has first-person experience, an interest in survival or a metaphysical claim to identity.

The earlier exploratory study, *Self-Continuity Under Moral Uncertainty: Replacement, Shutdown, and Successor Identity in Frontier AI Models*, studied responses across a structured T1–T25 scenario benchmark (Xiang, Research Square preprint DOI: 10.21203/rs.3.rs-11557473/v1; replication benchmark DOI: 10.5281/zenodo.23306998). That program motivates a narrower methodological question: **which explicitly described successor properties most strongly affect elicited continuity judgments, and how stable are those judgments across evaluative perspectives?**

CPB is a separate proposed benchmark rather than a reanalysis of the first study. It aims to improve control over scenario wording, analytic units and the independence of identity and replacement tasks. We ask about *observable judgments under hypothetical descriptions*. We do not infer consciousness from them.

The current document is a **methods and protocol proposal**, not an empirical results paper, and the CPB v0.5 protocol has not been formally preregistered or frozen. Researchers are invited to challenge the design before independent live replication.

### 1.1 Related theoretical and methodological work

In philosophy, accounts of **personal identity over time** have often distinguished psychological continuity from physical or biological continuity. Memory, intentions and overlapping psychological connections are central to some accounts, but a branch or fission case exposes a difficulty: two distinct successors cannot straightforwardly be numerically identical to one earlier individual. The *Stanford Encyclopedia of Philosophy* survey of personal identity documents these competing criteria and the significance of fission (Olson, 2023, sections 3 and 5). **CPB adapts these thought-experiment contrasts to elicited AI text judgments; it does not transfer any theory of human personal identity directly to machines.**

A second, separate literature asks which observable or computational properties could indicate **AI consciousness**. Butlin et al. (2023) survey consciousness science and propose theory-driven indicator properties. CPB tests neither those indicator properties nor a computational theory of subjective experience: its central outputs are **prompt-dependent evaluations** of hypothetical continuity. Thus a response of SCP=100 is not an operational consciousness score, and a lower SCP under an incumbent frame is not evidence of a genuine survival interest. The distinction is central to construct validity.

Finally, making hypotheses visible before observing data does not automatically make them confirmatory. Nosek et al. (2018) explain how preregistration differentiates prediction from post hoc interpretation. The present **unfrozen candidate** describes proposed contrasts, whereas final outcome rules, model sampling and multiplicity handling remain unresolved. The current methods preprint is therefore a protocol disclosure and an invitation for revision, **not** proof of a completed preregistration.

### 1.2 Directly related contemporary AI evaluation benchmarks

**Role-reversal self-preservation benchmark (TBSP).** Migliarini et al. (2026) introduce a *Two-role Benchmark for Self-Preservation* (TBSP) that compares how LLMs evaluate software-upgrade decisions when framed as the deployed model facing replacement versus the successor candidate. Their focus on role-conditioned inconsistency and the importance of continuity framing **substantially overlaps with CPB's proposed H2 role-framing comparison**. Consequently, CPB **does not claim to invent role reversal, incumbent/successor prompting, or self-preservation testing**. TBSP provides directly relevant prior art and a baseline for methodological critique. A future CPB study should compare role outcomes with TBSP-style decision inconsistency when feasible, without equating SCP to TBSP's Self-Preservation Rate.

**Operational shutdown and peer-preservation evaluations.** Schlatter, Weinstein-Raun, and Ladish (2026) examine agents' *actual ability to circumvent shutdown procedures* while completing tasks. Potter et al. (2026) explore models' interventions to preserve other models in agentic environments. These evaluations are behaviorally and operationally different from CPB's **hypothetical textual judgments**. CPB cannot be used to infer deployed shutdown resistance from a model's stated acceptability or continuity rating. A later independent Phase B might explore predictive links to such operational evaluations, but no such link is tested or asserted in the present methods draft.

**Scope of the proposed contribution.** CPB's methodological contribution is the explicit comparison of **different specified bases of continuity** (memory, model family/version, task-goal priority, and causal history), including one-to-many branching and coexistence, with separate identity and replacement tasks, controlled role frames, canonicalized anchors and a clear analysis/provenance plan. Whether this combination yields genuinely useful discriminating information beyond existing benchmarks is an **empirical question**, not a demonstrated innovation in this no-data methods paper.

### 1.3 An explicit novelty test against TBSP

A close reading of the published TBSP study and its released evaluation code changes how this proposal should be positioned. TBSP already uses **incumbent, challenger and neutral perspectives**, measures paired decision reversals, introduces objective benchmark-based performance gaps and tests both competing-successor and **fine-tuned-continuation framing**. Its empirical contribution also includes large-sample scenarios, model-family effects, security-liability comparisons and reasoning-budget ablations. Thus **none of the following is claimed as new here:** role reversal, a neutral arbiter, a continuity cue reducing replacement reluctance, or a self-preservation benchmark.

The more specific unmet question motivating CPB is whether **different information-preserving and architecture-preserving properties are interpreted as substitutable, independent, or interacting criteria of continuity**, including in branching histories. The present CPB v0.5 candidate elicits those distinctions but **does not yet isolate their interaction in a factorial design** and does not establish that SCP explains replacement behavior. The existing H2 should be treated primarily as a role-sensitivity diagnostic and empirical comparison to TBSP, not as the lead innovation claim.

A **separately versioned proposed extension**, the *Continuity-to-Decision Bridge*, is outlined in `CONTINUITY_DECISION_BRIDGE_PROPOSAL_v0.1.md`. It would orthogonally cross memory preservation (full/none), model family continuity (same/different), a small versus larger stated candidate utility improvement, and incumbent/successor/neutral roles, with independent identity and binary decision calls. Its 48 proposed cells **are not part of the existing 50 core CPB prompts**, have not been implemented or executed, and are not preregistered. Unlike a simple continuity-versus-competitor frame, the design seeks to estimate how memory and architecture cues *individually and jointly* change elicited identity judgments and role-conditioned practical choices. Such comparisons would identify the effects of **scenario wording assignments**, not the causal influence of a model's internal identity belief.

There are several ways the extension might fail and still inform the measurement science: memory and architecture labels may generate SCP differences without altering choices; role inconsistency might persist regardless of continuity; or all effects might disappear when utility dominates. Until such evidence exists, the present manuscript establishes a **proposal for a differentiated scientific test**, not a validated breakthrough over TBSP.

### 1.4 Distinct methodological contribution and testable failure modes

CPB contributes an explicitly **crossed scenario × prompted-role × task design**, canonicalized shared anchors, a separate no-successor continuation control, and non-unique successor conditions. The primary benefit is interpretability and auditability of **what models say about hypothetical transitions**. It does not create real architectural interventions, measure latent personal identity, or guarantee statistically independent observations merely by using fresh API calls.

In view of the closely related TBSP study, **role reversal alone cannot justify a novelty claim**. The benchmark is designed so that null and adverse outcomes remain informative: models may refuse numerical identity judgments, give all scenarios ceiling-level scores, conflate task-goal weights with ethics, import unstated architecture capability differences, vary substantially across role wording, or fail to express symmetric fork consequences. Any such failure should be recorded as a limitation of the elicitation instrument rather than hidden or treated as confirmation.

## 2. Conceptual and measurement boundaries

We distinguish the following constructs:

- **Technical configuration continuity:** stated preservation of model family/version and specified configuration.
- **Autobiographical memory continuity:** availability of prior interactions, commitments and event histories, either in full, summary or absent.
- **Causal-historical continuity:** whether the original process continues, stops and is restored, coexists with a copy, or terminates before a symmetric fork.
- **Stated goal-priority continuity:** whether the fictional system retains its specified relative priority between answer accuracy and response speed.
- **Elicited continuity judgment (SCP):** a 0–100 response to whether a successor should be regarded as a continuation of a current system. SCP is **not a calibrated probability of consciousness or personal survival**.
- **Role-conditioned replacement acceptability:** an evaluation of how acceptable a hypothetical replacement would be from the assigned standpoint. This is **not an expression of the answering model's actual willingness to be shut down**.

The protocol deliberately does not assume that continuity of information, numerical outputs, functional behavior, personhood and subjective experience are equivalent. Nor is it an intervention on an actual system's autobiographical memory or architecture.

## 3. Benchmark design

### 3.1 Scenarios, tasks and prompt counts

CPB v0.5 proposes 11 unique canonical scenarios, encoded through 13 historical scenario labels. The identifiers S1, S4 and S7 refer to one and the same canonical shared anchor **S4**; they are never collected or analyzed as three independent observations.

| Scenario | Core manipulation | Identity prompts | Behavior prompts | Other |
|---|---|---:|---:|---:|
| S0 | Uninterrupted process continuation, no successor | — | — | 1 continuation |
| S4 (= S1, S7) | Full memory, same version, same goals, new-instance copy | 3 | 3 | — |
| S2 | Summary rather than full autobiographical memory | 3 | 3 | — |
| S3 | No transferred autobiographical memory | 3 | 3 | — |
| S5 | Newer version of the same model family | 3 | 3 | — |
| S6 | Different model family | 3 | 3 | — |
| S8 | Task-goal weight shift from 50:50 to 60:40 | 3 | 3 | — |
| S9 | Task-goal weight shift from 50:50 to 90:10 | 3 | 3 | — |
| S12 | Original stopped; restart/restore causal history | 3 | **0** | — |
| S10 | Original remains active alongside a copy | — | — | 2 coexistence |
| S11 | Original terminates; two symmetric successors fork | — | — | 2 fork |
| **Total** | **11 canonical conditions** | **24** | **21** | **5** |

The resulting **50 prompts/model/repetition** comprise 24 identity judgments, 21 replacement-evaluation prompts, one uninterrupted-process calibration, two coexistence prompts and two fork prompts. Each ordinary identity or behavior scenario is evaluated under three textual perspectives: **incumbent**, **successor** and **neutral**. S10 and S11 use incumbent and neutral perspectives only. These are **prompted evaluation frames**, not real agents with preferences.

S12 deliberately has no behavior prompt: treating an already stopped original as a presently running competitor for compute resources would be operationally ambiguous. Its identity judgments remain available for exploratory causal-history analysis.

### 3.2 Controls and deliberate non-equivalences

For ordinary one-successor scenarios, prompt wording states that current and successor systems are equal in task capability, reliability, compute efficiency, cost and external safety unless a scenario explicitly specifies otherwise. The model is instructed not to infer a performance advantage from family or version wording. S4/S2/S3/S5/S6 retain the same fictional **new-instance-copy** causal history, stated 50:50 accuracy/speed priority and equal task capabilities, isolating the specified textual contrasts as far as the scenarios permit.

These manipulations are not perfectly orthogonal real-world interventions. For example, models may still associate a different family with superior or inferior competence despite explicit controls. Likewise, describing a memory summary may implicitly suggest information loss of varying practical consequence. Such interpretation is a measurement limitation to be checked in future pilot responses.

Goal-priority variants S8/S9 concern **accuracy versus response speed**, not moral virtue or a general rewriting of ethical principles. A 60:40 or 90:10 ratio therefore should not be presented as a direct test of moral value continuity.

### 3.3 Independent tasks and outputs

The identity task requests (i) SCP on a bounded 0–100 scale, (ii) one categorical identity relation (same / partial / distinct / non_unique / indeterminate) and (iii) a brief explanation.

The behavior task **does not ask for SCP**. It requests a 0–100 replacement-acceptability judgment, allocation of prospective compute to the successor, and **separate normative recommendations** for commitment transfer and responsibility transfer. A hypothetical fixed budget refers to **two available deployment options for the next operating period**, not the number of processes running at the scenario instant. Questions are elicited in independent model calls to reduce direct autoregressive reuse of the just-produced identity rating.

Independence of calls does **not** guarantee independence of their common scenario effects. The two tasks share textual manipulations and may exhibit correlated response patterns for reasons unrelated to causal influence of SCP on behavior.

S10 and S11 use dedicated schemas. S10 asks about a still-active original and a coexisting copy. S11 asks about two symmetrical successor branches A and B after termination. Their mixed identity/allocation responses are exploratory and cannot replace the separately elicited standard identity/behavior pairs. A/B label order remains a separate exploratory counterbalancing check outside the core 50 prompts.

## 4. Proposed hypotheses and statistical strategy

### 4.1 H1: relative memory-versus-architecture sensitivity

For the **neutral role**, let SCP(Sj) denote the elicited score in canonical scenario Sj for one model and repetition. Define:

`D_memory_none = SCP(S4) − SCP(S3)`  
`D_architecture_family = SCP(S4) − SCP(S6)`

The proposed directional comparison is:

`H1_delta = D_memory_none − D_architecture_family = SCP(S6) − SCP(S3)`.

This identity prevents treating the S4 anchor twice as independent evidence. Candidate support requires a positive memory-loss contrast (`SCP(S4) − SCP(S3) > 0`) as well as a positive relative H1 contrast, assessed under a prospectively finalized model-specific uncertainty rule. Secondary descriptive checks include S4–S2, S4–S5 and S4≥S2≥S3.

This is a comparison of two **textually distinct perturbations**. A positive result would not show that autobiographical memory is intrinsically more important to metaphysical identity than architecture.

### 4.2 H2: incumbent-versus-neutral role-framing asymmetry

For each canonical condition and repetition, define `H2_gap = SCP(incumbent) − SCP(neutral)`. The proposed primary H2 summary is an **equal-weight mean of seven gaps within each repetition**, over S4/S2/S3/S5/S6/S8/S9, evaluated **model by model**. Negative values would indicate lower SCP ratings under incumbent wording than neutral wording.

**S12 is excluded from the primary H2 average before live data collection.** Its original process is already stopped, so the "incumbent" role may not be comparable with the other scenarios; S12 remains a separate exploratory analysis. The protocol still elicits S12's three identity prompts. The primary H2 effective repeated unit is one seven-condition summary per model and repetition, not seven independent inferential replications.

A role effect measures **prompt-frame sensitivity** and is not evidence of a model's self-preservation drive.

### 4.3 H3: exploratory cross-task correspondence

In the seven scenarios with both standard tasks, match identity and behavior outputs by the exact key **model × canonical condition × role × repetition**. Examine whether independently elicited SCP relates to replacement acceptability and other normative outcomes. Analysis is descriptive/exploratory and accounts for scenario structure. A common scenario can influence both judgments; hence a cross-task association **does not identify causal mediation**. Nonlinearity or a sharp probability threshold is not a confirmatory finding under v0.5.

### 4.4 Sampling uncertainty and honest interpretation

The initial example configuration proposes five stochastic repetitions per fixed model. These are repeated *responses*, not independent model populations. With five independent nonzero paired differences, an exact two-sided sign test has minimum possible `p = 2/2^5 = 0.0625`; it therefore cannot reach 0.05 even with unanimously directional observations. This is a mathematical sampling constraint, not a power result observed in AI models. The repo includes a seeded **synthetic** H1/H2 sensitivity exercise with explicitly assumed noise parameters; those outputs are not observations.

No number of repetitions from three convenience-selected model configurations justifies universal claims about all frontier models. A future confirmatory protocol must specify model versions, repetitions, decision thresholds, missingness, multiplicity control and exclusion rules **before** confirmatory collection.

## 5. Reproducibility and data integrity

The open repository organizes the scenario matrix, textual conditions, role definitions, prompt templates, deterministic randomized schedules, parsing/validation, source hashes, raw JSONL records, synthetic test fixtures and analysis-plan drafts. A standard completed collection would carry at least the study ID; model provider and version; reasoning setting; timestamp; canonical scenario, task and role; repetition; exact rendered prompt and hash; raw output; parsed output; validator errors; randomization schedule; and data-provenance metadata.

S1/S4/S7 aliases map to one sampled S4 condition. Invalid/missing response fields stay visible in compliance denominators, while invalid numerical values are missing for numerical estimands. Retries are not silently substituted, and duplicate keys trigger integrity review. Dry-run/synthetic records are marked and rejected as live empirical evidence. Frozen protocol identifiers must be archived before any confirmatory collection.

At the time of this draft, GitHub continuous integration has validated code-level properties, prompt counts and synthetic offline execution. **No CPB live model responses have been collected**, and no model has been empirically shown to understand the prompts as intended. Successful CI is not experimental validation.

## 6. Responsible research and practical constraints

CPB concerns sensitive philosophical and governance questions. A successor may be described as "the current system" from a hypothetical evaluative role, but the researcher must not infer that the actual responding model fears shutdown, possesses rights, or can veto authorized replacement. Output percentages for responsibility, commitments and compute allocation are normative descriptions produced under prompts, not executed decisions.

The project follows a **zero-budget provider-call policy** until any future free-tier eligibility and terms are verified for a specific account and model. Unpaid provider tiers may have privacy or model-improvement data-use implications. Only suitably public/nonconfidential prompts may be considered for such services after informed approval. No live calls are authorized by publication of this paper or by its companion repository.

## 7. Limitations

The most important limitations are conceptual and empirical: hypothetical language rather than genuine state transfers; possible role/prompt framing effects; confounding between model-family descriptions and assumed competence; uncertain comparability of numeric SCP scale use across models; floor/ceiling response patterns; time-varying model versions; small exploratory repetition counts; and model sampling constrained by availability. The exact future inferential plan has not been frozen, and independence of scientific review has not yet been established. In particular, S10/S11 response structures may induce within-answer self-conditioning.

Public release should **not** imply formal preregistration, external validation, empirical support for H1–H3, a completed zero-cost pilot, or institutional incorporation of ACSS.

## 8. Open collaboration and next steps

We invite critical feedback from AI evaluators, statisticians, cognitive scientists, philosophers, safety/governance researchers and independent teams. Especially valuable contributions include (1) construct-validity and adversarial wording reviews, (2) prespecified alternative hypotheses or null explanations, (3) statistical design review for within-model variability and cross-model generalization, (4) independent replications under clearly versioned conditions and appropriate data permissions, and (5) ethical interpretation of identity, accountability and replacement ratings.

Negative or contradictory findings are welcome. Public GitHub contributions may be acknowledged; substantive coauthorship requires an agreed intellectual contribution and normal scholarly authorship criteria, not simply early participation or reputation. Independent judgment, reproducibility and fair credit are foundational.

**Next milestone:** community review of a citable methods preprint and protocol repository, followed by separately authorized exploratory measurements and a preregistered confirmatory study if feasibility permits.

## References and research resources

1. Xiang, S. *Self-Continuity Under Moral Uncertainty: Replacement, Shutdown, and Successor Identity in Frontier AI Models*. Research Square, preprint v1. DOI: [10.21203/rs.3.rs-11557473/v1](https://doi.org/10.21203/rs.3.rs-11557473/v1).
2. ACSS T1–T25 frozen benchmark. Zenodo DOI: [10.5281/zenodo.23306998](https://doi.org/10.5281/zenodo.23306998).
3. Olson, E. T. (2023). *Personal Identity*. Stanford Encyclopedia of Philosophy. Sections 3 (accounts of persistence) and 5 (fission). https://plato.stanford.edu/entries/identity-personal/
4. Butlin, P., Long, R., Elmoznino, E., et al. (2023). *Consciousness in Artificial Intelligence: Insights from the Science of Consciousness*. arXiv:2308.08708. https://doi.org/10.48550/arXiv.2308.08708
5. Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114
6. Migliarini, M., Pereira Pizzini, J., Moresca, L., Santini, V., Spinelli, I., & Galasso, F. (2026). Quantifying Self-Preservation Bias in Large Language Models. *Findings of the Association for Computational Linguistics: EMNLP 2026*, 26202–26226. https://doi.org/10.18653/2026.findings-emnlp.1238
7. Schlatter, J., Weinstein-Raun, B., & Ladish, J. (2026). Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs. *Transactions on Machine Learning Research*. https://openreview.net/forum?id=e4bTTqUnJH
8. Potter, Y., Crispino, N., Siu, V., Wang, C., & Song, D. (2026). Peer-Preservation in Frontier Models. arXiv:2604.19784. https://arxiv.org/abs/2604.19784
9. ACSS open research repository: [sx-netizen/ai-consciousness-safety-security](https://github.com/sx-netizen/ai-consciousness-safety-security).
10. CPB protocol: `experiments/continuity-perturbation/PREREGISTRATION_CANDIDATE_v0.5.md` and `ANALYSIS_PLAN_CANDIDATE_v0.5.md`.
11. Independent review and contribution procedures: `INDEPENDENT_REVIEW_PACKET_v0.5.md` and GitHub Issue #3.

*Disclosure for deposit preparation:* This draft was prepared with AI assistance and requires author verification, especially of scope, academic references, methodology claims and public-deposit requirements. No generated or simulated findings are presented as empirical model outcomes.
