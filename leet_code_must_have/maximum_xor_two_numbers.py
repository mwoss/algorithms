"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
"""

from typing import List


class Solution:
    def find_maximum_xor(self, nums: List[int]) -> int:
        max_xor = nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_xor = max(max_xor, nums[i] ^ nums[j])
        return max_xor


class Solution2:
    def find_maximum_xor(self, nums: List[int]) -> int:
        max_xor, mask = 0, 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            found = {mask & num for num in nums}

            start = max_xor | 1 << i
            if any(start ^ prefix in found for prefix in found):
                max_xor = start

        return max_xor


if __name__ == '__main__':
    s = Solution2()
    print(s.find_maximum_xor([3, 10, 5, 25, 2, 8]))
    print(s.find_maximum_xor([0]))
    print(s.find_maximum_xor([2, 4]))
    print(s.find_maximum_xor([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))
