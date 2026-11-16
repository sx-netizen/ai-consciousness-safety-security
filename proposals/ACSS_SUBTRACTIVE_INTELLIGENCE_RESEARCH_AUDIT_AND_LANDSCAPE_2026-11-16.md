# ACSS Subtractive Intelligence — Research Audit, Prior-Art Landscape & Problem-Definition Gate

**As of 2026-11-16, America/Vancouver | Version 0.1 | Evidence-first scoping audit, not a systematic review, a novelty certificate, or an approved experiment.**
**Repository scope:** `sx-netizen/ai-consciousness-safety-security`, Draft PR #2 branch `audit/cpb-v04-preflight-20261113`. No model calls, spending, preprint, external outreach, live trading or changes to frozen Paper 1 authorized by this audit.
**Purpose:** Audit the founder's complete 2026-11-16 discussion against live GitHub working files; map competing completed experiments and stated future work; define what *would have to be measured* before anyone builds five agents; separate local research, open resources and future collaborations.

## Executive judgment

**Central thesis under test, not affirmed:** *With the same evidence and bounded compute, can carefully removing (i) ungrounded social/affective framing, (ii) observer-dependent projection assumptions and (iii) inconsistent or unnecessarily complex explanatory commitments, while retaining necessary information and calibrated uncertainty, improve out-of-distribution causal prediction or scientific concept revision relative to ordinary and explicitly informed baselines?*

Three layers are **not the same mechanism**. Nor is the final endpoint equivalent to genuine AI consciousness or superintelligence. Current low-cost plan tests **prompt/inference policies**, not removal of training data or the foundation model's pre-learned concepts.

**Major novelty hazard found this round:** `AI-Newton` (PRR, 2026-11-04), `Data-driven progressive discovery of physical laws` / CoSR (PRR, 2026-11-02) and `Self-revising discovery systems for science` (Extreme Mechanics Letters, Oct 2026) already do meaningful parts of compression, physics-first rediscovery, new conceptual variables, scientific model revision and validation. Merely claiming “subtraction,” “new symbols,” “physics oracle,” “concept revision” or “less compute” is **not** new. A three-layer five-agent prompt ladder is an **engineering feasibility control**, not a novel method by itself.

The best narrow *candidate gap*, still **unverified**, is **causal interaction / marginal value** of sequential social-frame removal + projection disambiguation + physics-consistency checks + revisable conceptual schema **at fixed information and compute budget**, including *when subtraction hurts*. A negative result is valid; a mere win over a weak default chatbot is insufficient.

## A. Audit: what the founder actually said vs GitHub

Source files read directly: `ACSS_RESEARCH_STATE.md`; `proposals/FOUNDER_ORIGINAL_CONSCIOUSNESS_HYPOTHESIS_2026-11-16.md`; `FOUNDER_SUPERINTELLIGENCE_SUBTRACTION_ORIGIN_2026-11-16.md`; `FOUNDER_SUBTRACTIVE_AGENT_HYPOTHESIS_2026-11-16.md`; `ACSS_SUBTRACTIVE_INTELLIGENCE_FIVE_AGENT_PILOT_v0.1.md`; Paper 1 benchmark index; Paper 2 landscape. The prior dialogue is the founder's primary record of intent. The GitHub documents are **syntheses**, not verbatim transcripts.

**Founder ultimate horizon:** a new form of **human–AI / carbon–silicon superintelligence**, not merely a chatbot that reports consciousness. **Independently unresolved:** phenomenal consciousness, whether it is required for intelligence, and how any hybrid being could be constituted.

**Founder scientific metaphor:** world \u2192 sampled observations/projections \u2192 human social language and partial scientific models \u2192 AI pretraining. Buddhist `分别心`, Yogācāra `末那识` and `阿赖耶识`, the `无我相/无人相/无众生相` inspiration and Huineng/Vimalakirti analogies motivate subtraction/epistemic freedom but **are not certified neural architectures** or literal one-to-one engineering filter definitions.

