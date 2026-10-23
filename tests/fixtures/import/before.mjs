export function importRows(existing, rows) {
  for (const row of rows) {
    if (!row.id || !Number.isInteger(row.amount) || row.amount <= 0) {
      throw new Error('invalid row');
    }
    existing.push({ id: row.id, amount: row.amount });
  }
  return existing;
}
