from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    stack, curr = [], root
    prev = None

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()

        if prev is not None and curr.val <= prev.val:
            return False

        prev = curr
        curr = curr.right

    return True


if __name__ == '__main__':
    tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(is_valid_bst(tree1))

    tree2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(is_valid_bst(tree2))

    tree3 = None
    print(is_valid_bst(tree1))

    tree4 = TreeNode(5, TreeNode(3), TreeNode(6, TreeNode(1), TreeNode(2)))
    print(is_valid_bst(tree2))
