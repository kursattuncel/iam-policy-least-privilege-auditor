from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


HIGH_RISK_ACTIONS = {"iam:PassRole", "iam:CreateAccessKey", "iam:AttachUserPolicy", "sts:AssumeRole"}


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def load_policy(path: Path) -> dict[str, Any]:
    policy = json.loads(path.read_text(encoding="utf-8"))
    if "Statement" not in policy:
        raise ValueError("IAM policy must include a Statement field")
    return policy


def analyze_policy(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    statements = _as_list(policy.get("Statement"))
    for index, statement in enumerate(statements, start=1):
        effect = statement.get("Effect", "Allow")
        actions = [str(action) for action in _as_list(statement.get("Action") or statement.get("NotAction"))]
        resources = [str(resource) for resource in _as_list(statement.get("Resource") or statement.get("NotResource"))]
        has_condition = bool(statement.get("Condition"))

        if effect != "Allow":
            continue
        if "*" in actions or any(action.endswith(":*") for action in actions):
            findings.append(finding(index, "critical", "Wildcard action", "Replace broad actions with task-specific permissions."))
        if "*" in resources:
            findings.append(finding(index, "high", "Wildcard resource", "Scope permissions to specific ARNs where the service supports it."))
        for action in actions:
            if action in HIGH_RISK_ACTIONS:
                findings.append(finding(index, "high", f"High-risk action {action}", "Require conditions and explicit approval for privileged identity actions."))
        if not has_condition and (set(actions) & HIGH_RISK_ACTIONS or "*" in resources):
            findings.append(finding(index, "medium", "Missing condition", "Add conditions such as MFA, source account, permission boundary, or resource tags."))
    return findings


def finding(statement: int, severity: str, title: str, remediation: str) -> dict[str, str]:
    return {
        "statement": str(statement),
        "severity": severity,
        "title": title,
        "remediation": remediation,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit a local AWS IAM policy JSON file.")
    parser.add_argument("policy", type=Path)
    args = parser.parse_args(argv)
    print(json.dumps(analyze_policy(load_policy(args.policy)), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