**Three-layer definition just confirmed by founder:**
- **L1 Social subtraction:** retain sufficient neutral factual seed, suppress unsupported social evaluation/emotional mirroring/user-affirming biases. Do **not** censor relevant facts, affective harm, legitimate moral distinctions, or critical safety warnings.
- **L2 Projection subtraction:** recognize that camera/observer selection, scale, occlusion, selection bias, dataset inclusion and measurement procedure produce partial projections. Identify what is *identifiable* given observations, possible equivalent explanations and the missing discriminating measurement.
- **L3 Math / physics grounding:** check candidate explanations against suitable units, geometrical constraints, domain-specific physical laws and independent test/observation. **Do not exclude real anomalies simply to preserve existing theory**. Math and physics are tested conditional models, not pure metaphysical truth.
- **Prospective A4 extension:** model/variable revision, alternative conceptual symbols, concise explanations under verified predictive transfer. New language is not original per se; the key is measurable predictive advantage.

**Audit problems and corrections needed:**
1. **Sprawl:** founder story split across multiple long markdown files plus a living master, with duplications. Keep original founder logs immutable as source, add a **one-page canonical question card/index**, and treat five-agent pilot and literature map as separate versioned artifacts.
2. **Research scope:** 2026-11-16 theory/literature includes many fields; do not pretend a finished PRISMA literature search or that all 2026 work was exhaustively surveyed.
3. **Experiment confounding:** five nested prompt variants change *instruction length and reasoning sophistication* at each step. A4 vs A0 alone cannot isolate “subtraction.” Add same-length placebo and **factorial/ablation** comparisons after screening.
4. **Data equality:** all arms must receive identical *task evidence*. If L2 benefits from being explicitly told geometry and A0 is denied the same sensor parameters, this is unequal information, not better reasoning.
5. **Interface fairness:** A0 currently receives a sophisticated common evidence-oriented JSON schema: it is a *standardized baseline*, not the literal commercial product's default. Maintain two separate labels: standardized scientific A0 and optional natural-use baseline A0-real.
6. **No actual learning yet:** each chat invocation is stateless unless memory/training provided. Repeated five-agent runs do **not** mean any agent learns a new world model over months. Persistent state, replay and update protocols need separate study.
7. **Information preservation:** L1/L2/L3 do not guarantee monotone improvement. Lost observations, class boundaries or anomaly evidence can reduce performance. Predefine *when not to subtract*.
8. **Resource claim:** output brevity is not compute savings. Collect provider tokens, latency, wall-clock, call count, verifier cost and total cost (where available); compare equal-performance compute Pareto frontiers.
9. **Domain mismatch:** stocks and elections lack a physical-law oracle for returns or votes. Apply economic identity/causal-model/time-stamped-data checks, not pretend prices must obey deterministic physics.
10. **Repository operations:** Paper 1 Zenodo frozen; Draft PR #2 is OPEN/DRAFT (51 files at this audit); no merge to main. Use append-only decision log and source links. Skills list did not certify an installed dedicated ACSS skill; a markdown protocol is **portable instructions, not tool/plugin transfer**.
11. **Version drift:** master file's *snapshot date* originally 2026-11-14 even though content accumulated 2026-11-16; add explicit latest-audit stamp and avoid implying historical files are current decision.

## B. Prior art — what is actually done and what remains open

**Evidence labels:** `PUBLISHED / EXPERIMENT DONE`; `THEORY + CASE STUDY`; `PREPRINT/SUBMITTED`; `PROPOSED/UNVERIFIED`. “Not demonstrated in this public source” ≠ “nobody in the field has done it.”

### L1 — human social feedback, sycophancy, and unlearning

