from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        max_profit, curr_min = 0, prices[0]
        for price in prices:
            if curr_min > price:
                curr_min = price

            max_profit = max(max_profit, price - curr_min)

        return max_profit


if __name__ == '__main__':
    s = Solution()
    print(s.max_profit([7, 1, 5, 3, 6, 4]))
    print(s.max_profit([7, 6, 4, 3, 1]))
