"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
"""


def hamming_distance(n: int) -> int:
    return bin(n).count('1')


def hamming_distance_2(n: int) -> int:
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count
