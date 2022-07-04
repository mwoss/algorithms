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


def max_product_correct(nums: List[int]) -> int:
    min_prod, max_prod, result = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        temp_min = min(nums[i], min_prod * nums[i], max_prod * nums[i])
        temp_max = max(nums[i], min_prod * nums[i], max_prod * nums[i])
        min_prod, max_prod = temp_min, temp_max
        result = max(result, max_prod)
    return result


if __name__ == '__main__':
    print(max_product_correct([2, 3, -2, 4]))
    print(max_product_correct([-2, 0, -1, ]))
    print(max_product_correct([-2, 0, -1, -5]))
