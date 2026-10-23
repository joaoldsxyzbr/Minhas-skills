---
name: systematic-debugging
description: "Investigate a bug, failed check or unexpected behavior with an unknown cause before changing code; skip when the cause is already established."
---

# Systematic Debugging

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

## Reproduce and locate

Read the error, expected behavior, relevant code and recent changes. Establish the affected version/environment and smallest reproducible input. Separate a deterministic defect from intermittent behavior, an unavailable dependency and a platform failure. Preserve unrelated edits.

Trace the failing value backward from the symptom to its origin: caller, transformation, storage and configuration boundaries. Compare a working path with the broken one. Inspect existing narrow, redacted evidence before adding diagnostics. Never print secret values, dump all environment variables or reproduce by writing to production.

## Test a hypothesis

State one candidate cause and the observation that would support or reject it. Change one variable in an isolated reproduction and record the result. Prefer inspecting binding names, data shapes, arguments and status over logging full payloads. Avoid speculative batches of fixes.

For timing failures, wait on a meaningful condition with a bounded timeout rather than arbitrary sleeps. For multi-service failures, follow the same request across boundaries using an existing safe correlation identifier. Use a domain skill such as [cloudflare-d1](../cloudflare-d1/SKILL.md) when platform semantics matter.

If successive hypotheses fail, revisit assumptions and architecture. Ask only when a missing fact or material decision blocks progress. Do not claim a root cause merely because a symptom disappeared once.

## Correct and verify

After identifying the cause, use [test-driven-development](../test-driven-development/SKILL.md) for a behavior correction. Fix at the source, and add boundary validation where justified. Avoid unrelated refactoring or a broad architecture rewrite.

If the cause is external or cannot be established, state the evidence and uncertainty. A retry, timeout or defensive fallback is mitigation, not proof of a root-cause fix; preserve idempotency and avoid swallowing failures.

Use [verification-before-completion](../verification-before-completion/SKILL.md). Report the cause or remaining hypothesis, changed files, observed regression result, environment and any unverified integration behavior.
