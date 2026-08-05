"""Array and string drills.

Target complexities are stated in each docstring — interviewers care about them
as much as about correctness.
"""

from collections.abc import Sequence


def two_sum(nums: Sequence[int], target: int) -> tuple[int, int] | None:
    """Return the indices of the two numbers adding up to ``target``.

    Return ``None`` if no pair exists. Indices must be distinct and returned in
    ascending order.

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError


def max_subarray_sum(nums: Sequence[int]) -> int:
    """Return the largest sum of any non-empty contiguous subarray (Kadane).

    Raise ``ValueError`` on an empty input.

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def longest_unique_substring(s: str) -> int:
    """Return the length of the longest substring without repeating characters.

    Target: O(n) time, sliding window.
    """
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """Return ``True`` if ``s`` is a palindrome, ignoring case and non-alphanumerics.

    Target: O(n) time, O(1) extra space (two pointers, no cleaned copy).
    """
    raise NotImplementedError


def group_anagrams(words: Sequence[str]) -> list[list[str]]:
    """Group the words into lists of anagrams.

    Groups and the words within them keep their first-seen input order.

    Target: O(n * k log k) time.
    """
    raise NotImplementedError


def product_except_self(nums: Sequence[int]) -> list[int]:
    """Return a list where element i is the product of every element except i.

    Division is not allowed.

    Target: O(n) time, O(1) extra space besides the output.
    """
    raise NotImplementedError


def merge_intervals(intervals: Sequence[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping closed intervals and return them sorted by start.

    Target: O(n log n) time.
    """
    raise NotImplementedError


def rotate_matrix(matrix: list[list[int]]) -> None:
    """Rotate a square matrix 90 degrees clockwise **in place**.

    Target: O(n^2) time, O(1) extra space.
    """
    raise NotImplementedError
