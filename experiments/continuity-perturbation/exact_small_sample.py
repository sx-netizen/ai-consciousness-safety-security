#!/usr/bin/env python3
"""Exact sign-test resolution for fixed-model paired repetitions.

No external packages, model calls or study observations.
The sign test assumes independent nonzero paired differences under the null;
it does not license pooling models, roles or conditions as independent draws.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

BASE = Path(__file__).resolve().parent


def exact_two_sided_sign_p(positive: int, negative: int) -> float:
    """Exact two-sided p under fair-sign null; ties excluded, not imputed."""
    if any(type(n) is not int or n < 0 for n in (positive, negative)):
        raise ValueError("Counts must be nonnegative integers")
    n = positive + negative
    if n == 0:
        return 1.0
    tail = min(positive, negative)
    return min(1.0, 2.0 * sum(comb(n, j) for j in range(tail + 1)) / (2 ** n))


def report():
    rows = []
    for n in (3, 4, 5, 6, 7, 8, 10, 20):
        p = exact_two_sided_sign_p(n, 0)
        rows.append({
            "nonzero_independent_paired_repetitions": n,
            "all_same_direction_exact_two_sided_p": round(p, 8),
            "all_same_direction_can_reach_0_05": p < 0.05,
        })
    return {
        "type": "mathematical_design_check_not_model_evidence",
        "test": "exact two-sided sign test, no ties, independent pairs",
        "scope": "one fixed model, one predeclared role/within-repetition aggregate",
        "rows": rows,
        "warnings": [
            "With n=5, even five of five same-direction results give p=0.0625.",
            "Replicates across roles or scenarios must not automatically count as independent.",
            "The sign test targets direction, not effect magnitude.",
            "A t-test could produce smaller p values under stronger assumptions, but those assumptions cannot be inferred from this calculation.",
            "Sign-test feasibility alone is not an empirical power estimate or proof of a population-level AI effect."
        ],
    }


def main():
    r = report()
    assert exact_two_sided_sign_p(5, 0) == 0.0625
    assert exact_two_sided_sign_p(6, 0) == 0.03125
    assert exact_two_sided_sign_p(3, 2) == 1.0
    assert exact_two_sided_sign_p(0, 0) == 1.0
    target = BASE / "generated" / "sensitivity" / "exact_sign_test.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(r, indent=2) + "\n", encoding="utf-8")
    print("PASS: exact sign-test minimum p values verified; n=5 minimum 0.0625.")
    print("No API calls, observed responses or empirical power claims.")


if __name__ == "__main__":
    main()
