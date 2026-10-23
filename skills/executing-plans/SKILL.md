---
name: executing-plans
description: Carry out an agreed implementation plan in small verified steps while preserving the user's scope and keeping progress visible.
---

# Executing Plans

Use when requirements and an implementation plan are already agreed and the task is to carry them out. For a small direct change, work directly without unnecessary ceremony.

## Prepare

- Read the plan and the relevant repository guidance before editing.
- Check the current branch, working tree, and existing changes. Preserve work that is not part of this task.
- Confirm each step's expected outcome and verification method. Resolve a blocking ambiguity before dependent changes; otherwise state a reasonable assumption and continue.
- Keep user authorization in view. A plan does not authorize unrelated changes or consequential external actions.

## Execute

- Work through the plan in dependency order, keeping changes small and reviewable.
- Before changing behavior, understand the existing implementation and tests.
- For each meaningful step, run the narrowest useful check and inspect the result.
- If the plan conflicts with the repository, fails verification, or assumptions prove false, stop the affected step, explain the evidence, and revise the plan with the user when the change is material.
- Do not silently broaden scope to make a failing plan pass.
- Keep progress updates concise and tied to completed work, findings, or blockers.

## Finish

- Run the verification required by the plan and any relevant repository checks.
- Review the final diff for unintended files, secrets, generated artifacts, and incomplete work.
- Summarize what changed, checks run, and any limitation. Do not report unrun checks as passing.
- Integrate, publish, deploy, or merge only when that action is authorized.
