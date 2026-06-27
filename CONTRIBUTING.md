# Contributing

Thanks for helping improve this defensive cybersecurity project.

## Good First Issues

- Add a new benign sample input.
- Add a unit test for an existing rule.
- Improve documentation for a beginner reader.
- Add a detection, audit, or lesson that works only on local fixtures.

## Guardrails

- Keep the project defensive, educational, and lawful.
- Do not add exploit automation, credential harvesting, stealth, persistence,
  destructive behavior, or live-target scanning.
- Prefer clear explanations and reproducible examples over clever code.

## Development

```bash
python -m pip install -e .
python -m unittest discover -s tests
python -m iam_policy_auditor --help
```

Replace `iam_policy_auditor` with the package module for this repository.
