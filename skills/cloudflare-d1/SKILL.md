---
name: cloudflare-d1
description: Build, inspect, migrate, and troubleshoot Cloudflare D1 databases with safe environment selection and current official documentation.
---

# Cloudflare D1

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

Use for D1 schema, queries, migrations, Worker bindings, local development, deployment configuration, or troubleshooting. Consult current Cloudflare documentation before relying on CLI flags, limits, platform behavior, or syntax.

## Establish the target

- Inspect the repository's Wrangler configuration, package scripts, migration directory, environment names, and existing D1 bindings.
- Identify the intended account, database, and environment (local, preview/staging, or production) from the user's request and configuration.
- Never guess a database ID or assume a default environment is safe. If the target is unclear and a command could affect remote data, inspect further or ask one specific question.
- Prefer local development and a non-production database for schema changes and query experiments.

## Schema and migrations

- Follow the project's existing migration convention. If none exists, use the current official D1 migration guidance and describe the proposed structure.
- Keep migrations ordered, reviewable, and safe to apply. Account for existing rows, constraints, indexes, and rollback limitations.
- Inspect generated SQL before applying it. Test migrations against a local or disposable database where feasible.
- Check that application bindings and environment-specific database configuration agree.
- Use parameter binding for user values in queries; avoid building SQL by interpolating untrusted input.

## Remote changes

- Before applying a migration, importing data, or running a write against a remote database, verify the exact target and explain the effect.
- Never run production writes or destructive SQL merely because a command is available. Require explicit authorization for a consequential action unless the user already clearly authorized it.
- Check migration status and take an appropriate backup or recovery step when available before a risky change. Use current Cloudflare guidance; do not assume a backup method or recovery window.
- After a remote operation, verify the result using a narrow read or migration status check and report the target.

## Queries and troubleshooting

- Inspect query shape, binding names, parameter use, expected result size, and relevant indexes.
- Reproduce errors locally when possible. Separate application errors, SQL errors, binding/configuration errors, and platform/API failures.
- For performance or concurrency questions, use current platform docs rather than assuming generic SQLite behavior covers D1.
- Verify the exact Wrangler command syntax in the installed CLI help or current official documentation before running it.

## Official references

- D1 overview: https://developers.cloudflare.com/d1/
- Migrations: https://developers.cloudflare.com/d1/reference/migrations/
- Local development: https://developers.cloudflare.com/d1/best-practices/local-development/
- Environments: https://developers.cloudflare.com/d1/configuration/environments/
- Import and export: https://developers.cloudflare.com/d1/best-practices/import-export-data/

