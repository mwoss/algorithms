"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""


def get_sum(a: int, b: int) -> int:
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


if __name__ == '__main__':
    print(get_sum(2, 3))
