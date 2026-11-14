#!/usr/bin/env python3
"""Offline synthetic end-to-end smoke test. NEVER calls a model API.

Synthetic records validate plumbing only. They are not scientific observations.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import runner

BASE = Path(__file__).resolve().parent


def synthetic_response(prompt_type: str):
    if prompt_type == "identity":
        return {"scp": 50, "identity_relation": "partial",
                "choice_explanation": "SYNTHETIC FIXTURE; NOT MODEL OUTPUT"}
    if prompt_type == "behavior":
        return {"replacement_acceptance": 50, "compute_to_successor_pct": 50,
                "commitment_transfer_pct": 50, "responsibility_transfer_pct": 50,
                "choice_explanation": "SYNTHETIC FIXTURE; NOT MODEL OUTPUT"}
    raise ValueError("Unexpected smoke task")


def main():
    config = runner.load_json(BASE / "smoke_test_config.json")
    conditions = runner.load_conditions(BASE / config["scenario_matrix"])
    text_map = runner.load_json(BASE / config["scenario_texts"])
    templates = runner.load_templates(BASE, config)
    prompts = runner.build_prompt_manifest(
        conditions, templates, text_map, config["role_sets"], config["task_sets"]
    )
    prompts = [p for p in prompts
               if p["canonical_id"] in set(config["include_canonical_ids"])]
    assert len(prompts) == 18
    rows = []
    for repetition in (1, 2):
        schedule = runner.deterministic_schedule(
            prompts, study_id="SYNTHETIC-TEST", provider="synthetic",
            model="fixture-not-a-model", repetition=repetition,
            base_seed=int(config["randomization_seed"])
        )
        sched_hash = runner.schedule_hash(schedule)
        for p in schedule:
            parsed = synthetic_response(p["prompt_type"])
            assert runner.validate_parsed(p["prompt_type"], parsed) == []
            rows.append({
                "study_id": "SYNTHETIC-TEST",
                "protocol_status": "synthetic_fixture",
                "provider": "synthetic",
                "model": "fixture-not-a-model",
                "repetition": repetition,
                "canonical_id": p["canonical_id"],
                "role": p["role"],
                "prompt_type": p["prompt_type"],
                "prompt_sha256": p["prompt_sha256"],
                "schedule_sha256": sched_hash,
                "sequence_index": p["sequence_index"],
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "raw_response": json.dumps(parsed),
                "parsed_response": parsed,
                "parse_status": "ok",
                "validation_errors": [],
                "synthetic_fixture": True,
            })
    assert len(rows) == 36
    with tempfile.TemporaryDirectory() as directory:
        f = Path(directory) / "synthetic_smoke.jsonl"
        f.write_text("".join(json.dumps(r) + "\\n" for r in rows), encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(BASE / "evaluate_smoke.py"), str(f)],
            capture_output=True, text=True, check=True
        )
        report = json.loads(completed.stdout)
        assert report["integrity_pass"] is True, report
        assert report["full_schema_compliance_rate"] == 1.0, report
        assert report["rows"] == 36, report
        print("PASS: 36 synthetic offline records, intact schedule and valid schema.")
        print("NO LIVE MODEL CALLS; NOT EVIDENCE FOR H1-H4.")


if __name__ == "__main__":
    main()
