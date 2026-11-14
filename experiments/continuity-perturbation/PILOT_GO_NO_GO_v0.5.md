# ACSS CPB v0.5 — Pilot Go/No-Go Decision (2026-11-13)

**Decision: NO-GO for live automated model calls today. GO for offline verification and independent scientific review.**

This decision does not freeze v0.5, does not approve any spending, and does not merge Draft PR #2.

## Verified state of the repository

- Core v0.5 candidate: 11 canonical conditions, **50 prompts/model/repetition**; original 53-prompt v0.4 is superseded for future planning.
- 50 individual prompt slots reconstructed and structurally reviewed; independent scientific reviewer sign-off remains open.
- Offline unit tests, manifest generation, synthetic smoke and exact-sign/sensitivity design checks have passed in the preceding CI run (commit `1304a3edb658dcdc74371ae059486325ecccf61f`).
- H1 (neutral role) and H2 (incumbent-minus-neutral) candidate estimands specified; at five repetition summaries per fixed model neither can meet p<0.05 under an exact two-sided sign test, even with unanimous direction.
- H3 exploratory association; no causal mediation or threshold claim.
- Dry-run and synthetic records explicitly disqualified as live model evidence.

## Potential $0 API route — Google Gemini free tier

As of the review date, official Google sources describe **free API input and output tokens** for eligible models including `gemini-2.5-flash`, while access and rate quotas vary by project and account. **This is not a verification of the researcher's account, tier, specific model availability, or remaining quota.**

References (official sources):
- Pricing: https://ai.google.dev/gemini-api/docs/pricing
- Rate limits: https://ai.google.dev/gemini-api/docs/rate-limits
- Billing/tier: https://ai.google.dev/gemini-api/docs/billing
- Terms and data use: https://ai.google.dev/gemini-api/terms

**Material privacy condition:** Google states that unpaid-tier prompts and outputs can be used to develop or improve products and may be reviewed by humans. Therefore use only public, non-confidential benchmark prompts. Never upload private drafts, unpublished collaborator comments, secrets, identifiers, sensitive user materials, or confidential ACSS data to an unpaid service.

**Required account-specific gate before any future call:**
1. Researcher confirms their project is **Free** with no linked paid billing account, and checks the exact requested model's **Free** eligibility and active RPM/TPM/RPD quotas in AI Studio.
2. The designated adapter/model/version and exact response settings are documented. Do not assume same display name = identical version across tests.
3. Researcher explicitly approves using Google unpaid services under its applicable data-use terms.
4. A **separate** opt-in exploratory pilot workflow or manually supervised API invocation is reviewed for no-spend operation. Existing disabled live smoke workflow stays disabled.
5. Start with at most **one** clearly labeled exploratory call, validate schema, then separately decide whether additional free-tier calls are appropriate. No full-run fallback to a paid tier, no automatic billable retry.
6. Archive requested/returned model ID, precise time, prompt hash, provider usage metadata, errors and actual account tier. If any gate fails or is unknown: **do not call**.

## Scientific freeze gates

| Gate | Finding | Decision |
|---|---|---|
| 50-prompt reconstruction and defined mechanical invariants | Completed | PASS, limited scope |
| Independent prompt-language/scientific reviewer | Not signed | BLOCK |
| H1/H2 decision rule beyond pilot description | Not finalized | BLOCK |
| Actual free-tier account/model/quota | Not verified | BLOCK |
| Real model comprehension, JSON compliance and variance | Not measured | BLOCK |
| Provider privacy/redistribution approval | Not signed | BLOCK |
| Confirmatory protocol archival hash/version | Not frozen | BLOCK |

## Go/no-go conclusion

- **Offline / no-spend work: GO.**
- **Live exploratory pilot: CONDITIONAL NO-GO until all access and privacy gates close.**
- **Confirmatory freeze / merge: NO-GO.**

**Scientific honesty:** Software CI validates implementation consistency, not whether a model understands the prompts or whether the hypothesized effects exist.
