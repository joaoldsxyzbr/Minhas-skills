---
name: test-driven-development
description: "Develop or fix observable behavior with a failing regression test and minimal implementation. Skip prose, pure styling and trivial configuration edits."
---

# Test-Driven Development

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md); read once and reuse for this task.

## Protect existing work

Preserve user code and unrelated edits. Never delete or reset implementation because a test was not written first. If code already exists, add characterization/regression tests and report the actual sequence honestly. Unknown causes require investigation with [systematic-debugging](../systematic-debugging/SKILL.md) first.

## Red, green, refactor

1. Define the user-visible behavior and the realistic defect the test should catch. Read [writing-good-tests.md](writing-good-tests.md) when choosing assertions or doubles.
2. Write the smallest useful test. Run it against the unfixed code and confirm the intended failure, not a missing dependency, typo or broken harness. If it already passes, investigate rather than weakening expectations.
3. Implement the smallest correction within the user's scope.
4. Run the test again and relevant neighboring checks. Refactor only while behavior stays verified.
5. Run required repository gates and checks justified by affected behavior. Do not repeatedly run the whole suite without a remaining risk. Report baseline failures separately; do not repair unrelated failures silently.

Use the project's approved tools. Prefer Node native tests/assertions or Python unittest; do not install a community framework to follow these examples.

## Native JavaScript example

The code under test exports `retryOperation` from `retry.mjs`. This test should fail against an implementation that makes only one attempt; missing imports are a harness problem, not evidence of the retry defect.

```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import { retryOperation } from './retry.mjs';

test('retries transient failure and returns the result on attempt three', async () => {
  let attempts = 0;
  const result = await retryOperation(async () => {
    attempts += 1;
    if (attempts < 3) throw new Error('transient');
    return 'success';
  });
  assert.equal(result, 'success');
  assert.equal(attempts, 3);
});
```

Run `node --test retry.test.mjs`. A matching implementation:

```javascript
export async function retryOperation(operation) {
  for (let attempt = 0; attempt < 3; attempt += 1) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === 2) throw error;
    }
  }
}
```

Also exercise immediate success and final rejection when the real requirement includes both. This example is not a retry policy for payments or non-idempotent writes: retries there require an explicit idempotency contract.

## Exceptions and unavailable tools

Do not add artificial unit tests for prose, formatting or a purely visual edit. Use an appropriate review/render/config check. No extra permission is needed for this proportional choice. If execution is unavailable, provide tests when useful and clearly mark them unrun; do not claim a red-green cycle occurred.
