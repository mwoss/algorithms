"""
README: TODO
"""
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    parent: Optional["TreeNode"] = None
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def find_path(root: Optional[TreeNode], node_a_val: int, node_b_val: int) -> List[str]:
    node_a = find_node(root, node_a_val)
    print(node_a)

    stack, visited = [(node_a, [])], set([])

    while stack:
        node, path = stack.pop()
        visited.add(node.val)

        if node.val == node_b_val:
            return path

        if node.parent and node.parent.val not in visited:
            stack.append((node.parent, [*path, "up"]))
        if node.left and node.left.val not in visited:
            stack.append((node.left, [*path, "left"]))
        if node.right and node.right.val not in visited:
            stack.append((node.right, [*path, "right"]))

    raise Exception(f"Path between node A [{node_a_val}] and node B [{node_b_val}] could not be found in given tree")


def find_node(root: Optional[TreeNode], node_val: int) -> Optional[TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()

        if node.val == node_val:
            return node

        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    return None


if __name__ == '__main__':
    root = TreeNode(10, parent=None)
    node1 = TreeNode(5, parent=root)
    node2 = TreeNode(9, parent=root)
    root.left, root.right = node1, node2
    node3 = TreeNode(20, parent=node1)
    node4 = TreeNode(4, parent=node1)
    node1.left, node1.right = node3, node4
    node5 = TreeNode(1, parent=node2)
    node6 = TreeNode(2, parent=node2)
    node2.left, node2.right = node5, node6
    node7 = TreeNode(7, parent=node3)
    node3.left = node7

    print(find_path(root, 4, 2))
