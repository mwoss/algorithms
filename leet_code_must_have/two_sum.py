"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        buffer = {}
        for idx, num in enumerate(nums):
            current = target - num
            if current in buffer:
                return [idx, buffer[current]]
            else:
                buffer[num] = idx
        raise RuntimeError("No solution")
