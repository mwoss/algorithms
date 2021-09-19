"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence
(i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1],
..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
"""

from typing import List


class Solution:
    def find_length_of_LCIS(self, nums: List[int]) -> int:
        global_max, curr_max = 1, 1
        for i in range(1, len(nums)):  # we know array is at least with 1 element
            if nums[i - 1] < nums[i]:
                curr_max += 1
            else:
                curr_max = 1
            global_max = max(global_max, curr_max)
        return global_max


if __name__ == '__main__':
    s = Solution()
    print(s.find_length_of_LCIS([1, 3, 5, 4, 7]))
    print(s.find_length_of_LCIS([2, 2, 2, 2, 2]))
