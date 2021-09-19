"""
Given an array nums with n integers, your task is to check if it could become
non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1]
holds for every i (0-based) such that (0 <= i <= n - 2).
"""
from typing import List


class Solution:
    def check_possibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        dec = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                dec += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return dec <= 1


if __name__ == '__main__':
    s = Solution()
    print(s.check_possibility([4, 2, 3]))
    print(s.check_possibility([4, 2, 1]))
    print(s.check_possibility([3, 4, 2, 3]))
