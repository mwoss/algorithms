"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R inclusive
The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def range_sum_BST(self, root: TreeNode, l: int, r: int) -> int:
        overall_sum = 0

        if l <= root.val <= r:
            overall_sum = overall_sum + root.val

        if root.left and root.val >= l:
            overall_sum = overall_sum + self.range_sum_BST(root.left, l, r)

        if root.right and root.val <= r:
            overall_sum = overall_sum + self.range_sum_BST(root.right, l, r)

        return overall_sum
