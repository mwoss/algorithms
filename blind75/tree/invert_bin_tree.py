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


def invert_tree_iter(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    stack = [root]
    while stack:
        node = stack.pop()

        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

        tmp = node.left
        node.left = node.right
        node.right = tmp

    return root


def print_tree(root: Optional[TreeNode]):
    if root is None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


if __name__ == '__main__':
    tree1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inv_tree1 = invert_tree(tree1)
    print_tree(inv_tree1)

    print("--------------------")

    tree2 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inv_tree2 = invert_tree_iter(tree2)
    print_tree(inv_tree2)
