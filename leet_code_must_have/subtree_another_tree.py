"""
Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself
"""
from hashlib import sha256
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNodeMerkel:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.merkel = None


class Solution:
    def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        # check if subtrees matches (starting from current root node
        if self.is_same(root, sub_root):
            return True

        return self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)

    def is_same(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if root is None or sub is None:
            return root is sub
        return root.val == sub.val and self.is_same(root.left, sub.left) and self.is_same(root.right, sub.right)


class Solution2:
    def is_subtree(self, root: Optional[TreeNodeMerkel], sub_root: Optional[TreeNodeMerkel]) -> bool:
        # Merkel hashing (used by Git itself)
        # https://en.wikipedia.org/wiki/Merkle_tree
        self.merkel(root)
        self.merkel(sub_root)

        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node is not None:
        #         if node.merkel == sub_root.merkel:
        #             return True
        #
        #         stack.append(node.left)
        #         stack.append(node.right)
        #
        # return False

        def dfs(r: Optional[TreeNodeMerkel], t: Optional[TreeNodeMerkel]) -> bool:
            if r is None:
                return False
            return r.merkel == t.merkel or dfs(r.left, t) or dfs(r.right, t)

        return dfs(root, sub_root)

    def merkel(self, node: Optional[TreeNodeMerkel]) -> str:
        if node is None:
            return "$"

        left_node_hash = self.merkel(node.left)
        right_node_hash = self.merkel(node.right)
        node.merkel = self._merkel_hash(left_node_hash + str(node.val) + right_node_hash)

        return node.merkel

    def _merkel_hash(self, val: str) -> str:
        return sha256(val.encode("utf-8")).hexdigest()


class Solution3:
    def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        return self.map_to_str(sub_root) in self.map_to_str(root)

    def map_to_str(self, root: Optional[TreeNode]) -> str:
        # convert tree representation to string (values of nodes)
        if root is None:
            return "$"

        return "^" + str(root.val) + "#" + self.map_to_str(root.left) + self.map_to_str(root.right)
