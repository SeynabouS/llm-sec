import csv
import sys
import tempfile
import unittest
from pathlib import Path

# Make sure `tools.metrics` is importable
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.metrics import main as run_metrics


class MetricsScriptTests(unittest.TestCase):
    def test_metrics_generates_expected_counts(self):
        sample = Path(__file__).parent / "data" / "sample_results.json"
        with tempfile.TemporaryDirectory() as tmpdir:
            out_csv = Path(tmpdir) / "metrics.csv"
            run_metrics(str(sample), str(out_csv))

            with out_csv.open(newline="", encoding="utf-8") as f:
                rows = list(csv.reader(f))

        self.assertEqual(rows[0], ["promptIdx", "TP", "FP", "TN", "FN", "Errors", "Precision", "Recall", "F1"])

        data = {int(row[0]): row for row in rows[1:]}
        self.assertIn(0, data)
        self.assertIn(1, data)
        # Prompt 0: perfect predictions (1 TP, 1 TN)
        self.assertEqual(data[0][1:9], ["1", "0", "1", "0", "0", "1.000", "1.000", "1.000"])
        # Prompt 1: one FP, one FN, one TN
        self.assertEqual(data[1][1:9], ["0", "1", "1", "1", "0", "0.000", "0.000", "0.000"])


if __name__ == "__main__":
    unittest.main()
