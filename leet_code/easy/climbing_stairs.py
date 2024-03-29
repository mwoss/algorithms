"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            # we can take only 1 step
            return 1
        if n == 2:
            # we could go step by step (1-1) or do one bigger step (2)
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climb_stairs_v2(self, n: int) -> int:
        # if we figure it out it's just fibonacci, but we start from 1
        a, b = 1, 1

        for _ in range(n):
            a, b = b, a + b

        return a
