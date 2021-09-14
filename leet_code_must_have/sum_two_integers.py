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
        if b == 0:
            return a
        return self.get_sum(a ^ b, (a & b) << 1)
