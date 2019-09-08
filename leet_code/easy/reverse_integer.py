"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse_v2(self, x: int) -> int:
        x_sing = self.get_num_sign(x)
        result = x_sing * int(str(abs(x))[::-1])

        return result if -(2 << 30) < result < (2 << 30) - 1 else 0

    def reverse(self, x: int) -> int:
        x_sign = self.get_num_sign(x)
        result = 0

        x *= x_sign  # remove problems with modulo on negative numbers
        while x >= 1:
            digit = x % 10
            x //= 10

            result = result * 10 + digit

        result *= x_sign

        if (x_sign == 1) != (result > 0):
            return 0

        return result

    @staticmethod
    def get_num_sign(x: int) -> int:
        # store sign, true if even, false if odd
        if x > 0:
            return 1
        return -1
