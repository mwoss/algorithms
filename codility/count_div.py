"""
Write a function:
def solution(A, B, K)
that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3,
because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""


def solution(A, B, K):
    # time complexity O(B-A), way too slow
    divisible_nums = 0
    for i in range(A, B + 1):
        if i % K == 0:
            divisible_nums += 1

    return divisible_nums


def solution2(A, B, K):
    # time complexity, O(1) using prefix sum
    a = A // K  # from 0 to A number divisible by K
    b = B // K  # from 0 to B number divisible by K

    if A % K == 0:  # "A" is inclusive; if divisible by K then
        a -= 1  # remove 1 from "a"

    return b - a


if __name__ == '__main__':
    print(solution(6, 11, 2))
