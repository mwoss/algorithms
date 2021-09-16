"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the
two subtrees of every node never differs by more than one.
"""
from typing import List, Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        # slicing is expensive, thus this approach have O(nlgn) time complexity and O(n) space complexity
        if not nums:
            return None

        middle_node_idx = len(nums) // 2
        return TreeNode(
            val=nums[middle_node_idx],
            left=self.sorted_array_to_bst(nums[:middle_node_idx]),
            right=self.sorted_array_to_bst(nums[middle_node_idx + 1:])
        )


class Solution(object):
    def sorted_array_to_bst_optimal(self, nums: List[int]) -> Optional[TreeNode]:
        # more optimal solution as we avoid slicing
        # O(n) time complexity, O(lgn) space complexity
        return self.helper(nums, 0, len(nums))

    def helper(self, nums: List[int], lower: int, upper: int) -> Optional[TreeNode]:
        if lower == upper:
            return None

        middle_node_idx = (lower + upper) // 2
        return TreeNode(
            val=nums[middle_node_idx],
            left=self.helper(nums, lower, middle_node_idx),
            right=self.helper(nums, middle_node_idx + 1, upper)
        )
