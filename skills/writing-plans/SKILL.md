---
name: writing-plans
description: "Write a concrete implementation plan for a requested plan or substantial agreed specification; skip trivial edits and do not restart discovery."
---

# Writing Plans

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

Read the specification, relevant code, repository instructions and existing checks. Resolve constraints from evidence before asking. Do not require a separate specification file when the user's request already contains the requirements.

## Make an executable plan

Record the goal, boundaries, supported stack, dependencies, target environment, acceptance criteria and material assumptions. List tasks in dependency order with:

- Exact affected paths and responsibilities; preserve the existing architecture.
- Observable result and relevant interfaces, including data formats and error behavior.
- Verification command or manual procedure with an expected result; mark commands not yet checked as proposed.
- For behavior changes: regression test, observed failure, minimal fix, verification. For prose/config/styling: a proportional check instead of a ritual TDD cycle.
- Data migration, compatibility, deployment or rollback considerations only when relevant.

Exercise realistic failure cases such as malformed input, authorization, retries, partial failure and boundary values. Select cases based on the task; do not impose an arbitrary count or write tests that duplicate implementation.

Keep each task independently reviewable. Use native checks such as `node --test`, `python -m unittest discover`, or approved .NET tooling when appropriate. Preserve required repository gates, and report any incompatible existing toolchain without installing community dependencies.

## Review and deliver

Check coverage of the user's requirements, task dependencies, required capabilities and unresolved decisions. Prefer the project's plan location; otherwise use `docs/minhas-skills/plans/YYYY-MM-DD-topic.md` for substantial repository work. Do not create extra documents for a small edit.

A plan-only request ends here. When execution is authorized, continue with [executing-plans](../executing-plans/SKILL.md), without asking again to execute the same scope. Do not schedule unnecessary commits or require subagents/worktrees merely because a plan exists.
