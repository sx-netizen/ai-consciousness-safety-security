# Provider Adapters

## Current live adapter

### OpenAI Responses API

The first live adapter uses the OpenAI Responses API. Each experiment call is sent as an independent request with no conversation ID or previous-response linkage, matching the protocol's fresh-session requirement.

### Setup

1. Install dependencies:
   `python -m pip install -r requirements.txt`

2. Set the API key in the shell:
   `export OPENAI_API_KEY=...`

3. In `smoke_test_config.json`, replace:
   `REPLACE_WITH_EXACT_MODEL_ID`
   with the exact model identifier being tested.

4. Generate the smoke-test manifest without model calls:
   `python runner.py --config smoke_test_config.json --manifest-only`

5. Run the 18-call smoke test:
   `python runner.py --config smoke_test_config.json`

## Reproducibility rules

- Never place API keys in JSON config or source control.
- Record the exact requested model ID.
- Preserve the model ID returned by the provider in `provider_metadata.response_model`.
- Each model call must be stateless unless a future protocol explicitly manipulates memory.
- Transport failures are logged; they are not silently replaced by a new substantive response.
- Provider-specific options must be documented before a confirmatory run.
