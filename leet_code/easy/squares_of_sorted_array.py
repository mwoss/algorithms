"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""

from typing import List


class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        odd, even = self.split_array(a)
        even.reverse()  # we need ascending queue

        result = []
        while odd and even:
            if abs(odd[-1]) >= even[-1]:
                value = even.pop()
                result.append(value * value)
            else:
                value = odd.pop()
                result.append(value * value)

        result.extend([el * el for el in odd[::-1]])
        result.extend([el * el for el in even[::-1]])
        return result

    def split_array(self, A: List[int]) -> tuple:
        for i in range(0, len(A)):
            if A[i] >= 0:
                return A[:i], A[i:]

        return A, []
