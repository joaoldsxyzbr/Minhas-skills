---
name: workers-best-practices
description: "Implement or review Cloudflare Workers behavior, bindings, runtime safety and configuration; load only the affected reference sections."
---

# Workers Best Practices

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

Inspect the project's JavaScript, configuration, runtime target and existing checks. Verify changing API/limit/compatibility claims against official Cloudflare docs. Do not turn a narrow change into a complete platform migration.

| Concern | Reference |
| --- | --- |
| Config, bindings, secrets, compatibility and diagnostic privacy | [Configuration](references/configuration.md) |
| Streaming, async lifetime, state, validation, crypto and testing | [Runtime patterns](references/runtime-patterns.md) |
| Handlers, base classes and data serialization boundaries | [Platform API checks](references/platform-apis.md) |

## Review priorities

- Bound input size and validate malformed input before data writes.
- Keep request-specific state out of shared mutable module variables.
- Await required work; attach optional background work to the documented lifecycle. Use a durable mechanism if completion is required beyond that lifecycle.
- Use available bindings for supported service operations. Validate actual consistency, latency and pricing instead of treating all bindings as free local calls.
- Use native cryptography and real authentication. Never use an always-successful auth placeholder or trust an identity header unless the ingress contract authenticates it.
- Preserve explicit authorization and environment selection. Check remote bindings even during local development.
- Preserve privacy choices. Do not flag intentionally disabled logs/traces as a defect or enable them automatically.

For D1 use the bundled [cloudflare-d1](../cloudflare-d1/SKILL.md); for CLI operations use [wrangler](../wrangler/SKILL.md); for other service architecture use [cloudflare-platform](../cloudflare-platform/SKILL.md). Run checks appropriate to the change and state whether runtime behavior was actually exercised.
