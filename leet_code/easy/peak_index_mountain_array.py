"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain,
return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        for i in range(0, len(a) - 1):
            if a[i] < a[i + 1] > a[i + 2]:
                return i + 1

        return -1
