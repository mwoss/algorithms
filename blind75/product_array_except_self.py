"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List
from math import prod


def product_except_self(nums: List[int]) -> List[int]:
    answers = []
    for i in range(len(nums)):
        partial_answer = prod(nums[:i] + nums[i + 1:])
        answers.append(partial_answer)
    return answers


if __name__ == '__main__':
    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([-1, 1, 0, -3, -3]))
