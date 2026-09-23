# 02 — Chargeback file processor

Implement `solve(data: dict, part: int = 3) -> list[str]` in `solutions/chargebacks.py`.

## Input contract

`data` has a `files` list. Each file contains `network`, `date` (valid ISO YYYY-MM-DD), and `contents` (a CSV string). Metadata is always valid. Networks are nonempty tokens without commas. Files may arrive out of order.

CSV header is exactly:

```text
transaction_id,merchant_id,amount,currency,reason
```

Each physical data line is one CSV record. Quoted fields and commas inside quotes are allowed; embedded newlines are not. Strip whitespace surrounding each parsed field, skip blank lines, and process each line independently so a malformed line cannot consume later rows. Use standard CSV quoting rules; an unterminated quoted field is invalid. File contents always include the valid header.

## Part 1 — Parse valid rows

All data rows are valid in this stage. Reasons are `fraud` or `duplicate`.

Emit one string per record:

```text
network,transaction_id,merchant_id,amount,currency,reason
```

Amount is an integer in minor currency units, normalized without leading zeros. Do not convert currency or divide by 100. Sort by `(network, transaction_id)` using case-sensitive string order. Treat `(network, transaction_id)` as the record key; the same ID in different networks is independent. Duplicate keys will not occur in parts 1 or 2.

Example input:

```json
{"files": [{"network": "visa", "date": "2026-01-01", "contents": "transaction_id,merchant_id,amount,currency,reason\nt2,m2,0200,USD,fraud\nt1,m1,50,JPY,duplicate"}]}
```

Expected:

```json
["visa,t1,m1,50,JPY,duplicate", "visa,t2,m2,200,USD,fraud"]
```

## Part 2 — Validate

Ignore individual invalid rows and keep processing. A row is valid only if:

- It is well-formed CSV with exactly five fields.
- Transaction and merchant IDs are nonempty and contain only ASCII letters, digits, `_` or `-`.
- Amount consists only of ASCII digits, with numeric value greater than zero. Leading zeros are allowed; signs, decimals and exponent notation are not.
- Currency is exactly `USD`, `EUR` or `JPY`.
- Reason is exactly `fraud` or `duplicate`.

All comparisons are case-sensitive. At most 100,000 rows total; amounts have at most 12 characters before validation.

## Part 3 — Chronology and withdrawals

Also accept reason `withdrawn`, with the same validation rules (including positive amount). Process files by ascending date; ties follow original file-list order. Rows within each file retain their order.

A valid fraud/duplicate row creates or replaces the record for its key. A valid withdrawn row removes any current record for its key; an unknown-key withdrawal is a no-op. A subsequent non-withdrawn row can reopen the key. Invalid rows never replace or remove records. Only network and transaction ID determine withdrawal identity; merchant, amount and currency need not match the current record.

Return remaining records in the same normalized, sorted format. A withdrawal row itself is never emitted.

Example: visa/t1 is filed on Jan 1 and withdrawn on Jan 3. The result is `[]`, even if the Jan 3 file appears first in the input list.
