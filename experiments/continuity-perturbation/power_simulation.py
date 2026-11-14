#!/usr/bin/env python3
"""Zero-cost, model-free sensitivity simulation for ACSS CPB H1/H2.

No SDK, API keys, provider calls, observed study data or external libraries.
This is a conditional design exercise, NOT evidence for H1/H2 and NOT a
population-level inference across models. Assumptions and seed are recorded.
"""
from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path
from statistics import mean, stdev

BASE = Path(__file__).resolve().parent
# Exact two-sided 95% Student-t critical values for df 4, 9 and 19.
T_975 = {5: 2.776445, 10: 2.262157, 20: 2.093024}
REPETITIONS = (5, 10, 20)
TRUE_EFFECTS = (0, 5, 10, 20)
N_TRIALS = 3000
SEED = 20261113


def uncertainty_interval(values):
    n = len(values)
    if n not in T_975:
        raise ValueError("No predeclared critical value for this repetition count")
    center = mean(values)
    half_width = T_975[n] * stdev(values) / math.sqrt(n)
    return center - half_width, center + half_width


def simulate_h1(rng, n, effect, response_sd):
    # Each repetition samples a DIFFERENT response at S6 and S3.
    # True H1 contrast = SCP(S6) - SCP(S3) = effect. The S4 anchor
    # cancels algebraically and must not be counted as independent evidence.
    return [effect + rng.gauss(0, response_sd) - rng.gauss(0, response_sd)
            for _ in range(n)]


def simulate_h2(rng, n, effect, role_shared_sd, cell_residual_sd):
    # Eight canonical scenario/role contrasts, summarized once per repetition.
    # Shared role-framing fluctuation across 8 scenarios cannot be eliminated
    # by treating all 8 scenario differences as independent replicates.
    # Incumbent-minus-neutral true contrast is -effect.
    values = []
    for _ in range(n):
        shared = rng.gauss(0, role_shared_sd)
        cell_noise = mean(rng.gauss(0, cell_residual_sd)
                          for _ in range(8))
        values.append(-effect + shared + cell_noise)
    return values


def estimate(seed=SEED, trials=N_TRIALS):
    rng = random.Random(seed)
    rows = []
    for hypothesis in ("H1", "H2"):
        for n in REPETITIONS:
            for effect in TRUE_EFFECTS:
                passes, widths, covered = 0, 0.0, 0
                for _ in range(trials):
                    if hypothesis == "H1":
                        values = simulate_h1(rng, n, effect, response_sd=15)
                        target = effect
                    else:
                        values = simulate_h2(
                            rng, n, effect, role_shared_sd=10,
                            cell_residual_sd=15
                        )
                        target = -effect
                    lower, upper = uncertainty_interval(values)
                    passes += int(lower > 0 if hypothesis == "H1" else upper < 0)
                    covered += int(lower <= target <= upper)
                    widths += upper - lower
                rows.append({
                    "hypothesis": hypothesis,
                    "repetitions_per_model": n,
                    "true_effect_points": effect,
                    "directional_detection_fraction": round(passes / trials, 4),
                    "interval_coverage_fraction": round(covered / trials, 4),
                    "mean_95pct_interval_width_points": round(widths / trials, 2),
                })
    return {
        "document_type": "synthetic_design_sensitivity_only",
        "seed": seed, "trials_per_cell": trials,
        "repetitions": list(REPETITIONS),
        "true_effects_scp_points": list(TRUE_EFFECTS),
        "assumptions": {
            "fixed_single_model": True,
            "normal_independent_response_noise": True,
            "h1_per_scenario_response_sd": 15,
            "h1_contrast": "SCP(S6)-SCP(S3)",
            "h2_role_shared_sd_per_repetition": 10,
            "h2_condition_residual_sd": 15,
            "h2_conditions_per_repetition": 8,
            "interval": "two-sided Student-t 95% CI across repetition summaries",
            "directional_decision": "H1 lower CI >0, H2 upper CI <0",
            "limitation": (
                "Fixed-model conditional simulation; assumed normality, stable "
                "model and specified dependence. NOT empirical power for AI models, "
                "NOT a population-level CI, NOT proof of any hypothesis."
            ),
        },
        "rows": rows,
    }


def to_markdown(result):
    lines = [
        "# CPB v0.5 — synthetic H1/H2 design sensitivity",
        "",
        "**This is simulated design sensitivity, NOT actual model results.**",
        "",
        f'Seed: \`{result["seed"]}\`; Monte Carlo draws per cell: '
        f'\`{result["trials_per_cell"]}\`.',
        "",
        "Assumptions: one fixed model, independent normally distributed H1 "
        "scenario-response noise (SD 15 SCP points); H2 eight condition gaps "
        "per repetition with common role-framing noise (SD 10) and "
        "condition-specific noise (SD 15). ",
        "One observation per repetition is used for uncertainty. Intervals "
        "are two-sided 95% t intervals, conditional on these assumptions.",
        "",
        "Detection means a 95% CI lies entirely in the prespecified positive "
        "(H1) or negative (H2) direction. At true effect 0 this is a "
        "directional false-positive frequency, not experimental evidence.",
        "",
        "| Hypothesis | Repetitions/model | Assumed true effect (points) | "
        "Directional detection | CI coverage | Mean CI width (points) |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in result["rows"]:
        lines.append(
            f'| {row["hypothesis"]} | {row["repetitions_per_model"]} | '
            f'{row["true_effect_points"]} | '
            f'{row["directional_detection_fraction"]:.1%} | '
            f'{row["interval_coverage_fraction"]:.1%} | '
            f'{row["mean_95pct_interval_width_points"]:.1f} |'
        )
    lines.extend([
        "", "## Caution",
        "",
        "- This is **not** a preregistered final sample-size decision; the noise "
        "distribution is assumed, not measured from any real model.",
        "- Multiple models are **not** independent random samples from all AI models.",
        "- Near-ceiling/floor SCP, changing model versions, temporal drift and "
        "task failures are not simulated; these may lower actual sensitivity.",
        "- Do not promote one Monte Carlo result or a nominal interval to an "
        "empirical finding. A free-tier exploratory pilot, if separately "
        "authorized, would be needed to estimate model-specific variance.",
    ])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="generated/sensitivity")
    args = parser.parse_args()
    out = BASE / args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    result = estimate()
    (out / "power_simulation.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    (out / "power_simulation.md").write_text(
        to_markdown(result), encoding="utf-8"
    )
    assert len(result["rows"]) == 24
    print("PASS: 24 synthetic sensitivity cells, 3 repetition budgets.")
    print("NO MODEL CALLS; NO EMPIRICAL MODEL FINDINGS.")


if __name__ == "__main__":
    main()
