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

    return temp.neighbors[0]


if __name__ == '__main__':
    graph1 = Node(1, [Node(2), Node(3, [Node(4)])])

    cloned_graph = clone_graph(graph1)

    print(graph1)
    print(cloned_graph)
