"""Report which practice solutions are slowest.

``top_k`` below is vendored from Drishtantr/pytorch#25 (ml_utils/ranking.py)
-- the two repos share no package, so it is copied rather than imported.
"""

import contextlib
import io
import sys
import time

from vendor.pytorch_toolkit import top_k

sys.path.insert(0, "old")
with contextlib.redirect_stdout(io.StringIO()):
    import recursion

REPEAT = 200
TOP_N = 3


SOLUTIONS = [
    ("factorial", lambda: recursion.factorial(15)),
    ("sumOfDigits", lambda: recursion.sumOfDigits(987654)),
    ("reverseString", lambda: recursion.reverseString("hello world")),
    ("fibo", lambda: recursion.fibo(18)),
]


def elapsed(fn) -> float:
    """Total seconds to run ``fn`` REPEAT times."""
    start = time.perf_counter()
    for _ in range(REPEAT):
        fn()
    return time.perf_counter() - start


def main() -> None:
    names = [name for name, _ in SOLUTIONS]
    timings = [elapsed(fn) for _, fn in SOLUTIONS]

    ranked = top_k(timings, TOP_N)

    print(f"Slowest {TOP_N} of {len(SOLUTIONS)} solutions ({REPEAT} runs each):\n")
    for position, (index, seconds) in enumerate(ranked, start=1):
        print(f"  {position}. {names[index]:<16} {seconds * 1000:8.3f} ms")

    slowest_index, slowest_seconds = ranked[0]
    print(
        f"\nSlowest solution: {names[slowest_index]} ({slowest_seconds * 1000:.3f} ms)"
    )


if __name__ == "__main__":
    main()
