# Workers Runtime Patterns

Read only the affected section. Verify current behavior with the linked official docs and the project's runtime target. Examples are focused fragments, not full applications.

## Streaming and bounded input

Pass response streams through rather than buffering unbounded bodies. Enforce an application-specific byte limit for input parsing; a Content-Length check alone does not bound chunked input. Cancel or abort a failed stream pipeline so readers do not hang. See [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/).

```javascript
export default {
  async fetch() {
    const upstream = await fetch('https://example.com/large-file');
    return new Response(upstream.body, upstream);
  }
};
```

The URL is a fixed illustration, not an instruction to send user data. Real forwarding must use an authorized destination and handle status, headers and caching deliberately.

## Validation and state

Validate JSON types, required fields, lengths, ranges and permitted values with native JavaScript before using them. Do not add a community schema library. Reject malformed input with a controlled response and do not leak internal errors.

Keep per-request mutable data inside the handler and pass it explicitly. Module-level immutable configuration is different from mutable identity or request state. Do not assume a user header is authenticated.

## Async lifetime and delivery

Await work needed for the response. Use `ctx.waitUntil()` for authorized optional background work with a handled failure path, keeping the receiver intact. It is not a durable queue and does not guarantee completion after failures. For required delivery, evaluate Queues or Workflows, idempotency and retry semantics. Never retry a non-idempotent write blindly.

Check current duration, CPU, memory and request limits in [Workers limits](https://developers.cloudflare.com/workers/platform/limits/); they vary by product, plan, configuration and invocation type. Do not copy fixed limits from memory.

## Bindings and external services

Use a service's binding when it supports the required operation. A binding simplifies credentials and access; it does not imply every operation is in-process, has no network latency or is free. Check the service's actual [binding contract](https://developers.cloudflare.com/workers/runtime-apis/bindings/) and pricing.

Use [service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) for appropriate Worker-to-Worker calls. Example call site:

```javascript
const response = await env.CATALOG.fetch(request);
```

For external databases, assess [Hyperdrive](https://developers.cloudflare.com/hyperdrive/) only when needed. Verify that the required database client is allowed by the dependency policy before adopting it. Close/release connections according to the selected official client's lifecycle; do not install a community driver implicitly.

## Security and error handling

Use `crypto.randomUUID()` for identifiers and `crypto.getRandomValues()` for random secret material. Use native verification for cryptographic signatures; do not design authentication or cryptography from scratch.

For secret equality in Workers, check the Workers-specific `crypto.subtle.timingSafeEqual` API, accepted types and length requirements in [Web Crypto](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/). It is not a portable browser API. Apply bounded input and the documented comparison pattern; never replace it with homemade constant-time loops.

Return controlled error responses. Do not emit raw exceptions, tokens, full requests or identity data into logs. Use existing authorized diagnostics with redaction. Do not add `passThroughOnException()` as a generic fix: forwarding on failure must be an intentional product behavior.

## Runtime verification

Use `node:test` for portable JavaScript logic and pure modules. That does not emulate Workers bindings. Exercise integration behavior through the project's approved official runtime tools and disposable local resources; verify current setup in [testing docs](https://developers.cloudflare.com/workers/testing/).

An official adapter can require a community runner; do not add that runner automatically. If approved runtime tools are unavailable, finish supported unit/config checks and explicitly report the missing runtime validation. Test null returns, malformed inputs, repeated calls, authorization and failed writes where relevant. Never use production bindings merely to obtain a passing test.
