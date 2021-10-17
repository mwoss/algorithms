"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def largest_number(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        self._quick_sort(str_nums, 0, len(nums) - 1)

        if nums[0] == 0:
            return "0"

        return "".join(str_nums)

    def _quick_sort(self, nums: List[str], begin: int, end: int):
        if begin >= end:
            return

        part = self._partition(nums, begin, end)
        self._quick_sort(nums, begin, part - 1)
        self._quick_sort(nums, part + 1, end)

    def _partition(self, nums: List[str], begin: int, end: int) -> int:
        pivot = begin

        # while begin < end:
        #     if self._compare(nums[begin], nums[end]):
        #         nums[begin], nums[pivot] = nums[pivot], nums[begin]
        #         pivot += 1
        #     begin += 1
        # nums[end], nums[pivot] = nums[pivot], nums[end]

        for i in range(begin + 1, end + 1):
            if self._compare(nums[i], nums[pivot]):
                pivot += 1
                nums[i], nums[pivot] = nums[pivot], nums[i]

        nums[pivot], nums[begin] = nums[begin], nums[pivot]

        return pivot

    def _compare(self, e1: str, e2: str) -> bool:
        return e1 + e2 > e2 + e1


class Solution2:
    def largest_number(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        str_nums.sort(key=cmp_to_key(self._compare))

        if str_nums[0] == "0":
            return "0"

        return "".join(str_nums)

    @staticmethod
    def _compare(e1: str, e2: str) -> int:
        if e1 + e2 < e2 + e1:
            return 1
        elif e1 + e2 > e2 + e1:
            return -1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.largest_number([10, 2]))
    print(s.largest_number([3, 30, 34, 5, 9]))
