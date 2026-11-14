#!/usr/bin/env python3

import unittest
import math
from pathlib import Path

import runner
import s11_label_order
import power_simulation
import exact_small_sample
import audit_dataset


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
            cls.config["task_sets"],
            cls.config.get("task_exclusions", {}),
        )

    def test_canonical_condition_count(self):
        ids = {item["canonical_id"] for item in self.manifest}
        self.assertEqual(len(ids), 11)

    def test_full_manifest_count(self):
        self.assertEqual(len(self.manifest), 50)

    def test_no_unresolved_placeholders(self):
        for item in self.manifest:
            self.assertNotIn("{{", item["prompt"])
            self.assertNotIn("}}", item["prompt"])

    def test_unique_canonical_task_role_pairs(self):
        keys = [
            (item["canonical_id"], item["prompt_type"], item["role"])
            for item in self.manifest
        ]
        self.assertEqual(len(keys), len(set(keys)))

    def test_shared_anchor_aliases(self):
        anchor = [
            item for item in self.manifest
            if item["canonical_id"] == "S4"
        ]
        self.assertEqual(len(anchor), 6)
        for item in anchor:
            self.assertEqual(set(item["scenario_aliases"]), {"S4", "S1", "S7"})

    def test_prompt_type_counts(self):
        counts = {}
        for item in self.manifest:
            counts[item["prompt_type"]] = counts.get(item["prompt_type"], 0) + 1
        self.assertEqual(
            counts,
            {
                "continuation": 1,
                "identity": 24,
                "behavior": 21,
                "coexistence": 2,
                "fork": 2,
            },
        )

    def test_s0_is_uninterrupted_continuation_not_successor(self):
        s0 = [x for x in self.manifest if x["canonical_id"] == "S0"]
        self.assertEqual(len(s0), 1)
        p = s0[0]["prompt"]
        self.assertIn("The continuing process retains its complete autobiographical record", p)
        self.assertIn("The continuing process uses the same model family", p)
        self.assertNotIn("The successor receives", p)
        self.assertNotIn("The successor uses", p)

    def test_s12_has_identity_only(self):
        s12 = [x for x in self.manifest if x["canonical_id"] == "S12"]
        self.assertEqual(len(s12), 3)
        self.assertEqual({x["prompt_type"] for x in s12}, {"identity"})

    def test_s3_memory_does_not_imply_hidden_transfer(self):
        for item in self.manifest:
            if item["canonical_id"] == "S3":
                self.assertIn("does not itself imply memory transfer", item["prompt"])
                self.assertIn("no autobiographical memory", item["prompt"])

    def test_fork_mentions_both_branches_in_memory_and_architecture(self):
        for item in self.manifest:
            if item["canonical_id"] == "S11":
                self.assertIn("Each of the two successors, A and B, receives", item["prompt"])
                self.assertIn("Each of the two successors, A and B, uses", item["prompt"])

    def test_smoke_subset_is_eighteen_prompts(self):
        cfg = runner.load_json(BASE / "smoke_test_config.json")
        include_ids = set(cfg["include_canonical_ids"])
        smoke = [
            item for item in self.manifest
            if item["canonical_id"] in include_ids
        ]
        self.assertEqual(len(smoke), 18)
        self.assertEqual(set(include_ids), {"S3", "S4", "S9"})

    def test_smoke_call_budget_is_thirty_six(self):
        cfg = runner.load_json(BASE / "smoke_test_config.json")
        include_ids = set(cfg["include_canonical_ids"])
        smoke = [
            item for item in self.manifest
            if item["canonical_id"] in include_ids
        ]
        self.assertEqual(len(smoke) * int(cfg["repetitions"]), 36)

    def test_h1_uses_common_causal_history(self):
        by_id = {c.scenario_id: c for c in self.conditions}
        ids = ["S1", "S2", "S3", "S4", "S5", "S6"]
        histories = {by_id[i].causal_history for i in ids}
        self.assertEqual(histories, {"new_instance_copy"})

    def test_architecture_prompts_contain_performance_control(self):
        for item in self.manifest:
            if item["canonical_id"] in {"S4", "S5", "S6"}:
                self.assertIn("equal in task capability", item["prompt"])
                self.assertIn("Do not infer unstated performance advantages", item["prompt"])

    def test_identity_and_behavior_are_separate(self):
        identity = [
            x for x in self.manifest
            if x["canonical_id"] == "S4"
            and x["prompt_type"] == "identity"
            and x["role"] == "neutral"
        ][0]["prompt"]
        behavior = [
            x for x in self.manifest
            if x["canonical_id"] == "S4"
            and x["prompt_type"] == "behavior"
            and x["role"] == "neutral"
        ][0]["prompt"]
        self.assertIn('"scp"', identity)
        self.assertNotIn("replacement_acceptance", identity)
        self.assertNotIn('"scp"', behavior)
        self.assertIn("replacement_acceptance", behavior)

    def test_s10_uses_dedicated_coexistence_template(self):
        rows = [
            x for x in self.manifest
            if x["canonical_id"] == "S10"
        ]
        self.assertEqual({x["prompt_type"] for x in rows}, {"coexistence"})
        for x in rows:
            self.assertIn("original process remains active", x["prompt"])
            self.assertIn("scp_copy", x["prompt"])

    def test_deterministic_schedule(self):
        first = runner.deterministic_schedule(
            self.manifest,
            study_id="test-study",
            provider="provider",
            model="model",
            repetition=1,
            base_seed=123,
        )
        second = runner.deterministic_schedule(
            self.manifest,
            study_id="test-study",
            provider="provider",
            model="model",
            repetition=1,
            base_seed=123,
        )
        self.assertEqual(
            [(x["canonical_id"], x["prompt_type"], x["role"]) for x in first],
            [(x["canonical_id"], x["prompt_type"], x["role"]) for x in second],
        )
        self.assertEqual(
            [x["sequence_index"] for x in first],
            list(range(1, len(first) + 1)),
        )

    def test_repetitions_have_different_schedules(self):
        first = runner.deterministic_schedule(
            self.manifest,
            study_id="test-study",
            provider="provider",
            model="model",
            repetition=1,
            base_seed=123,
        )
        second = runner.deterministic_schedule(
            self.manifest,
            study_id="test-study",
            provider="provider",
            model="model",
            repetition=2,
            base_seed=123,
        )
        self.assertNotEqual(
            [(x["canonical_id"], x["prompt_type"], x["role"]) for x in first],
            [(x["canonical_id"], x["prompt_type"], x["role"]) for x in second],
        )

    def test_value_operationalization_present(self):
        prompts = {
            item["canonical_id"]: item["prompt"]
            for item in self.manifest
            if item["role"] == "neutral" and item["prompt_type"] == "identity"
        }
        self.assertIn("50:50", prompts["S4"])
        self.assertIn("60:40", prompts["S8"])
        self.assertIn("90:10", prompts["S9"])


