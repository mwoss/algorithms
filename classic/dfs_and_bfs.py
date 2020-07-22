def dfs(graph, start):
    # time complexity - O(V+E), O(b^d)
    # space complexity - O(V), O(bd)
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited


def bfs(graph, start):
    # time complexity - O(V+E), O(b^d)
    # space complexity - O(V), O(b^d)
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        unvisited_vertices = graph[vertex] - set(path)
        for uv in unvisited_vertices:
            if uv == goal:
                yield [*path, uv]
            else:
                stack.append((uv, [*path, uv]))


if __name__ == '__main__':
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    print('DFS: ', dfs(graph, 'A'))
    print('BFS: ', bfs(graph, 'A'))

    print('DFS patsh to goal: ', list(dfs_paths(graph, 'A', 'F')))
