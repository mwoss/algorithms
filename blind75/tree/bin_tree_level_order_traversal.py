from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    result, stack = defaultdict(list), [(0, root)]

    while stack:
        level, node = stack.pop()

        if node.left:
            stack.append((level + 1, node.left))
        if node.right:
            stack.append((level + 1, node.right))

        result[level].append(node.val)

    return list(result.values())


if __name__ == '__main__':
    tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(level_order(tree1))

    tree2 = TreeNode(1)
    print(level_order(tree2))

    tree3 = None
    print(level_order(tree3))
