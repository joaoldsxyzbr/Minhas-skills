---
name: using-git-worktrees
description: Isolate a substantial change in a Git worktree when parallel work or a clean working directory will reduce risk.
---

# Using Git Worktrees

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

Use when a task needs isolation from current edits, multiple branches must be checked out at once, or an agreed plan is substantial enough to benefit from a separate working directory. Do not create a worktree for a one-line edit without a reason.

## Before creating one

- Inspect the repository status, current branch, existing worktrees, and the requested base branch.
- Preserve uncommitted changes. Never clean, reset, or overwrite the user's working tree to prepare a worktree.
- Choose a descriptive branch name and a location outside the main working directory, following repository conventions.
- Confirm the branch does not already contain unrelated work.

## Work in isolation

- Create or reuse the appropriate worktree using Git's worktree commands.
- Verify the worktree path, branch, and clean starting state before editing.
- Keep task changes in the isolated branch; do not move unrelated files or commits.
- Run relevant checks within the worktree and inspect the final diff.

## Clean up

Remove a worktree only after its changes are safely committed, integrated, or explicitly discarded with authorization. Do not delete a branch or worktree containing uncommitted or unmerged user work.

