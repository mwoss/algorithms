"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
"""
from collections import defaultdict
from typing import List, Optional, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_to_nodes = defaultdict(list)
        self._traversal(root, 0, level_to_nodes)
        return list(level_to_nodes.values())

    def _traversal(self, root: Optional[TreeNode], level: int, level_to_nodes: Dict[int, List[int]]) -> None:
        if root:
            level_to_nodes[level].append(root.val)
            self._traversal(root.left, level + 1, level_to_nodes)
            self._traversal(root.right, level + 1, level_to_nodes)


class Solution2:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        stack, result = [(root, 0)], defaultdict(list)
        while stack:
            node, level = stack.pop(0)
            if node is not None:
                result[level].append(node.val)
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))

        return list(result.values())


if __name__ == '__main__':
    s = Solution2()
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.level_order(tree))
