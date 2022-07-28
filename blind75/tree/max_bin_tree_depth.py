from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    result, stack = 1, [(root, 1)]
    while stack:
        node, current_depth = stack.pop()

        if node.left is not None:
            stack.append((node.left, current_depth + 1))
        if node.right is not None:
            stack.append((node.right, current_depth + 1))

        result = max(current_depth, result)

    return result


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_depth(tree))
