"""
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number,
including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if self.is_self_divide(num):
                result.append(num)

        return result

    def is_self_divide(self, number: int):
        divider = number
        while divider >= 1:
            last_num = divider % 10

            if last_num == 0:
                return False
            if number % last_num != 0:
                return False

            divider -= last_num
            divider /= 10

        return True
