# 01 — Merchant fraud monitor

Implement `solve(data: dict, part: int = 3) -> list[str]` in `solutions/fraud.py`.

A marketplace needs a final list of merchants whose observed charges meet a risk threshold.

## Input contract

```json
{
  "merchants": {"m1": "retail", "m2": "travel"},
  "thresholds": {"retail": "0.5", "travel": "2"},
  "min_charges": 2,
  "fraud_codes": ["stolen", "lost"],
  "safe_codes": ["ok"],
  "events": ["CHARGE,c1,m1,stolen", "CHARGE,c2,m1,ok", "DISPUTE,c1"]
}
```

Configuration is always valid: every merchant has a category with a threshold; code sets are disjoint; minimum charge count is a positive integer. IDs and codes are nonempty case-sensitive tokens without commas or whitespace. There are at most 100,000 events. Aim for linear processing plus output sorting.

Events are comma-separated strings. Strip surrounding whitespace from each field. Ignore malformed events, unknown commands, unknown merchants and unrecognized charge codes. A charge needs exactly four fields and a dispute exactly two; IDs must be nonempty.

A valid charge ID is globally unique. The first accepted charge wins; later duplicates have no effect, even if they name another merchant. Rejected charges do not reserve their IDs.

Return qualifying merchant IDs sorted lexicographically. Merchants with fewer than `min_charges` accepted charges never qualify. Evaluate final statistics, not whether a merchant ever crossed the threshold.

## Part 1 — Count thresholds

All thresholds are strings of nonnegative integers, such as `"2"`. A merchant qualifies when its fraud count is **at least** its category threshold and it meets the minimum charge count. Count accepted charges with codes in `fraud_codes` as fraudulent. Ignore DISPUTE events in this stage.

Example: one merchant with threshold `"2"`, minimum 1, and codes `stolen, ok, stolen` qualifies. Expected output: `["m1"]`.

## Part 2 — Ratio thresholds

Continue supporting integer thresholds. A threshold containing a decimal point, such as `"0.5"` or `"1.0"`, is a ratio in [0, 1]. This distinction is based on the string representation: `"1"` means one fraudulent charge; `"1.0"` means 100% fraudulent.

For a ratio threshold, compare fraud count / accepted charge count against the threshold inclusively. Avoid rounding errors at exact boundaries. Ignore disputes in this stage too.

For the input above, part 2 returns `["m1"]`: 1 of 2 charges is fraudulent.

## Part 3 — Disputes

A dispute changes a previously accepted fraudulent charge to non-fraudulent. Total charge count stays unchanged. Repeated disputes, disputes for safe charges, and disputes for unknown charge IDs have no effect. An early dispute is ignored permanently; it is not queued for a future charge.

For the input above, part 3 returns `[]`.

A merchant may become unflagged after disputes. A zero threshold can qualify a merchant with no fraudulent charges, provided the minimum accepted count is met.
