from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def print_tree(root: Optional[TreeNode]):
    if root is None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


if __name__ == '__main__':
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inv_tree = invert_tree(tree)
    print_tree(inv_tree)
