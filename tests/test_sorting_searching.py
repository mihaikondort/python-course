import random

import pytest

from interview_prep.algorithms.sorting_searching import (
    binary_search,
    kth_largest,
    merge_sort,
    quick_sort,
    search_insert_position,
    search_rotated,
    top_k_frequent,
)


class TestBinarySearch:
    @pytest.mark.parametrize(
        ("nums", "target", "expected"),
        [
            ([1, 3, 5, 7, 9], 5, 2),
            ([1, 3, 5, 7, 9], 1, 0),
            ([1, 3, 5, 7, 9], 9, 4),
            ([1, 3, 5, 7, 9], 4, -1),
            ([], 1, -1),
            ([2], 2, 0),
        ],
    )
    def test_cases(self, nums, target, expected):
        assert binary_search(nums, target) == expected


class TestSearchInsertPosition:
    @pytest.mark.parametrize(
        ("nums", "target", "expected"),
        [([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4), ([1, 3, 5, 6], 0, 0), ([], 5, 0)],
    )
    def test_cases(self, nums, target, expected):
        assert search_insert_position(nums, target) == expected


class TestSearchRotated:
    @pytest.mark.parametrize(
        ("nums", "target", "expected"),
        [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([4, 5, 6, 7, 0, 1, 2], 4, 0),
            ([1, 2, 3, 4, 5], 4, 3),
            ([1], 1, 0),
        ],
    )
    def test_cases(self, nums, target, expected):
        assert search_rotated(nums, target) == expected


@pytest.mark.parametrize("sort_func", [merge_sort, quick_sort])
class TestSorts:
    def test_sorts(self, sort_func):
        assert sort_func([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]

    def test_empty(self, sort_func):
        assert sort_func([]) == []

    def test_already_sorted(self, sort_func):
        assert sort_func([1, 2, 3]) == [1, 2, 3]

    def test_reverse_sorted(self, sort_func):
        assert sort_func([3, 2, 1]) == [1, 2, 3]

    def test_does_not_mutate_input(self, sort_func):
        original = [3, 1, 2]
        sort_func(original)
        assert original == [3, 1, 2]

    def test_random_fuzz(self, sort_func):
        rng = random.Random(1234)
        for _ in range(20):
            data = [rng.randint(-50, 50) for _ in range(rng.randint(0, 60))]
            assert sort_func(data) == sorted(data)


class TestKthLargest:
    def test_basic(self):
        assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_first(self):
        assert kth_largest([3, 2, 1], 1) == 3

    def test_with_duplicates(self):
        assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    @pytest.mark.parametrize("k", [0, 4])
    def test_out_of_range(self, k):
        with pytest.raises(ValueError):
            kth_largest([1, 2, 3], k)


class TestTopKFrequent:
    def test_basic(self):
        assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]

    def test_single(self):
        assert top_k_frequent([1], 1) == [1]

    def test_tie_broken_by_first_appearance(self):
        assert top_k_frequent([3, 3, 1, 1, 2], 2) == [3, 1]
