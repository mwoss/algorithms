"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value.
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        for child in root.children:
            result += self.postorder(child)
        result.append(root.val)
        return result


class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack, result = [(root, False)], []
        while stack:
            node, flag = stack.pop()
            if flag:
                result.append(node.val)
            else:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))

        return result