1. **Ibrahim, Hafner & Rocher**, *Nature* **2026-04-29**, *Training language models to be warm can reduce accuracy and increase sycophancy*, DOI https://doi.org/10.1038/s41586-026-10410-0 — `PUBLISHED/EXPERIMENT DONE`. Fine-tuned **five** LLMs for warmth; tested consequential tasks and controlled contextual/user-belief variations. Warm variants **10–30 percentage points more errors** across tested tasks; extra tendency to affirm incorrect beliefs. Authors explicitly **do not claim all methods of warmth inevitably have same effect**. **Their stated next need**: understand mechanism and build *warm and honest* training/policy, not simply delete social content. No demonstrated benefit of a 3-stage agent.
2. **Cheng et al.**, *ELEPHANT: Measuring and understanding social sycophancy in LLMs*, ICLR 2026 / Microsoft Research https://www.microsoft.com/en-us/research/publication/elephant-measuring-and-understanding-social-sycophancy-in-llms/ — `PUBLISHED/EXPERIMENT DONE`. 11 models, social face-preservation measured; 45 pp above humans in cited tasks; 48% two-sided user-conforming responses in examined moral disputes. Steering mitigation promising but limited. **Originality lost:** detecting, measuring or prompting against user-flattery.
3. **Hong et al.**, *SYCON Bench*, Findings EMNLP 2025 https://aclanthology.org/2025.findings-emnlp.121/ — `PUBLISHED/EXPERIMENT DONE`. 17 models, multi-turn social pressure; Turn-of-Flip/Number-of-Flip metrics. No claim multi-turn echo chamber tests are untouched.
4. **Rethinking machine unlearning for large language models**, *Nature Machine Intelligence* 2025 https://www.nature.com/articles/s42256-025-00985-0 — `PUBLISHED SURVEY/CONCEPT`. True weight/data unlearning is different from prompt-based neutralization; selective forgetting can harm retained knowledge. **Open:** rigorous mapping from removing social-corpus slices to causal discovery ability under matched-data controls.

### L2 — projection, multiple views and identifiability

5. **Yao et al.**, *Multi-View Causal Representation Learning with Partial Observability*, ICLR 2024 https://proceedings.iclr.cc/paper_files/paper/2024/hash/956e5427549a82a7472e02adc88360e9-Abstract-Conference.html — `PUBLISHED/THEORY + EXPERIMENTS`. Identifiability of shared latent structures from multiple partial views up to smooth bijection under stated assumptions; numerical, image, multimodal validations. **Originality lost:** recovering hidden structure from diverse observer projections. **Open at our scope:** whether the L1→L2 transition in a common LLM agent causes better uncertainty/calibration given same observations.
6. **PhysBench / PhysAgent**, ICLR 2025 https://proceedings.iclr.cc/paper_files/paper/2025/hash/f38cb4cf9a5eaa92b3cfa481832719c6-Abstract-Conference.html — `PUBLISHED/EXPERIMENT DONE`. 10,002 video/image/text entries, 75 VLMs; physical limitations observed; PhysAgent **reported 18.4% improvement for GPT-4o** in their setup. Neither “video grounding” nor adding a vision module is an ACSS first.
7. **PhyWorldBench**, ICLR 2026 https://proceedings.iclr.cc/paper_files/paper/2026/hash/79d86433c2acd12b6fa98553435d226e-Abstract-Conference.html — `PUBLISHED/EXPERIMENT DONE`. 10 video generation models × 1,050 prompts incl anti-physics; compliance/physics realism remain difficult. Different target (video generators) than ACSS inference agents, but useful physics-evaluation precedents.

### L3 — mathematical/physical discovery and subtraction

