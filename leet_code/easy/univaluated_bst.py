"""
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Input: [1,1,1,1,1,null,1]
Output: tru
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.right is None and root.left is None:
            return True
        if root.right and root.right.val != root.val:
            return False
        if root.left and root.left.val != root.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

    def isUnivalTree_iterative(self, root: TreeNode) -> bool:
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node:
                stack.append(cur_node.right)
                stack.append(cur_node.left)

                if cur_node.val != root.val:
                    return False

        return True
