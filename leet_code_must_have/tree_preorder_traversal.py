"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value.
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = [root.val]
        for child in root.children:
            result += self.preorder(child)
        return result


class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(reversed(node.children))

        return result
