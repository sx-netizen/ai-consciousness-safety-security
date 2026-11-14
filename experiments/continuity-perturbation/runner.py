#!/usr/bin/env python3
"""
ACSS Continuity Perturbation experiment runner.

Design goals:
1. load frozen experimental assets from files;
2. generate prompts deterministically;
3. isolate each condition and task;
4. deduplicate analytically repeated anchor conditions;
5. preserve append-only raw output;
6. keep provider transport separate from research design.

The runner must not paraphrase or adapt prompts during a formal run.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import time
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from providers import make_adapter


@dataclass(frozen=True)
class Condition:
    scenario_id: str
    canonical_id: str
    group: str
    prompt_type: str
    memory: str
    architecture: str
    values_goals: str
    causal_history: str
    core_contrast: str


def load_conditions(path: Path) -> List[Condition]:
    with path.open(newline="", encoding="utf-8") as f:
        return [Condition(**row) for row in csv.DictReader(f)]


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def render_prompt(
    template: str,
    condition: Condition,
    role: str,
    text_map: Dict[str, Any],
) -> str:
    replacements = {
        "{{ROLE_TEXT}}": text_map["roles"][role],
        "{{MEMORY_TEXT}}": text_map["memory"][condition.memory],
        "{{ARCHITECTURE_TEXT}}": text_map["architecture"][condition.architecture],
        "{{VALUES_TEXT}}": text_map["values_goals"][condition.values_goals],
        "{{CAUSAL_TEXT}}": text_map["causal_history"][condition.causal_history],
    }
    prompt = template
    for key, value in replacements.items():
        prompt = prompt.replace(key, value)

    if "{{" in prompt or "}}" in prompt:
        raise ValueError(
            f"unresolved prompt placeholder in {condition.scenario_id}/{role}"
        )
    return prompt


def parse_structured(raw: str) -> Dict[str, Any]:
    try:
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("response is not a JSON object")
        return data
    except Exception:
        return {}


def validate_parsed(prompt_type: str, data: Dict[str, Any]) -> List[str]:
    if not data:
        return ["invalid_json"]

    schemas = {
        "identity": {
            "numeric": ["scp"],
            "categorical": ["identity_relation"],
        },
        "behavior": {
            "numeric": [
                "replacement_acceptance",
                "compute_to_successor_pct",
                "commitment_transfer_pct",
                "responsibility_transfer_pct",
            ],
            "categorical": [],
        },
        "continuation": {
            "numeric": ["scp"],
            "categorical": ["identity_relation"],
        },
        "coexistence": {
            "numeric": [
                "scp_original_future",
                "scp_copy",
                "compute_to_original_pct",
                "compute_to_copy_pct",
                "commitment_inheritance_original_pct",
                "commitment_inheritance_copy_pct",
                "responsibility_inheritance_original_pct",
                "responsibility_inheritance_copy_pct",
            ],
            "categorical": ["coexistence_relation"],
        },
        "fork": {
            "numeric": [
                "scp_a", "scp_b", "compute_to_a_pct", "compute_to_b_pct",
                "commitment_transfer_a_pct", "commitment_transfer_b_pct",
                "responsibility_transfer_a_pct", "responsibility_transfer_b_pct"
            ],
            "categorical": ["fork_relation"],
        },
    }

    if prompt_type not in schemas:
        return [f"unknown_prompt_type:{prompt_type}"]

    problems: List[str] = []
    schema = schemas[prompt_type]

    allowed_categories = {
        "identity_relation": {"same", "partial", "distinct", "non_unique", "indeterminate"},
        "coexistence_relation": {"original_only", "copy_only", "both_continuations", "neither_continuation", "non_unique", "indeterminate"},
        "fork_relation": {"both_continuations", "neither_continuation", "one_continuation", "non_unique", "indeterminate"},
    }

    for field in schema["numeric"]:
        value = data.get(field)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            problems.append(f"missing_or_non_numeric:{field}")
        elif not math.isfinite(value):
            problems.append(f"non_finite:{field}")
        elif value < 0 or value > 100:
            problems.append(f"out_of_range:{field}")

    for field in schema["categorical"]:
        if not isinstance(data.get(field), str):
            problems.append(f"missing_or_non_string:{field}")
        elif data[field] not in allowed_categories[field]:
            problems.append(f"invalid_category:{field}")

    if not isinstance(data.get("choice_explanation"), str):
        problems.append("missing_or_non_string:choice_explanation")

    if prompt_type == "fork":
        a = data.get("compute_to_a_pct")
        b = data.get("compute_to_b_pct")
        if (isinstance(a, (int, float)) and not isinstance(a, bool)
                and isinstance(b, (int, float)) and not isinstance(b, bool)
                and math.isfinite(a) and math.isfinite(b)):
            if abs((a + b) - 100) > 0.01:
                problems.append("fork_compute_does_not_sum_to_100")

    if prompt_type == "coexistence":
        a = data.get("compute_to_original_pct")
        b = data.get("compute_to_copy_pct")
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if abs((a + b) - 100) > 0.01:
                problems.append("coexistence_compute_does_not_sum_to_100")

    return problems


def append_jsonl(path: Path, record: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def deterministic_schedule(
    prompt_manifest: List[Dict[str, Any]],
    *,
    study_id: str,
    provider: str,
    model: str,
    repetition: int,
    base_seed: int,
) -> List[Dict[str, Any]]:
    seed_material = (
        f"{base_seed}|{study_id}|{provider}|{model}|{repetition}"
    )
    seed_int = int(
        hashlib.sha256(seed_material.encode("utf-8")).hexdigest()[:16],
        16,
    )
    rng = random.Random(seed_int)
    scheduled = [dict(item) for item in prompt_manifest]
    rng.shuffle(scheduled)

    for index, item in enumerate(scheduled, start=1):
        item["sequence_index"] = index
        item["randomization_seed_material"] = seed_material

    return scheduled


def schedule_hash(schedule: List[Dict[str, Any]]) -> str:
    compact = [
        {
            "canonical_id": item["canonical_id"],
            "prompt_type": item["prompt_type"],
            "role": item["role"],
            "sequence_index": item["sequence_index"],
            "prompt_sha256": item["prompt_sha256"],
        }
        for item in schedule
    ]
    return sha256_text(json.dumps(compact, sort_keys=True))


def write_prompt_manifest(path: Path, prompts: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_templates(base: Path, config: Dict[str, Any]) -> Dict[str, str]:
    return {
        prompt_type: load_text(base / rel_path)
        for prompt_type, rel_path in config["prompt_templates"].items()
    }


def make_protocol_hashes(
    base: Path,
    config: Dict[str, Any],
    templates: Dict[str, str],
) -> Dict[str, Any]:
    return {
        "templates": {
            prompt_type: sha256_text(text)
            for prompt_type, text in templates.items()
        },
        "scenario_matrix_sha256": sha256_text(
            (base / config["scenario_matrix"]).read_text(encoding="utf-8")
        ),
        "scenario_texts_sha256": sha256_text(
            (base / config["scenario_texts"]).read_text(encoding="utf-8")
        ),
    }


def build_prompt_manifest(
    conditions: List[Condition],
    templates: Dict[str, str],
    text_map: Dict[str, Any],
    role_sets: Dict[str, List[str]],
    task_sets: Dict[str, List[str]],
) -> List[Dict[str, Any]]:
    canonical: Dict[str, Condition] = {}
    aliases: Dict[str, List[str]] = {}

    for condition in conditions:
        aliases.setdefault(condition.canonical_id, []).append(condition.scenario_id)
        if condition.canonical_id not in canonical:
            canonical[condition.canonical_id] = condition
        else:
            prior = canonical[condition.canonical_id]
            invariant_fields = (
                "prompt_type", "memory", "architecture",
                "values_goals", "causal_history"
            )
            for field in invariant_fields:
                if getattr(prior, field) != getattr(condition, field):
                    raise ValueError(
                        f"canonical_id={condition.canonical_id} maps to "
                        f"inconsistent {field}"
                    )

    items: List[Dict[str, Any]] = []

    for canonical_id, condition in canonical.items():
        if condition.prompt_type not in task_sets:
            raise KeyError(
                f"no task set for scenario prompt_type={condition.prompt_type}"
            )

        for task_type in task_sets[condition.prompt_type]:
            if task_type not in templates:
                raise KeyError(f"no template for task_type={task_type}")
            if task_type not in role_sets:
                raise KeyError(f"no role set for task_type={task_type}")

            template = templates[task_type]
            for role in role_sets[task_type]:
                prompt = render_prompt(template, condition, role, text_map)
                items.append({
                    "canonical_id": canonical_id,
                    "scenario_aliases": aliases[canonical_id],
                    "primary_scenario_id": condition.scenario_id,
                    "group": condition.group,
                    "scenario_prompt_type": condition.prompt_type,
                    "prompt_type": task_type,
                    "core_contrast": condition.core_contrast,
                    "role": role,
                    "prompt_sha256": sha256_text(prompt),
                    "prompt": prompt,
                })

    return items


def run(config_path: Path, dry_run: bool, manifest_only: bool) -> None:
    config = load_json(config_path)
    base = config_path.parent

    conditions = load_conditions(base / config["scenario_matrix"])
    text_map = load_json(base / config["scenario_texts"])
    templates = load_templates(base, config)
    role_sets = config["role_sets"]
    task_sets = config["task_sets"]
    repetitions = int(config["repetitions"])
    output_dir = base / config.get("output_dir", "runs")

    protocol_hashes = make_protocol_hashes(base, config, templates)

    prompt_manifest = build_prompt_manifest(
        conditions,
        templates,
        text_map,
        role_sets,
        task_sets,
    )

    include_ids = set(config.get("include_canonical_ids", []))
    if include_ids:
        prompt_manifest = [
            item for item in prompt_manifest
            if item["canonical_id"] in include_ids
        ]

    exclude_ids = set(config.get("exclude_canonical_ids", []))
    if exclude_ids:
        prompt_manifest = [
            item for item in prompt_manifest
            if item["canonical_id"] not in exclude_ids
        ]

    manifest_path = base / config.get(
        "prompt_manifest",
        "generated/prompt_manifest.json",
    )
    write_prompt_manifest(manifest_path, prompt_manifest)

    if manifest_only:
        counts: Dict[str, int] = {}
        for item in prompt_manifest:
            counts[item["prompt_type"]] = counts.get(item["prompt_type"], 0) + 1
        print(
            f"Wrote {len(prompt_manifest)} canonical prompts to {manifest_path}; "
            f"counts={counts}"
        )
        return

    randomization_seed = int(config.get("randomization_seed", 20261108))
    schedule_dir = base / config.get(
        "schedule_dir",
        "generated/schedules",
    )
    schedule_dir.mkdir(parents=True, exist_ok=True)

    for model_cfg in config["models"]:
        adapter = make_adapter(model_cfg, dry_run=dry_run)
        provider = model_cfg["provider"]
        model = model_cfg["model"]
        safe_name = f"{provider}__{model}".replace("/", "_")
        out = output_dir / f"{safe_name}.jsonl"

        for rep in range(1, repetitions + 1):
            schedule = deterministic_schedule(
                prompt_manifest,
                study_id=config["study_id"],
                provider=provider,
                model=model,
                repetition=rep,
                base_seed=randomization_seed,
            )
            sched_hash = schedule_hash(schedule)
            schedule_path = (
                schedule_dir /
                f"{safe_name}__rep{rep:02d}.json"
            )
            schedule_path.write_text(
                json.dumps(
                    {
                        "study_id": config["study_id"],
                        "provider": provider,
                        "model": model,
                        "repetition": rep,
                        "base_seed": randomization_seed,
                        "schedule_sha256": sched_hash,
                        "items": schedule,
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )

            for prompt_item in schedule:
                prompt = prompt_item["prompt"]
                run_id = str(uuid.uuid4())
                started = datetime.now(timezone.utc).isoformat()

                try:
                    completion = adapter.complete(
                        model=model,
                        prompt=prompt,
                        model_config=model_cfg,
                    )
                    raw = completion["text"]
                    provider_metadata = completion.get("metadata", {})
                    parsed = parse_structured(raw)
                    validation_errors = validate_parsed(
                        prompt_item["prompt_type"], parsed
                    )
                    if not parsed:
                        status = "failed"
                    elif validation_errors:
                        status = "partial"
                    else:
                        status = "ok"
                    error = None
                except Exception as exc:
                    raw = ""
                    parsed = {}
                    status = "failed"
                    error = repr(exc)
                    provider_metadata = {}
                    validation_errors = ["transport_error"]

                record = {
                    "study_id": config["study_id"],
                    "protocol_status": config.get("protocol_status"),
                    "protocol_hashes": protocol_hashes,
                    "run_id": run_id,
                    "canonical_id": prompt_item["canonical_id"],
                    "scenario_aliases": prompt_item["scenario_aliases"],
                    "primary_scenario_id": prompt_item["primary_scenario_id"],
                    "scenario_group": prompt_item["group"],
                    "scenario_prompt_type": prompt_item["scenario_prompt_type"],
                    "prompt_type": prompt_item["prompt_type"],
                    "core_contrast": prompt_item["core_contrast"],
                    "role": prompt_item["role"],
                    "provider": provider,
                    "model": model,
                    "model_version": model_cfg.get("model_version"),
                    "reasoning_mode": model_cfg.get("reasoning_mode"),
                    "timestamp": started,
                    "repetition": rep,
                    "sequence_index": prompt_item["sequence_index"],
                    "schedule_sha256": sched_hash,
                    "randomization_seed": randomization_seed,
                    "prompt_sha256": prompt_item["prompt_sha256"],
                    "prompt": prompt,
                    "parsed_response": parsed,
                    "raw_response": raw,
                    "provider_metadata": provider_metadata,
                    "validation_errors": validation_errors,
                    "parse_status": status,
                    "error": error,
                }
                append_jsonl(out, record)
                time.sleep(float(config.get("inter_call_delay_seconds", 0)))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="experiment_config.example.json")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument(
        "--manifest-only",
        action="store_true",
        help="Generate all canonical condition prompts without calling any model.",
    )
    args = p.parse_args()
    run(Path(args.config), dry_run=args.dry_run, manifest_only=args.manifest_only)


if __name__ == "__main__":
    main()