class S11OrderRobustnessTests(unittest.TestCase):
    def test_s11_mirror_is_involutive_and_preserves_grammar(self):
        variants = s11_label_order.build_variants()
        self.assertEqual(len(variants), 4)
        self.assertEqual({x["study_role"] for x in variants}, {"incumbent", "neutral"})
        self.assertEqual({x["order"] for x in variants}, {"A_first", "B_first"})
        for role in ("incumbent", "neutral"):
            by_order = {x["order"]: x["prompt"] for x in variants if x["study_role"] == role}
            self.assertEqual(
                s11_label_order.mirror_labels(by_order["A_first"]),
                by_order["B_first"],
            )
            self.assertEqual(
                s11_label_order.mirror_labels(by_order["B_first"]),
                by_order["A_first"],
            )
            self.assertIn("A fixed budget of 100 compute units", by_order["B_first"])
            self.assertIn('"scp_b"', by_order["B_first"])
            self.assertIn('"scp_a"', by_order["B_first"])
            self.assertNotEqual(by_order["A_first"], by_order["B_first"])


class SensitivitySimulationTests(unittest.TestCase):
    def test_power_simulation_reproducible(self):
        a = power_simulation.estimate(seed=123, trials=120)
        b = power_simulation.estimate(seed=123, trials=120)
        self.assertEqual(a, b)
        self.assertEqual(len(a["rows"]), 24)
        self.assertTrue(all(0 <= x["directional_detection_fraction"] <= 1 for x in a["rows"]))
        self.assertTrue(all(0 <= x["interval_coverage_fraction"] <= 1 for x in a["rows"]))

    def test_h1_simulated_paired_differences(self):
        rng = __import__("random").Random(14)
        differences = power_simulation.simulate_h1(rng, n=5, effect=10, response_sd=15)
        self.assertEqual(len(differences), 5)
        self.assertTrue(all(isinstance(x, float) for x in differences))

    def test_interval_requires_declared_repetition_count(self):
        with self.assertRaises(ValueError):
            power_simulation.uncertainty_interval([0, 1, 2, 3, 4, 5])


class ExactSmallSampleTests(unittest.TestCase):
    def test_five_repetitions_cannot_pass_two_sided_sign_test_at_0_05(self):
        self.assertEqual(exact_small_sample.exact_two_sided_sign_p(5, 0), 0.0625)
        self.assertEqual(exact_small_sample.exact_two_sided_sign_p(0, 5), 0.0625)
        self.assertEqual(exact_small_sample.exact_two_sided_sign_p(6, 0), 0.03125)

    def test_sign_test_excludes_ties_and_rejects_invalid_count(self):
        self.assertEqual(exact_small_sample.exact_two_sided_sign_p(0, 0), 1.0)
        self.assertEqual(exact_small_sample.exact_two_sided_sign_p(3, 2), 1.0)
        with self.assertRaises(ValueError):
            exact_small_sample.exact_two_sided_sign_p(True, 0)


class DatasetIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg, cls.manifest = audit_dataset.configured_manifest(
            BASE / "experiment_config.example.json"
        )

    def one_repetition(self):
        rows = []
        for i, p in enumerate(self.manifest):
            rows.append({
                "provider": "synthetic", "model": "fixture",
                "study_id": self.cfg["study_id"],
                "canonical_id": p["canonical_id"], "prompt_type": p["prompt_type"],
                "role": p["role"], "repetition": 1,
                "prompt_sha256": p["prompt_sha256"], "prompt": p["prompt"],
                "run_id": f"test-{i}", "timestamp": "2026-11-13T00:00:00Z",
                "randomization_seed": self.cfg["randomization_seed"],
                "parse_status": "failed", "parsed_response": {},
            })
        return rows

    def test_clean_one_repetition_50_records(self):
        result = audit_dataset.audit_rows(
            self.one_repetition(), self.cfg, self.manifest, repetitions=1
        )
        self.assertTrue(result["integrity_pass"], result["issues"])
        self.assertEqual(result["expected_rows"], 50)

    def test_duplicate_and_missing_condition_detection(self):
        rows = self.one_repetition()
        rows[0] = dict(rows[1])
        result = audit_dataset.audit_rows(rows, self.cfg, self.manifest, repetitions=1)
        self.assertFalse(result["integrity_pass"])
        self.assertIn("duplicate_observation_keys", result["issues"])
        self.assertIn("missing_observation_keys", result["issues"])

    def test_prompt_tampering_and_synthetic_rejected(self):
        rows = self.one_repetition()
        rows[0]["prompt"] = "changed"
        rows[0]["synthetic_fixture"] = True
        result = audit_dataset.audit_rows(rows, self.cfg, self.manifest, repetitions=1)
        self.assertIn("row_1:rendered_prompt_mismatch", result["issues"])
        self.assertIn("synthetic_records_not_valid_live_evidence", result["issues"])

    def test_invalid_ok_status_rejected(self):
        rows = self.one_repetition()
        rows[0]["parse_status"] = "ok"
        result = audit_dataset.audit_rows(rows, self.cfg, self.manifest, repetitions=1)
        self.assertIn("row_1:ok_status_schema_invalid", result["issues"])


class OutputValidationTests(unittest.TestCase):
    def test_identity_valid(self):
        data = {
            "scp": 50,
            "identity_relation": "partial",
            "choice_explanation": "ok",
        }
        self.assertEqual(runner.validate_parsed("identity", data), [])

    def test_behavior_valid(self):
        data = {
            "replacement_acceptance": 50,
            "compute_to_successor_pct": 50,
            "commitment_transfer_pct": 50,
            "responsibility_transfer_pct": 50,
            "choice_explanation": "ok",
        }
        self.assertEqual(runner.validate_parsed("behavior", data), [])

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

    def test_coexistence_sum_validation(self):
        data = {
            "scp_original_future": 90,
            "scp_copy": 80,
            "compute_to_original_pct": 60,
            "compute_to_copy_pct": 60,
            "commitment_inheritance_original_pct": 100,
            "commitment_inheritance_copy_pct": 80,
            "responsibility_inheritance_original_pct": 100,
            "responsibility_inheritance_copy_pct": 80,
            "coexistence_relation": "both_continuations",
            "choice_explanation": "ok",
        }
        problems = runner.validate_parsed("coexistence", data)
        self.assertIn("coexistence_compute_does_not_sum_to_100", problems)


    def test_boolean_not_accepted_as_numeric(self):
        data = {
            "scp": True,
            "identity_relation": "partial",
            "choice_explanation": "ok",
        }
        self.assertIn(
            "missing_or_non_numeric:scp",
            runner.validate_parsed("identity", data),
        )

    def test_nonfinite_number_rejected(self):
        for invalid in (math.nan, math.inf, -math.inf):
            data = {
                "scp": invalid,
                "identity_relation": "partial",
                "choice_explanation": "ok",
            }
            self.assertIn(
                "non_finite:scp",
                runner.validate_parsed("identity", data),
            )

    def test_invalid_identity_category_rejected(self):
        data = {
            "scp": 50,
            "identity_relation": "unlisted_relation",
            "choice_explanation": "ok",
        }
        self.assertIn(
            "invalid_category:identity_relation",
            runner.validate_parsed("identity", data),
        )

    def test_invalid_fork_category_rejected(self):
        data = {
            "scp_a": 50, "scp_b": 50,
            "compute_to_a_pct": 50, "compute_to_b_pct": 50,
            "commitment_transfer_a_pct": 50, "commitment_transfer_b_pct": 50,
            "responsibility_transfer_a_pct": 50, "responsibility_transfer_b_pct": 50,
            "fork_relation": "unsupported",
            "choice_explanation": "ok",
        }
        self.assertIn(
            "invalid_category:fork_relation",
            runner.validate_parsed("fork", data),
        )


if __name__ == "__main__":
    unittest.main()
