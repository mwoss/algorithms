"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
"""
from typing import List


class Solution:
    def find_disappeare_numbers(self, nums: List[int]) -> List[int]:
        unique_nums = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in unique_nums:
                result.append(i)
        return result


class Solution2:
    def find_disappeare_numbers(self, nums: List[int]) -> List[int]:
        # as input should only contains numbers in range [1, n]
        # we know that every number should have its corresponding index
        for num in nums:
            num_idx = abs(num) - 1
            nums[num_idx] = -abs(nums[num_idx])

        return [i + 1 for i in range(0, len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    s = Solution2()
    print(s.find_disappeare_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.find_disappeare_numbers([1, 1]))
