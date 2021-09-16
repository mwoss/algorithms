"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
from collections import Counter, defaultdict


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t


class Solution2:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = defaultdict(lambda: 0)
        for letter_s, letter_t in zip(s, t):
            counter[letter_s] += 1
            counter[letter_t] -= 1

        for count in counter.values():
            if count != 0:
                return False

        return True


class Solution3:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet = [0] * 26
        for letter_s, letter_t in zip(s, t):
            alphabet[ord(letter_s) - 97] += 1
            alphabet[ord(letter_t) - 97] -= 1

        for count in alphabet:
            if count != 0:
                return False

        return True


if __name__ == '__main__':
    s = Solution3()
    print(s.is_anagram("anagram", "nagaram"))
    print(s.is_anagram("rat", "car"))
