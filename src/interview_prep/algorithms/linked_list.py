"""Singly linked list drills.

``ListNode`` is provided; the helpers below are the exercises.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass


@dataclass
class ListNode:
    """A singly linked list node."""

    val: int
    next: ListNode | None = None

    def __iter__(self) -> Iterator[int]:
        node: ListNode | None = self
        while node is not None:
            yield node.val
            node = node.next


def build_list(values: Iterable[int]) -> ListNode | None:
    """Build a linked list from ``values`` and return its head (helper, implemented)."""
    head: ListNode | None = None
    tail: ListNode | None = None
    for value in values:
        node = ListNode(value)
        if tail is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head: ListNode | None) -> list[int]:
    """Materialise a linked list into a Python list (helper, implemented)."""
    return list(head) if head is not None else []


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse the list in place and return the new head.

    Target: O(n) time, O(1) space, iterative.
    """
    raise NotImplementedError


def merge_sorted_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Merge two ascending sorted lists into one sorted list, reusing the nodes.

    Target: O(n + m) time, O(1) extra space.
    """
    raise NotImplementedError


def has_cycle(head: ListNode | None) -> bool:
    """Return ``True`` if the list contains a cycle (Floyd's tortoise and hare).

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def find_middle(head: ListNode | None) -> ListNode | None:
    """Return the middle node; for even lengths return the second of the two.

    Target: single pass with two pointers.
    """
    raise NotImplementedError


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """Remove the nth node from the end and return the (possibly new) head.

    Raise ``ValueError`` if ``n`` is not in ``1..len``.

    Target: single pass.
    """
    raise NotImplementedError
