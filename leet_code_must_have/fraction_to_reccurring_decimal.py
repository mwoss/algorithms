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
        result = sign + str(numerator // denominator) + "."
        numerator = numerator % denominator
        i, fraction = 0, ""
        buffer = {numerator: i}
        while numerator % denominator:
            numerator *= 10

            reminder = numerator % denominator
            fraction += str(numerator // denominator)
            if reminder in buffer:
                f = fraction[:buffer[reminder]] + "(" + fraction[buffer[reminder]:] + ")"
                return result + f
            i += 1
            buffer[reminder] = i
            numerator = reminder

        return result + fraction


if __name__ == '__main__':
    s = Solution()
    print(s.fraction_to_decimal(2, 3))
