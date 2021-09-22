"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""
from typing import List


class Solution:
    digit_to_letters = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letter_combinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        result = [""]
        for digit in digits:
            current_res = []
            for letter in self.digit_to_letters[digit]:
                for r in result:
                    current_res.append(r + letter)

            result = current_res

        return result


class Solution2:
    digit_to_letters = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letter_combinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        result = []
        combinations = ""
        self.dfs(digits, 0, combinations, result)

        return result

    def dfs(self, digits: str, index: int, combinations: str, result: list):
        if index == len(digits):
            result.append(combinations)
            return

        for letter in self.digit_to_letters[digits[index]]:
            combinations += letter
            self.dfs(digits, index + 1, combinations, result)
            combinations = combinations[:-1]


if __name__ == '__main__':
    s = Solution2()
    print(s.letter_combinations("23"))
    print(s.letter_combinations("2"))
