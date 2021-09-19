"""
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.
You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.
Note: The merging process must start from the root nodes of both trees.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None or root2 is None:
            return root1 or root2

        return TreeNode(
            val=root1.val + root2.val,
            left=self.merge_trees(root1.left, root2.left),
            right=self.merge_trees(root1.right, root2.right)
        )


class Solution2:
    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None or root2 is None:
            return root1 or root2

        stack = [(root1, root2)]
        while stack:
            node1, node2 = stack.pop()

            if node2 is None:
                continue

            node1.val += node2.val

            if node1.left is None:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))
            if node1.right is None:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))

        return root1
