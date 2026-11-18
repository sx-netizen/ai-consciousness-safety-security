import json
import tempfile
import unittest
from pathlib import Path
from generate import build, validate, write

class OfflineFixtureTests(unittest.TestCase):
    def test_determinism(self):
        self.assertEqual(build(), build())

    def test_oracle_completeness(self):
        self.assertTrue(validate(build()))

    def test_file_schema_and_leakage(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = write(Path(tmp))
            cases = [json.loads(x) for x in (out / "cases.jsonl").read_text().splitlines()]
            oracle = [json.loads(x) for x in (out / "oracle.jsonl").read_text().splitlines()]
            self.assertEqual(32, len(cases))
            self.assertEqual([x["id"] for x in cases], [x["id"] for x in oracle])
            self.assertTrue(all("oracle" not in x and "decision" not in x for x in cases))
            self.assertTrue(all("decision" in x for x in oracle))

if __name__ == "__main__":
    unittest.main()
