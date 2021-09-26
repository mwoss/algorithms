"""
I have a flower pot with a water particle sensor.
When I pour water into it, I want to tell if the water reaches the bottom of the pot.
The sensor provides a 2D grid of 1s and 0s. The 1s represent a solid ground and the 0s represent stones.
In short, given a grid of 1s and 0s determine whether there is a path of 0s from the top to the bottom of the grid.
The path cannot travel diagonally, nor can the water travel back upwards, due to the force of gravity.


[[0, 0, 0]
 [0, 1, 0]
 [0, 0, 0]]

[[0, 0, 0]
 [0, 1, 0]
 [0, 0, 1]]

"""
from typing import List


def is_path_exists(graph: List[List[int]], start: tuple, goal: tuple) -> bool:
    matrix_size = len(graph)
    stack, visited = [start], set()
    while stack:
        cords = stack.pop(0)

        visited.add(cords)

        i, j = cords
        if (i + 1, j) not in visited and i + 1 < matrix_size and graph[i + 1][j] != 1:
            stack.append((i + 1, j))
        if (i, j + 1) not in visited and j + 1 < matrix_size and graph[i][j + 1] != 1:
            stack.append((i, j + 1))

    return goal in visited


if __name__ == '__main__':
    graph = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(is_path_exists(graph, (0, 0), (2, 2)))

    graph2 = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(is_path_exists(graph2, (0, 0), (2, 2)))

    graph3 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    print(is_path_exists(graph3, (0, 0), (2, 2)))

    graph4 = [[0, 0, 0], [0, 1, 0], [0, 1, 0]]
    print(is_path_exists(graph4, (0, 0), (2, 2)))
