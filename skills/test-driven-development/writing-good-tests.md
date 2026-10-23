# Writing Good Tests

Read when designing behavior tests, fixtures or test doubles.

## Choose independent expectations

Name the defect each test catches. Derive expected values by hand from the contract, not by calling the same helper as the implementation. Cover boundary inputs and negative paths relevant to the task; a percentage alone does not establish correctness.

```javascript
import assert from 'node:assert/strict';
// Independent expectation for an escaping contract:
assert.equal(buildSearchQuery({ tag: 'urgent' }), 'tag:"urgent"');
```

Assert observable results and side effects, not a private method name or the mere existence of a mock. A change in wording or layout needs an assertion only if that exact value is contractual. Structure validation can check document syntax and references; skill behavior needs a consuming-agent exercise.

## Use representative data and boundaries

Use real pure logic and local disposable storage where possible. Isolate network, clocks or external services with focused doubles only when needed. Verify arguments, ordering and call counts when those are part of the public boundary contract. Do not assert that a mock works as configured.

Fixtures must represent the fields and failure cases the consumer relies on, including null, missing and malformed values. Do not copy production secrets or personal data. Test concurrent/repeated calls when idempotency or isolation is required.

Keep test-only cleanup in test helpers. Do not remove a legitimate production lifecycle method merely because tests also use it. Clean up only resources the test created.

## Challenge a passing test

In a disposable copy, remove a validation branch or reintroduce the known bug and check that the expected assertion fails. Restore the code and run again. Never mutate production data or unrelated user edits to demonstrate a test.

Use native test runners and assertions. Reuse an already-approved repository harness when compatible; do not add a dependency for convenience. Save the observed command, result and scope so a later completion report distinguishes actual execution from planned checks.
