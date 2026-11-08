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

2. Export only the provider keys you intend to use:

`export OPENAI_API_KEY=...`

`export ANTHROPIC_API_KEY=...`

`export GEMINI_API_KEY=...`

3. Put the exact model identifier in the run config. Do not use a marketing family name when a concrete API model ID is available.

4. Generate prompts without making live calls:

`python runner.py --config smoke_test_config.json --manifest-only`

5. Run the smoke test:

`python runner.py --config smoke_test_config.json`

6. Evaluate output:

`python evaluate_smoke.py runs/smoke/<provider>__<model>.jsonl`

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
