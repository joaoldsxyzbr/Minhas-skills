---
name: finishing-branch
description: Prepare completed branch work for handoff or integration after verification and a final diff review.
---

# Finishing a Branch

Use after implementation and review are complete, before handing off, opening a pull request, merging, or cleaning up a branch.

## Verify the result

- Run the checks required by the plan and relevant repository guidance.
- Inspect the complete diff, working tree, branch, and commit history.
- Confirm there are no accidental files, secrets, unresolved review findings, or unexplained generated changes.
- Report checks accurately, including failures and unrun checks.

## Choose the next step

Present the applicable options clearly: keep the branch for handoff, open a pull request, merge into the target branch, or discard the work. Recommend the lowest-risk option that matches the user's request and repository conventions.

Proceed with an integration or publication step only when the user has authorized it. A request to implement a change does not by itself authorize merging, deployment, or deleting work. Preserve uncommitted work and keep branches that contain useful commits.

## Handoff

Summarize the implementation, verification, commit or pull request, and any remaining limitations. If cleanup is requested and safe, remove only the task's worktree and branch after confirming the work is integrated or intentionally discarded.
