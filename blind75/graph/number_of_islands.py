from typing import List, Tuple, Set

Grid = List[List[str]]
VisitedCells = Set[Tuple[int, int]]


def num_islands(grid: Grid) -> int:
    island_count = 0
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visited:
                island_count += 1
                visited = _propagate(grid, i, j, visited)

    return island_count


def _propagate(grid: Grid, start_x: int, start_y: int, visited: VisitedCells) -> VisitedCells:
    stack = [(start_x, start_y)]

    visited.add((start_x, start_y))

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


def num_islands_mutate(grid: Grid) -> int:
    # cells marked with hash (#) are treated as already visited
    island_count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                island_count += 1
                _propagate_mutate(grid, i, j)

    return island_count


def _propagate_mutate(grid: Grid, start_x: int, start_y: int) -> None:
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack.pop()

        grid[x][y] = "#"

        if x > 0 and grid[x - 1][y] == "1":
            stack.append((x - 1, y))

        if y > 0 and grid[x][y - 1] == "1":
            stack.append((x, y - 1))

        if x < len(grid) - 1 and grid[x + 1][y] == "1":
            stack.append((x + 1, y))

        if y < len(grid[0]) - 1 and grid[x][y + 1] == "1":
            stack.append((x, y + 1))


if __name__ == '__main__':
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(num_islands(grid1))
    print(num_islands(grid2))

    grid1_mut = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    grid2_mut = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "1"],
        ["1", "0", "0", "1", "1"]
    ]
    print(num_islands_mutate(grid1_mut))
    print(num_islands_mutate(grid2_mut))