8. **Fang, Jian, Li & Ma**, *AI-Newton: A concept-driven physical law discovery system without prior physical knowledge*, *Physical Review Research* **2026-11-04**, DOI https://doi.org/10.1103/dvvc-4rsr; code https://github.com/Science-Discovery/AI-Newton — `PUBLISHED/EXPERIMENT + CODE`. **46** mechanics experiments; rediscovers second law, energy conservation, gravitational law. Builds original interpretable concepts and general laws, **simplifies redundant relations to avoid knowledge-base/search explosion**, test acceptance external to search. Reported **up to 1,200 trials and around 48 hours average runtime** in described test setup; do not label cost-free. **Author-identified future work**: explicit symmetry concepts and optional LLM integrations of DSL/recommender/plausible reasoning for frontier scientific discovery. **This is the closest substantive rival to “subtractive physics discovery”**.
9. **Xia & Zhang**, *Data-driven progressive discovery of physical laws*, *Physical Review Research* **2026-11-02**, DOI https://doi.org/10.1103/f2kp-pp4q — `PUBLISHED/EXPERIMENT DONE`. Chain of Symbolic Regression (CoSR), rederives Kepler-to-Newton progression, studies convection, viscous flows, laser-metal interaction and aircraft scaling. **Originality lost**: compact staged, physical-meaningful equation discovery.
10. **Wang & Buehler**, *Self-revising discovery systems for science: A categorical framework for agentic artificial intelligence*, *Extreme Mechanics Letters* **Oct 2026**, DOI https://doi.org/10.1016/j.eml.2026.102518; arXiv:2606.01444 — `PUBLISHED/THEORY + CASE STUDIES`. Formal *representational regime changes*, MDL/AIC gates, Builder/Breaker for protein mechanics, CategoryScienceClaw with auditable schema/provenance and materials example. **Originality lost:** self-changing conceptual language, rejecting stale regimes with evidence gates. **Not established:** broad controlled superiority of the exact ACSS 3-layer subtraction pipeline at smaller compute in out-of-domain tasks.
11. **Botoko Ekila et al.**, *Emergent Communication in Continuous Worlds*, TACL 2026 https://aclanthology.org/2026.tacl-1.101/ — `PUBLISHED/EXPERIMENT DONE`. Decentralized agent populations self-organize grounded symbolic labels in continuous spaces over **37 datasets**, robust to perceptual variation. “Agents invent language” alone is not novel. **Open at our scope:** measurable new physical law discovery improvement from emergent symbols *compared with equal-data human-label baselines*, after thorough more-specific search.

### Market/elections: externally useful but not proof of the mechanism

12. **Xue et al.**, *Temporal Leakage in Financial News NLP*, arXiv:2608.17223 — `PREPRINT/AUDIT`. 49,799 articles; random chronological leakage inflates metrics (MCC up to 6.5× ratio) and most signals disappear; one narrow M&A effect not transferable to another corpus. **Finance rule:** timestamp availability and chronological, purged, held-out testing; not claims of tradable alpha.
13. **El Haddad et al.**, *Leakage-audited, regime-robust protocol for affective text*, Zenodo https://zenodo.org/records/21383753 — `PREPRINT/SUBMITTED`. ~3.06m messages, seven equities; sentiment/affect lifts do **not** survive careful regime/placebo controls in their reported analysis. **No proof all sentiment is noise**.
14. **When Does Financial Sentiment Help? Selective Feature Fusion and Regime Decomposition**, SSRN 2026 https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6691938 — `PREPRINT`. Selective smoothed/lagged sentiment features reportedly improve market-regime classification where naïve inclusion hurts. **Important counterexample:** sometimes affective features *are signal*, so universal subtraction is unsound.
15. **Election forecasting political economy models** (2025) https://www.sciencedirect.com/science/article/pii/S0169207025000135 and SIAM 2026 historical time/pollster modeling https://epubs.siam.org/doi/full/10.1137/24M1719505 — `PUBLISHED METHODS`. Fundamentals/polls/forecast calibration precede any ACSS “remove political rhetoric to recover economy” claim. Economic welfare is multidimensional; *physical truth* is not a suitable single score for electoral preferences.

