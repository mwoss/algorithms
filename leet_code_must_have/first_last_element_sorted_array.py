"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        start = -1
        for idx, num in enumerate(nums):
            if num == target and start == -1:
                start = idx
            if num != target and start != -1:
                return [start, idx - 1]

        if start != -1:
            return [start, len(nums) - 1]

        return [-1, -1]


class Solution2:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, 1]

        result = [-1, -1]

        # this bin-search is shifted towards left side
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2  # this value is always rounded towards smaller integer
            if nums[mid] < target:
                left = mid + 1  # move left side
            else:
                right = mid

        if nums[left] != target:
            return result

        result[0] = left

        # and this bin-search is shifted towards right side
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1  # this value is always rounded towards bigger integer
            if nums[mid] > target:
                right = mid - 1  # move right side
            else:
                left = mid

        result[1] = right

        return result


if __name__ == '__main__':
    s = Solution2()
    print(s.search_range([5, 7, 7, 8, 8, 10], 8))
    print(s.search_range([5, 7, 7, 8, 8, 10], 6))
    print(s.search_range([], 6))
    print(s.search_range([1], 1))
    print(s.search_range([2, 2], 2))
