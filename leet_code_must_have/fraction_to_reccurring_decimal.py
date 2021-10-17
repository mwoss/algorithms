"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
"""


class Solution:
    def fraction_to_decimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        sign = "" if numerator * denominator >= 0 else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        whole = sign + str(numerator // denominator) + "."

        index, fractional = 0, ""
        numerator = numerator % denominator
        buffer = {numerator: index}

        while numerator % denominator:
            numerator *= 10
            reminder = numerator % denominator
            fractional += str(numerator // denominator)
            if reminder in buffer:
                f = fractional[:buffer[reminder]] + "(" + fractional[buffer[reminder]:] + ")"
                return whole + f
            index += 1
            buffer[reminder] = index
            numerator = reminder

        return whole + fractional


if __name__ == '__main__':
    s = Solution()
    print(s.fraction_to_decimal(2, 3))
    print(s.fraction_to_decimal(1, 5))
    print(s.fraction_to_decimal(4, 333))