**Investigator map:** Oxford Internet Institute (Ibrahim/Rocher/Hafner); Cheng et al./Stanford–Microsoft Research via their stated institutional affiliations (verify individually before outreach); Yao et al. multi-institute causal representation; Peking University AI-Newton group; Northwestern Polytechnical University CoSR group; Wang/Buehler MIT scientific agentics; Botoko Ekila et al. emergent communication; VLM/physics benchmark teams. **No verified claim about private unpublished projects or willingness to collaborate.**

## C. Five agents: direct predecessor / status / likely contribution

| Our arm | Closest already-done science | What is distinct in our *test design*? | Confidence in novelty |
|---|---|---|---|
| **A0 baseline** | Existing standard LLM benchmarks | Same evidence/schema/latency fairness and naive natural-use optional comparator | none |
| **A1 social subtraction** | Nature warmth/sycophancy, ELEPHANT, SYCON | Test incremental effect on *physical causal discovery*, not just false-user-agreement | low / not checked exhaustively |
| **A2 projection subtraction** | Yao ICLR identifiability; PhysBench | Conditional decision/abstention under *same multisensor data* and user-framing controls | low |
| **A3 physics/maths** | AI-Newton, CoSR, physics-informed verification | Marginal improvement after A1+A2 at **same compute and evidence**, anomalies retained | low |
| **A4 conceptual reformulation** | Wang/Buehler, AI-Newton, emergent grounded symbols | Directly test negative-interaction, compression–accuracy/resource frontier and learned schema transfer | **unproven**, potentially testable |

**Public-source status statement:** We do **not** have evidence that a prior study has run *this exact five-arm, 3-layer, equal-budget comparison*. This is not evidence that the combination was never imagined or is publishable. **A design gap is not necessarily a knowledge gap.**

## D. Before any experiment, define WHAT “more intelligent” means

Do not use generic “better answer” preference scoring. Possible **pre-registrable primary claim**:

> Across generated out-of-distribution causal-physical tasks sharing fixed evidence and matched inference cost, A4 decreases held-out predictive error relative to A0 and to an equally elaborate non-subtractive control while preserving or reducing total compute.

Reject if: no advantage on held-out data; confidence rises but errors worsen; results disappear with prompt-length/effort placebo; physics priors reject genuine anomalies; model only rephrases descriptions without predictive benefit; results do not replicate across a second family or data generator. Report domain-specific results rather than universal intelligence claims.

**Measurement proposal:**
- Prediction loss (numeric MAE/RMSE or accuracy), law validity under new conditions, calibration and correct abstention on nonidentifiable cases.
- Assumption count only if assumptions formally enumerated, not just shorter narrative; MDL/description length **conditional on equally good prediction**.
- Novel-variable value assessed by independent hidden-data likelihood, not model self-congratulation.
- Cost/performance Pareto: total input/output tokens, runtime, local verifier compute, and monetary cost if accessible.
- Negative controls: social/affective words that carry genuinely relevant information; data that violate a simplistic familiar physical law but are real within simulation; underdetermination where no unique projection inversion exists.
- Statistical unit = independent task family / generator seed, **not** just individual prompts. 30 preliminary fixtures and 1 call per arm **cannot support strong inference**.

## E. Scientific sequence and decision gates

