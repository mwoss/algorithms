"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        intervals.sort(key=lambda e: e[0])

        temp_interval = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= temp_interval[1]:
                temp_interval = [temp_interval[0], max(temp_interval[1], end)]
            else:
                result.append(temp_interval)
                temp_interval = intervals[i]

        result.append(temp_interval)

        return result


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Instead of using sorting, the more optimal solution would be to use interval or segment tree.
        Yet, it will require additional space for that, each node has to store (start, end) and max interval (end) value
        """


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 4], [4, 5]]))
