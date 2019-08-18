"""
Given an n-ary tree, return the postorder traversal of its nodes' values.
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = [root.val]
        for child in reversed(root.children):
            result = self.postorder(child) + result

        return result

    def postorder_iterative(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result, stack = [], [(root, False)]
        while stack:
            node, flag = stack.pop()
            if flag:
                result.append(node.val)
            else:
                stack.append((node, True))
                if node.children:
                    for child in reversed(node.children):
                        stack.append((child, False))

        return result
