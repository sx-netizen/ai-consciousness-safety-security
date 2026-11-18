# Zero-Cost Research Execution Policy — ACSS CPB

**Effective for the current pilot development phase. No paid model calls are authorized.**

## Allowed now

- GitHub repository editing, draft PR review, and standard GitHub-hosted CI in this public repository, subject to GitHub's applicable terms.
- Python unit tests, validation tests, manifest generation, structural scenario audits, statistical simulations and synthetic datasets.
- Offline/dry-run adapter and software smoke checks with clearly marked synthetic outputs.
- Investigation of free-tier model APIs without sending any live calls until access, model identity, privacy terms, free quota and nonbilling project settings are verified.

## Not authorized

- Calling OpenAI, Anthropic, Google paid-tier, or any other billable model API.
- Enabling payment methods, automatic top-ups, premium GitHub runners or billable infrastructure.
- Treating a dry-run or mock response as actual model evidence.
- Automatically substituting free models for preregistered frontier model IDs.

## How to proceed with free models later

1. Verify the exact model's current Free Tier status and eligible region/account.
2. Ensure the API project has **no billing account that can incur costs**, and confirm quota / privacy and data-use terms.
3. Register the substituted free model under a new protocol version / pilot label.
4. Run a tiny diagnostic set within free limits, track quota and stop immediately on limit errors.
5. Mark all outputs *exploratory free-tier pilot*, not the original confirmatory frontier-model comparison.

## Practical limitation

Free-tier model availability and limits change. Free GitHub Actions compute does not imply free model inference. The current `ACSS Smoke Test` workflow invokes a live OpenAI API and **must not be manually launched** during the zero-cost phase, even though the GitHub runner itself is free.

## Restart condition

Any cost-bearing experiment requires a separate explicit authorization. No paid call is implied by approving a GitHub documentation or code PR.
