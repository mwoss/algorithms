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

    stack, visited = [(node_a, [])], set([])

    while stack:
        node, path = stack.pop()
        visited.add(node.val)

        if node.val == node_b_val:
            return path

        if node.val not in visited and node.parent:
            stack.append((node.left, [*path, "up"]))
        if node.val not in visited and node.left:
            stack.append((node.left, [*path, "left"]))
        if node.val not in visited and node.right:
            stack.append((node.left, [*path, "right"]))

    raise Exception("Path between node A and node B could not be found in given tree")


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
