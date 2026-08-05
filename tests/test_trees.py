from interview_prep.algorithms.trees import (
    TreeNode,
    build_tree,
    inorder,
    invert_tree,
    is_valid_bst,
    level_order,
    lowest_common_ancestor,
    max_depth,
)


class TestInorder:
    def test_bst(self):
        assert inorder(build_tree([2, 1, 3])) == [1, 2, 3]

    def test_empty(self):
        assert inorder(None) == []

    def test_right_skewed(self):
        assert inorder(build_tree([1, None, 2, None, 3])) == [1, 2, 3]


class TestLevelOrder:
    def test_full_tree(self):
        assert level_order(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]

    def test_empty(self):
        assert level_order(None) == []

    def test_single(self):
        assert level_order(build_tree([1])) == [[1]]


class TestMaxDepth:
    def test_empty(self):
        assert max_depth(None) == 0

    def test_single(self):
        assert max_depth(build_tree([1])) == 1

    def test_unbalanced(self):
        assert max_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 3


class TestIsValidBst:
    def test_valid(self):
        assert is_valid_bst(build_tree([2, 1, 3])) is True

    def test_invalid_deep_violation(self):
        # 3 is in the right subtree of 5 but smaller than the root.
        assert is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])) is False

    def test_empty_is_valid(self):
        assert is_valid_bst(None) is True

    def test_duplicates_invalid(self):
        assert is_valid_bst(build_tree([2, 2, 3])) is False


class TestLowestCommonAncestor:
    def test_split_children(self):
        root = build_tree([3, 5, 1, 6, 2, 0, 8])
        assert root is not None and root.left is not None and root.right is not None
        lca = lowest_common_ancestor(root, root.left, root.right)
        assert lca is not None and lca.val == 3

    def test_ancestor_is_one_of_the_nodes(self):
        root = build_tree([3, 5, 1, 6, 2])
        assert root is not None and root.left is not None
        p = root.left
        q = root.left.right
        assert q is not None
        lca = lowest_common_ancestor(root, p, q)
        assert lca is not None and lca.val == 5


class TestInvertTree:
    def test_inverts(self):
        root = invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))
        assert level_order(root) == [[4], [7, 2], [9, 6, 3, 1]]

    def test_empty(self):
        assert invert_tree(None) is None

    def test_single(self):
        root = invert_tree(TreeNode(1))
        assert root is not None and root.val == 1
