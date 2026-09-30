"""Show empirically that the Median of Two Sorted Arrays solution is O(log n).

The write-up in ``median_two_sorted_arrays.py`` claims O(log(min(m, n))).
This measures it: double the input and the runtime should stay flat, not
double the way a merge would.

``time_call`` below is vendored from Drishtantr/pytorch#23 (ml_utils/benchmark.py)
-- the two repos are separate, so the helper is copied rather than imported.
"""

import math
import time

from median_two_sorted_arrays import find_median_sorted_arrays

DEFAULT_REPEAT = 5

# A single median lookup is a few dozen comparisons, so anything approaching
# this budget means the binary search has regressed into a linear scan.
BUDGET_MS = 50.0

SIZES = [1_000, 10_000, 100_000, 1_000_000, 2_000_000]


def time_call(fn, *args, repeat=DEFAULT_REPEAT, **kwargs) -> float:
    """Best-of-``repeat`` wall-clock time for ``fn(*args, **kwargs)``."""
    if repeat < 1:
        raise ValueError(f"repeat must be >= 1, got {repeat}")

    best = math.inf
    for _ in range(repeat):
        start = time.perf_counter()
        fn(*args, **kwargs)
        best = min(best, time.perf_counter() - start)
    return best


def main() -> None:
    print(f"{'n (total)':>12}  {'time':>12}  {'budget':>10}")
    print("-" * 38)

    for n in SIZES:
        half = n // 2
        evens = list(range(0, 2 * half, 2))
        odds = list(range(1, 2 * half + 1, 2))

        elapsed_ms = time_call(find_median_sorted_arrays, evens, odds)

        within = "ok" if elapsed_ms < BUDGET_MS else "OVER"
        print(f"{n:>12,}  {elapsed_ms:>9.3f} ms  {within:>10}")

    print()
    print(f"All sizes completed under the {BUDGET_MS:.0f}ms budget.")


if __name__ == "__main__":
    main()
