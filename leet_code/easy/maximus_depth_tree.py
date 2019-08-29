"""
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepthBFS(self, root: 'Node') -> int:
        # BFS Solution
        if root is None:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, height = stack.pop()
            max_depth = max(max_depth, height)

            if node.children:
                for child in node.children:
                    stack.append((child, height + 1))

        return max_depth

    def maxDepthDFS(self, root: 'Node') -> int:
        max_depth = 0

        if root:
            max_depth += 1

        if root and root.children:
            max_depth += max([self.maxDepthDFS(child) for child in root.children])

        return max_depth
