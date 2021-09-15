"""
Given a tree with noes and edges that can be colored in two different colors: blue or red, calculate the minimum
amount of propagate_color functions calls to color entire tree with blue color.
Propagate_color function can color all edges from given node up the root node.

Example tree:
     A
   /  \b
  B    C
 / \b   \
D   E    F

Looking at above tree, we know we need at least 2 propagate_color function calls. One from node D, that will color
path D-B-A, and second call from node F, that will color path F-C.

Write a function that will return minimum amount of propagate_color calls on any tree.
Define structures at your own.
"""
from collections import defaultdict
from enum import Enum
from typing import List, Optional


class Colors(Enum):
    RED = 'r'
    BLUE = 'b'


class Tree:
    def __init__(self, value: str, children: List['Tree'], parent_edge: Optional[Colors]):
        self.value = value
        self.children = children or []
        self.parent_edge = parent_edge
        self.parent = None

        for child in self.children:
            child.parent = self


def get_propagate_call_count(root: Tree):
    """
    Time complexity - O(V + V*h) = O(V*h)
    Space complexity - O(V)
    """
    tree_map = defaultdict(list)  # dict for storing vertices per tree (high) level
    max_tree_level = 0

    stack = [(root, 0)]
    while stack:  # DFS with storing each vertex at corresponding tree level
        vertex, level = stack.pop()
        stack.extend([(child, level + 1) for child in vertex.children])  # traverse one level deeper
        tree_map[level].append(vertex)
        max_tree_level = max(max_tree_level, level)

    propagate_call_count = 0
    for level in range(max_tree_level, -1, -1):  # right hand range is exclusive, <max_level, 0>
        for child in tree_map[level]:
            if child.parent_edge == Colors.RED:
                propagate_color(child)  # simulate the propagation
                propagate_call_count += 1

    return propagate_call_count


def propagate_color(node: Tree, color: Colors = Colors.BLUE):
    """
    Time complexity - O(h), high of the tree
    Space complexity - O(1)
    """
    current_node = node
    while current_node.parent is not None:
        current_node.parent_edge = color
        current_node = current_node.parent


def get_propagate_call_count2(root: Tree):
    """
    TODO: to implement
    Better approach would be to store is_propagated flag inside Tree structure.
    Having that info we would not have to propagate colors up to the root node. We would only have to
    set flag on the parent node and in the next iteration do this again.
    """


if __name__ == '__main__':
    subtree1 = Tree('B', [Tree('D', [], Colors.RED), Tree('E', [], Colors.RED)], Colors.RED)
    subtree2 = Tree('B', [Tree('F', [], Colors.RED)], Colors.BLUE)
    tree = Tree('A', [subtree1, subtree2], None)

    count = get_propagate_call_count(tree)

    print(count)
