"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
a node to be a descendant of itself).”
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowest_common_ancestor(self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if root is None or p.val == root.val or q.val == root.val:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root
        if left is None:
            return right
        if right is None:
            return left


class Solution2:
    def lowest_common_ancestor(self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        stack, parents = [root], {root: None}
        while p not in parents and q not in parents:
            node = stack.pop()
            if node.left is not None:
                parents[node.left] = node
                stack.append(node.left)
            if node.right is not None:
                parents[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p is not None:
            ancestors.add(p)
            p = parents[p]
        while q not in ancestors:
            q = parents[q]

        return q


class Solution3:
    def lowest_common_ancestor(self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        path_p = self.find_path(root, p)
        path_q = self.find_path(root, q)

        return self.find_last_common_element(path_p, path_q)

    def find_path(self, start: Optional['TreeNode'], goal: 'TreeNode'):
        stack = [(start, [])]
        while stack:
            node, path = stack.pop()

            if node.val == goal.val:
                return [*path, node]

            if node.left is not None:
                stack.append((node.left, [*path, node]))
            if node.right is not None:
                stack.append((node.right, [*path, node]))

        raise RuntimeError("Goal node was not found in given tree")

    def find_last_common_element(self, path1: List[TreeNode], path2: List[TreeNode]) -> Optional[TreeNode]:
        common_len = min(len(path1), len(path2))
        for i in range(common_len):
            if path1[i] != path2[i] and i != 0:
                return path1[i - 1]
        return None


if __name__ == '__main__':
    s = Solution3()
    tree = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, TreeNode(0), TreeNode(8))
    )
    print(s.lowest_common_ancestor(tree, TreeNode(5), TreeNode(1)).val)
