"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        self.rec_helper(root, result)
        return result

    def rec_helper(self, root: Optional[TreeNode], result: List[int]):
        if root:
            self.rec_helper(root.left, result)
            result.append(root.val)
            self.rec_helper(root.right, result)


class Solution2:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        stack, curr = [], root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result


class Solution3:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right) if root else []


if __name__ == '__main__':
    s = Solution3()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(s.inorder_traversal(tree))
