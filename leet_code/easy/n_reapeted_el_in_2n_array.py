"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
"""
from typing import List


class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        if len(a) <= 2:
            return a[0]  # we can pick first, whatever xD

        for i in range(0, len(a) - 2):
            if a[i] == a[i + 1] or a[i] == a[i + 2]:
                return a[i]

        return a[-1]
