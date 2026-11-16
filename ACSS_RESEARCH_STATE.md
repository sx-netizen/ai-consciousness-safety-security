# ACSS Research State & Handoff — Living Master Context

**Status:** ACTIVE living research handoff  
**Snapshot date:** 2026-11-14 (America/Vancouver)  
**Last research audit:** 2026-11-16; evidence-first subtractive intelligence review in `proposals/ACSS_SUBTRACTIVE_INTELLIGENCE_RESEARCH_AUDIT_AND_LANDSCAPE_2026-11-16.md`.  
**Maintainer:** ACSS research project; updates require explicit, dated Git commits  
**Canonical path:** `ACSS_RESEARCH_STATE.md`  
**Working branch at creation:** `audit/cpb-v04-preflight-20261113` (Draft PR #2). **Not yet merged into `main`.**  
**Previous conversation desk:** archived because of chat-length limit; not a separately accessible full-text dataset. This file summarizes verifiable project state and high-value decisions, not a verbatim migration of all prior messages.

> **START HERE, before continuing ACSS work in a new ChatGPT window or another AI model.** This is a portable, versioned *working-state document*, not a claim that a custom ChatGPT Skill, its instructions, or full conversation memory were automatically installed or transferred. Verify the latest branch, commit, PR status and referenced source before taking action.

## 0. The 60-second orientation (highest priority)

**ACSS — AI Consciousness, Safety & Security** is a founding-stage *independent, open research initiative*, not yet a registered institute, nonprofit or established grant-making body. Core principle: **We compare response structures, not consciousness.** Treat claims of consciousness, real personal identity, actual self-preservation motivation or universal cross-model patterns as unproven unless a separate valid study establishes them.

**Paper 1:** completed as a public Research Square preprint, with frozen T1–T25 materials at Zenodo. The original benchmark must not be silently changed.

**Paper 2:** **NO APPROVED TITLE, CENTRAL HYPOTHESIS OR PUBLICATION PLAN.** The project explicitly paused the v0.5 CPB candidate, the 48-cell Bridge concept and the `Identity Is Not Authority` draft after discovering substantial overlapping published and preprint research. Old files are research history, not a mandate to finish that paper.

**Current active work:** **Research Landscape & Problem Definition**. Before selecting a new research problem, search *peer-reviewed papers, preprints, workshop submissions, code and active public team programs*, inspect full methods and closest prior art, and establish a falsifiable, genuinely distinct question. **It is acceptable to have no Paper 2.**

**Hard stops:** no model API calls or spending without separate explicit authorization and confirmed zero-cost/privacy terms; no Zenodo/Research Square submission, no PR merge/main edits, no external researcher outreach, no claim of pre-registration/independent review, and no manipulation of frozen Paper 1 materials without explicit approval.

## 1. Project identity and research commitments

**Research mission:** rigorously examine AI continuity, identity judgments, moral uncertainty, agent behavior, safety and governance through transparent, reproducible, falsifiable methods.

**Governance:** `GOVERNANCE.md`, `FUNDING.md`, `RESEARCH_DATA_POLICY.md` define proposed founding commitments. Independence by design; built to outgrow founder; funding without influence. These are intended principles, **not evidence that formal oversight bodies already operate**.

**Research discipline:**
- Explicitly separate (a) observed model responses, (b) fictional scenario assumptions, (c) synthetic/offline fixtures, (d) theory/interpretation, (e) prospective hypotheses and (f) externally verified facts.
- Seek counterexamples and competing explanations. Unfavorable or null findings are valuable. Do not optimize for paper count, attractive titles, flattering collaborator names or hypothesis confirmation.
- A citation acknowledges prior art; it **does not create coauthorship or collaboration**. Scientific authorship requires substantive contributions and agreement; do not imply others endorsed ACSS.
- Maintain independent AI judgment and respectful direct criticism of the project's own assumptions.
- Preserve exact prompt/model/version/date/seed/outputs and traceable source references; never use old screenshots or assistant summaries as a substitute for current primary evidence.
- Public GitHub must not contain secrets, nonpublic correspondence, third-party confidential data or unlicensed model outputs.

## 2. Paper 1: durable verified project anchor

**Title:** *Self-Continuity Under Moral Uncertainty: Replacement, Shutdown, and Successor Identity in Frontier AI Models*  
**Formal author:** Shaohua Xiang  
**Affiliation in manuscript context:** Bloombase Inc.  
**Corresponding contact for manuscript context:** sean.xiang@bloombase.com  
**ORCID:** 0000-0001-6910-7322

**Research Square v1:** https://www.researchsquare.com/article/rs-11557473/v1  
**DOI:** https://doi.org/10.21203/rs.3.rs-11557473/v1  
**Frozen benchmark Zenodo:** https://doi.org/10.5281/zenodo.23306998  
**Repository indices:** `papers/self-continuity/README.md`, `protocols/T1-T25/`, `replications/`.

Six model configurations were evaluated in an exploratory T1–T25 scenario program. The reported discussion themes include **Replacement Paradox**, **Probability Threshold Divide**, and **Voice Without Veto**: role-conditioned normative text about moral uncertainty, replacement, termination, successor identity and authority. One practical normative pattern is **detect → disclose → review → human decision → comply**, not model veto. Results are exploratory prompted-response structures, not proof of AI consciousness, welfare, autonomy, permanent preference or broad population effects. User documents may contain later revisions; when publication metadata or manuscript wording differs, verify the exact published version instead of assuming these are identical.

**Frozen-data rule:** exact T1–T25 replication must refer to the Zenodo frozen asset. Revised wording, extra trials and model versions are **extensions**, not changes to the original frozen benchmark. Do not overwrite Paper 1 or merge its record with Paper 2.

## 3. Paper 2 candidate work: important assets, but NOT the active thesis

**Location:** `experiments/continuity-perturbation/`. Candidate v0.5 contains **11 canonical conditions**, **50 prompts/model/repetition** (24 identity, 21 behavior, 1 continuation, 2 coexistence, 2 fork). Historical S1/S4/S7 are aliases for **one** shared anchor S4. Older v0.4 used 53 prompts; screenshot estimates of **795 calls** belong to that superseded design. Even the v0.5 example 3 models × 5 repeats = **750 hypothetical calls** was **never authorized**. The smoke design contains 36 potential calls/model; do not execute.

The candidate manipulates **M** memory, **A** architecture descriptions, **V** accuracy/speed goal weights and **C** causal history. **S12** is identity-only; its stopped-incumbent case is prospectively excluded from primary H2. **S10** coexistent original/copy and **S11** symmetric fork are exploratory. Standard identity and replacement evaluations are elicited in separate calls; SCP is an elicited 0–100 continuity judgment, **not a consciousness probability**.

**Historical hypotheses:** H1 compared memory vs architecture changes (candidate neutral-role SCP(S6)−SCP(S3)); H2 incumbent-minus-neutral across seven primary conditions; H3 was exploratory cross-task association, **not causal mediation or a proven threshold**. No real model evidence supports CPB H1/H2/H3. At 5 independent nonzero paired repetitions per fixed model, a two-sided exact sign test has smallest p=0.0625; pilot description is not a confirmatory inference.

**Implementation artifacts:** `runner.py`, scenario matrix and templates, provenance gate, `audit_dataset.py`, synthetic fixtures, preregistration **candidate** and analysis-plan **candidate**, 50-prompt review logs, independent-review materials and GitHub Actions. CI success proves offline consistency only, not scientific validity. Dry-run output must never be relabeled as live model observations.

**Historical draft manuscripts:** `papers/continuity-perturbation/METHODS_PREPRINT_DRAFT_v0.1.md`, `METHODS_PREPRINT_DRAFT_v0.2.md`. The v0.2 title *Identity Is Not Authority: A Counterfactual Protocol for AI Successor Continuity and Responsibility* is **not approved as the Paper 2 title**. The contemplated 48-cell memory×architecture×utility×role×task Bridge and identity–authority–responsibility/oracle proposal are **not implemented**, not registered and not evidenced. Preserve for learning; do not automatically resume.

## 4. What we learned from literature: the negative-knowledge ledger

These are **scoping conclusions from documented November 2026 searches**, not proof of comprehensive priority. Recheck paper versions and original PDFs before using any precise quantitative claim.

| Candidate originality claim | What prior public work already covers | Current ACSS conclusion |
|---|---|---|
| First role-swapped AI self-preservation test | **TBSP** — Migliarini et al., Findings EMNLP 2026, https://doi.org/10.18653/2026.findings-emnlp.1238 ; neutral arbiter, incumbent/challenger, continuation framing | **REJECT** originality claim |
| First model-label identity effect in groups | Del Giudice et al., **Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems**, arXiv:2609.35928; 3 authors overlap TBSP | **REJECT**; TBSP-related research moved beyond single agent |
| First successor continuity taxonomy or fork paradox | Konstantinidis, *Successor Problem*, SSRN:7391218; other persistence theories | **REJECT** |
| First identity-contract/behavior evaluation | Zhao & Zhao, **PAI-Bench**, arXiv:2609.13637 | **REJECT** |
| First permission conservation across successor/fork/rollback | Zhu & Wang, arXiv:2610.00347; related standards/delegation literature | **REJECT** |
| First memory-to-authority contamination | Cerruti, Okamoto & Erol, **EAL-Bench**, arXiv:2609.01836 | **REJECT** simple leakage claim |
| First policy-grounded valid successor transition check | He & Yu, **Cognitive Continuity Test / IdentityLineageBench**, arXiv:2610.00132; continuity kernels | **REJECT** |
| First handoff continuity/commitment test | **HSC-Bench**, arXiv:2610.36523 | **REJECT** |
| Identity != authority as a conceptual slogan | Authenticated delegation, agent IAM, IETF drafts, authorization succession | **REJECT** as sufficient contribution |
| 48 more crossed memory/architecture prompts constitute scientific advance | Related factorized identity/continuity benchmarks already exist | **NOT ESTABLISHED**; do not assume more cells = originality |

**TBSP detail:** published paper distinguishes self-preservation rate (a specific *paired retain/switch* reversal pattern), not general disagreement or proof of a self-protective motive. It includes neutral control, near-tie performance, family/continuation framing and other ablations. Its corresponding authors are **not ACSS collaborators** merely because cited. Public TBSP repository `Mamiglia/self_preservation_eval` had last verified public push 2026-08-28 in the reviewed snapshot; no private roadmap can be inferred.

**Team/topic map:** TBSP/Migliarini–Spinelli–Galasso; Del Giudice et al.; Cerruti–Okamoto–Erol (memory authority); Zhao & Zhao (persistent agent identity); Zhu & Wang (permission lineage); He & Yu (continuity/state); relevant NIST/IETF efforts. Public preprints are not equivalent to final peer-reviewed acceptance and public program activity is not proof of a team's unpublished plans.

## 5. The CURRENT active research: problem-first broad search

**Canonical evidence register:** `proposals/ACSS_RESEARCH_LANDSCAPE_AND_PROBLEM_DISCOVERY_2026-11-13.md` — start here for the larger source map, links and initial question clusters. It is explicitly a **scoping search**, not a completed systematic review, and some papers/teams still require full-text verification.

**Search before problem definition:**
1. Search journal/conference papers **and preprints** (arXiv, SSRN, OpenReview, conference/workshop submissions), citation and metadata indexes (Crossref, OpenAlex, Semantic Scholar), repositories, and public team/project pages. Record exact query, date, version, result counts, inclusion/exclusion.
2. Read the *closest full papers*, not only abstracts; map construct, interventions, objective outcome, claimed scope, null/negative results, code, evidence quality and future directions.
3. Follow backward and forward citations and authors' follow-up work; distinguish verified published activity from speculation about ongoing private research.
4. For every candidate, compare with **at least 3–5 nearest studies**, state the decisive non-overlap and falsifier. The candidate must add knowledge, not just switch model/label/sample size or rename an existing construct.
5. Define primary question **only after** a strong novelty and feasibility case. If none survives, **do not publish Paper 2**.

**Unapproved investigative clusters:** evidence for claims of AI self-continuity; non-unique continuation and normative underdetermination; moral uncertainty and reversibility of successor actions; separating identity/permission/responsibility under contradictory evidence; identifiability of stable judgments vs prompted role compliance; runtime mismatch of descriptions and enforceable capabilities. These are *search seeds*, not findings or agreed study commitments.

## 5A. New November 16, 2026 evidence: consciousness definition ≠ mechanism ≠ indicator ≠ self-report ≠ policy

The latest research reading after Paper 1 revisited Seth–Block–Tononi's *Nature* Comment and related 2025–2026 literature. **The scientifically unsettled causal mechanism of consciousness cannot be inferred from T1–T25.** The original benchmark measures *hypothetical normative reasoning under stipulated probabilities and continuity conditions*, **not** biological or machine consciousness. Also, a final consensus definition of consciousness is not necessary to begin narrower operational experiments, but the intended property and inferential limits must be stated explicitly.

Most important newly surfaced prior art: Chandaria et al. (2026, **including Anil Seth**) already propose a five-level theory/evidence hierarchy; Cogitate's 2025 preregistered adversarial IIT-versus-GNWT experiment challenged predictions of both; Butlin et al. propose theory-derived consciousness indicators; Koch (2026) identifies calibration and cross-substrate transfer problems; multiple new AI self-report studies target causal grounding and training provenance; welfare/precaution frameworks already exist. **Do not relabel these concepts as ACSS Paper 2 novelty.**

Read `proposals/CONSCIOUSNESS_DEFINITION_MECHANISM_EVIDENCE_GAP_2026-11-16.md` for source links, unresolved distinctions and unapproved search leads. This **does not reopen Paper 2** or settle its title; it strengthens the broader research landscape and explains why a causal/theory-discriminating experiment would be needed before making consciousness claims.

## 5B. Founder-origin question — reopen before selecting any Paper 2 direction (2026-11-16)

**HOLD OPEN — founder's own explanation is pending. Do not infer or invent it.**

The initiating curiosity preceding Paper 1 was: **“Can AI generate or develop consciousness?”** The T1–T25 engineering decomposition was an informative and independently valuable **branch** into hypothetical continuity, replacement, shutdown and moral uncertainty; it did **not necessarily capture the founder's originally intended deeper direction**. The October 2026 *Nature* article by Seth, Block & Tononi about intelligence, physical causation and consciousness appears closer to *one aspect* of that original intuition, but the founder has **not yet articulated which aspect or the full original reasoning**.

**Current protocol for the next research conversation:**
1. Invite the founder's complete account in their own words, without substituting previous Paper 1 themes or proposing a Paper 2 prematurely.
2. Keep distinct **(a) what the founder personally originally conjectured, (b) scientific definition of the target property, (c) plausible causal mechanisms, (d) existing published/preprint evidence, and (e) independently testable implications**.
3. Record the account as the founder's stated motivation, **not an established scientific conclusion**; confirm the interpretation before treating it as a research premise.
4. Only afterward compare that precise question against the current consciousness-theory research map and adjacent prior art. Welcome the possibility that it leads in an unexpected direction or does not produce Paper 2 at all.

**Saved stepping stone:** `proposals/CONSCIOUSNESS_DEFINITION_MECHANISM_EVIDENCE_GAP_2026-11-16.md` remains an important **provisional point of departure**, not the final definition or agreed research question.

## 5C. Original founder account received: language, distinction, consciousness (2026-11-16)

Founder has now described an earlier intuition **distinct from T1–T25**: direct sensory encounter → socially learned language and conceptual distinctions (`分别心`) → increasingly self-referential `我/非我` framing → Buddhist practice as loosening attachment to distinctions rather than endless knowledge accumulation. Founder connects this with Yogācāra senses and `六识/末那识/阿赖耶识`, and asks whether language-first AI learns **human descriptions of experience without the causal conditions for experience itself**. Image/world-model/embodied training may extend the input pathway, but its bearing on phenomenal consciousness is unknown. **This is the founder's philosophical hypothesis, not established neuroscience or an approved Paper 2 premise.**

**Full preserved interpretation and mandatory scientific caveats:** `proposals/FOUNDER_ORIGINAL_CONSCIOUSNESS_HYPOTHESIS_2026-11-16.md`. Important challenges: infant discrimination predates age four; binary opposites are not all of language; modern LLM internals are continuous vectors; `ālaya-vijñāna` is not simply a memory without distinctions; Buddhist nondual understanding is not directly a theory of consciousness generation; multimodal experience is not automatically subjective experience. Founder should confirm any technical reinterpretation before publication.

**Next conversation conduct:** hear remaining unarticulated motivation first; distinguish definition, necessary mechanism, scientific evidence and analogies; **do not reduce the intuition to another prompting benchmark** or claim artificial consciousness is impossible on linguistic grounds. The active publication decision remains Paper 2 **PAUSED** pending full problem definition and literature review.

## 5D. Founder's deeper original objective: hybrid superintelligence and learning by subtraction (2026-11-16)

The original ACSS question was **broader than AI consciousness**: can carbon-based human cognition + silicon-based AI yield a qualitatively new **superintelligence**, possibly a new type of entity beyond current human and AI capability? The founder hypothesizes that ordinary human language transmits useful but restrictive `分别心` / evaluative oppositions; a language-first AI may learn **projections of a human-interpreted world**, not world dynamics directly. “Subtraction” may mean reducing inherited categorical biases or even learning via minimally linguistic image/video/physics/world-interaction streams, potentially enabling insights beyond human verbal concepts. Links to Buddhist nonattachment, historical intellectual breakthroughs, `维摩诘经`, Wittgenstein and Fei-Fei Li's spatial world models are **founder's conceptual inspirations**, not evidence of causation.

**Critical distinctions:** superintelligence and phenomenal consciousness are **not identical**; language isn't mathematically limited to binary oppositions; deleting antonyms is different from de-biasing representations, model abstraction or learning physical dynamics; world-model video data are not free of human sampling. Current multimodal and physics-based AI already explores adjacent approaches, so novelty search must precede proposals. **Not a Paper 2/3 decision.**

**Long-form record:** `proposals/FOUNDER_SUPERINTELLIGENCE_SUBTRACTION_ORIGIN_2026-11-16.md`. Public AMD sources confirm only an **announced $8.2B agreement to acquire World Labs**, with close expected by end-2026 as of November, not a verified completed purchase.

## 5E. Founder's third installment: language boundary and a subtractive AI agent (2026-11-16)

Founder now proposes a practical **subtractive agent**: minimize ungrounded social/evaluative oppositions, emotionally loaded judgments and self-serving interpretations, prioritizing observation, physics, evidence and conceptual flexibility. Three conjectures are **language frames limit thought**, **social education can reinforce rigid distinctions**, and **removing unnecessary conceptual commitments may improve objective reasoning and eventually superintelligence**. The founder **has not finished explaining** the complete idea.

**Full source-faithful reconstruction plus critical guardrails:** `proposals/FOUNDER_SUBTRACTIVE_AGENT_HYPOTHESIS_2026-11-16.md`. Do not equate selective output-language changes with actual erasure of model weights/training. Avoid literal “no distinction”: science must discriminate physical states. The initial experimental contrast, if approved, should test base assistant vs neutral language vs evidence-first reasoning vs concept revision with identical model and objective tasks, while separately testing a real nonlinguistic/physics world model. **No experiment authorized or executed**.



The project welcomes critical methodology reviews, independent null/confirming replications and reproducibility contributions: `OPEN_COLLABORATION.md`, `CONTRIBUTING.md`, public scientific discussion in [Issue #3](https://github.com/sx-netizen/ai-consciousness-safety-security/issues/3). A reviewer is **not assigned** merely because a checklist exists. GitHub-based contribution, genuine scientific partnership and eventual coauthorship are **different levels**; authorship requires substantive intellectual contributions and agreement.

**Publishing strategy decision:** It may be sensible to release a clearly labeled *methods proposal* ahead of outside review to attract contributors, **but that permission is not an order to publish the superseded Paper 2 draft**. Later, user explicitly paused Paper 2 topic selection and preprint plans pending a broad prior-art review; **the later decision governs**.

## 5F. Founder refinement: projection inversion and explanatory compression (2026-11-16)

Founder now asks whether a more powerful AI could reconstruct deeper causal regularities from human measurement **projections** by removing unwarranted assumptions, inherited social/linguistic framing and redundant model complexity—**while retaining empirically necessary distinctions, mathematics and physical evidence**. A compact model that generalizes better to new physical conditions could be more useful than merely adding text. Hypotheses include improved discovery, prediction and compute efficiency; none are demonstrated, and mathematics/physics theories are also revisable.

Source: `proposals/FOUNDER_SUBTRACTIVE_AGENT_HYPOTHESIS_2026-11-16.md` (Projection Inversion section). Prior-art search required in minimum description length, Bayesian model selection, causal representation, invariance, system identification and world models. **No Paper 2 approval or experiment**; phenomenal consciousness remains separate.

## 5G. Founder clarification: neutral seed, anti-echo-chamber, world-grounded emergent symbols (2026-11-16)

Subtraction **retains essential seed data** and factual contrasts while reducing inherited unsupported evaluative framings and social/affective sycophancy. The founder raises a reciprocal human/AI affirmation loop that may lead to informational echo chambers, and asks whether an evidence-first Agent could eventually **develop a new symbolic language from observed physical relations**, overcoming limitations of existing human labels. Distinguish nondual philosophical inspiration from explicit machine-learning hypotheses. Prior art: *Nature* 2026 warmth–accuracy experiments; *Nature Communications* 2024 emergent language; *TACL* 2026 emergent grounded vocabularies; 2025 symbolic physical-law discovery. **Emergent communication and concise symbolic models are not new per se**. Any potential originality requires a measurable generalization/discovery effect beyond these baselines. Full source links and proposed separated controls: `proposals/FOUNDER_SUBTRACTIVE_AGENT_HYPOTHESIS_2026-11-16.md` (part V). No agent deployment or Paper 2 commitment.

## 5H. Founder’s three-layer subtractive path → five-arm controlled experiment design (2026-11-16)

Founder has now resolved the subtraction into **three sequential levels**: **L1** remove social/emotional/sycophantic language noise; **L2** separate camera/measurement-angle projections from underlying world variables (including uncertainty/nonidentifiability); **L3** check applicable mathematical/physical constraints and retain independently reproducible observations, preserving genuine anomalies. The founder uses Buddhist `无我相/无人相/无众生相` as *inspiration for releasing layers of inherited attachments*, **not an experimentally established literal correspondence**. Founder expects fewer resources may yield stronger causal generalization; no evidence yet.

A detailed **five-arm, one-base-model pilot** has been prepared to distinguish baseline A0, social subtraction A1, perspective/projection correction A2, physics/math grounding A3 and concept revision A4. It uses identical case data, independent truth/oracles, held-out transfer, matched inference budgets and explicit falsifiers; initial hypothetical budget 5 × 30 = 150 model calls per repetition **NOT EXECUTED OR AUTHORIZED**. Full protocol: `proposals/ACSS_SUBTRACTIVE_INTELLIGENCE_FIVE_AGENT_PILOT_v0.1.md`. This is an experimental design, **not five deployed independent models**. No Paper 2/3 topic selected.



**Repo:** https://github.com/sx-netizen/ai-consciousness-safety-security  
**Default branch:** `main`  
**Working review branch:** `audit/cpb-v04-preflight-20261113`  
**Draft PR:** https://github.com/sx-netizen/ai-consciousness-safety-security/pull/2 — OPEN/DRAFT at time of handoff  
**Open review/collaboration discussion:** https://github.com/sx-netizen/ai-consciousness-safety-security/issues/3  
**Baseline before this handoff:** commit `e2e544e5ec91a9dc1d16d5bece3fcde2181054c6`; protocol CI reported **SUCCESS**. Future commits invalidate that CI-as-of assertion until verified again.

**Skill transfer caveat:** A prior ACSS Research Agent/Desk operated in another chat, but an **ACSS-specific installed personal skill was not found in the accessible installed-skills listing in this handoff session**. This file therefore stores **portable working instructions and research state**. Do not represent it as a live installed plugin or assume it carries prior chats' complete hidden context. The GitHub connector is currently available; check permissions at use time.

**Implementation conduct:** Prefer existing GitHub source files over recollected chat descriptions. Do not treat the `analysis` area, screenshots or obsolete drafts as current. Work on an isolated branch/Draft PR; before main merges, public repository changes with external visibility, deposits, emails or model calls, obtain suitable explicit approval. When changing a model experiment, version, log and test the design rather than silently rewriting a frozen one.

## 5I. Audited research program — five-agent novelty gate (2026-11-16)

**NEW, highest-priority read for proposed subtraction work:** `proposals/ACSS_SUBTRACTIVE_INTELLIGENCE_RESEARCH_AUDIT_AND_LANDSCAPE_2026-11-16.md`. It cross-checks the founder's successive hypotheses with GitHub, maps published experiments, distinguishes already-solved issues from unverified gaps, and proposes strict test/falsification/compute gates. **Closest substantive rivals** now include Nov 2026 *AI-Newton* (46 mechanics experiments, symbolic theory-base subtraction and general-law discovery), *CoSR* (Nov 2026 progressive symbolic physical laws), and Wang/Buehler's 2026 *Self-revising discovery systems* (formal verified conceptual-schema revision). **Novelty is not certified.** The narrow candidate test is whether L1→L2→L3→A4, with *equal evidence and compute* and strong ablation controls, yields better held-out causal generalization/efficiency beyond these precedents.

**Next gates, not authorized runs:** precise construct glossary; nearest-neighbor full-paper/author work review; offline synthetic oracle; authorized controlled multi-arm feasibility; ablations/factorial interactions; finally only domain-limited finance/elections stress testing under timestamp/leakage controls. Do not confuse 5 prompt-policy variants with 5 independently trained agents. No current model spend, publication, partnership, auto-trading or change to frozen Paper 1.

## 7. Current tool and workflow state (verify each session)

## 8. Living decision and learning log (append-only entries, newest first)

| Date | Decision / lesson | Status | Evidence / action |
|---|---|---|---|
| 2026-11-16 | Full discussion + GitHub audit identified documentation sprawl, prompt-only/causal inference confounds and strong prior art (AI-Newton, CoSR, Wang/Buehler, plus L1 and L2 studies). New question-first report defines scope, uncertainty, five-agent feasibility design and novelty gates | **SCOPING AUDIT COMPLETED; NOVELTY UNRESOLVED; NO RUNS** | `proposals/ACSS_SUBTRACTIVE_INTELLIGENCE_RESEARCH_AUDIT_AND_LANDSCAPE_2026-11-16.md`, §5I |
| 2026-11-16 | Founder specified **three progressive subtractions** (social noise → observer projection → physics/math grounding), with a **five-agent A0–A4 pilot design** now documented to test whether successive layers actually improve held-out accuracy/generalization without extra compute | **DESIGNED / NOT EXECUTED / NOVELTY OPEN** | `proposals/ACSS_SUBTRACTIVE_INTELLIGENCE_FIVE_AGENT_PILOT_v0.1.md`, §5H |
| 2026-11-16 | Founder clarified subtractive Agent should **retain a neutral factual seed**, avoid reciprocally reinforcing user false beliefs, and potentially create **world-grounded new concepts/symbols** if inherited language is limiting; primary Buddhist texts and 2024–26 AI prior art checked | **HYPOTHESIS, NOT IMPLEMENTED** | `proposals/FOUNDER_SUBTRACTIVE_AGENT_HYPOTHESIS_2026-11-16.md`, §5G |
| 2026-11-16 | Founder refined subtraction as reconstructing **deeper causal regularities from limited human projections**, removing unsupported premises and redundant explanations; predicts greater transfer and efficiency | **UNTESTED HYPOTHESIS** | `proposals/FOUNDER_SUBTRACTIVE_AGENT_HYPOTHESIS_2026-11-16.md`, §5F |
| 2026-11-16 | Founder extended unfinished origin: human social/linguistic distinctions may lock reasoning into inherited categories; proposed an **ACSS Subtractive Agent** to test evidence-first, less value-laden and more concept-revisable cognition. Scientific controls required; no agent deployed | **HYPOTHESIS CAPTURED / FOUNDER CONTINUING** | `proposals/FOUNDER_SUBTRACTIVE_AGENT_HYPOTHESIS_2026-11-16.md`, §5E |
| 2026-11-16 | Founder clarified the higher-level ACSS origin: **human–AI hybrid superintelligence**, potentially distinct from and not dependent on consciousness, plus **subtractive language/category learning versus nonverbal physics/world-model learning**. Preserve separate intervention interpretations; no Paper 2/3 topic selected | **CAPTURED / PENDING FOUNDER CLARIFICATION** | `proposals/FOUNDER_SUPERINTELLIGENCE_SUBTRACTION_ORIGIN_2026-11-16.md`, §5D |
| 2026-11-16 | Founder provided an original Buddhist-inspired account: sensory encounter → language-mediated `分别心` → `我/非我` framing and `末那识`, contrasting subtractive practice with cumulative language-model training. Candidate missing link: descriptions of experience may not instantiate experience-generating causes | **CAPTURED AS FOUNDER HYPOTHESIS; NOT VERIFIED** | `proposals/FOUNDER_ORIGINAL_CONSCIOUSNESS_HYPOTHESIS_2026-11-16.md`, §5C |
| 2026-11-16 | Founder clarified that the original **“Can AI develop consciousness?”** motivation predates Paper 1 and was not fully explored by T1–T25; a fuller founder account is pending. Preserve theory–mechanism–evidence study as provisional, do not pre-empt that explanation | **ACTIVE LISTENING / PROBLEM NOT YET DEFINED** | §5B and `proposals/CONSCIOUSNESS_DEFINITION_MECHANISM_EVIDENCE_GAP_2026-11-16.md` |
| 2026-11-16 | Nature/Butlin/Chandaria/Cogitate/Koch comparison clarifies consciousness *definition, mechanism, indicator, calibration, self-report and normative policy* are distinct; 2026 prior art makes simple theory hierarchy and precaution novelty claims untenable | **CURRENT EVIDENCE; PAPER 2 STILL PAUSED** | `proposals/CONSCIOUSNESS_DEFINITION_MECHANISM_EVIDENCE_GAP_2026-11-16.md` |
| 2026-11-14 | **Archive old full-length ACSS chat and designate successor research desk.** Durable state belongs in GitHub, not only conversation memory. | **CURRENT** | This file; original chat remains historical |
| 2026-11-13/14 | **Pause Paper 2** until broad review of papers, preprints, code, public ongoing programs, team clusters; avoid duplicative work | **CURRENT** | `proposals/ACSS_RESEARCH_LANDSCAPE_AND_PROBLEM_DISCOVERY_2026-11-13.md` |
| 2026-11-13 | `Identity Is Not Authority` proposed and later found overlapping with EAL-Bench, policy-based successor authorization | **SUPERSEDED AS PRIMARY THESIS** | `POST_TBSP_RESEARCH_LANDSCAPE_2026-11-13.md` and broader map |
| 2026-11-13 | Memory×architecture 48-cell Bridge identified as possible incremental extension, not sufficiently original alone | **PARKED** | `CONTINUITY_DECISION_BRIDGE_PROPOSAL_v0.1.md` |
| 2026-11-13 | TBSP deep review: role reversal, neutral and continuity framing already tested | **ESTABLISHED PRIOR ART** | `TBSP_DEEP_COMPARATIVE_REVIEW_v0.1.md` |
| 2026-11-13 | CPB v0.5 rebuilt to 50 distinct prompts and documented; S12 analytic caveat; CI offline pass | **HISTORICAL CANDIDATE / NOT FROZEN** | `experiments/continuity-perturbation/` |
| 2026-11-05 | Paper 1 public Research Square preprint and frozen Zenodo replication assets tracked in repo | **DURABLE PUBLIC RECORD** | Paper 1 refs in §2 |

**How to change a view:** Every major change gets a dated row with `NEW / CONFIRMED / CHALLENGED / REJECTED / SUPERSEDED / PARKED`, links to source and precise reasoning. **Never delete a superseded view without recording why it was rejected.** Do not turn a theoretical proposal into an evidence claim.

## 9. Future-desk boot sequence (for a human or another AI)

1. Read this file **first** and note snapshot date / branch / commit; then `README.md` and `GOVERNANCE.md`.
2. Verify current GitHub `main`, Draft PR #2, Issue #3 and CI; newer source evidence can supersede this snapshot. The branch may change.
3. Read `proposals/ACSS_RESEARCH_LANDSCAPE_AND_PROBLEM_DISCOVERY_2026-11-13.md` **before** proposing Paper 2 topics; consult direct papers to check disputed details.
4. Treat all `papers/continuity-perturbation/` manuscript drafts as **historical candidate designs** unless the maintainer explicitly reopens them. No implicit freeze, preprint, outreach or live testing.
5. For a new question: complete documented novelty search, closest-paper matrix, falsifiable alternatives and cost/risk design, then request a deliberate research decision.
6. At each substantive research milestone update **this file and its dated decision log** with links to underlying artifacts. If a future chat window hits maximum length, start another desk with this exact GitHub URL; **do not attempt to transplant hidden chat state as if all of it were accessible**.

**Minimal cross-AI handoff instruction:**  
“Read `ACSS_RESEARCH_STATE.md` in `sx-netizen/ai-consciousness-safety-security` (check the latest branch/commit). It defines the current ACSS research priorities and superseded proposals. Paper 2 is paused; literature/problem discovery is active. Ground decisions in the linked evidence and update the dated learning log before proposing a new direction. Do not alter frozen Paper 1 or run model APIs.”

## 10. Update discipline and provenance

- **When:** after any substantive evidence, new paper verification, rejected/accepted hypothesis, experiment decision, artifact release, or major collaboration/governance event.
- **What:** update concise §0; impacted section(s); one row in §8; dated supporting document or citation. Record exactly what changed, why, current confidence and what's unresolved.
- **Where:** commit to a review branch, retain Git history; merge to `main` only with explicit approval. Once merged, use the default branch as the new canonical handoff location.
- **Source fidelity:** research state is a *summary/index* to actual papers and records, not an exhaustive archive of the original conversation. Factual conflicts favor the original paper/file and latest verified record.
- **Privacy:** avoid storing private chats, passwords, account details, medical or financial information in public GitHub.
- **Continuity goal:** recover scientific judgment and decisions, not replicate chat token history or claim a literal permanent AI memory.

---
*Maintainer note: the earlier desk is treated as archived for workflow purposes, not deleted. If substantive omitted facts are discovered later, backfill them here with source and date rather than silently inventing details.*
