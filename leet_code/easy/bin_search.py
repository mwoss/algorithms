"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1
"""

from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = int((l + r) / 2)

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1

        return l


if __name__ == '__main__':
    x = Solution()
    res = x.search_insert([1,3,5,6], 2)
    print(res)