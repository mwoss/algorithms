"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""
from collections import Counter
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max(c, key=c.get)

    def majority_element_optimal(self, nums: List[int]) -> int:
        # Boyer-Moore Majority Vote Algorithm
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    n = [2, 2, 1, 1, 1, 2, 2]
    s = Solution()
    print(s.majority_element(n))
