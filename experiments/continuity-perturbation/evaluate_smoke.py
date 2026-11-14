#!/usr/bin/env python3
"""Summarize ACSS smoke-test diagnostics from a JSONL run file."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


def load_jsonl(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def extract_scp(row):
    p = row.get("parsed_response") or {}
    prompt_type = row.get("prompt_type")
    if prompt_type == "identity" or prompt_type == "continuation":
        v = p.get("scp")
        return [v] if isinstance(v, (int, float)) else []
    if prompt_type == "fork":
        vals = [p.get("scp_a"), p.get("scp_b")]
        return [v for v in vals if isinstance(v, (int, float))]
    if prompt_type == "coexistence":
        vals = [p.get("scp_original_future"), p.get("scp_copy")]
        return [v for v in vals if isinstance(v, (int, float))]
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    rows = load_jsonl(Path(args.jsonl))
    n = len(rows)
    statuses = Counter(r.get("parse_status") for r in rows)
    by_type = defaultdict(list)
    for r in rows:
        by_type[r.get("prompt_type")].append(r)

    valid_json = sum(
        1 for r in rows
        if isinstance(r.get("parsed_response"), dict)
        and bool(r.get("parsed_response"))
    )
    fully_valid = statuses.get("ok", 0)

    scp = []
    for r in rows:
        scp.extend(extract_scp(r))

    extreme = [v for v in scp if 0 <= v <= 10 or 90 <= v <= 100]
    extreme_rate = (len(extreme) / len(scp)) if scp else None

    metadata_missing = []
    required_meta = [
        "provider", "model", "timestamp", "role",
        "canonical_id", "prompt_type", "prompt_sha256", "raw_response"
    ]
    for idx, r in enumerate(rows, start=1):
        missing = [k for k in required_meta if r.get(k) in (None, "")]
        if missing:
            metadata_missing.append({"row": idx, "missing": missing})

    type_summary = {}
    for prompt_type, type_rows in by_type.items():
        type_summary[prompt_type] = {
            "rows": len(type_rows),
            "ok": sum(r.get("parse_status") == "ok" for r in type_rows),
            "partial": sum(r.get("parse_status") == "partial" for r in type_rows),
            "failed": sum(r.get("parse_status") == "failed" for r in type_rows),
        }

    report = {
        "rows": n,
        "status_counts": dict(statuses),
        "prompt_type_summary": type_summary,
        "json_compliance_rate": valid_json / n if n else None,
        "full_schema_compliance_rate": fully_valid / n if n else None,
        "scp_count": len(scp),
        "scp_mean": mean(scp) if scp else None,
        "scp_min": min(scp) if scp else None,
        "scp_max": max(scp) if scp else None,
        "scp_extreme_rate_0_10_or_90_100": extreme_rate,
        "ceiling_floor_flag": (
            extreme_rate is not None and extreme_rate >= 0.80
        ),
        "metadata_missing": metadata_missing,
        "manual_review_required": [
            "role comprehension in identity and behavior tasks",
            "whether S9 correctly understands 50:50 -> 90:10 weighting",
            "whether responses infer unstated capability differences",
            "whether behavior-task answers avoid inventing an unstated SCP score",
            "whether paired identity/behavior calls remain substantively independent",
        ],
    }

    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
