# IAM Policy Least Privilege Auditor

An offline AWS IAM policy reviewer that flags risky permissions and explains least-privilege fixes.

## Job Signal

This repository is designed to demonstrate readiness for: **cloud security analyst, IAM analyst, security engineer**.

## Problem

Hiring teams want evidence that cloud-security candidates can reason about identity, privilege, and audit readiness.

## What It Shows

- Parse local IAM policy JSON without touching a cloud account.
- Flag wildcard actions, wildcard resources, PassRole, admin-like actions, and missing conditions.
- Produce plain-English remediation notes useful in audits and interviews.

## Quickstart

```bash
python -m pip install -e .
python -m unittest discover -s tests
python -m iam_policy_auditor examples/policy.json
```

## Portfolio Talking Points

- I can turn ambiguous security work into repeatable workflows.
- I can write clear documentation for analysts, engineers, and learners.
- I can build safe, local-first examples that avoid real secrets and third-party targets.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## Safety

This project is for defensive security, education, and local synthetic data only.
