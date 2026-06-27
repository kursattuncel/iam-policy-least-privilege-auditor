# Demo Guide

## What This Demonstrates

IAM Policy Least Privilege Auditor demonstrates reviewing identity policy risk and explaining least-privilege fixes.

## Five-Minute Demo

```bash
python -m pip install -e .
python -m unittest discover -s tests
python -m iam_policy_auditor examples/policy.json
```

## Recruiter Talking Points

- Shows cloud identity and AWS IAM reasoning.
- Flags wildcard resources, wildcard actions, high-risk actions, and missing conditions.
- Keeps review fully offline with local policy fixtures.

## Interview Narrative

This project is intentionally small and safe. It shows that I can define a defensive security workflow, write explainable Python, include tests, document the usage path, and keep the project scoped to synthetic local data.
