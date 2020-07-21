"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n^2) time complexity
        longest_substrng = 0
        for i in range(len(s)):
            characters = set()
            current_len = 0
            for j in range(i, len(s)):
                if s[j] in characters:
                    break
                characters.add(s[j])
                current_len += 1

            if current_len > longest_substrng:
                longest_substrng = current_len

        return longest_substrng


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        used_chars = {}  # store index of last occurrence of given char
        for index, char in enumerate(s):
            # Every time we met a new char, we check have we met it before
            if char in used_chars and start <= used_chars[char]:
                # if we have met. we get that position + 1
                start = used_chars[char] + 1
            else:
                # if char is not in used_chars map we can update max_length
                max_length = max(max_length, index - start + 1)  # sometimes we are not moving at all

            used_chars[char] = index  # update the used_chars map with current char at given index

        return max_length
