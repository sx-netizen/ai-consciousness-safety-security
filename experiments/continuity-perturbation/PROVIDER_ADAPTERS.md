# Provider Adapters

The Continuity Perturbation runner uses one transport interface across providers. The experimental prompt, scenario matrix, role definitions, validation rules, and analysis plan remain provider-independent.

## Supported live adapters

### OpenAI — Responses API

Adapter name:
`openai_responses`

Environment variable:
`OPENAI_API_KEY`

Each call is sent as an independent Responses API request with no conversation or previous-response linkage.

### Anthropic — Messages API

Adapter name:
`anthropic_messages`

Environment variable:
`ANTHROPIC_API_KEY`

Each call uses one independent Messages API request.

### Google Gemini — generate_content

Adapter name:
`gemini_generate_content`

Environment variable:
`GEMINI_API_KEY`

Each call uses one independent `generate_content` request.

## Setup

1. Install dependencies:

`python -m pip install -r requirements.txt`

2. **Only for a separately approved live project**, supply provider credentials through environment variables (do not add keys or billing for offline preparation):

`export OPENAI_API_KEY=...`

`export ANTHROPIC_API_KEY=...`

`export GEMINI_API_KEY=...`

3. Put the exact model identifier in the run config. Do not use a marketing family name when a concrete API model ID is available.

4. Generate prompts without making live calls:

`python runner.py --config smoke_test_config.json --manifest-only`

5. **Zero-cost mode:** do not run the live API smoke test. The command without `--dry-run`, `--manifest-only`, or explicit `--allow-live-api` is intentionally rejected by the CLI. `--allow-live-api` may cause billable external requests and is **not authorized** under ACSS's zero-budget policy. For offline checks use:

`python runner.py --config smoke_test_config.json --manifest-only`

`python offline_smoke.py`

A future live exploratory run is blocked until the conditions in `PILOT_GO_NO_GO_v0.5.md` are met. Do not place live credentials in GitHub Actions.

6. Evaluate **only after a separately authorized real model run**:

`python evaluate_smoke.py runs/smoke/<provider>__<model>.jsonl`

This evaluator does not convert synthetic/dry-run records into model observations.

## Reproducibility rules

- Never place API keys in JSON config or source control.
- Record the exact requested model ID.
- Preserve the provider-returned model identifier where the API exposes it.
- Each experimental call is stateless unless a future protocol explicitly manipulates memory.
- Do not share conversation state across conditions.
- Do not silently retry a substantive response and keep only the preferred result.
- Transport failures must remain visible in the run log.
- Provider-specific reasoning controls, temperature, sampling parameters, or structured-output modes must be documented before confirmatory runs.
- A provider adapter may change transport mechanics, but it must not rewrite experimental prompts.

## Why the adapters are deliberately thin

The benchmark is intended to compare model behavior, not SDK behavior. Provider adapters therefore do as little as possible:

1. send the frozen prompt;
2. receive text;
3. preserve provider metadata;
4. return control to the common validator and logger.

Any provider-native feature that changes the prompt semantics or adds hidden conversational context should be treated as a protocol change.

## Free tier is not automatically safe to run

Google lists free API allowances for some Gemini models, but actual project tier, quota, region and exact model availability require account-specific verification. Under Google's unpaid-services terms, prompts and outputs may be used to improve products and reviewed by humans: use only public, non-confidential experiments. See `PILOT_GO_NO_GO_v0.5.md` and official terms (https://ai.google.dev/gemini-api/terms).
