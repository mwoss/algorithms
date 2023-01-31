from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None

    # no repeated edges and no self-loops in the graph

    stack = [node]
    cloned = {node.val: Node(node.val, [])}

    while stack:
        curr = stack.pop()
        curr_clone = cloned[curr.val]

        for neighbour in curr.neighbors:
            if neighbour.val not in cloned:
                cloned[neighbour.val] = Node(neighbour.val, [])
                stack.append(neighbour)

            curr_clone.neighbors.append(cloned[neighbour.val])

    return cloned[node.val]


if __name__ == '__main__':
    original_graph = Node(1, [Node(2), Node(3, [Node(4)])])
    cloned_graph = clone_graph(original_graph)
