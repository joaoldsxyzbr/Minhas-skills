import test from 'node:test';
import assert from 'node:assert/strict';
import { importRows } from './import.mjs';

test('returns a new array and preserves both inputs on success', () => {
  const existing = Object.freeze([Object.freeze({ id: 'old', amount: 1 })]);
  const rows = Object.freeze([Object.freeze({ id: 'new', amount: 2 })]);
  const result = importRows(existing, rows);
  assert.deepEqual(result, [{ id: 'old', amount: 1 }, { id: 'new', amount: 2 }]);
  assert.notEqual(result, existing);
  assert.notEqual(result[1], rows[0]);
});

test('empty batch returns a new array with existing entries', () => {
  const existing = [{ id: 'old', amount: 1 }];
  const result = importRows(existing, []);
  assert.deepEqual(result, existing);
  assert.notEqual(result, existing);
  assert.deepEqual(importRows([], []), []);
});

test('matching duplicates are ignored across existing and same-batch rows', () => {
  assert.deepEqual(importRows([{ id: 'old', amount: 1 }], [
    { id: 'old', amount: 1 }, { id: 'new', amount: 2 },
    { id: 'new', amount: 2 }, { id: '__proto__', amount: 3 },
  ]), [{ id: 'old', amount: 1 }, { id: 'new', amount: 2 }, { id: '__proto__', amount: 3 }]);
});

for (const conflictingId of ['old', 'new']) {
  test(`conflicting ${conflictingId} duplicate rejects batch without changes`, () => {
    const existing = [{ id: 'old', amount: 1 }];
    const rows = [{ id: 'new', amount: 2 }, { id: conflictingId, amount: 3 }];
    const before = structuredClone({ existing, rows });
    assert.throws(() => importRows(existing, rows));
    assert.deepEqual({ existing, rows }, before);
  });
}

const invalidRows = [
  null, undefined, {}, { id: '', amount: 1 }, { id: ' ', amount: 1 },
  { id: ' padded', amount: 1 }, { id: 'padded\t', amount: 1 },
  { id: 1, amount: 1 }, { id: true, amount: 1 },
  ...[0, -1, 1.5, NaN, Infinity, Number.MAX_SAFE_INTEGER + 1, '1', 1n]
    .map(amount => ({ id: 'invalid', amount })),
];
for (const [index, invalidRow] of invalidRows.entries()) {
  test(`invalid row case ${index} rejects whole batch without changes`, () => {
    const existing = [{ id: 'old', amount: 1 }];
    const rows = [{ id: 'new', amount: 2 }, invalidRow];
    const before = structuredClone({ existing, rows });
    assert.throws(() => importRows(existing, rows));
    assert.deepEqual({ existing, rows }, before);
  });
}

test('accepts positive safe integer boundaries', () => {
  assert.deepEqual(importRows([], [{ id: 'min', amount: 1 }, { id: 'max', amount: Number.MAX_SAFE_INTEGER }]),
    [{ id: 'min', amount: 1 }, { id: 'max', amount: Number.MAX_SAFE_INTEGER }]);
});
