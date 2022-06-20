"""
Given an integer array nums, find a contiguous non-empty subarray within
the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.
"""
from typing import List


def max_product(nums: List[int]) -> int:
    # solution not handle cases with 0 in the input array
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] * nums[i - 1])
    return max(nums)


if __name__ == '__main__':
    print(max_product([2, 3, -2, 4]))
    print(max_product([-2, 0, -1, ]))
    print(max_product([-2, 0, -1, -5]))
