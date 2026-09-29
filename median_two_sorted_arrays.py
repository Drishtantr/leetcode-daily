"""LeetCode 4 — Median of Two Sorted Arrays (Hard)

Given two sorted arrays ``nums1`` and ``nums2`` of size m and n, return the
median of the combined sorted array. Required complexity: O(log(m + n)).

    Input:  nums1 = [1, 3], nums2 = [2]
    Output: 2.0

    Input:  nums1 = [1, 2], nums2 = [3, 4]
    Output: 2.5   (the merged array is [1, 2, 3, 4], median (2 + 3) / 2)


Approach
--------
Merging both arrays is O(m + n), which the problem forbids. The trick is to
stop thinking about *merging* and think about *partitioning*.

The median splits the combined array into two halves of equal size, where
every element in the left half is <= every element in the right half. So we
don't need the merged array at all — we only need to find where each input
gets cut.

Pick a cut position ``i`` in nums1. That takes ``i`` elements from nums1 into
the left half. Since the left half must hold exactly ``half`` elements, the
cut in nums2 is forced: ``j = half - i``. One unknown, not two.

                 i                        j
    nums1:  ... L1 | R1 ...      nums2: ... L2 | R2 ...
            left half            <->         right half

A cut is correct when both cross-conditions hold::

    L1 <= R2   and   L2 <= R1

(The within-array conditions L1 <= R1 and L2 <= R2 are free — the arrays are
already sorted.)

If ``L1 > R2`` we took too much from nums1, so search left. Otherwise we took
too little, so search right. That is a binary search over ``i``, and because
we binary-search the *smaller* array the bound is O(log(min(m, n))), which is
tighter than the required O(log(m + n)).

Two details make the bookkeeping painless:

- Cuts at the very edge use ±infinity as the missing neighbour, so an empty
  side never needs a special case.
- ``half = (m + n + 1) // 2`` puts the extra element on the left when the
  total is odd, so the odd case is just ``max(L1, L2)`` with no off-by-one.


Complexity
----------
Time   O(log(min(m, n)))  — binary search over the shorter array only.
Space  O(1)               — a handful of indices, nothing allocated.
"""

import math


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """Return the median of two sorted arrays without merging them.

    Raises ``ValueError`` when both arrays are empty, since a median is not
    defined for zero elements.
    """
    # Binary search the shorter array so the loop is O(log(min(m, n))) and
    # j = half - i can never fall outside nums2.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    if total == 0:
        raise ValueError("median is undefined for two empty arrays")

    # Size of the left partition. The +1 parks the odd element on the left.
    half = (total + 1) // 2

    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2  # elements taken from nums1
        j = half - i  # elements taken from nums2, forced by i

        # Neighbours either side of each cut; ±inf when the cut is at an edge.
        left1 = nums1[i - 1] if i > 0 else -math.inf
        right1 = nums1[i] if i < m else math.inf
        left2 = nums2[j - 1] if j > 0 else -math.inf
        right2 = nums2[j] if j < n else math.inf

        if left1 <= right2 and left2 <= right1:
            # Correct partition found.
            if total % 2:
                return float(max(left1, left2))
            return (max(left1, left2) + min(right1, right2)) / 2

        if left1 > right2:
            hi = i - 1  # took too many from nums1
        else:
            lo = i + 1  # took too few from nums1

    # Unreachable for sorted inputs; a fallthrough means the arrays were not
    # actually sorted, which is worth saying out loud rather than returning
    # a wrong number.
    raise ValueError("inputs must each be sorted in non-decreasing order")


if __name__ == "__main__":
    cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([], [2, 3], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([1, 2, 3, 4, 5], [6, 7, 8], 4.5),
        ([-5, -3, -1], [-2, 0], -2.0),
    ]
    for a, b, expected in cases:
        got = find_median_sorted_arrays(a, b)
        status = "ok " if got == expected else "FAIL"
        print(f"{status} median({a}, {b}) = {got}  (expected {expected})")
