"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.
This is the number of students that must move in order for all students to be standing in non-decreasing order of height

Example 1:
Input: [1,1,4,2,1,3]
Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right positions.
"""

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        not_in_order = 0
        for org, srt in zip(heights, sort_heights):
            if org != srt:
                not_in_order += 1
        return not_in_order
