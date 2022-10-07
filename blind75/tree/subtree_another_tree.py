from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    if root is None or sub_root is None:
        return root is sub_root

    if root.val == sub_root.val:
        return _is_same_tree(root, sub_root)

    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


def _is_same_tree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    if root is None or sub_root is None:
        return root is sub_root

    return root.val == sub_root.val and is_subtree(root.left, sub_root.left) and is_subtree(root.right, sub_root.right)


if __name__ == '__main__':
    tree1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subtree1 = TreeNode(4, TreeNode(1), TreeNode(2))
    print(is_subtree(tree1, subtree1))

    tree2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    subtree2 = TreeNode(4, TreeNode(1), TreeNode(2))
    print(is_subtree(tree2, subtree2))
