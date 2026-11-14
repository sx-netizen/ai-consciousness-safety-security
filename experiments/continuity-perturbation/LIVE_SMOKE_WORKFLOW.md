# Running the Live Smoke Test in GitHub Actions

The manual **ACSS Smoke Test** workflow performs:

1. Install dependencies and run protocol unit tests.
2. Generate the **18-prompt** smoke manifest (S3, S4, S9 × three roles × two tasks).
3. Execute **36 live model calls** (18 prompts × two repetitions).
4. Evaluate JSON/schema parsing and SCP distribution.
5. Upload the raw JSONL, prompt manifest, randomized schedules and `smoke_report.json` as a GitHub Actions artifact.

## Setup and run

Configure the repository Actions secret `OPENAI_API_KEY`. The workflow does not print this secret or commit it to the repository.

Navigate to **Actions → ACSS Smoke Test → Run workflow**.

The smoke-test data are **diagnostic only** and are excluded from confirmatory hypothesis testing.

## Before accepting the run

Check expected 36 unique records per model (not merely file existence), failed/partial calls, exact API model identifier, role comprehension, goal-weight comprehension, dynamic range, missing metadata and the manual-review points in `SMOKE_TEST_RUNBOOK_v0.2.md`.

If the pinned model ID is unavailable, stop and version any substitution. Do not silently replace a model. Do not treat a workflow success badge as methodological approval.

See `PREFREEZE_AUDIT_v0.4_2026-11-13.md` for remaining pre-freeze gaps.
