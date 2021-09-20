"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
"""
from collections import Counter
from typing import List


class Solution:
    def count_characters(self, words: List[str], chars: str) -> int:
        available_letters = Counter([char for char in chars])
        result = 0
        for word in words:
            word_letters = Counter([char for char in word])
            for letter, occurrence in word_letters.items():
                if letter not in available_letters or available_letters[letter] < occurrence:
                    break
            else:
                result += len(word)

        return result


class Solution2:
    def count_characters(self, words: List[str], chars: str) -> int:
        available_letters = [0] * 26  # number of letters in english alphabet
        for char in chars:
            available_letters[ord(char) - 97] += 1

        result = 0
        for word in words:
            correct, word_letters = True, [0] * 26
            for letter in word:
                idx_letter = ord(letter) - 97
                word_letters[idx_letter] += 1
                if word_letters[idx_letter] > available_letters[idx_letter]:
                    correct = False
                    break

            if correct:
                result += len(word)

        return result


class Solution3:
    def count_characters(self, words: List[str], chars: str) -> int:
        result, available_letters = 0, Counter(chars)

        for word in words:
            word_letters = Counter(word)
            if all(available_letters[letter] >= word_letters[letter] for letter in word_letters):
                result += len(word)

        return result


if __name__ == '__main__':
    s = Solution3()
    print(s.count_characters(["cat", "bt", "hat", "tree"], "atach"))
    print(s.count_characters(["hello", "world", "leetcode"], "welldonehoneyr"))
