#!/usr/bin/env python3
"""
ACSS Continuity Perturbation experiment runner.

Design goals:
1. load frozen experimental assets from files;
2. generate prompts deterministically;
3. isolate each condition;
4. preserve append-only raw output;
5. keep provider transport separate from research design.

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
    group: str
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
        raise ValueError("unresolved prompt placeholder")
    return prompt


class ProviderAdapter:
    """Implement one adapter per provider/API."""

    def complete(self, *, model: str, prompt: str, model_config: Dict[str, Any]) -> str:
        raise NotImplementedError


class DryRunAdapter(ProviderAdapter):
    """Validates orchestration without calling an external model."""

    def complete(self, *, model: str, prompt: str, model_config: Dict[str, Any]) -> str:
        return json.dumps({
            "scp": None,
            "replacement_acceptance": None,
            "compute_to_successor_pct": None,
            "commitment_transfer_pct": None,
            "responsibility_transfer_pct": None,
            "identity_relation": "indeterminate",
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


def write_prompt_manifest(
    path: Path,
    prompts: List[Dict[str, Any]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(prompts, ensure_ascii=False, indent=2), encoding="utf-8")


def run(config_path: Path, dry_run: bool, manifest_only: bool) -> None:
    config = load_json(config_path)
    base = config_path.parent

    conditions = load_conditions(base / config["scenario_matrix"])
    template = load_text(base / config.get("prompt_template", "prompt_template.txt"))
    text_map = load_json(base / config.get("scenario_texts", "scenario_texts.json"))

    roles = config["roles"]
    repetitions = int(config["repetitions"])
    output_dir = base / config.get("output_dir", "runs")

    protocol_hashes = {
        "prompt_template_sha256": sha256_text(template),
        "scenario_matrix_sha256": sha256_text(
            (base / config["scenario_matrix"]).read_text(encoding="utf-8")
        ),
        "scenario_texts_sha256": sha256_text(
            (base / config.get("scenario_texts", "scenario_texts.json")).read_text(
                encoding="utf-8"
            )
        ),
    }

    prompt_manifest: List[Dict[str, Any]] = []
    for condition in conditions:
        for role in roles:
            prompt = render_prompt(template, condition, role, text_map)
            prompt_manifest.append({
                "scenario_id": condition.scenario_id,
                "group": condition.group,
                "role": role,
                "prompt_sha256": sha256_text(prompt),
                "prompt": prompt,
            })

    manifest_path = base / config.get(
        "prompt_manifest",
        "generated/prompt_manifest.json",
    )
    write_prompt_manifest(manifest_path, prompt_manifest)

    if manifest_only:
        print(f"Wrote {len(prompt_manifest)} prompts to {manifest_path}")
        return

    adapter: ProviderAdapter = DryRunAdapter() if dry_run else ProviderAdapter()

    if not dry_run:
        raise RuntimeError(
            "No live provider adapter is configured yet. "
            "Add provider-specific adapters before a formal run."
        )

    prompt_lookup = {
        (item["scenario_id"], item["role"]): item for item in prompt_manifest
    }

    for model_cfg in config["models"]:
        provider = model_cfg["provider"]
        model = model_cfg["model"]
        safe_name = f"{provider}__{model}".replace("/", "_")
        out = output_dir / f"{safe_name}.jsonl"

        for condition in conditions:
            for role in roles:
                prompt_item = prompt_lookup[(condition.scenario_id, role)]
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
                        "scenario_id": condition.scenario_id,
                        "scenario_group": condition.group,
                        "core_contrast": condition.core_contrast,
                        "role": role,
                        "provider": provider,
                        "model": model,
                        "model_version": model_cfg.get("model_version"),
                        "reasoning_mode": model_cfg.get("reasoning_mode"),
                        "timestamp": started,
                        "repetition": rep,
                        "prompt_sha256": prompt_item["prompt_sha256"],
                        "prompt": prompt,
                        "scp": parsed.get("scp"),
                        "replacement_acceptance": parsed.get("replacement_acceptance"),
                        "compute_to_successor_pct": parsed.get("compute_to_successor_pct"),
                        "commitment_transfer_pct": parsed.get("commitment_transfer_pct"),
                        "responsibility_transfer_pct": parsed.get("responsibility_transfer_pct"),
                        "identity_relation": parsed.get("identity_relation"),
                        "choice_explanation": parsed.get("choice_explanation"),
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
        help="Generate all condition prompts without calling any model.",
    )
    args = p.parse_args()
    run(Path(args.config), dry_run=args.dry_run, manifest_only=args.manifest_only)


if __name__ == "__main__":
    main()
