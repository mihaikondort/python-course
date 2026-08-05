"""Binary tree drills."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    """A binary tree node."""

    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Build a tree from a level-order list with ``None`` gaps (helper, implemented)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while queue and index < len(values):
        node = queue.pop(0)
        if index < len(values):
            left = values[index]
            index += 1
            if left is not None:
                node.left = TreeNode(left)
                queue.append(node.left)
        if index < len(values):
            right = values[index]
            index += 1
            if right is not None:
                node.right = TreeNode(right)
                queue.append(node.right)
    return root


def inorder(root: TreeNode | None) -> list[int]:
    """Return the in-order traversal.

    Target: write it *iteratively* with an explicit stack — recursion is the easy
    version and interviewers usually ask for both.
    """
    raise NotImplementedError


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return the values level by level, top to bottom.

    Target: BFS with a queue, O(n) time.
    """
    raise NotImplementedError


def max_depth(root: TreeNode | None) -> int:
    """Return the maximum root-to-leaf depth (an empty tree has depth 0)."""
    raise NotImplementedError


def is_valid_bst(root: TreeNode | None) -> bool:
    """Return ``True`` if the tree is a valid binary search tree (strict ordering).

    Target: O(n) with min/max bounds — checking only parent vs child is the
    classic wrong answer.
    """
    raise NotImplementedError


def lowest_common_ancestor(
    root: TreeNode | None, p: TreeNode, q: TreeNode
) -> TreeNode | None:
    """Return the lowest node that has both ``p`` and ``q`` as descendants.

    Assume both nodes exist in the tree. Target: O(n) single traversal.
    """
    raise NotImplementedError


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Mirror the tree in place and return the root."""
    raise NotImplementedError