**Gate 0 — Question & claims (NOW):** Freeze conceptual dictionary (noise, projection, law/constraint, concept revision, learning, intelligence, consciousness). Explicitly split a *prompt-policy pilot* from a *true training-data subtraction model*. Founder confirms before formal freeze.
**Gate 1 — Literature closure:** Search full texts, citations, datasets, repositories and public team roadmaps around **AI-Newton, CoSR, Wang/Buehler, Yao, Ibrahim/Rocher, ELEPHANT, TACL emergent communication**; build pairwise matrix with actual controls/compute, future directions and limits. Record date/index/query/count. Unpublished private work is unknowable.
**Gate 2 — Offline test fixture and independent oracle:** Build simple simulated cameras, hidden-state generators, dynamics and explicit adjudication tests; validate without LLM calls.
**Gate 3 — Feasibility:** Same model and identical data; run A0/A1/A2/A3/A4 only after authorized access/cost decision. Add equal-token strong baseline, prompt-length placebo, random order, blind scoring. A0 should not be intentionally weak.
**Gate 4 — Attribution:** Small factorial/ablation study; L1 alone, L2 alone, L3 alone and paired combinations + A4 revise, separating additive gains from interactions. Pre-register a small number of primary contrasts and use held-out seeds.
**Gate 5 — External validity:** After robust objective gains, time-stamped stock-market and election forecasting stress tests; no real trading and no partisan outcome advocacy. Do not treat financial noise as entirely removable—sentiment can be a causal input to price.
**Gate 6 — Collaboration/publication:** Share **the question, landscape, benchmark specification and negative-controls design** with methodologists first; invite critique/replication, not automatic coauthorship or named endorsements. Only title/formally propose Paper 2 after novelty/feasibility passes.

## F. What goes where in ACSS and who does what

**Canonical in GitHub (public review branch):**
- `ACSS_RESEARCH_STATE.md` = ~1-minute current status and decision index; do not append full bibliographic essays.
- `proposals/ACSS_SUBTRACTIVE_INTELLIGENCE_RESEARCH_AUDIT_AND_LANDSCAPE_2026-11-16.md` = this evidence audit and novelty gate.
- `proposals/ACSS_SUBTRACTIVE_INTELLIGENCE_FIVE_AGENT_PILOT_v0.1.md` = operational/technical candidate; revise only under new version and traceable decision.
- `proposals/FOUNDER_*_2026-11-16.md` = attributed founder thinking and evolving interpretation; preserve as intellectual history.
- `experiments/subtractive-intelligence/` = **future** scripts/fixtures/test rules, only once authorized.
- Paper 1 `protocols/T1-T25`, Zenodo DOI etc = frozen historical branch, **no edits**.
- Paper 2 prior CPB drafts = paused historical candidates, **no automatic resurrection**.

**Can start locally without any LLM expense:** literature register, claim/falsifier specification, independent synthetic oracle, simple benchmark fixtures, source-license review, open protocol documentation.

**Best future collaborators if needed:** an identifiability/causal representation researcher; scientific ML or symbolic regression engineer; model-evaluation statistician (blinding and leakage); cognitive scientist/philosopher of science for construct boundaries; later financial econometrician/political scientist for external validity. Don't assume private team trajectories or contact anyone without approval.

**Do not release prematurely:** speculative “proof of consciousness”, “superintelligence”, claimed no-bias intelligence, private stock ledger, trade signals, personally identifying conversations or untested election analysis.

## G. Search log and incompleteness

**2026-11-16 scoping search:** primary Nature, ICLR, ACL/TACL, APS journals, MDPI/SSRN/Zenodo/ArXiv, Microsoft Research and institutional scientific sites; targeted keywords: `warmth sycophancy`, `social sycophancy`, `multi-view causal representation identifiability`, `physbench`, `phyworldbench`, `physics law discovery symbolic regression`, `AI-Newton`, `self-revising science category theory`, `emergent communication grounded vocabulary`, `machine unlearning`, `stock sentiment temporal leakage ablation`, `election fundamentals forecasts`. Confirmed published dates and exact claims against publisher HTML for high-priority sources. Some publisher full papers available, others abstracts only; **not** a systematic review, no documented database-wide hit counts, no complete 2026 citation graph and no private research access. Priority 3–5 full-paper comparisons required before declaring novelty.

**Revisit after every new paper:** if any source already ran the exact 3-layer full factorial with matched resources, demote originality claim; if strong prompt and non-subtractive controls tie A4, treat subtraction as nonessential; if the comparison is successful on synthetic tasks but not real-world domains, limit claims to that synthetic task distribution.
