"""
Imagine being a robber whose goal is to rob houses alongside the street.
From your colleague who observed the street you know the amount of money stored in each house.
Moreover he warned you that houses have security system connected and it will automatically contact
the police if two adjacent houses were broken into on the same night.

Example: [6,5,8,11,18,13]
Solution: 32

Example: [6]
Solution: 6

Example: [6,5,8,18,11,13]
Solution: 33
"""
from typing import List


def find_maximum_robbery_gain(houses: List[int]) -> int:
    """
    Example: [6,5,8,11,18,13]
    [6, 5, 8+6, 11+5 or 11+6, 18+8+6 or 18+5, 13+11+6 or 13+8+6]

    Example: [1, 1, 1, 8000, 1, 1 8000]
    [1, 1, 2, 8000+1 or 8000+1, 1+1 or 1+2, 8000+1+1 or 1+1+1, 8000+8000+1+1 or 8000+1+1+1]
    """
    if len(houses) <= 2:
        return max(houses)

    dp = [0 for _ in range(len(houses))]
    dp[0] = houses[0]
    dp[1] = houses[1]
    dp[2] = houses[0] + houses[2]

    for i in range(3, len(houses)):
        prev_house, prev_prev_house = dp[i - 2], dp[i - 3]
        dp[i] = max(houses[i] + prev_house, houses[i] + prev_prev_house)

    return max(dp[-2], dp[-1])


def find_maximum_robbery_gain_optimized(houses: List[int]) -> int:
    """
    Solution can be optimized (memory). Instead of storing entire DP table, we can just use four
    variables for storing n-3, n-2, n-1 and current index values.
    """


if __name__ == '__main__':
    print(find_maximum_robbery_gain([6, 5, 8, 11, 18, 13]))
    print(find_maximum_robbery_gain([6, 5]))
    print(find_maximum_robbery_gain([6, 5, 8]))
    print(find_maximum_robbery_gain([6, 5, 8, 18, 11, 13]))
