# GitHub-centered project lifecycle

Apply this reference to **repository-backed engineering work** when GitHub access is available. It coordinates existing skills; it is not an additional lead workflow. The user's scope, permissions, repository `AGENTS.md`, and the shared rules still govern every action. Do not invoke it for general conversation, standalone research, or a task without a repository.

## 1. Recover the source of truth

- Identify the exact owner/repository and selected branch. Do not infer which of several projects the user means if the available context cannot resolve it safely.
- Read repository instructions, relevant source, current branch/commits, open Issues, PRs, existing plans, and CI status as relevant to the request. Distinguish open suggestions from approved tasks, and stale state from current evidence.
- For **"continue", "what remains?", or "is it ready?"**, reconstruct the last verified milestone, unfinished work, blocking checks, and the next safe action from GitHub before relying on conversation memory. Never treat memory as proof of a remote write or passing check.
- If GitHub is unavailable, use accessible local state when relevant; explain the missing repository verification and avoid inventing issue/PR/CI status.

## 2. Choose the smallest suitable work path

- **Simple, specified edit:** read impacted files, make a focused change, review the diff, run proportionate checks, and report. Do not require an Issue, separate plan, PR, or ceremonial TDD for documentation/style-only changes.
- **Bug with unknown cause:** `systematic-debugging`, then `test-driven-development` when fixing observable behavior; use a domain skill only when relevant.
- **Feature or substantial change:** use `writing-plans` if a plan is needed, then `executing-plans` for authorized implementation; add targeted tests, review, and verification. An explicit plan-only request does not authorize code changes.
- **Review-only request:** `code-review` without modifying, approving, or merging unless separately authorized.
- Reuse existing accepted plans or Issues; avoid duplicate planning and duplicate Issues. Do not automatically execute arbitrary Issues merely because they are open.

## 3. Record planning and work without bureaucracy

- For significant or multi-session work, prefer an existing relevant Issue; when authorized, create/update one with objective, scope, acceptance criteria, ordered tasks, evidence, blockers, and links to PRs. A large executable plan can live in the repository's established plan location; link to it from the Issue when appropriate.
- Use the Issue for progress and outstanding work, the branch/commits for implementation, the PR for review, and GitHub Actions for CI evidence. These have different purposes; an Issue alone does not prove implementation.
- Do not create or update shared Issues, PRs, releases, or repository settings unless specifically requested or previously authorized for this work.

## 4. Implement safely

- Prefer an isolated feature/test branch for nontrivial work; respect an explicitly selected branch. Do not move work to `main` merely for convenience. Inspect the base and any unrelated edits before modifying files.
- Preserve project architecture and existing instructions. Commit focused, reviewable changes with descriptive messages; never include secrets or unrequested files.
- If executable local tools are available, run the narrowest meaningful checks during work, then required project gates. GitHub connector write access alone does **not** establish that code can be built or executed.
- When checks fail, investigate the actual cause and avoid hiding failures, bypassing protections, or changing unrelated code merely to obtain green CI.

## 5. Verify, review, and hand off

- Apply `verification-before-completion` and `code-review` as appropriate. Check the final diff and the status of relevant GitHub Actions checks for the exact commit/PR, when accessible. Distinguish not-run, blocked, failed, and passed checks; don't equate CI success with end-to-end or production validation.
- For a meaningful branch handoff, use `finishing-branch`; when authorized, open or update the PR with purpose, notable changes, tests actually run, risks, and remaining manual validation. Link related Issues when applicable.
- **Merge, deploy, release, delete a branch, alter permissions, or change production data only with the applicable authorization.** Requesting implementation does not grant those permissions. Never enable automatic merge or deployment by default.
- Read back remote changes where possible. Report: repository/branch and commit/PR; implemented behavior; checks and CI evidence; pending work; next safe step. Update the Issue/checkpoint when authorized.

## 6. Specialized cases

- A project already running in production requires extra caution: protect production data, existing API contracts, migrations, and deploy steps; favor a reviewable PR and independent validation before integration.
- When modifying the Minhas Skills plugin itself, treat its GitHub repository as source truth: synchronize changes in an identifiable branch first, run available package checks, then update the **same** account plugin with Plugin Creator. Record the resulting plugin version and PR; if the PR is not merged, state clearly that `main` is not yet synchronized.
- The workflow describes what to do **when tools and authorization permit it**; it cannot guarantee connected GitHub access, autonomous task execution, CI coverage, host skill activation, or production correctness.
