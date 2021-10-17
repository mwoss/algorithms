"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""
from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0]),
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self._matrix_dfs(grid, i, j)
                    count += 1

        return count

    def _matrix_dfs(self, grid: List[List[str]], i: int, j: int):
        stack = [(i, j)]

        while stack:
            cord_i, cord_j = stack.pop()

            grid[cord_i][cord_j] = "X"

            if cord_i + 1 < len(grid) and grid[cord_i + 1][cord_j] == "1":
                stack.append((cord_i + 1, cord_j))
            if cord_j + 1 < len(grid[0]) and grid[cord_i][cord_j + 1] == "1":
                stack.append((cord_i, cord_j + 1))
            if cord_i - 1 >= 0 and grid[cord_i - 1][cord_j] == "1":
                stack.append((cord_i - 1, cord_j))
            if cord_j - 1 >= 0 and grid[cord_i][cord_j - 1] == "1":
                stack.append((cord_i, cord_j - 1))


if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(s.num_islands(grid))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(s.num_islands(grid))

    grid = [["1", "0", "1", "1", "0", "1", "1"]]
    print(s.num_islands(grid))
