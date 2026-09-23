# Stripe-style OA practice — Python

Three language-agnostic exercises, provided with Python 3.9+ starter files and a local test runner. No external dependencies.

These are **original practice reconstructions**, not official Stripe questions or exact copies of an assessment. Public candidate reports informed the themes; all detailed rules, examples, and tests here define this practice set only. No solutions are included.

## Start in VS Code

1. Open this folder in VS Code (File → Open Folder).
2. Install/select Python 3.9 or later. The Microsoft Python extension is optional but useful.
3. Open the integrated terminal and run:

```sh
python3 run.py fraud --part 1
```

On Windows, use `py` instead of `python3` if needed.

Read `problems/01_fraud.md`, then edit `solutions/fraud.py`. Keep the function name and arguments. Return the answer; do not print it. The initial NOT IMPLEMENTED results are expected.

```sh
python3 run.py fraud --part 2
python3 run.py fraud --part 3
python3 run.py chargebacks --part 1
python3 run.py payments --part 1
python3 run.py all
```

`--part N` runs that stage only; omit it to run all three stages. A single implementation must support all stages through the `part` argument. Fixtures are readable JSON under `tests/`; add objects in the same format to add your own tests.

## Suggested order

| Exercise | Main skills | Suggested timer |
|---|---|---|
| 01 Merchant fraud | Maps, aggregation, reversible events | 60 minutes |
| 02 Chargeback files | CSV, validation, chronological updates | 60 minutes |
| 03 Payment lifecycle | Command parsing, state transitions, time limits | 60 minutes |

Spend roughly 5 minutes reading, 40 implementing, and 15 checking edge cases. Read all stages before coding. Tests are useful coverage, not a guarantee that every possible input is covered.

## Debugging

With the Python extension installed, select **Run and Debug → Practice current exercise** and press F5. Choose an exercise and stage when prompted. Set breakpoints in its solution file. Terminal tasks are also available under **Terminal → Run Task**.

## Files

- `problems/`: complete specifications and examples.
- `solutions/`: your three starter functions.
- `tests/`: named test cases with expected answers (contains spoilers about edge cases).
- `run.py`: readable test runner with failure diffs and a nonzero exit code on failure.
- `SOURCES.md`: provenance and reconstruction notes.
