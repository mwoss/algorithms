"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current = 0
        while current < len(nums):
            if nums[current] == val:
                del nums[current]
                current -= 1

            current += 1

        return len(nums)
