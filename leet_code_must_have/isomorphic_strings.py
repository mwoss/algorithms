"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for letter_s, letter_t in zip(s, t):
            if letter_s in s2t and s2t[letter_s] != letter_t:
                return False

            if letter_t in t2s and t2s[letter_t] != letter_s:
                return False

            s2t[letter_s] = letter_t
            t2s[letter_t] = letter_s

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("egg", "ads"))
    print(s.isIsomorphic("badc", "baba"))
    print(s.isIsomorphic("paper", "title"))
