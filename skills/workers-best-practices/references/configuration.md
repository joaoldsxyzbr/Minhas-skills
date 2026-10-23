# Workers Configuration

Read the installed Wrangler schema, selected config, package scripts and target environment. Consult [configuration docs](https://developers.cloudflare.com/workers/wrangler/configuration/) for current fields.

## Compatibility

Preserve the existing compatibility date during unrelated work. For a new Worker choose a supported date and document it; review intervening behavior changes before advancing an existing date. Enable Node compatibility only if actual runtime imports require it, and check the relevant date/flag combination in [compatibility docs](https://developers.cloudflare.com/workers/configuration/compatibility-flags/).

Do not convert JavaScript to TypeScript to obtain binding hints. Existing generated declarations may help inspection; preserve approved tooling without adding a new language or build system.

## Binding consistency

Check the entrypoint, Worker name and environment-specific bindings. Every used binding must exist under the same name in the effective target configuration. Do not assume fields inherit across environments. For Durable Objects, check exported class names and migration history against current docs.

Distinguish local simulation from remote bindings. A preview URL or local server does not prove its resources are isolated. Do not modify resources until account, environment and requested action are established.

## Secrets

Keep secrets out of config, source, logs and command arguments. Verify local secret files are ignored. Use the existing protected secret workflow and verify whether a command uploads a version or immediately deploys it before running it. Do not print values to prove presence. See [secrets](https://developers.cloudflare.com/workers/configuration/secrets/).

## Diagnostics and privacy

Do not enable Logs, Traces or analytics automatically. Preserve the project's settings, including explicit disabled collection. Use existing safe error information, local reproduction and redacted samples first.

If new collection is authorized, define purpose, minimum fields, sampling, retention and access. Avoid full URLs, request bodies, headers, cookies, credentials and raw exception messages that may contain private data. Use stable error codes and safe correlation identifiers where necessary. Do not silently remove required audit controls.

Consult [Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) and [Traces](https://developers.cloudflare.com/workers/observability/traces/) only when configuring or investigating those features. Missing collection alone is not a defect.
