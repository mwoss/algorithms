from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    zero_cells = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_cells.append((i, j))

    for i, j in zero_cells:
        clear_row(i, matrix)
        clear_column(j, matrix)


def clear_row(row: int, matrix: List[List[int]]):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def clear_column(column: int, matrix: List[List[int]]):
    for i in range(len(matrix)):
        matrix[i][column] = 0


if __name__ == '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(matrix)
    print(matrix)
