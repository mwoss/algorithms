"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_idx = self._find_pivot_point(nums)

        self._rotate_arr(nums, 0, pivot_idx - 1)
        self._rotate_arr(nums, pivot_idx, len(nums) - 1)
        self._rotate_arr(nums, 0, len(nums) - 1)

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return (mid + pivot_idx) % len(nums)

        return -1

    def _rotate_arr(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def _find_pivot_point(self, nums: List[int]) -> int:
        pivot = nums[0]
        for idx, num in enumerate(nums):
            if num < pivot:
                return idx
        return 0


if __name__ == '__main__':
    s = Solution()
    # print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    # print(s.search([1], 1))
    print(s.search([3, 1], 3))
