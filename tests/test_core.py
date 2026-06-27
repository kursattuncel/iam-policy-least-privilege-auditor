import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from iam_policy_auditor.cli import analyze_policy


class IamPolicyAuditorTests(unittest.TestCase):
    def test_flags_wildcards_and_passrole(self):
        findings = analyze_policy({"Statement": [{"Effect": "Allow", "Action": ["s3:*", "iam:PassRole"], "Resource": "*"}]})
        titles = {finding["title"] for finding in findings}
        self.assertIn("Wildcard action", titles)
        self.assertIn("Wildcard resource", titles)
        self.assertIn("High-risk action iam:PassRole", titles)


if __name__ == "__main__":
    unittest.main()
