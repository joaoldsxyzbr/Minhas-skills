# Workers Platform API Checks

Check the JavaScript implementation, installed runtime definitions and current official docs. Do not prescribe a TypeScript conversion or generic type syntax for JavaScript.

## Handlers and base classes

Module handlers receive bindings through their documented `env` argument. Platform base classes expose the environment according to their own contract, commonly `this.env`. Check each API rather than rejecting any local variable named `env` inside a class.

Verify import paths, inheritance, constructor calls and handler signatures against the actual target. Do not assume every platform class has the same name or package. Check that a fetch handler yields a Response (directly or via a promise) and that asynchronous work has an appropriate lifetime.

A base class must really be extended when its runtime behavior is needed; a type-only declaration cannot supply that behavior. In JavaScript, preserve valid existing conventions and validate exported classes against configured bindings/migrations.

## Serialization boundaries

Structured clone, JSON and SQL binding values are different contracts. Verify the encoding and supported types at each boundary; do not apply a universal ban on objects or a universal assumption they serialize.

| Boundary | Official reference and check |
| --- | --- |
| Queue messages | [JavaScript APIs](https://developers.cloudflare.com/queues/configuration/javascript-apis/): selected encoding, payload limit and retry/delivery semantics |
| Workflow step results | [Workers API](https://developers.cloudflare.com/workflows/build/workers-api/): result serialization and retry-safe side effects |
| Durable Object storage | [Storage API](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/): distinguish KV values from SQL parameters |
| D1 | [Prepared statements](https://developers.cloudflare.com/d1/worker-api/prepared-statements/): supported parameter types, binding and result shape |
| WebSocket messages | [WebSockets](https://developers.cloudflare.com/workers/runtime-apis/websockets/): accepted payload types and explicit object encoding |

If platform evidence is missing, report that uncertainty instead of rejecting valid code based on another service's rules.
