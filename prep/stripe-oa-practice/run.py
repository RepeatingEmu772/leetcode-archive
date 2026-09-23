"""Run local fixtures: python3 run.py fraud --part 1."""
import argparse
import copy
import importlib
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parent
NAMES = ("fraud", "chargebacks", "payments")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exercise", choices=(*NAMES, "all"))
    parser.add_argument("--part", type=int, choices=(1, 2, 3))
    args = parser.parse_args()
    passed = total = 0
    started = time.perf_counter()
    for name in NAMES if args.exercise == "all" else (args.exercise,):
        cases = json.loads((ROOT / "tests" / (name + ".json")).read_text())
        selected = [c for c in cases if args.part is None or c["part"] == args.part]
        print("\n" + name.upper())
        try:
            solve = importlib.import_module("solutions." + name).solve
        except Exception as exc:
            total += len(selected)
            print(f"  IMPORT ERROR: {type(exc).__name__}: {exc}")
            continue
        for case in selected:
            total += 1
            label = f"part {case['part']} / {case['name']}"
            try:
                actual = solve(copy.deepcopy(case["input"]), part=case["part"])
                if actual == case["expected"]:
                    passed += 1
                    print(f"  PASS {label}")
                else:
                    print(f"  FAIL {label}\n    expected: {case['expected']!r}\n    actual:   {actual!r}")
            except NotImplementedError:
                print(f"  NOT IMPLEMENTED {label}")
            except Exception as exc:
                print(f"  ERROR {label}: {type(exc).__name__}: {exc}")
    print(f"\n{passed}/{total} passed ({time.perf_counter() - started:.3f}s)")
    return 0 if total and passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
