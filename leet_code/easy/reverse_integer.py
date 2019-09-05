class Solution:
    def reverse(self, x: int) -> int:
        x_sign = self.get_num_sign(x)
        result = 0

        x *= x_sign  # remove problems with modulo on negative numbers
        while x >= 1:
            digit = x % 10
            x //= 10

            result = result * 10 + digit

        result *= x_sign

        if (x_sign == 1) != (result > 0):
            return 0

        return result

    @staticmethod
    def get_num_sign(x: int) -> int:
        # store sign, true if even, false if odd
        if x > 0:
            return 1
        return -1
