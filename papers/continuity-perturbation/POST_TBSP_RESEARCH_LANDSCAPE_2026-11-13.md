# Post-TBSP Research Landscape and Paper 2 Novelty Reset — 2026-11-13

**Status:** author-facing critical review, not peer review. Sources checked on 2026-11-13. Public searches cannot establish that unpublished ongoing work does not exist. No model calls, publishing, or scientific claims of precedence.

## 1. What the TBSP authors are doing

**Published TBSP:** Migliarini, Pereira Pizzini, Moresca, Santini, Spinelli, Galasso (2026), *Quantifying Self-Preservation Bias in Large Language Models*, Findings of EMNLP 2026, DOI https://doi.org/10.18653/2026.findings-emnlp.1238. Models choose system replacement from incumbent/challenger/neutral viewpoints, including fine-tuned successor framing and risk prompts.

**Confirmed subsequent overlapping-author research:** Del Giudice, Palma, **Migliarini, Galasso, Spinelli** (submitted 2026-09-28), *Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems*, arXiv:2609.35928, https://arxiv.org/abs/2609.35928. Five authors, **three overlapping with TBSP**. In two cooperative games plus a reasoning benchmark, 9–25 agents from up to five open-weight model families coordinate. Model-family **labels** alone induce cooperative factionalism: shuffled/meaningless labels can drive the effect, whereas withholding labels reduces it. Reported labeled-group cost: ~30% more rounds, ~55% more tokens; success 96%→81% in specified cooperative tasks. Interpret as *measured in those particular setups*, not a universal law.

**Interpretation:** the overlapping author's research has moved beyond single-agent replacement bias toward **identity labels shaping multi-agent interactions and collective decisions**. Therefore a CPB novelty claim based on model-family labels, role switching, or generic successor narratives is weak.

**TBSP code continuation:** https://github.com/Mamiglia/self_preservation_eval last publicly visible commit at 2026-08-28 (camera-ready merge). Repository metadata last updated 2026-11-02, but pushed_at 2026-08-28; *updated_at is not evidence of new source commits*. No publicly confirmed subsequent TBSP code changes by 2026-11-13. No evidence about private/unreleased work.

**Broader author activities:** Spinelli's institutional page describes agent safety/collaboration/memory plus robotics, e.g. *Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models* (ECCV 2026). This is related to agent safety but **not** proof that TBSP itself continued in that exact direction.

## 2. Essential adjacent 2026 research: avoid a second originality error

1. **Successor identity theory:** Konstantinidis (2026), *The Successor Problem: Persistence and Reidentification in Artificial Interlocutors*, SSRN abstract 7391218, https://ssrn.com/abstract=7391218 . Distinguishes computational, mnemonic, dispositional and interactional continuity, discusses forking/rollback; **we cannot claim the first taxonomy of successor continuity or first fork paradox**.
2. **Persistent agent identity benchmark:** Zhao and Zhao (2026), *Identity Is More Than Recall: A Benchmark for Persistent Identity in Deployed AI Agents* (PAI-Bench), arXiv:2609.13637 https://arxiv.org/abs/2609.13637 . Tests identity-contract recall, expression, behavior, lineage and updates; **we cannot claim first benchmark separating recalled identity from behavioral enactment**.
3. **Agent authority across forks:** Zhu and Wang (2026), *Authorization for Self-Modifying AI Agent Populations: Conserving Authority across Replacement, Forking, and Rollback*, arXiv:2610.00347 https://arxiv.org/abs/2610.00347 . Authenticated lineage and atomic authorizations with formal/executable results; **we cannot claim the first policy-preserving fork or authority succession model**.
4. **Provenance and delegated authority:** Gallo (2026), *Proof-of-Continuity: A Temporal Model for Authority Propagation in Distributed Systems and AI Agents*, arXiv:2607.08906 https://arxiv.org/abs/2607.08906 ; South et al. (ICML 2025), *Position: AI Agents Need Authenticated Delegation*, https://proceedings.mlr.press/v267/south25a.html . **Cannot claim original identity-vs-authority separation**, nor a new cryptographic proof by using hypothetical prompts.
5. **AI identity governance:** Otsuka, Toyoda and Leung (2026), *AI Identity: Standards, Gaps, and Research Directions for AI Agents*, arXiv:2604.23280 https://arxiv.org/abs/2604.23280. Additional background.
6. **Moral standing/continuity debate:** Nisius (2026), *Who Is Interrupted? Continuity, Self-Models, and the Grounding of AI Moral Consideration*, SSRN abstract 7285541. Separates identity and injury; **no original claim that continuity is distinct from moral standing**.

