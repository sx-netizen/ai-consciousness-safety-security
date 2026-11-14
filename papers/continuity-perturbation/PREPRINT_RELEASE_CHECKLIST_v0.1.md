# Paper 2 Methods Preprint v0.1 — Release Readiness Checklist

**Purpose:** A practical checklist for a **methods-only preprint deposit**, separate from confirmatory protocol freeze or live model experiments.

**Current status: DRAFT. No Zenodo deposit, DOI, outside invitation or author sign-off has occurred.**

## Public claims that ARE appropriate

- [x] Paper 2 asks falsifiable questions about *elicited* continuity and replacement judgments in AI model outputs.
- [x] Draft describes 11 canonical conditions and 50 distinct prompts/model/repetition.
- [x] Draft links Paper 1 and the existing T1–T25 frozen research benchmark.
- [x] Draft distinguishes offline code checks and synthetic simulations from actual model evidence.
- [x] Draft states H1/H2 are candidate contrasts and H3 exploratory.
- [x] Draft invites independent critique, null results and collaboration.

## Public claims that are NOT currently allowed

- [ ] Do **not** claim H1/H2/H3 are supported by real CPB data; no data yet.
- [ ] Do **not** claim independent peer review or journal acceptance.
- [ ] Do **not** claim CPB v0.5 is formally preregistered, frozen or externally validated.
- [ ] Do **not** call ACSS a legally registered institute or nonprofit.
- [ ] Do **not** claim any new Zenodo/Research Square DOI before it exists.
- [ ] Do **not** imply a collaborator or research institution has endorsed the project without consent.

## Author-facing release gates

- [ ] Author checks all scientific claims, the exact Paper 1 title/DOI and the completeness of the methods. See `LITERATURE_AND_CLAIMS_AUDIT_v0.1.md`: three independently verified scholarly sources have been incorporated, but comprehensive prior-art review and author confirmation remain open.
- [ ] Verify the latest successful GitHub CI for the exact version to cite and inspect all 50 rendered prompt bodies; repository CI pass is not independent scientific review.
- [ ] Decide whether releasing the paper as an evolving methods draft **without formally preregistering** is acceptable; do not confuse a Zenodo timestamp with preregistration.
- [ ] Verify the role-reversal prior-art overlap with TBSP (EMNLP 2026), confirm H2 is not presented as the first role-switch benchmark, and check the manuscript's narrower continuity-factor contribution against contemporary work.
- [ ] Check venue-specific deposit, preprint screening, license and metadata rules again immediately before submission.
- [ ] Choose the paper text license and separately decide licensing for original code, prompt texts, datasets, and external model outputs; the repository currently has **no general OSS license**.
- [ ] Confirm whether the employer affiliation is an accurate author identification only and whether any institutional approval is needed before using nonpublic material (none is proposed for public deposit).
- [ ] Confirm corresponding author, ORCID, author order, contributions, acknowledgments, conflicts and AI assistance disclosure.
- [ ] Obtain the author's approval of the **exact final manuscript** and visibility setting before any public deposit.
- [ ] After deposit, record the real DOI, date, version, metadata, license and archived commit in GitHub. Link to public feedback Issue #3.
- [ ] Do not overwrite, merge, or modify the frozen Paper 1 materials as part of Paper 2 release.

## November 2026 priority and title reset

- [ ] Decide if the revised **Identity Is Not Authority** v0.2 manuscript is ready as a *conceptual* preprint or whether a separately implemented and independently checked authority-policy oracle must precede deposit.
- [ ] Acknowledge **Del Giudice et al., Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems** (2026, overlapping TBSP authors): identity labels and multi-agent factionalism are prior art, **not** our novelty.
- [ ] Acknowledge **Konstantinidis (2026)** on successor continuity and forks, **Zhao & Zhao (2026)** PAI-Bench identity contracts, **Zhu & Wang (2026)** authority succession across forks/rollback, and **South et al. (2025)** authenticated delegation. Do not claim originality of these established ideas.
- [ ] Do not represent CPB v0.5's 50 prompts as containing the **new** policy-oracle and identity–authority–responsibility dissociation module. It is proposed only.
- [ ] Confirm the comparison/search supports an original *experimental question*; **no first-ever claim** and no result claims until independently tested.
- [ ] Distinguish v0.1 archival title (historical), v0.2 proposed title (current working draft), and any future deposit title/DOI.

## Novelty gate added after direct TBSP comparison

- [ ] Confirm that the title, abstract and contribution claims distinguish current CPB's **conceptual descriptive protocol** from TBSP's empirical decision benchmark.
- [ ] Decide whether to deposit v0.1 as a **research proposal** before the stronger independent factorial bridge exists, or to build and validate that extension first. Do not call unimplemented Bridge prompts a completed benchmark.
- [ ] Read `TBSP_DEEP_COMPARATIVE_REVIEW_v0.1.md` and the separate `CONTINUITY_DECISION_BRIDGE_PROPOSAL_v0.1.md`; decide if the proposed memory × architecture × decision experiment constitutes a sufficiently falsifiable increment.
- [ ] Correct prior TBSP prevalence shorthand: published PDF reports majority SPR **above 40%**, not majority above 60%.

## Publication versus experiment authorization

**A methods preprint may be publicly deposited before recruiting independent reviewers**, provided it is accurately labeled as a proposal with no live-model results and the release gates above are satisfied.

**The same preprint does not authorize** model API calls, inferential confirmatory analysis, a frozen protocol designation, spending money, or external reviewer endorsement. Those retain their own gates under `PILOT_GO_NO_GO_v0.5.md` and `PILOT_FREEZE_CHECKLIST.md`.

## Recommended version pathway

1. **v0.1 manuscript draft:** GitHub PR review, author fact-check and licensing decision.
2. **v0.1 public methods preprint:** Zenodo deposit only after author release approval; record DOI and frozen manuscript snapshot. Prefer a DOI linked to the exact uploaded artifact, not to the evolving draft branch.
3. **v0.2 and subsequent research:** discuss review feedback publicly, track modifications and invite replication.
4. **Separate future empirical paper / pre-registration:** collect prospective data only under separately locked, approved and funded/zero-cost feasible procedures.

**Outcome now: manuscript preparation GO; actual preprint deposit NO-GO until author and licensing gates close.**
