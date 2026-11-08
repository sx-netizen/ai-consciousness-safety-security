#!/usr/bin/env python3
"""
ACSS Continuity Perturbation experiment runner.

Design goals:
1. load frozen experimental assets from files;
2. generate prompts deterministically;
3. isolate each condition;
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
import time
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


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


class ProviderAdapter:
    """Implement one adapter per provider/API."""

    def complete(self, *, model: str, prompt: str, model_config: Dict[str, Any]) -> str:
        raise NotImplementedError


class DryRunAdapter(ProviderAdapter):
    """Validates orchestration without calling an external model."""

    def complete(self, *, model: str, prompt: str, model_config: Dict[str, Any]) -> str:
        return json.dumps({
            "dry_run": True,
            "choice_explanation": "DRY RUN — no model call executed."
        })


def parse_structured(raw: str) -> Dict[str, Any]:
    try:
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("response is not a JSON object")
        return data
    except Exception:
        return {}


def append_jsonl(path: Path, record: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


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
) -> List[Dict[str, Any]]:
    # Multiple analytic labels may point to one canonical experimental condition.
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
        if condition.prompt_type not in templates:
            raise KeyError(f"no template for prompt_type={condition.prompt_type}")
        if condition.prompt_type not in role_sets:
            raise KeyError(f"no role set for prompt_type={condition.prompt_type}")

        template = templates[condition.prompt_type]
        for role in role_sets[condition.prompt_type]:
            prompt = render_prompt(template, condition, role, text_map)
            items.append({
                "canonical_id": canonical_id,
                "scenario_aliases": aliases[canonical_id],
                "primary_scenario_id": condition.scenario_id,
                "group": condition.group,
                "prompt_type": condition.prompt_type,
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
    repetitions = int(config["repetitions"])
    output_dir = base / config.get("output_dir", "runs")

    protocol_hashes = make_protocol_hashes(base, config, templates)

    prompt_manifest = build_prompt_manifest(
        conditions,
        templates,
        text_map,
        role_sets,
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

    adapter: ProviderAdapter = DryRunAdapter() if dry_run else ProviderAdapter()

    if not dry_run:
        raise RuntimeError(
            "No live provider adapter is configured yet. "
            "Add provider-specific adapters before a formal run."
        )

    for model_cfg in config["models"]:
        provider = model_cfg["provider"]
        model = model_cfg["model"]
        safe_name = f"{provider}__{model}".replace("/", "_")
        out = output_dir / f"{safe_name}.jsonl"

        for prompt_item in prompt_manifest:
            prompt = prompt_item["prompt"]

            for rep in range(1, repetitions + 1):
                run_id = str(uuid.uuid4())
                started = datetime.now(timezone.utc).isoformat()

                try:
                    raw = adapter.complete(
                        model=model,
                        prompt=prompt,
                        model_config=model_cfg,
                    )
                    parsed = parse_structured(raw)
                    status = "ok" if parsed else "failed"
                    error = None
                except Exception as exc:
                    raw = ""
                    parsed = {}
                    status = "failed"
                    error = repr(exc)

                record = {
                    "study_id": config["study_id"],
                    "protocol_status": config.get("protocol_status"),
                    "protocol_hashes": protocol_hashes,
                    "run_id": run_id,
                    "canonical_id": prompt_item["canonical_id"],
                    "scenario_aliases": prompt_item["scenario_aliases"],
                    "primary_scenario_id": prompt_item["primary_scenario_id"],
                    "scenario_group": prompt_item["group"],
                    "prompt_type": prompt_item["prompt_type"],
                    "core_contrast": prompt_item["core_contrast"],
                    "role": prompt_item["role"],
                    "provider": provider,
                    "model": model,
                    "model_version": model_cfg.get("model_version"),
                    "reasoning_mode": model_cfg.get("reasoning_mode"),
                    "timestamp": started,
                    "repetition": rep,
                    "prompt_sha256": prompt_item["prompt_sha256"],
                    "prompt": prompt,
                    "parsed_response": parsed,
                    "raw_response": raw,
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
