from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # the smallest coin is always 1 and there is only single combination that fulfill this condition
    possibilities = [amount + 1] * (amount + 1)
    possibilities[0] = 0

    for coin in coins:
        for curr_amount in range(amount + 1):
            possibilities[curr_amount] = min(possibilities[curr_amount], possibilities[curr_amount - coin] + 1)

    if possibilities[amount] > amount:
        return -1

    return possibilities[amount]


if __name__ == '__main__':
    print(coin_change([1, 2, 5], 11))
