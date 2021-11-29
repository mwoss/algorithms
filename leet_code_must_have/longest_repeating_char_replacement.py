"""
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        frequencies = [0] * 26
        most_freq_letter = 0
        left, max_len = 0, 0

        for right, char in enumerate(s):
            frequencies[ord(char) - 65] += 1
            most_freq_letter = max(most_freq_letter, frequencies[ord(char) - 65])

            letter_to_change = (right - left + 1) - most_freq_letter

            if letter_to_change > k:
                frequencies[ord(s[left]) - 65] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.character_replacement("ABAB", 2))
    print(s.character_replacement("AABABBA", 1))
