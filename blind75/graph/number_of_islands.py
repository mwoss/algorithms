from typing import List, Tuple, Set


def num_islands(grid: List[List[str]]) -> int:
    island_count = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visited:
                island_count += 1
                visited = _propagate(grid, i, j, visited)
    return island_count


def _propagate(grid: List[List[str]], i: int, j: int, visited: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    stack = [(i, j)]
    visited.add((i, j))
    while stack:
        x, y = stack.pop()

        visited.add((x, y))

        if x > 0 and grid[x - 1][y] == "1" and (x - 1, y) not in visited:
            stack.append((x - 1, y))

        if y > 0 and grid[x][y - 1] == "1" and (x, y - 1) not in visited:
            stack.append((x, y - 1))

        if x < len(grid) - 1 and grid[x + 1][y] == "1" and (x + 1, y) not in visited:
            stack.append((x + 1, y))

        if y < len(grid[0]) - 1 and grid[x][y + 1] == "1" and (x, y + 1) not in visited:
            stack.append((x, y + 1))

    return visited


if __name__ == '__main__':
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(num_islands(grid1))

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(num_islands(grid2))
