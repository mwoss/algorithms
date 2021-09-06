"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = {n: idx for idx, n in enumerate(nums)}
        for idx, num in enumerate(nums):
            current = target - num
            if current in indexed and idx != indexed[current]:
                return [idx, indexed[current]]
        raise RuntimeError
