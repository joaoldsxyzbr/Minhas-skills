---
name: cloudflare-platform
description: Plan, build, debug, or review applications and infrastructure using Cloudflare Workers, Pages, D1, KV, R2, Durable Objects, and Wrangler.
---

# Cloudflare Platform

Use this skill for Cloudflare development and operations. Keep the implementation aligned with the project's existing architecture and current Cloudflare product behavior.

## Start from the repository

1. Read project guidance and inspect the relevant files, configuration, migrations, and deployment scripts.
2. Identify the existing runtime and CLI. If the project uses Wrangler, continue with Wrangler; do not switch tooling without a reason.
3. Determine which Cloudflare account, environment, database, and deployment target the user means. Never infer production when the environment is ambiguous.
4. For current API details, limits, pricing, compatibility dates, or newly released features, consult official Cloudflare documentation. Treat project code and deployed configuration as the source of truth for what is currently configured.

## Choose services by requirement

- Workers for request handling and edge logic.
- Pages for an existing Pages project; preserve it during unrelated work.
- D1 for relational SQL data and migrations.
- KV for key-value data where its consistency model fits.
- R2 for object and file storage.
- Durable Objects when strongly coordinated state is needed.
- Queues or Workflows for asynchronous or durable multi-step work.

Use the smallest set that meets the requirement. Explain tradeoffs when two services are plausible.

## Safe changes

- Keep secrets out of source files, logs, command output, and commits. Use the project's existing secret-binding approach.
- Review bindings, migrations, compatibility settings, and environment selection before changing them.
- For D1, inspect the schema and migration history first. Make additive, reversible migrations where practical; preserve existing data and verify queries against the correct database.
- Before production operations, state the exact resource and action. Take a backup or use a preview/staging environment when the action could alter or remove user data.
- Do not deploy, delete resources, rotate secrets, or change DNS unless the user explicitly requested that action.
- Prefer local validation and dry runs before deployment. Report what was checked and what remains unverified.

## Cloudflare CLI

Follow the CLI already used in the repository. Inspect its version and help before relying on unfamiliar flags. Use official Cloudflare documentation for current syntax. Do not install a CLI, create a new configuration, or migrate from Wrangler to another CLI without a concrete project need.

## Completion report

Summarize the changed resources or files, checks run, environment affected, and whether a deployment occurred. Distinguish verified results from assumptions.
