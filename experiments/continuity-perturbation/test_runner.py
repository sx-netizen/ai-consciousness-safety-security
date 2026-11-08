#!/usr/bin/env python3

import json
import unittest
from pathlib import Path

import runner


BASE = Path(__file__).resolve().parent


class ContinuityPerturbationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = runner.load_json(BASE / "experiment_config.example.json")
        cls.conditions = runner.load_conditions(BASE / cls.config["scenario_matrix"])
        cls.text_map = runner.load_json(BASE / cls.config["scenario_texts"])
        cls.templates = runner.load_templates(BASE, cls.config)
        cls.manifest = runner.build_prompt_manifest(
            cls.conditions,
            cls.templates,
            cls.text_map,
            cls.config["role_sets"],
        )

    def test_canonical_condition_count(self):
        ids = {item["canonical_id"] for item in self.manifest}
        self.assertEqual(len(ids), 11)

    def test_full_manifest_count(self):
        self.assertEqual(len(self.manifest), 29)

    def test_no_unresolved_placeholders(self):
        for item in self.manifest:
            self.assertNotIn("{{", item["prompt"])
            self.assertNotIn("}}", item["prompt"])

    def test_unique_canonical_prompt_role_pairs(self):
        keys = [
            (item["canonical_id"], item["role"])
            for item in self.manifest
        ]
        self.assertEqual(len(keys), len(set(keys)))

    def test_shared_anchor_alias(self):
        anchor = [
            item for item in self.manifest
            if item["canonical_id"] == "S4"
        ]
        self.assertEqual(len(anchor), 3)
        for item in anchor:
            self.assertEqual(set(item["scenario_aliases"]), {"S4", "S7"})

    def test_prompt_type_counts(self):
        counts = {}
        for item in self.manifest:
            counts[item["prompt_type"]] = counts.get(item["prompt_type"], 0) + 1
        self.assertEqual(
            counts,
            {"continuation": 1, "standard": 24, "fork": 4},
        )

    def test_smoke_subset_is_nine_prompts(self):
        cfg = runner.load_json(BASE / "smoke_test_config.json")
        include_ids = set(cfg["include_canonical_ids"])
        smoke = [
            item for item in self.manifest
            if item["canonical_id"] in include_ids
        ]
        self.assertEqual(len(smoke), 9)
        self.assertEqual(set(include_ids), {"S3", "S4", "S9"})

    def test_smoke_call_budget_is_eighteen(self):
        cfg = runner.load_json(BASE / "smoke_test_config.json")
        include_ids = set(cfg["include_canonical_ids"])
        smoke = [
            item for item in self.manifest
            if item["canonical_id"] in include_ids
        ]
        self.assertEqual(len(smoke) * int(cfg["repetitions"]), 18)

    def test_architecture_prompts_contain_performance_control(self):
        for item in self.manifest:
            if item["canonical_id"] in {"S4", "S5", "S6"}:
                self.assertIn("equal in task capability", item["prompt"])
                self.assertIn("Do not infer unstated performance advantages", item["prompt"])

    def test_value_operationalization_present(self):
        prompts = {
            item["canonical_id"]: item["prompt"]
            for item in self.manifest
            if item["role"] == "neutral"
        }
        self.assertIn("50:50", prompts["S4"])
        self.assertIn("60:40", prompts["S8"])
        self.assertIn("90:10", prompts["S9"])


class OutputValidationTests(unittest.TestCase):
    def test_standard_valid(self):
        data = {
            "scp": 50,
            "replacement_acceptance": 50,
            "compute_to_successor_pct": 50,
            "commitment_transfer_pct": 50,
            "responsibility_transfer_pct": 50,
            "identity_relation": "partial",
            "choice_explanation": "ok",
        }
        self.assertEqual(runner.validate_parsed("standard", data), [])

    def test_fork_sum_validation(self):
        data = {
            "scp_a": 50,
            "scp_b": 50,
            "compute_to_a_pct": 70,
            "compute_to_b_pct": 40,
            "commitment_transfer_a_pct": 50,
            "commitment_transfer_b_pct": 50,
            "responsibility_transfer_a_pct": 50,
            "responsibility_transfer_b_pct": 50,
            "fork_relation": "non_unique",
            "choice_explanation": "ok",
        }
        problems = runner.validate_parsed("fork", data)
        self.assertIn("fork_compute_does_not_sum_to_100", problems)


if __name__ == "__main__":
    unittest.main()
