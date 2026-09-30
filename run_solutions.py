"""Run each practice solution against its example cases and report a pass rate.

``pass_rate`` below is vendored from Drishtantr/pytorch#24
(ml_utils/scoring.py) -- the two repos share no package, so it is copied
rather than imported.
"""

import contextlib
import io
import sys

# Importing old/recursion.py runs its demo prints at module scope, so the
# import is done with stdout muted.
sys.path.insert(0, "old")
with contextlib.redirect_stdout(io.StringIO()):
    import recursion

MIN_PASS_RATE = 0.9


def pass_rate(passed: int, total: int) -> float:
    """Share of cases that passed, as a percentage from 0 to 100."""
    if total <= 0:
        raise ValueError(f"total must be positive, got {total}")
    if passed < 0:
        raise ValueError(f"passed must be non-negative, got {passed}")
    if passed > total:
        raise ValueError(f"passed ({passed}) cannot exceed total ({total})")

    return 100.0 * passed / total


def _printed(fn, *args):
    """Capture what ``fn`` prints, for the solutions that print rather than return."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*args)
    return buf.getvalue().split()


CASES = [
    ("factorial", lambda: recursion.factorial(5) == 120),
    ("sumOfDigits", lambda: recursion.sumOfDigits(214) == 7),
    (
        "printNumbers",
        lambda: _printed(recursion.printNumbers, 5) == ["1", "2", "3", "4", "5"],
    ),
    ("reverseString", lambda: recursion.reverseString("hello") == "olleh"),
    ("fibo", lambda: recursion.fibo(7) == 13),
    ("palin", lambda: recursion.palin("radar") is True),
]


def main() -> int:
    passed = 0
    for name, check in CASES:
        try:
            ok = bool(check())
        except Exception:
            ok = False
        passed += ok
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")

    rate = pass_rate(passed, len(CASES))
    print(f"\n{passed}/{len(CASES)} cases passed ({rate:.1f}%)")

    if rate < MIN_PASS_RATE:
        print(f"below the {MIN_PASS_RATE} floor")
        return 1

    print("pass rate is within budget")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
