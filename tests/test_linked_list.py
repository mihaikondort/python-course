import pytest

from interview_prep.algorithms.linked_list import (
    ListNode,
    build_list,
    find_middle,
    has_cycle,
    merge_sorted_lists,
    remove_nth_from_end,
    reverse_list,
    to_list,
)


class TestReverseList:
    def test_multiple(self):
        assert to_list(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]

    def test_single(self):
        assert to_list(reverse_list(build_list([1]))) == [1]

    def test_empty(self):
        assert reverse_list(None) is None


class TestMergeSortedLists:
    def test_interleaved(self):
        merged = merge_sorted_lists(build_list([1, 3, 5]), build_list([2, 4, 6]))
        assert to_list(merged) == [1, 2, 3, 4, 5, 6]

    def test_one_empty(self):
        assert to_list(merge_sorted_lists(None, build_list([1, 2]))) == [1, 2]

    def test_both_empty(self):
        assert merge_sorted_lists(None, None) is None

    def test_duplicates(self):
        merged = merge_sorted_lists(build_list([1, 1]), build_list([1]))
        assert to_list(merged) == [1, 1, 1]


class TestHasCycle:
    def test_no_cycle(self):
        assert has_cycle(build_list([1, 2, 3])) is False

    def test_empty(self):
        assert has_cycle(None) is False

    def test_cycle(self):
        head = build_list([1, 2, 3, 4])
        assert head is not None
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = head.next
        assert has_cycle(head) is True

    def test_self_loop(self):
        node = ListNode(1)
        node.next = node
        assert has_cycle(node) is True


class TestFindMiddle:
    def test_odd_length(self):
        node = find_middle(build_list([1, 2, 3, 4, 5]))
        assert node is not None and node.val == 3

    def test_even_length_returns_second(self):
        node = find_middle(build_list([1, 2, 3, 4]))
        assert node is not None and node.val == 3

    def test_empty(self):
        assert find_middle(None) is None


class TestRemoveNthFromEnd:
    def test_middle(self):
        assert to_list(remove_nth_from_end(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]

    def test_head(self):
        assert to_list(remove_nth_from_end(build_list([1, 2]), 2)) == [2]

    def test_only_element(self):
        assert remove_nth_from_end(build_list([1]), 1) is None

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            remove_nth_from_end(build_list([1, 2]), 5)

    def test_zero(self):
        with pytest.raises(ValueError):
            remove_nth_from_end(build_list([1, 2]), 0)
