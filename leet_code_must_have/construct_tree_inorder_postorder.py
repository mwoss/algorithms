"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder
is the postorder traversal of the same tree, construct and return the binary tree.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node_inorder_positions = {val: idx for idx, val in enumerate(inorder)}

        def build(low, high):
            if low > high:
                return None

            root = TreeNode(postorder.pop())
            mid = node_inorder_positions[root.val]
            root.right = build(mid + 1, high)
            root.left = build(low, mid - 1)

            return root

        return build(0, len(inorder) - 1)


def inorder_traversal(root: Optional[TreeNode]):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


if __name__ == '__main__':
    s = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    tree = s.build_tree(inorder, postorder)
    inorder_traversal(tree)
