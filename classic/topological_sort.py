from collections import deque
from typing import List


def topological_sort(graph: List[List[int]]):
    degrees = [0] * len(graph)
    for adj in graph:
        for v in adj:
            degrees[v] += 1

    top_order, queue = [], deque([])
    vertex_count = len(graph)

    for node, degree in enumerate(degrees):
        if degree == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        top_order.append(node)

        for n in graph[node]:
            degrees[n] -= 1
            if degrees[n] == 0:
                queue.append(n)

        vertex_count -= 1

    if vertex_count != 0:
        raise RuntimeError("Only acyclic graphs can be topologically sorted")

    print(vertex_count)
    return top_order


if __name__ == '__main__':
    # graph represented by adj list, each node is uniquely distinguishable by index
    graph = [
        [1, 2],
        [],
        [1, 3],
        [1]
    ]
    print(topological_sort(graph))
