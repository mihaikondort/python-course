"""Dynamic programming drills.

For each one, be ready to say out loud: what is the state, what is the
recurrence, what is the base case, and can the table be reduced to O(1) rows.
"""

from collections.abc import Sequence


def fib(n: int) -> int:
    """Return the nth Fibonacci number (``fib(0) == 0``).

    Target: O(n) time, O(1) space. Raise ``ValueError`` for negative ``n``.
    """
    raise NotImplementedError


def climb_stairs(n: int) -> int:
    """Return the number of ways to climb ``n`` stairs taking 1 or 2 steps."""
    raise NotImplementedError


def coin_change(coins: Sequence[int], amount: int) -> int:
    """Return the fewest coins summing to ``amount``, or ``-1`` if impossible.

    Coins may be reused. Target: O(amount * len(coins)).
    """
    raise NotImplementedError


def longest_common_subsequence(a: str, b: str) -> int:
    """Return the length of the longest common subsequence of ``a`` and ``b``.

    Target: O(len(a) * len(b)) time.
    """
    raise NotImplementedError


def longest_increasing_subsequence(nums: Sequence[int]) -> int:
    """Return the length of the longest strictly increasing subsequence.

    Target: O(n log n) with ``bisect`` (the O(n^2) DP is the warm-up).
    """
    raise NotImplementedError


def knapsack(weights: Sequence[int], values: Sequence[int], capacity: int) -> int:
    """Return the maximum value fitting in ``capacity`` (0/1 knapsack).

    Target: O(n * capacity) time, O(capacity) space.
    """
    raise NotImplementedError


def edit_distance(a: str, b: str) -> int:
    """Return the Levenshtein distance between ``a`` and ``b``.

    Insert, delete and substitute each cost 1.
    """
    raise NotImplementedError


def word_break(s: str, words: Sequence[str]) -> bool:
    """Return ``True`` if ``s`` can be segmented into a sequence of ``words``.

    Words may be reused. Target: O(n^2) DP with a set lookup.
    """
    raise NotImplementedError
