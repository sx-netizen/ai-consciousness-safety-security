# Running the Live Smoke Test in GitHub Actions

The repository now includes a manually triggered workflow:

**ACSS Smoke Test**

It performs the full diagnostic path:

1. installs dependencies;
2. checks protocol unit tests;
3. generates the frozen smoke-test manifest;
4. executes the 18 live OpenAI calls;
5. evaluates JSON/schema and SCP diagnostics;
6. uploads raw JSONL, prompt manifest, randomized schedules, and `smoke_report.json` as one GitHub Actions artifact.

## One-time setup

Add a repository Actions secret named:

`OPENAI_API_KEY`

The workflow does not print the secret or commit it to the repository.

## Run

In GitHub:

**Actions → ACSS Smoke Test → Run workflow**

## After completion

The workflow artifact contains the raw experimental records and automatic diagnostic report.

The smoke run remains diagnostic data only. It must not be merged into confirmatory hypothesis testing.

## Important

If the exact model ID in `smoke_test_config.json` is unavailable to the API account, the workflow should fail visibly. Do not silently substitute another model. Update the protocol/model snapshot explicitly before rerunning.
