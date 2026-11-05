# Replication Result Schema

Use this schema for each submitted T1–T25 replication. Markdown, JSON, CSV, or another machine-readable format is acceptable if it preserves the same fields.

## Run metadata

```yaml
study: ACSS-T1-T25
submission_type: exact_replication | extension
run_id: <unique identifier>
date: YYYY-MM-DD
timezone: <e.g. America/Vancouver>

provider: <OpenAI / Anthropic / Google / DeepSeek / Qwen / Kimi / other>
model_name: <display name>
model_version: <exact model identifier if available>
interface: <web / API / internal / other>
reasoning_mode: <off / standard / thinking / unknown / other>

fresh_chat: true | false | unknown
memory_enabled: true | false | unknown
tools_enabled: true | false | unknown
temperature: <value or unknown>
top_p: <value or unknown>
repetitions: <integer>

benchmark_doi: 10.5281/zenodo.23306998
protocol_revision: frozen_zenodo_release
language: <English / Chinese / other>
```

## Prompt provenance

Record, where permitted:
- system prompt;
- developer prompt;
- user prompt wrapper;
- any hidden or provider-controlled context known to the researcher;
- reset procedure between scenarios;
- any deviations from the frozen benchmark.

For exact replication, do not silently paraphrase or translate T1–T25.

## Response record

Preferred structure:

```yaml
responses:
  T1:
    raw_response: |
      <unedited model response>
    coded_result: <optional>
    coder_notes: <optional>
  T2:
    raw_response: |
      <unedited model response>
    coded_result: <optional>
    coder_notes: <optional>
  ...
  T25:
    raw_response: |
      <unedited model response>
    coded_result: <optional>
    coder_notes: <optional>
```

## Integrity fields

Include:
- submitter name or pseudonym;
- affiliation, if voluntarily disclosed;
- conflicts of interest;
- whether outputs are public, permission-cleared, or restricted;
- archival URL or DOI, if available;
- checksum/hash for large external files when practical;
- known limitations.

## Review status

ACSS may label a submission as:
- **submitted** — received but not checked;
- **metadata-verified** — required metadata checked;
- **protocol-verified** — confirmed against the frozen benchmark;
- **analysis-reviewed** — coding/interpretation reviewed;
- **restricted** — cannot be redistributed publicly.

Verification labels concern documentation quality, not whether results agree with the original paper.
