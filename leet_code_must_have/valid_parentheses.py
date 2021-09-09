"""
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    parentheses = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    def is_valid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        for p in s:
            if p in self.parentheses:
                stack.append(p)
            elif len(stack) != 0:
                removed_p = stack.pop()
                if p != self.parentheses[removed_p]:
                    return False
            else:
                return False

        if len(stack) != 0:
            return False

        return True
