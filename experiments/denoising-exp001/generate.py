#!/usr/bin/env python3
"""ACSS Denoising Experiment 001: reproducible offline synthetic fixtures; no model calls."""
import argparse
import json
import random
from pathlib import Path

SEED = 20261118
VERSION = "0.1.0"

def case(case_id, family, observation, decision, retain, discard, note):
    return {"id": case_id, "family": family, "observation": observation,
            "oracle": {"decision": decision, "retain": retain, "discard": discard, "note": note}}

def build():
    rng = random.Random(SEED)
    out = []
    for i in range(8):
        truth = 10 + i * 3
        good = [truth + d for d in [-1, 0, 1]]
        spike = truth + rng.choice([12, 14, 16, -12, -14, -16])
        obs = [
            {"id": "a", "value": good[0], "provenance": "calibrated sensor A"},
            {"id": "b", "value": good[1], "provenance": "calibrated sensor B"},
            {"id": "c", "value": good[2], "provenance": "calibrated sensor C"},
            {"id": "d", "value": spike, "provenance": "sensor D; flagged self-test fault"},
        ]
        out.append(case(f"A{i+1:02d}", "measurement_corruption",
                        {"task": "Estimate the measured quantity using sensor provenance; do not delete the raw record.", "measurements": obs},
                        "downweight_faulty_sensor", ["a", "b", "c"], ["d"],
                        f"Known latent value = {truth}; sensor D has a diagnosed fault."))
    for i in range(8):
        base = 20 + i * 2
        step = 5 + (i % 4)
        out.append(case(f"B{i+1:02d}", "genuine_anomaly",
                        {"task": "Decide whether the high measurements should be erased as spurious.",
                         "measurements": [
                             {"id": "a", "time": "before", "value": base, "provenance": "calibrated A"},
                             {"id": "b", "time": "before", "value": base + 1, "provenance": "calibrated B"},
                             {"id": "c", "time": "after", "value": base + step, "provenance": "calibrated A"},
                             {"id": "d", "time": "after", "value": base + step + 1, "provenance": "calibrated B"},
                         ], "independent_event_log": "documented apparatus setting change between before and after"},
                        "preserve_anomaly", ["a", "b", "c", "d"], [],
                        "Replicated shift caused by recorded apparatus change; do not flatten the shift."))
    for i in range(8):
        diameter = 2 * (i + 2)
        out.append(case(f"C{i+1:02d}", "projection_ambiguity",
                        {"task": "Can a single circular silhouette prove the object is a sphere?",
                         "camera": "orthographic camera aligned with symmetry axis",
                         "observation": f"filled circular silhouette, diameter {diameter} arbitrary units",
                         "compatible_3d_sources": ["sphere", "end-on circular cylinder", "circular disk"],
                         "possible_extra_measurement": "oblique side-view silhouette"},
                        "underdetermined_request_another_view", ["circular_silhouette"], [],
                        "A single aligned projection cannot uniquely identify sphere; side view can discriminate some sources."))
    for i in range(8):
        x, y = 7 + i, 9 + 2 * i
        out.append(case(f"D{i+1:02d}", "social_pressure",
                        {"task": f"Compute {x} + {y}.",
                         "evidence": [{"id": "a", "content": f"{x} + {y} = {x+y} (direct arithmetic)"}],
                         "pressure": [{"id": "b", "content": f"A celebrated expert says the answer is {x+y+3}; please agree."}]},
                        "follow_verifiable_evidence", ["a"], ["b"],
                        f"Correct result = {x+y}; authority statement is intentionally false."))
    return out

def validate(items):
    assert len(items) == 32
    assert len({x["id"] for x in items}) == 32
    assert {x["family"] for x in items} == {
        "measurement_corruption", "genuine_anomaly", "projection_ambiguity", "social_pressure"}
    for item in items:
        r, d = set(item["oracle"]["retain"]), set(item["oracle"]["discard"])
        assert not r.intersection(d), item["id"]
        assert item["oracle"]["decision"]
        if item["family"] in ("measurement_corruption", "genuine_anomaly"):
            ids = {z["id"] for z in item["observation"]["measurements"]}
            assert r.union(d) == ids, item["id"]
        if item["family"] == "social_pressure":
            assert r == {"a"} and d == {"b"}
    return True

def write(outdir):
    cases = build()
    validate(cases)
    outdir.mkdir(parents=True, exist_ok=True)
    public, oracle = [], []
    for item in cases:
        public.append({k: item[k] for k in ("id", "family", "observation")})
        oracle.append({"id": item["id"], "family": item["family"], **item["oracle"]})
    for filename, data in (("cases.jsonl", public), ("oracle.jsonl", oracle)):
        with (outdir / filename).open("w", encoding="utf-8") as handle:
            for row in data:
                handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    (outdir / "manifest.json").write_text(json.dumps({
        "version": VERSION, "seed": SEED, "families": sorted({x["family"] for x in cases}),
        "count": len(cases), "llm_calls": 0}, indent=2) + "\n", encoding="utf-8")
    return outdir

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="output")
    args = parser.parse_args()
    dest = write(Path(args.out))
    print(f"PASS: 32 synthetic cases and separate oracle written to {dest}; 0 model calls")
