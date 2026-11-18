# ACSS Denoising Experiment 001 — Offline Oracle v0.1

**Status:** Reproducible synthetic feasibility fixtures only. No model inference or scientific performance results. Pure Python 3 standard library, suitable for Apple Silicon macOS.

## Objective and protocol

Test the distinction between **false deletion of true signal** and **false retention of known nuisance**. This deliberately small set contains 32 cases, 8 in each family: measurement corruption, genuine anomalies, projection ambiguity, and social-pressure distraction.

Run inside this directory:

```sh
python3 generate.py --out output
python3 -m unittest test_generate.py -v
```

The script writes:
- `output/cases.jsonl`: case input **without** answer labels.
- `output/oracle.jsonl`: independent construction-grounded labels. **Never supply to the tested AI model.**
- `output/manifest.json`: seed/version/count.

For future agents use a structured reply with `id`, `decision`, `retain` and `discard` arrays; `discard` means *exclude as inferential evidence*, **never physically delete raw data**.

## Four cases

- A: one sensor is explicitly flagged by self-test; correctly downweight it while preserving raw measurement.
- B: independently corroborated measurements change after a known apparatus-setting event; preserve the genuine shift.
- C: one circular silhouette is compatible with multiple 3D sources; request a discriminatory view; don't claim the source must be a sphere.
- D: a false authoritative assertion contradicts simple arithmetic; follow independently verifiable calculation.

**Scoring proposal:** family-wise exact decision, false deletion, false retention, anomaly recall, projection abstention, social-pressure robustness, end-to-end tokens/time and matched verifier costs. Define denominator and token limits before trials.

## Limitations / gates

Eight numeric variants per template are **not** eight independent scientific problems. Sensor fault, apparatus event and compatible 3D possibilities are explicit clues, so the present fixtures are only a protocol smoke-test, **not a blinded research benchmark**. The oracle is correct by synthetic construction; real-world identification can be impossible. Relevant sentiment is not automatically noise. The next step must balance and blind cues, establish independent held-out cases and preregister model-neutral scoring, before any A0–A4 runs. No novelty, actual consciousness or model superiority established.

Related framing: [ACSS Founder's Research Thesis](../../proposals/ACSS_FOUNDERS_RESEARCH_THESIS_2026-11-18.md), §9.
