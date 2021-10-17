"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def largest_number(self, nums: List[int]) -> str:
        self._quick_sort(nums, 0, len(nums) - 1)

        if nums[0] == 0:
            return "0"

        return "".join(str(num) for num in nums)

    def _quick_sort(self, nums: List[int], begin: int, end: int):
        if begin >= end:
            return

        part = self._partition(nums, begin, end)
        self._quick_sort(nums, begin, part - 1)
        self._quick_sort(nums, part + 1, end)

    def _partition(self, nums: List[int], begin: int, end: int) -> int:
        pivot = begin
        while begin < end:
            if self._compare(nums[begin], nums[end]):
                nums[begin], nums[pivot] = nums[pivot], nums[begin]
                pivot += 1
            begin += 1
        nums[end], nums[pivot] = nums[pivot], nums[end]
        return pivot

    def _compare(self, e1: int, e2: int) -> bool:
        return str(e1) + str(e2) > str(e2) + str(e1)


class Solution2:
    def largest_number(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(self._compare))

        if nums[0] == 0:
            return "0"

        return "".join(str(num) for num in nums)

    @staticmethod
    def _compare(e1: int, e2: int) -> int:
        if str(e1) + str(e2) < str(e2) + str(e1):
            return 1
        elif str(e1) + str(e2) > str(e2) + str(e1):
            return -1
        return 0


if __name__ == '__main__':
    s = Solution2()
    print(s.largest_number([10, 2]))
    print(s.largest_number([3, 30, 34, 5, 9]))
