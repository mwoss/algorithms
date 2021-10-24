"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
a node to be a descendant of itself).”
"""
from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowest_common_ancestor(self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if root is None or p.val == root.val or q.val == root.val:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root
        if left is None:
            return right
        if right is None:
            return left


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, TreeNode(0), TreeNode(8))
    )
    print(s.lowest_common_ancestor(tree, TreeNode(5), TreeNode(1)).val)
