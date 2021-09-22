"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which,
together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""
from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        water = 0

        while start < end:
            water = max(water, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return water


if __name__ == '__main__':
    s = Solution()
    print(s.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
