"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        valid_par = {'(': ')', '[': ']', '{': '}'}

        stack = []
        for p in s:
            if p in valid_par:
                stack.append(p)
            elif len(stack) == 0 and p not in valid_par:
                return False
            else:
                r_p = stack.pop()
                if valid_par[r_p] != p:
                    return False

        return len(stack) == 0
