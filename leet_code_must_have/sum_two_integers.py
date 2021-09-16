"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""


class Solution:
    def get_sum(self, a: int, b: int) -> int:
        """
        we can use only bit operators
        or, and, xor, not, lshift, rshift

        b00000001
        b00000010
        --------
        b00000011
        
        
        b00000010
        b00000011
        --------
        b00000101
        """

        # yup, crazy bit wise operations :<
        while b != 0:
            c = a & b
            a = a ^ b
            b = c << 1
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.get_sum(-1, 1))
