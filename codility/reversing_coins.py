"""
Consider n coins aligned in a row. Each coin is showing heads at the beginning.
Then, n people turn over corresponding coins as follows. Person i reverses coins with numbers
that are multiples of i. That is, person i flips coins i, 2 · i, 3 · i, . . . until no more appropriate
coins remain. The goal is to count the number of coins showing tails.
"""


def reverse_coins(n):
    result = 0
    coins = [0] * (n + 1)  # n + 1 to omit the 0 value easily
    for i in range(1, n + 1):  # here also
        k = i
        while k <= n:
            coins[k] = (coins[k] + 1) % 2
            k += i

        result += coins[i]

    return result
