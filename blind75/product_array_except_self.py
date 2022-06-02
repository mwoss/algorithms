"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from itertools import accumulate
from math import prod
from operator import mul
from typing import List


def product_except_self_naive(nums: List[int]) -> List[int]:
    answers = []
    for i in range(len(nums)):
        partial_answer = prod(nums[:i] + nums[i + 1:])
        answers.append(partial_answer)
    return answers


def product_except_self(nums: List[int]) -> List[int]:
    n, answer, suffix = len(nums), [1] * len(nums), 1
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]

    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


def product_except_self_2(nums: List[int]) -> List[int]:
    prefixes, suffixes, n = list(accumulate(nums, mul)), list(accumulate(nums[::-1], mul))[::-1], len(nums)
    return [(prefixes[i - 1] if i > 0 else 1) * (suffixes[i + 1] if i + 1 < n else 1) for i in range(n)]


if __name__ == '__main__':
    print(product_except_self_naive([1, 2, 3, 4]))
    print(product_except_self_naive([-1, 1, 0, -3, -3]))

    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([-1, 1, 0, -3, -3]))

    print(product_except_self_2([1, 2, 3, 4]))
    print(product_except_self_2([-1, 1, 0, -3, -3]))
