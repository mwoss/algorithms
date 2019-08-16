"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Return its preorder traversal as: [1,3,5,6,2,4].
"""
from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = [root.val]
        for child in root.children:
            result.extend(self.preorder(child))

        return result

    def preorder_iterative(self, root: Node) -> List[int]:
        if root is None:
            return []

        result, stack = [], [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(reversed(node.children))

        return result
