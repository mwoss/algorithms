"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing
the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""
from typing import List


class Solution:
    def length_of_LIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis)


if __name__ == '__main__':
    s = Solution()
    print(s.length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.length_of_LIS([0, 1, 0, 3, 2, 3]))
    print(s.length_of_LIS([7, 7, 7, 7, 7, 7, 7]))
