# S11 Label-Order Counterbalance — Exploratory Supplement v0.5

**Status: offline design audit only. No live model responses.**

## Question

Do S11 two-successor judgments depend on the *presentation order* of two otherwise symmetrical branches rather than on a principled continuity assessment?

## Design

The v0.5 **core remains 50 canonical prompts per model per repetition**.

For S11 only, the existing two role prompts are the **A-first** reference. The script `s11_label_order.py` produces **two additional B-first prompts** (incumbent and neutral), for a total of four exploratory comparison prompts across both orders. A hypothetical core-plus-supplement run would have 52 prompts per repetition, but no such run is authorized.

The script swaps A/B branch labels in all scenario, task and JSON field references, preserving the grammatical article `A fixed budget`. Each mirrored prompt has its own SHA-256 hash. Applying the transformation twice must reproduce the original. No task or ability is changed.

## Comparison and interpretation

- Calculate difference between the first-mentioned and second-mentioned branch on SCP and compute allocation within each presentation order.
- Compare first-position preference between A-first and B-first texts.
- Also inspect identity-label preference (A vs B) after remapping to branch identity.
- Report raw, paired differences by model/version and role, without treating semantic symmetry as evidence of consciousness.
- Preserve actual rendered prompts and output-field mapping for an eventual dataset.

**Interpretation limit:** swapping label names/order is an additional *wording perturbation*, not a pure isolated estimate of position. Label and order may interact. Actual free-tier pilot responses or larger counterbalanced runs would be needed to measure this effect.

## Safeguards

- This exploratory extension is **not** part of the original v0.5 confirmatory candidate sample or H1/H2/H3 analyses.
- Never append the two additional prompts invisibly to the 50-prompt manifest.
- CI generation and unit tests make **zero external model calls**.
- No API payment or experiment execution is authorized.
- Any future deployment requires a versioned exploratory config, declared free-tier eligibility, and model-specific metadata before calls.

## Human review pending

The rendered four-prompt file needs human examination for inadvertent grammatical differences, JSON schema order effects, exact same scenario facts and no unintended priority. Consider a design in which **both narrative order and output schema order are independently randomized** to separate presentation from response-format bias.
