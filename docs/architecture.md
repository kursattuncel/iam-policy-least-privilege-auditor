# Architecture

## Design Goals

- Keep the tool local-first and deterministic.
- Make the security reasoning visible in code and documentation.
- Prefer standard-library Python so reviewers can run the project quickly.

## Core Flow

1. Read local synthetic input from `examples/`.
2. Normalize or parse the input into simple Python data structures.
3. Apply explainable security logic.
4. Print JSON or Markdown output that can be used in a ticket, lesson, or review.

## Non-Goals

- No live scanning.
- No exploit automation.
- No collection of real secrets, real customer data, or third-party telemetry.
