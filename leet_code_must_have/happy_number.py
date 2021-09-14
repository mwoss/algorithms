"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        square_steps = set()
        curr_square = n
        while curr_square != 1:
            curr_square = self.squareSum(curr_square)

            if curr_square in square_steps:
                return False

            square_steps.add(curr_square)

        return True

    def isHappy2(self, n: int) -> bool:
        curr_square = n

        walker = self.squareSum(curr_square)
        runner = self.squareSum(curr_square)
        runner = self.squareSum(runner)

        if runner == 1:
            return True

        while walker != runner:
            walker = self.squareSum(walker)
            runner = self.squareSum(runner)
            runner = self.squareSum(runner)

            if runner == 1:
                return True

        return False

    def squareSum(self, n: int) -> int:
        result = 0
        while n != 0:
            digit = n % 10
            result += digit * digit
            n = n // 10
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy2(19))
    # 19 -> 82 -> 68 -> 100 -> 1
