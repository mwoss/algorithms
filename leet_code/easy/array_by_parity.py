"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.
You may return any answer array that satisfies this condition.


Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

from typing import List


class Solution:
    def sortArrayByParity(self, a: List[int]) -> List[int]:
        result = [0] * len(a)
        even = 0
        odd = len(a) - 1
        for el in a:
            if el % 2 == 0:
                # result.insert(0, el)
                result[even] = el
                even += 1
            else:
                # result.append(el)
                result[odd] = el
                odd -= 1

        return result
