"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However,
the numeral for four is not IIII. Instead, the number four is written as IV. Because
the one is before the five we subtract it making four. The same principle applies to the number nine,
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


class Solution:
    roman_mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    def roman_to_int(self, s: str) -> int:
        number = 0
        num_len = len(s)
        i = 0
        while i < num_len:
            letter = s[i]
            if letter == "I" or letter == "X" or letter == "C":
                if i < num_len:
                    t = s[i:i + 2]
                    try:
                        number += self.roman_mapping[t]
                        i += 2
                    except KeyError:
                        number += self.roman_mapping[letter]
                        i += 1
            else:
                number += self.roman_mapping[letter]
                i += 1
        return number

    def roman_to_int_2(self, s: str) -> int:
        if len(s) == 1:
            return self.roman_mapping[s]

        i, result = 0, 0
        while i < len(s) - 1:
            first, second = self.roman_mapping[s[i]], self.roman_mapping[s[i + 1]]

            if first < second:
                result += second - first
                i += 2
            else:
                result += first
                i += 1

        result += self.roman_mapping[s[-1]]

        return result


if __name__ == '__main__':
    s = Solution()
    number = s.roman_to_int_2("IV")
    print(number)
