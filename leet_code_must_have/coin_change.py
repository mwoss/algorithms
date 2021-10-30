"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for curr_amount in range(amount + 1):
                if curr_amount >= coin:
                    dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)

        if dp[amount] > amount:
            return -1

        return dp[amount]


class Solution2:
    def coin_change(self, coins: List[int], amount: int, memo: dict) -> int:
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0
        if amount < 0:
            return -1

        results = []
        for coin in coins:
            coins_count = self.coin_change(coins, amount - coin, memo)
            if coins_count != -1:
                results.append(coins_count)

        result = min(results) + 1 if results else -1
        memo[result] = result

        return result


if __name__ == '__main__':
    s = Solution()
    print("Bottom-up approach")
    print(s.coin_change([1, 2, 5], 11))
    print(s.coin_change([2], 3))
    print(s.coin_change([1], 0))
    print(s.coin_change([1], 1))

    s2 = Solution2()
    print("Top-down approach")
    print(s2.coin_change([1, 2, 5], 11, {}))
    print(s2.coin_change([2], 3, {}))
    print(s2.coin_change([1], 0, {}))
    print(s2.coin_change([1], 1, {}))
