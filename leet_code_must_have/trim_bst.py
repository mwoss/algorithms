"""
Given the root of a binary search tree and the lowest and highest boundaries as low and high,
trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure
of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant).
It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trim_BST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < low:
            return self.trim_BST(root.right, low, high)
        if root.val > high:
            return self.trim_BST(root.left, low, high)

        return TreeNode(
            val=root.val,
            left=self.trim_BST(root.left, low, high),
            right=self.trim_BST(root.right, low, high)
        )
