"""
Given the root of a binary tree, invert the tree, and return its root.
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # both left and right have to be called recursively in the same time,
        # otherwise we would lose track of left/right children
        # we could also store data and then pass it to method
        # temp = root.left
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(temp)

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


class SolutionDFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root


class SolutionBFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node is not None:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root

    def invertTreeMoreOptimal(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque([root])
        while stack:
            node = stack.popleft()  # popleft time complexity is O(1)
            if node is not None:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
