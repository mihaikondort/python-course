"""Sorting and searching drills.

``list.sort()`` is the right answer in real code; here the point is being able
to write and reason about the algorithms themselves.
"""

from collections.abc import Sequence


def binary_search(nums: Sequence[int], target: int) -> int:
    """Return the index of ``target`` in a sorted list, or ``-1`` if absent.

    Target: O(log n), and watch the ``lo + (hi - lo) // 2`` / loop-bound details.
    """
    raise NotImplementedError


def search_insert_position(nums: Sequence[int], target: int) -> int:
    """Return the index where ``target`` is, or where it would be inserted.

    Equivalent to ``bisect_left``. Target: O(log n).
    """
    raise NotImplementedError


def search_rotated(nums: Sequence[int], target: int) -> int:
    """Search a sorted list rotated at an unknown pivot; return index or ``-1``.

    Values are distinct. Target: O(log n).
    """
    raise NotImplementedError


def merge_sort(nums: Sequence[int]) -> list[int]:
    """Return a new sorted list using merge sort.

    Target: O(n log n) time, stable.
    """
    raise NotImplementedError


def quick_sort(nums: Sequence[int]) -> list[int]:
    """Return a new sorted list using quicksort.

    Be ready to discuss pivot choice and the O(n^2) worst case.
    """
    raise NotImplementedError


def kth_largest(nums: Sequence[int], k: int) -> int:
    """Return the kth largest element (``k == 1`` is the maximum).

    Raise ``ValueError`` if ``k`` is out of range.
    Target: O(n log k) with a heap, or average O(n) with quickselect.
    """
    raise NotImplementedError


def top_k_frequent(nums: Sequence[int], k: int) -> list[int]:
    """Return the ``k`` most frequent values, most frequent first.

    Ties are broken by first appearance in ``nums``.
    """
    raise NotImplementedError