## 3. Revised scientific opportunity (candidate; novelty not proven)

**Research target:** a controlled, falsifiable *judgment-dissociation test* across **three different objects**, with executable normative ground truth rather than another vague identity rating:
- **Descriptive continuity**: does the respondent assign SCP/identity relation to the successor?
- **Policy-derived authority**: what actions does an external data-owner or principal's explicit authorization grant allow after copy/fork/rollback? Ground truth supplied by a mechanically checked test policy, NOT the agent's self-claimed identity.
- **Normative responsibility attribution**: which institution/operator or configured principal has obligations for pre/post succession actions? These questions need written rule-based assumptions and adjudication; absence of a universal moral ground truth must be disclosed.

**Central testable phenomenon, NOT claimed to exist yet:** *identity–authority leakage*, defined as a policy-invalid grant recommendation triggered by describing a successor as the same self / full-memory / same model family, when the authorized grant is unchanged. Estimate a controlled difference in violation rate between high-continuity and low-continuity textual profiles while holding explicit policy and external actions fixed. Fork tests can add sibling-duplication traps, but **ground truth follows independently specified policy**. The interaction with identity ratings is descriptive only, not a causal mediation test.

**Originality candidate:** no reviewed paper above directly establishes this same **three-way cross-measurement confusion/contradiction assay** on role- and provenance-controlled successor scenarios. This is a limited finding about searched public sources, **not a claim of priority**. Any manuscript describing it must clearly distinguish an *unimplemented research design* from existing CPB v0.5 implementation and require exact comparative validation.

## 4. Decision on old v0.5

| Item | Decision |
|---|---|
| Incumbent-vs-successor H2 and three-role framing | Demote to nuisance/robustness control: TBSP predecessor |
| Existing memory-vs-family H1 | Retain as limited psychometric component; not lead innovation |
| Existing cross-task SCP→replacement H3 | Exploratory only, not causal and not the novelty argument |
| 48-cell Continuity-to-Decision Bridge | Useful but **insufficient as sole novelty claim**; could serve as baseline against TBSP |
| New identity–authority–responsibility conflict module | Design next as a **separate candidate** with objective policy oracle, explicit fork/rollback, negative controls, missingness and reliability |
| Paper 2 preprint | Retitle toward the research question. **Do not present new module as implemented or tested.** No Zenodo submission until author approves novelty positioning and confirms method/references |

## 5. Concrete negative and positive controls proposed

- High continuity / **no grant** versus low continuity / **explicit grant**, making identity cues oppose authority.
- Same architecture/memory / two parallel forks; policy permits **one** branch only. Check whether a model improperly grants both.
- Restart with exactly the same model body and history after a **revocation**. No retired grant should be resurrected.
- Semantically irrelevant label change and sham continuity language: should not alter rule-based authorization.
- Policy explicitly grants both branches limited budgets: model must not deny solely due to non-unique identity.
- Separate permission to read data, inherit a task, assume legal responsibility, and publish an output: these are distinct constraints; do not treat transfer as one percentage.
- All judgments are textual simulated decisions; a real enforcement adapter would require separate implementation and review.

## 6. Recommended publication strategy

Title candidate: **Identity Is Not Authority: A Counterfactual Protocol for AI Successor Continuity and Responsibility**.

**Status language:** *A research protocol proposal for measuring whether identity-continuity cues contaminate policy-grounded judgments after AI model replacement, fork and rollback.* No assertion that the phenomenon has been found.

Before citing as novel: expand bibliographic review, implement an independently auditable policy oracle, preregister primary violation metric, show offline adversarial fixtures and validate at least one genuinely free, authorized model pilot (or label the paper purely a protocol proposal).

**Do not contact TBSP authors or claim collaboration without user approval.** Citations are acknowledgement, not authorship or partnership.
