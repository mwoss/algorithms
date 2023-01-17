from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(curr: Optional[Node]) -> Optional[Node]:
    if curr is None:
        return None

    # no repeated edges and no self-loops in the graph

    temp = head = Node(-1, [])

    stack = [curr]
    while stack:
        curr = stack.pop()

        node_copy = Node(curr.val, [])

        head.neighbors.append(node_copy)

        head = node_copy

        if curr.neighbors is not None:
            stack.extend(curr.neighbors)


if __name__ == '__main__':
    pass
