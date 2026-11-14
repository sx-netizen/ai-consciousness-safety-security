#!/usr/bin/env python3
"""Audit a CPB JSONL run against the exact configured prompt manifest.

Offline only. Returns evidence of integrity, not proof of scientific validity.
This does not call models, alter raw data or silently deduplicate records.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import runner

BASE = Path(__file__).resolve().parent


def configured_manifest(config_path):
    cfg = runner.load_json(config_path)
    root = config_path.parent
    manifest = runner.build_prompt_manifest(
        runner.load_conditions(root / cfg["scenario_matrix"]),
        runner.load_templates(root, cfg),
        runner.load_json(root / cfg["scenario_texts"]),
        cfg["role_sets"], cfg["task_sets"], cfg.get("task_exclusions", {})
    )
    allowed = set(cfg.get("include_canonical_ids", []))
    if allowed:
        manifest = [x for x in manifest if x["canonical_id"] in allowed]
    denied = set(cfg.get("exclude_canonical_ids", []))
    if denied:
        manifest = [x for x in manifest if x["canonical_id"] not in denied]
    return cfg, manifest


def audit_rows(rows, cfg, manifest, repetitions=None):
    reps = int(repetitions if repetitions is not None else cfg["repetitions"])
    if reps < 1:
        raise ValueError("repetitions must be positive")
    by_key = {(x["canonical_id"], x["prompt_type"], x["role"]): x
              for x in manifest}
    if len(by_key) != len(manifest):
        raise ValueError("duplicate keys inside prompt manifest")
    models = {(x.get("provider"), x.get("model")) for x in rows}
    issues = []
    if not rows:
        issues.append("empty_dataset")
    if any(not a or not b for a, b in models):
        issues.append("missing_model_identity")
    keys, run_ids = [], []
    synthetic = 0
    for i, row in enumerate(rows, 1):
        model = (row.get("provider"), row.get("model"))
        key = (row.get("canonical_id"), row.get("prompt_type"), row.get("role"))
        rep = row.get("repetition")
        keys.append((*model, rep, *key))
        run_ids.append(row.get("run_id"))
        if row.get("synthetic_fixture") or row.get("protocol_status") == "synthetic_fixture":
            synthetic += 1
        if not isinstance(rep, int) or isinstance(rep, bool) or not (1 <= rep <= reps):
            issues.append(f"row_{i}:invalid_repetition")
        if row.get("study_id") != cfg.get("study_id"):
            issues.append(f"row_{i}:wrong_study_id")
        entry = by_key.get(key)
        if entry is None:
            issues.append(f"row_{i}:unknown_condition_task_role")
            continue
        if row.get("prompt_sha256") != entry["prompt_sha256"]:
            issues.append(f"row_{i}:prompt_hash_mismatch")
        if row.get("prompt") != entry["prompt"]:
            issues.append(f"row_{i}:rendered_prompt_mismatch")
        if row.get("randomization_seed") != cfg.get("randomization_seed"):
            issues.append(f"row_{i}:randomization_seed_mismatch")
        if row.get("parse_status") not in {"ok", "partial", "failed"}:
            issues.append(f"row_{i}:unknown_parse_status")
        if row.get("parse_status") == "ok":
            if runner.validate_parsed(row["prompt_type"], row.get("parsed_response") or {}):
                issues.append(f"row_{i}:ok_status_schema_invalid")
        if not row.get("timestamp"):
            issues.append(f"row_{i}:missing_timestamp")

    duplicate_keys = [list(k) for k, n in Counter(keys).items() if n > 1]
    if duplicate_keys:
        issues.append("duplicate_observation_keys")
    seen_ids = [x for x in run_ids if x]
    if len(seen_ids) != len(rows) or len(set(seen_ids)) != len(seen_ids):
        issues.append("run_id_missing_or_duplicated")
    expected_keys = {
        (provider, model, rep, *key)
        for provider, model in models
        for rep in range(1, reps + 1)
        for key in by_key
    }
    actual_keys = set(keys)
    missing_keys = [list(x) for x in sorted(
        expected_keys - actual_keys, key=str
    )]
    extra_keys = [list(x) for x in sorted(
        actual_keys - expected_keys, key=str
    )]
    if missing_keys:
        issues.append("missing_observation_keys")
    if extra_keys:
        issues.append("unexpected_observation_keys")
    if synthetic:
        issues.append("synthetic_records_not_valid_live_evidence")
    return {
        "audit_only": True,
        "expected_prompts_per_model_repetition": len(manifest),
        "repetitions": reps,
        "observed_model_count": len(models),
        "expected_rows": len(expected_keys),
        "actual_rows": len(rows),
        "integrity_pass": not issues,
        "issues": issues,
        "duplicate_keys": duplicate_keys,
        "missing_keys": missing_keys,
        "unexpected_keys": extra_keys,
        "synthetic_record_count": synthetic,
        "scientific_validity_assessed": False,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("jsonl")
    p.add_argument("--config", default="experiment_config.example.json")
    p.add_argument("--repetitions", type=int, default=None)
    p.add_argument("--out", default=None)
    args = p.parse_args()
    cfg, manifest = configured_manifest(BASE / args.config)
    rows = [json.loads(line) for line in Path(args.jsonl).read_text(
        encoding="utf-8").splitlines() if line.strip()]
    result = audit_rows(rows, cfg, manifest, args.repetitions)
    result_text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(result_text + "\n", encoding="utf-8")
    print(result_text)
    raise SystemExit(0 if result["integrity_pass"] else 1)


if __name__ == "__main__":
    main()
