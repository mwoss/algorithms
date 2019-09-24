"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        lh, ln = len(haystack), len(needle)

        if lh < ln:
            return -1

        for i in range(lh - ln):
            if haystack[i:i + ln] == needle:
                return i

        return -1
