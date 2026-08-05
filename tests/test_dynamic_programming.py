import pytest

from interview_prep.algorithms.dynamic_programming import (
    climb_stairs,
    coin_change,
    edit_distance,
    fib,
    knapsack,
    longest_common_subsequence,
    longest_increasing_subsequence,
    word_break,
)


class TestFib:
    @pytest.mark.parametrize(("n", "expected"), [(0, 0), (1, 1), (2, 1), (10, 55), (50, 12586269025)])
    def test_values(self, n, expected):
        assert fib(n) == expected

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            fib(-1)


class TestClimbStairs:
    @pytest.mark.parametrize(("n", "expected"), [(0, 1), (1, 1), (2, 2), (3, 3), (5, 8)])
    def test_values(self, n, expected):
        assert climb_stairs(n) == expected


class TestCoinChange:
    def test_basic(self):
        assert coin_change([1, 2, 5], 11) == 3

    def test_impossible(self):
        assert coin_change([2], 3) == -1

    def test_zero_amount(self):
        assert coin_change([1], 0) == 0

    def test_no_coins(self):
        assert coin_change([], 5) == -1


class TestLongestCommonSubsequence:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0), ("", "abc", 0)],
    )
    def test_cases(self, a, b, expected):
        assert longest_common_subsequence(a, b) == expected


class TestLongestIncreasingSubsequence:
    @pytest.mark.parametrize(
        ("nums", "expected"),
        [
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([0, 1, 0, 3, 2, 3], 4),
            ([7, 7, 7, 7], 1),
            ([], 0),
        ],
    )
    def test_cases(self, nums, expected):
        assert longest_increasing_subsequence(nums) == expected


class TestKnapsack:
    def test_basic(self):
        assert knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9

    def test_nothing_fits(self):
        assert knapsack([10], [100], 5) == 0

    def test_zero_capacity(self):
        assert knapsack([1, 2], [10, 20], 0) == 0


class TestEditDistance:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [("horse", "ros", 3), ("intention", "execution", 5), ("", "abc", 3), ("same", "same", 0)],
    )
    def test_cases(self, a, b, expected):
        assert edit_distance(a, b) == expected


class TestWordBreak:
    def test_segmentable(self):
        assert word_break("leetcode", ["leet", "code"]) is True

    def test_reuses_words(self):
        assert word_break("applepenapple", ["apple", "pen"]) is True

    def test_not_segmentable(self):
        assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False

    def test_empty_string(self):
        assert word_break("", ["a"]) is True
