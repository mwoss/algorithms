from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    stack = [root]
    prev = None

    while root:
        node = stack.pop()

        if prev is not None and node.left <= prev.left:
            return False

        prev = node

    return True
