from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None or q is None:
        return p is q

    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == '__main__':
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(is_same_tree(t1, t2))

    t3 = None
    t4 = None
    print(is_same_tree(t3, t4))

    t5 = TreeNode(1, TreeNode(2), TreeNode(5))
    t6 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(is_same_tree(t5, t6))
