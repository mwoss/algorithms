"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position
among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its
adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
representing the number of adjacent mines.
Return the board when no more squares will be revealed.
"""

from typing import List


class Solution:
    def update_board(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click

        if board[x][y] == "M":
            board[x][y] = "X"

        if board[x][y] == "E":
            self._reveal_cells(board, click)

        return board

    def _reveal_cells(self, board: List[List[str]], cords: List[int]):
        x, y = cords

        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != "E":
            return

        if board[x][y] != "E":
            return

        mines = self._count_mines_nearby(board, cords)

        if mines == 0:
            board[x][y] = "B"
        else:
            board[x][y] = str(mines)

        if board[x][y] != "B":
            return

        self._reveal_cells(board, [x + 1, y])
        self._reveal_cells(board, [x - 1, y])
        self._reveal_cells(board, [x, y + 1])
        self._reveal_cells(board, [x, y - 1])
        self._reveal_cells(board, [x + 1, y + 1])
        self._reveal_cells(board, [x - 1, y - 1])
        self._reveal_cells(board, [x - 1, y + 1])
        self._reveal_cells(board, [x + 1, y - 1])

    def _count_mines_nearby(self, board: List[List[str]], cords: List[int]) -> int:
        mines = 0
        x, y = cords
        max_x, max_y = len(board), len(board[0])

        if 0 < x + 1 < max_x and 0 < y < max_y and board[x + 1][y] == "M":
            mines += 1
        if 0 < x - 1 < max_x and 0 < y < max_y and board[x - 1][y] == "M":
            mines += 1
        if 0 < x < max_x and 0 < y + 1 < max_y and board[x][y + 1] == "M":
            mines += 1
        if 0 < x < max_x and 0 < y - 1 < max_y and board[x][y - 1] == "M":
            mines += 1
        if 0 < x + 1 < max_x and 0 < y + 1 < max_y and board[x + 1][y + 1] == "M":
            mines += 1
        if 0 < x - 1 < max_x and 0 < y - 1 < max_y and board[x - 1][y - 1] == "M":
            mines += 1
        if 0 < x - 1 < max_x and 0 < y + 1 < max_y and board[x - 1][y + 1] == "M":
            mines += 1
        if 0 < x + 1 < max_x and 0 < y - 1 < max_y and board[x + 1][y - 1] == "M":
            mines += 1

        return mines


class Solution2:
    def update_board(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click

        if board[x][y] == "M":
            board[x][y] = "X"
        elif board[x][y] == "E":
            self._reveal_cells(board, click)

        return board

    def _reveal_cells(self, board: List[List[str]], cords: List[int]):
        x, y = cords

        if x < 0 or len(board) <= x or y < 0 or len(board[0]) <= y or board[x][y] != "E":
            return

        neighbors = [
            [x + 1, y], [x, y + 1], [x + 1, y + 1], [x - 1, y],
            [x, y - 1], [x - 1, y - 1], [x + 1, y - 1], [x - 1, y + 1]
        ]

        nearby_mines = 0
        for neighbor in neighbors:
            if neighbor[0] < 0 or len(board) <= neighbor[0] or neighbor[1] < 0 or len(board[0]) <= neighbor[1]:
                continue
            if board[neighbor[0]][neighbor[1]] == "M":
                nearby_mines += 1

        board[x][y] = str(nearby_mines) if nearby_mines else "B"

        if board[x][y] != "B":
            return

        for neighbor in neighbors:
            self._reveal_cells(board, neighbor)


if __name__ == '__main__':
    board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    s = Solution2()
    import pprint

    pprint.pprint(s.update_board(board, click))
