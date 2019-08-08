"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves,
judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. V
alid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it
finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L"
will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

Example:
Input: "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude,
 so it ended up at the origin where it started. Therefore, we return true.
"""


class Solution:
    def judgeCznaczyircle(self, moves: str) -> bool:
        possitions = {
            'U': (1, 0),
            'D': (-1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

        x, y = 0, 0

        for move in moves:
            ch_m = possitions[move]
            x += ch_m[0]
            y += ch_m[1]

        return x == 0 and y == 0