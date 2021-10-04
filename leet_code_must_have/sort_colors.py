"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
from typing import List


class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, 0
        for color in nums:
            if color == 0:
                red += 1
            elif color == 1:
                white += 1
            else:
                blue += 1

        for i in range(0, red):
            nums[i] = 0
        for i in range(red, red + white):
            nums[i] = 1
        for i in range(red + white, len(nums)):
            nums[i] = 2


class Solution2:
    def sort_colors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


if __name__ == '__main__':
    s = Solution2()
    nums = [1, 2, 0, 2, 1, 1, 0]
    s.sort_colors(nums)
    print(nums)
