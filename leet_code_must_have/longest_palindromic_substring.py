"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longest_palindrome(self, s: str) -> str:
        # naive solution O(n^2) time complexity
        start, end = 0, len(s) - 1
        longest = s[0]  # input is at least 1 character long
        while start != len(s) - 1:
            if self._is_palindrome(s, start, end):
                if len(longest) < end - start + 1:
                    longest = s[start:end + 1]

            if start == end:
                start += 1
                end = len(s) - 1
            else:
                end -= 1

        return longest

    def _is_palindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1
        return True


class Solution2:
    def longest_palindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        s_len, longest = len(s), s[0]

        # dp[i][j] states if s[i:j] is a palindrome
        dp = [[False for _ in range(s_len)] for _ in range(s_len)]

        # base case, one character strings are always palindrome
        for i in range(s_len):
            dp[i][i] = True

        for start in range(s_len - 2, -1, -1):  # iterate in range [len(s)-1..0]
            for end in range(start + 1, s_len, 1):
                # if beginning and end of string are the same we can check if inner string is a palindrome
                # or if string is the size of 1 we can simply mark it as palindrome
                if s[start] == s[end] and (dp[start + 1][end - 1] is True or end - start == 1):
                    dp[start][end] = True
                    if len(longest) < end - start + 1:
                        longest = s[start:end + 1]

        return longest


if __name__ == '__main__':
    s = Solution2()
    print(s.longest_palindrome("babda"))
    print(s.longest_palindrome("cbbd"))
