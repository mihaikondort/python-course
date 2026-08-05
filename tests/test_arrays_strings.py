import pytest

from interview_prep.algorithms.arrays_strings import (
    group_anagrams,
    is_palindrome,
    longest_unique_substring,
    max_subarray_sum,
    merge_intervals,
    product_except_self,
    rotate_matrix,
    two_sum,
)


class TestTwoSum:
    def test_finds_pair(self):
        assert two_sum([2, 7, 11, 15], 9) == (0, 1)

    def test_pair_later_in_list(self):
        assert two_sum([3, 2, 4], 6) == (1, 2)

    def test_duplicates(self):
        assert two_sum([3, 3], 6) == (0, 1)

    def test_negatives(self):
        assert two_sum([-1, -2, -3, -4], -6) == (1, 3)

    def test_no_pair(self):
        assert two_sum([1, 2, 3], 100) is None

    def test_empty(self):
        assert two_sum([], 0) is None

    def test_does_not_reuse_same_index(self):
        assert two_sum([5], 10) is None


class TestMaxSubarraySum:
    def test_mixed(self):
        assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_all_negative(self):
        assert max_subarray_sum([-3, -1, -2]) == -1

    def test_single(self):
        assert max_subarray_sum([7]) == 7

    def test_all_positive(self):
        assert max_subarray_sum([1, 2, 3]) == 6

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            max_subarray_sum([])


class TestLongestUniqueSubstring:
    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ("abcdef", 6),
            ("dvdf", 3),
        ],
    )
    def test_cases(self, text, expected):
        assert longest_unique_substring(text) == expected


class TestIsPalindrome:
    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            ("", True),
            (" ", True),
            ("ab_a", True),
            ("0P", False),
        ],
    )
    def test_cases(self, text, expected):
        assert is_palindrome(text) is expected


class TestGroupAnagrams:
    def test_groups(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert result == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    def test_empty(self):
        assert group_anagrams([]) == []

    def test_single_empty_string(self):
        assert group_anagrams([""]) == [[""]]


class TestProductExceptSelf:
    def test_basic(self):
        assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_with_zero(self):
        assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    def test_two_zeros(self):
        assert product_except_self([0, 0, 3]) == [0, 0, 0]


class TestMergeIntervals:
    def test_overlapping(self):
        assert merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]) == [
            (1, 6),
            (8, 10),
            (15, 18),
        ]

    def test_touching_merge(self):
        assert merge_intervals([(1, 4), (4, 5)]) == [(1, 5)]

    def test_unsorted_input(self):
        assert merge_intervals([(5, 6), (1, 3)]) == [(1, 3), (5, 6)]

    def test_contained(self):
        assert merge_intervals([(1, 10), (2, 3)]) == [(1, 10)]

    def test_empty(self):
        assert merge_intervals([]) == []


class TestRotateMatrix:
    def test_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_matrix(matrix)
        assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    def test_1x1(self):
        matrix = [[1]]
        rotate_matrix(matrix)
        assert matrix == [[1]]

    def test_returns_none_mutates_in_place(self):
        matrix = [[1, 2], [3, 4]]
        assert rotate_matrix(matrix) is None
        assert matrix == [[3, 1], [4, 2]]
