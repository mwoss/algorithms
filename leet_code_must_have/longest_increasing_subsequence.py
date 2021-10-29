"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing
the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""
from typing import List


class Solution:
    def length_of_LIS(self, nums: List[int]) -> int:
        # lis tells as about longest increasing subsequence starting from index i to the end of the nums list
        lis = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis)


class Solution2:
    def length_of_LIS(self, nums: List[int]) -> int:
        buckets = []
        for num in nums:
            if len(buckets) == 0 or buckets[-1] < num:
                buckets.append(num)
            else:
                idx = self._bisect_left(buckets, num)
                buckets[idx] = num

        return len(buckets)

    def _bisect_left(self, arr: List[int], target: int):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    s = Solution2()
    print(s.length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.length_of_LIS([0, 1, 0, 3, 2, 3]))
    print(s.length_of_LIS([7, 7, 7, 7, 7, 7, 7]))
