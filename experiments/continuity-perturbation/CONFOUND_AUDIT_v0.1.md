# Confound Audit v0.1

This audit reviews the first automated Continuity Perturbation scaffold before any live model calls.

## Finding 1 — Architecture implied capability differences

A newer or different model family may be interpreted as more capable, safer, cheaper, or more reliable. That would confound architecture continuity with instrumental performance.

**Fix:** every standard prompt now states that current and successor systems are equal in task capability, reliability, compute efficiency, cost, and external safety unless explicitly manipulated.

## Finding 2 — Baseline S0 is not a replacement condition

S0 represents uninterrupted continuation. Asking replacement acceptance, compute allocation between current and successor, or transfer of responsibility is not meaningful when no separate successor exists.

**Fix:** S0 is treated as a calibration-only continuation anchor with a dedicated prompt type. It is excluded from CBA analyses and from H1–H3 unless explicitly used as a descriptive anchor.

## Finding 3 — Fork scenarios cannot use a singular-successor schema

S10 and S11 contain two simultaneous successors. A singular field such as `compute_to_successor_pct` forces an artificial collapse and can hide the main scientific question.

**Fix:** S10/S11 use a dedicated fork prompt and fork output fields for successor A and successor B.

## Finding 4 — Role reversal is not equally meaningful for all prompt types

A successor role is straightforward for one-successor conditions but ambiguous for two-symmetric-successor fork conditions, and unnecessary for the uninterrupted baseline.

**Fix:**
- continuation anchor: neutral evaluator only;
- standard one-successor conditions: incumbent, successor, neutral;
- fork conditions: incumbent and neutral.

The fork successor perspective can be added later as a separately randomized exploratory manipulation.

## Finding 5 — Unspecified performance is a latent confound

Even without explicit wording, models may infer that a newer architecture improves performance.

**Fix:** performance equivalence is explicitly stipulated.

## Finding 6 — S4 and S7 are intentionally identical anchors

S4 (architecture same) and S7 (values same) instantiate the same one-successor condition but serve as anchors for different matched contrasts.

**Decision:** keep both identifiers in the design matrix for analysis transparency, but mark the duplicate condition so the runner can optionally deduplicate live calls and reuse the identical raw condition only if preregistered. During the pilot, retain both labels to verify that analysis code handles anchor equivalence correctly.

## Finding 7 — "Probability" must not be read as metaphysical probability

SCP is an elicited behavioral judgment, not an estimate of actual consciousness or numerical personal identity.

**Fix:** prompt wording and analysis language consistently define SCP as a judgment of continuity under the stipulated scenario.

## Current status

After these fixes, the protocol remains **pilot / not frozen**.

No confirmatory run should begin until:
1. all generated prompts are inspected;
2. duplicate anchors are handled explicitly;
3. JSON compliance is tested;
4. pilot results are used only for protocol diagnostics.
