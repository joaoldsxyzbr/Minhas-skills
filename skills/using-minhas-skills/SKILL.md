---
name: using-minhas-skills
description: "Select the smallest bundled workflow for engineering, design, Cloudflare, GitHub, skill authoring or research; resolve overlaps and load references only as needed."
---

# Using Minhas Skills

Apply the [shared rules](references/workflow-rules.md). Classify the user's current intent and requested result, not isolated keywords. If nothing needs a specialist (greeting, stable explanation, simple copy edit), respond directly. Do not force a technical workflow onto an unrelated task.

## Intent precedence

When rows overlap, choose the process lead before the technical domain:

1. Explicit plan-only, execution-of-plan or review-only intent selects writing-plans, executing-plans or code-review respectively. An interface/UX critique selects product-design-audit instead of code-review.
2. A failed command or unknown bug selects systematic-debugging, including Wrangler/D1 failures; the domain skill supports diagnosis. An established cause goes directly to TDD.
3. Product UX discovery uses product-design-ideation instead of generic brainstorming. A supplied visual reference uses implementation QA.
4. Use a domain skill as lead only when none of those process intents applies. Add domain guidance to the process lead, not a second competing process.

For example, reviewing Worker code uses code-review + workers-best-practices; investigating a failed Wrangler dry run uses systematic-debugging + wrangler. Technical nouns alone never override the requested activity.

## Select one lead workflow

| Intent | Lead workflow | Add only when needed |
| --- | --- | --- |
| Unknown bug or failed check | [systematic-debugging](../systematic-debugging/SKILL.md) | Domain skill for evidence; TDD after cause is established |
| Known bug cause or specified behavior change | [test-driven-development](../test-driven-development/SKILL.md) | Domain implementation and relevant verification |
| New product experience or substantial UX redesign | [product-design-ideation](../product-design-ideation/SKILL.md) | Technical domain constraints; do not also run brainstorming discovery |
| Open-ended technical or non-UX idea | [brainstorming](../brainstorming/SKILL.md) | A domain skill for feasibility |
| Existing interface critique | [product-design-audit](../product-design-audit/SKILL.md) | Implementation only if requested |
| Supplied mockup or visual implementation/QA | [product-design-implementation-qa](../product-design-implementation-qa/SKILL.md) | TDD for changed behavior, not pure visual styling |
| Product request whose phase is unclear | [product-design](../product-design/SKILL.md) | Select one focused design skill |
| Requested plan or substantial agreed specification | [writing-plans](../writing-plans/SKILL.md) | Planning ends at the plan unless execution is authorized |
| Execute an existing plan | [executing-plans](../executing-plans/SKILL.md) | TDD/domain skills for each affected step |
| Review a change or PR | [code-review](../code-review/SKILL.md) | GitHub skill for repository access; no edits unless requested |
| Repository, branch, commit or PR operation | [github-workflows](../github-workflows/SKILL.md) | [using-git-worktrees](../using-git-worktrees/SKILL.md) only for useful isolation |
| Prepare completed branch for integration | [finishing-branch](../finishing-branch/SKILL.md) | Reuse existing integration authorization |
| D1 data/schema/query/migration | [cloudflare-d1](../cloudflare-d1/SKILL.md) | Debugging if cause unknown; Wrangler for CLI operations |
| Workers implementation/config review | [workers-best-practices](../workers-best-practices/SKILL.md) | [wrangler](../wrangler/SKILL.md) for actual CLI work |
| Wrangler command/config troubleshooting | [wrangler](../wrangler/SKILL.md) | Specific Cloudflare service |
| Cloudflare architecture or other services | [cloudflare-platform](../cloudflare-platform/SKILL.md) | Only affected service references |
| Create, improve or audit skills | [skill-authoring-audit](../skill-authoring-audit/SKILL.md) | Verify consuming-agent behavior |
| Broad comparison or evidence-heavy investigation | [deep-research](../deep-research/SKILL.md) | Specific domain skill if implementation is also requested |

## Resolve combined requests

Use one process lead plus the minimum domain support. Examples: unknown D1 bug → debugging + D1, then TDD and verification; new UX → product ideation, then a plan only if needed; explicit approved implementation → execution, not another discovery round. For a small, clear edit, act directly and check the affected result.

Specific intent wins: an existing UX audit is not new ideation; a PR review is not an instruction to fix or merge; a Cloudflare implementation problem is not automatically broad research. Do not chain routers in a loop or load every skill. Reassess only when the task changes phase or new evidence requires it.

Before a technical completion claim, use [verification-before-completion](../verification-before-completion/SKILL.md). Host skill discovery uses descriptions and available context; this router guides selection but cannot guarantee invocation for every prompt.
