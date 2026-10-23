export function importRows(existing, rows) {
  const result = [...existing];
  const amountsById = new Map(existing.map(row => [row.id, row.amount]));

  for (const row of rows) {
    if (row === null || typeof row !== 'object' ||
        typeof row.id !== 'string' || row.id.length === 0 ||
        row.id !== row.id.trim() ||
        !Number.isSafeInteger(row.amount) || row.amount <= 0) {
      throw new Error('invalid row');
    }

    if (amountsById.has(row.id)) {
      if (amountsById.get(row.id) !== row.amount) {
        throw new Error('conflicting duplicate id');
      }
      continue;
    }

    amountsById.set(row.id, row.amount);
    result.push({ id: row.id, amount: row.amount });
  }
  return result;
}
