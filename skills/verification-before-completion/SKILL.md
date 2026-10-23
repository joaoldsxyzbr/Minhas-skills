---
name: verification-before-completion
description: "Verify technical completion claims against fresh evidence for the current artifact; distinguish local checks, remote results and untested behavior."
---

# Verification Before Completion

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

Before reporting completion, identify what evidence supports each material claim. Reuse a successful check for the same unchanged artifact and environment; rerun after changes that invalidate it. Do not rerun solely because another message was sent.

## Verify the claim

- Run the relevant command, inspect its exit status and complete relevant output. For non-code tasks, inspect the actual resulting artifact or remote read-back.
- Separate a failing assertion from an unavailable tool, baseline failure or environmental error. Do not call a partial check a full pass.
- Validate changed behavior and necessary repository gates. A unit test does not prove deployment, platform compatibility, accessibility or visual fidelity.
- Review the diff and requirements. Check unrelated files, secrets, missing references, accidental dependencies and incomplete work.
- Inspect delegated work independently: read its changes and rerun a useful check. A subagent's success statement alone is insufficient evidence.
- After remote writes, read back the resulting revision/resource. If unavailable, report saved state separately from unverified read-back.

## Evidence and boundaries

Report changed behavior, checks actually run and material gaps. Tie evidence to the revision or artifact when available. Do not fabricate tests, logs, citations or a numeric quality score. If a tool is unavailable, finish supported work and name exactly what could not be tested.

For skill collections, distinguish structural validation, manual scenario analysis, independent agent executions and actual host invocation. A passing routing table cannot prove that ChatGPT activates every skill automatically.
