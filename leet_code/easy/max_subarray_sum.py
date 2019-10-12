"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""
from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        max_so_far, max_ending = nums[0], nums[0]

        for el in nums:
            max_ending = max(max_ending + el, el)
            max_so_far = max(max_so_far, max_ending)

        return max_so_far

    def max_sub_array_v22(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)
