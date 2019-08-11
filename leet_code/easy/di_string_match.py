"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:
Input: "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: "III"
Output: [0,1,2,3]
Example 3:
"""

from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        #         stack = list(range(0, len(S) + 1))
        #         result = []
        #         for mod in S:
        #             if mod == 'I':
        #                 # result.append(stack.pop(0))
        #                 result.append(stack[0])
        #                 del stack[0]
        #             else:
        #                 result.append(stack.pop())
        #         result.extend(stack)  # for the last remaining element
        #         return result

        result = []
        left, right = 0, len(S)

        for mod in S:
            if mod == 'I':
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1

        result.append(left)

        return result
