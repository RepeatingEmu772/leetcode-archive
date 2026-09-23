# 03 — Payment lifecycle simulator

Implement `solve(data: dict, part: int = 3) -> list[str]` in `solutions/payments.py`.

`data` contains `commands`, a list of whitespace-separated command strings. Return all initialized accounts as `"account_id balance"`, sorted by account ID. Amounts and balances use integer minor units. IDs are case-sensitive nonempty tokens. There are at most 100,000 commands.

Invalid commands have no side effects. This includes unknown verbs or IDs, wrong field counts, invalid numbers, duplicate IDs, and invalid state transitions. Numeric fields contain ASCII digits only, with no signs or decimal points. Extra whitespace is allowed. Initial balances may be zero; payment amounts must be positive. A rejected creation does not reserve its ID.

## Part 1 — Basic lifecycle

| Command | Behavior |
|---|---|
| `ACCOUNT account_id balance` | Create an account; duplicate account IDs are ignored. |
| `CREATE payment_id account_id amount` | Create a payment in NEW state for an existing account. Payment IDs are globally unique. |
| `SUBMIT payment_id` | NEW → PROCESSING. |
| `SETTLE payment_id` | PROCESSING → PAID; credit the account exactly once. |

No other commands are recognized in this stage. Settling a NEW payment is invalid. Repeating SETTLE cannot credit twice.

```json
{"commands": ["ACCOUNT shop 10", "CREATE p1 shop 90", "SUBMIT p1", "SETTLE p1"]}
```

Expected: `["shop 100"]`.

## Part 2 — Changes and refunds

Continue supporting part 1 and add:

| Command | Behavior |
|---|---|
| `UPDATE payment_id amount` | Change amount only in NEW state; amount must be positive. |
| `RETRY payment_id` | PROCESSING → NEW. |
| `REFUND payment_id` | PAID → REFUNDED; subtract the full payment amount exactly once. |

REFUNDED is terminal. No partial refunds. There are no withdrawals or other balance changes, so refunding a properly settled payment cannot make an account balance negative.

Appending `REFUND p1` twice to the example returns `["shop 10"]`.

## Part 3 — Refund deadlines

Every command now starts with a nonnegative integer timestamp:

```text
10 ACCOUNT shop 0 5
11 CREATE p1 shop 100
12 SUBMIT p1
20 SETTLE p1
25 REFUND p1
```

ACCOUNT accepts an optional fourth argument after its balance: a nonnegative refund-window duration. Omitted means unlimited; zero disables refunds, including at settlement time. A positive window permits refunds when `refund_time - settlement_time <= window`. The boundary is inclusive; use successful settlement time, not creation or submission time.

The example returns `["shop 0"]`. Refunding at time 26 instead returns `["shop 100"]`.

Inputs with valid timestamp tokens are guaranteed nondecreasing. Equal timestamps use input order. Missing or invalid timestamps cause the command to be ignored. All other stage-2 rules still apply. The optional refund window is supported only in part 3.
