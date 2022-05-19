from typing import List


def maximum_profit(prices: List[int]):
    high_sum, price_sum = 0, 0
    curr_highest = prices.pop()

    for p in reversed(prices):
        curr_highest = max(p, curr_highest)
        high_sum += curr_highest
        price_sum += p

    return high_sum - price_sum


if __name__ == "__main__":
    print(maximum_profit([3, 5, 4, 3, 6, 8]))
