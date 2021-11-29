"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
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

        if 0 > x < len(board) or 0 > y < len(board[0]):
            return

        if board[x][y] == "M":
            return

        mines = self._count_mines_nearby(board, cords)

        if mines == 0:
            board[x][y] = "B"
        else:
            board[x][y] = str(mines)

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


if __name__ == '__main__':
    board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    s = Solution()
    print(s.update_board(board, click))
