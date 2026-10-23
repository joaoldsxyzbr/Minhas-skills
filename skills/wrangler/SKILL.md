---
name: wrangler
description: "Run or troubleshoot Wrangler CLI commands and configuration in a Wrangler project or on explicit request; verify installed help and target before operations."
---

# Wrangler

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

## Inspect before issuing commands

Find the project's package manager, scripts, installed Wrangler version, config and selected environment. Use the project's existing approved CLI; do not silently upgrade it, change frameworks or migrate to a different CLI. For non-Wrangler projects, use the bundled [cloudflare-platform](../cloudflare-platform/SKILL.md).

Inspect local CLI help and schema before relying on flags. Use current official docs when platform semantics or unfamiliar syntax matter. Do not run commands that auto-install an unverified latest package merely to inspect help.

| Task | Evidence |
| --- | --- |
| Command and flags | Installed help and [commands](https://developers.cloudflare.com/workers/wrangler/commands/) |
| Configuration and environment overrides | Installed schema, source config, [configuration](https://developers.cloudflare.com/workers/wrangler/configuration/) and [environments](https://developers.cloudflare.com/workers/wrangler/environments/) |
| Local runtime and bindings | [Local development](https://developers.cloudflare.com/workers/local-development/) and the effective binding targets |
| D1 schema/data operations | Bundled [cloudflare-d1](../cloudflare-d1/SKILL.md) |
| Secrets | [Secret lifecycle](https://developers.cloudflare.com/workers/configuration/secrets/) and whether the exact operation deploys immediately |
| Deployment or rollback | Project scripts and [rollback limits](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/) |
| Preview deployments | [Previews](https://developers.cloudflare.com/workers/previews/), installed version support and current resource isolation rules |

## Choose the exact target

Establish account, Worker, environment, config, resource and local/remote mode from evidence. Inspect authentication identity without printing credentials. Use narrow scopes and protected input mechanisms. An omitted environment can target a default resource; do not assume it is staging.

A local process can use remote resources. A preview name does not prove isolation. Before a remote write/deployment, match the exact effect to the user's authorization. If the target is ambiguous, finish safe inspection and ask for the missing target before executing.

## Apply and validate

Edit config sources rather than generated output. Preserve format and runtime dates unless the change needs otherwise. Reconcile dashboard and repository configuration before a deploy that could overwrite it. Consider data/migration effects separately from code rollback.

Prefer the project's build and supported dry-run workflow before remote deployment. A dry run proves only what it actually checks, not remote bindings or production behavior. For JavaScript preserve its language; do not add a TypeScript build step for binding checks.

After authorized remote changes, perform a narrow read-back or functional check. Report exact target, revision/result, checks and remaining limitations. If docs/help are unavailable, do not invent a flag or claim a command ran.
