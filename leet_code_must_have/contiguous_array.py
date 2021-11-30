"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""

from typing import List


class Solution:
    def find_max_length(self, nums: List[int]) -> int:
        for win_len in range(len(nums), 0, -1):
            for offset in range(0, len(nums) - win_len + 1):
                if sum(nums[offset:win_len + offset]) == win_len / 2:
                    return win_len
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.find_max_length([0, 1]))
    print(s.find_max_length([0, 1, 0]))
    print(s.find_max_length([0, 1, 0, 1]))
    print(s.find_max_length([0, 1, 0, 1, 1, 1, 0]))
    print(s.find_max_length([0, 1, 0, 1, 1, 0, 0, 1, 0, 0]))
