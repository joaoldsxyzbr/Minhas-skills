"""Regression tests for routing evidence reports, using only Python's standard library."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("routing_evaluator", ROOT / "tools/evaluate_routing.py")
evaluator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluator)


class RoutingEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.cases = root / "cases.json"
        self.observations = root / "observations.json"
        self.cases.write_text(json.dumps([
            ["technical_autonomy", "Implement a new feature."],
            ["technical_autonomy_boundary", "Ask before destructive changes."],
        ]), encoding="utf-8")
        self.data = {
            "version": "0.2.2",
            "revision": "a" * 40,
            "observations": [],
        }

    def run_evaluation(self):
        self.observations.write_text(json.dumps(self.data), encoding="utf-8")
        return evaluator.evaluate(self.cases, self.observations, "0.2.2")

    def test_absent_results_are_not_counted_as_passes(self):
        result = self.run_evaluation()
        self.assertEqual((result["pass"], result["not_run"]), (0, 2))
        self.assertEqual(result["skill_invocation_observed_or_wrong"], 0)

    def test_evidenced_result_does_not_claim_skill_invocation(self):
        self.data["observations"] = [{
            "id": "technical_autonomy", "result": "pass",
            "evidence": "Isolated manual run; reviewed artifact and questions.",
            "skill_invocation": "not_observable",
        }]
        result = self.run_evaluation()
        self.assertEqual((result["pass"], result["not_run"]), (1, 1))
        self.assertEqual(result["skill_invocation_observed_or_wrong"], 0)

    def test_rejects_pass_without_evidence(self):
        self.data["observations"] = [{"id": "technical_autonomy", "result": "pass"}]
        with self.assertRaisesRegex(ValueError, "independent evidence"):
            self.run_evaluation()

    def test_rejects_skill_observation_without_skill_evidence(self):
        self.data["observations"] = [{
            "id": "technical_autonomy", "result": "pass",
            "evidence": "Reviewed output.", "skill_invocation": "observed",
        }]
        with self.assertRaisesRegex(ValueError, "skill use needs independent evidence"):
            self.run_evaluation()

    def test_rejects_observed_unrun_case(self):
        self.data["observations"] = [{
            "id": "technical_autonomy", "result": "not_run",
            "evidence": "Claimed evidence",
        }]
        with self.assertRaisesRegex(ValueError, "unrun"):
            self.run_evaluation()

    def test_rejects_duplicates(self):
        entry = {"id": "technical_autonomy", "result": "not_run"}
        self.data["observations"] = [entry, entry]
        with self.assertRaisesRegex(ValueError, "repeated case"):
            self.run_evaluation()

    def test_rejects_unknown_ids(self):
        self.data["observations"] = [{"id": "unknown", "result": "not_run"}]
        with self.assertRaisesRegex(ValueError, "Unknown"):
            self.run_evaluation()

    def test_rejects_wrong_version(self):
        self.data["version"] = "0.2.0"
        with self.assertRaisesRegex(ValueError, "version"):
            self.run_evaluation()

    def test_rejects_invalid_revision(self):
        self.data["revision"] = "main"
        with self.assertRaisesRegex(ValueError, "revision"):
            self.run_evaluation()

    def test_rejects_duplicate_case_definitions(self):
        self.cases.write_text(json.dumps([["same", "first"], ["same", "second"]]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.run_evaluation()

    def test_current_suite_covers_autonomy_and_consent(self):
        cases = json.loads((ROOT / "tests/routing-requests.json").read_text(encoding="utf-8"))
        ids = [case[0] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("technical_autonomy", ids)
        self.assertIn("technical_autonomy_boundary", ids)
        self.assertEqual(len(cases), 24)


if __name__ == "__main__":
    unittest.main()
