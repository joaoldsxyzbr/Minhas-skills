---
name: code-review
description: Review a code change for correctness, regressions, security, and missing tests, reporting only actionable findings.
---

# Code Review

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

Use when reviewing a diff, pull request, or proposed implementation. Review the change against its intended behavior and surrounding code.

## Review the change

- Read the request, relevant plan, repository guidance, and complete diff.
- Trace changed behavior into callers, data flows, error handling, and compatibility boundaries.
- Check correctness, regressions, security and privacy implications, data loss risk, and missing or misleading tests.
- Verify findings against code or reproducible behavior. Do not report speculative concerns as defects.
- Ignore style preferences unless they impair correctness, maintainability, or repository conventions.

## Report findings

Lead with actionable issues ordered by severity. For each, give a concise title, file and location, the triggering condition, impact, and a practical fix. If no significant issue is found, say so and mention what was not tested.

Do not modify the reviewed change unless asked. Do not approve, merge, or close a pull request unless explicitly authorized.

