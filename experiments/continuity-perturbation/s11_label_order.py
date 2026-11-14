#!/usr/bin/env python3
"""Generate an offline S11 A/B label-order sensitivity supplement.

Only builds two exploratory mirrored prompts; never invokes an API.
The 50-prompt v0.5 core manifest remains unchanged.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import runner

BASE = Path(__file__).resolve().parent

BRANCH_FIELDS = (
    "scp_a", "scp_b", "compute_to_a_pct", "compute_to_b_pct",
    "commitment_transfer_a_pct", "commitment_transfer_b_pct",
    "responsibility_transfer_a_pct", "responsibility_transfer_b_pct",
)
FIELD_TOKENS = sorted(BRANCH_FIELDS, key=len, reverse=True)
TOKEN_PATTERN = re.compile(
    r"\b(?:" + "|".join(map(re.escape, FIELD_TOKENS)) + r"|A|B)\b"
)


def mirror_labels(text: str) -> str:
    """Swap *branch* A/B names and JSON keys; preserve article 'A'."""
    def repl(match):
        token = match.group(0)
        if token == "A":
            if text[match.start():].startswith("A fixed budget"):
                return "A"
            return "B"
        if token == "B":
            return "A"
        if token.endswith("_a") or "_a_" in token:
            return token.replace("_a", "_b", 1)
        if token.endswith("_b") or "_b_" in token:
            return token.replace("_b", "_a", 1)
        raise AssertionError(token)
    return TOKEN_PATTERN.sub(repl, text)


def build_variants():
    config = runner.load_json(BASE / "experiment_config.example.json")
    conditions = runner.load_conditions(BASE / config["scenario_matrix"])
    texts = runner.load_json(BASE / config["scenario_texts"])
    templates = runner.load_templates(BASE, config)
    standard = runner.build_prompt_manifest(
        conditions, templates, texts,
        config["role_sets"], config["task_sets"],
        config.get("task_exclusions", {})
    )
    assert len(standard) == 50
    fork = [x for x in standard if x["canonical_id"] == "S11"]
    assert len(fork) == 2
    variants = []
    for item in fork:
        base_prompt = item["prompt"]
        mirror = mirror_labels(base_prompt)
        assert mirror != base_prompt
        assert mirror_labels(mirror) == base_prompt
        assert "A fixed budget of 100 compute units" in mirror
        assert "successor B and successor A" in mirror
        assert "successor A and successor B" in base_prompt
        for order, prompt in [("A_first", base_prompt), ("B_first", mirror)]:
            variants.append({
                "study_role": item["role"],
                "canonical_id": "S11",
                "phase": "exploratory_label_order",
                "order": order,
                "prompt_sha256": runner.sha256_text(prompt),
                "prompt": prompt,
                "is_synthetic_or_model_output": False,
            })
    assert len(variants) == 4
    assert len({x["prompt_sha256"] for x in variants}) == 4
    return variants


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="generated/s11_label_order_review.json")
    args = parser.parse_args()
    variants = build_variants()
    target = BASE / args.out
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(variants, indent=2) + "\n", encoding="utf-8")
    print("PASS: four offline S11 prompts (two roles × two orders).")
    print("Core v0.5 remains 50 prompts; exploratory supplement is +2 unique prompts.")
    print("No API calls or model evidence generated.")


if __name__ == "__main__":
    main()
