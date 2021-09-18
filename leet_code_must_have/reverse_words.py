"""
Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.
"""


class Solution:
    def reverse_words(self, s: str) -> str:
        words = s.split(" ")
        return " ".join(word[::-1] for word in words)


if __name__ == '__main__':
    s = Solution()
    print(s.reverse_words("Let's take LeetCode contest"))
