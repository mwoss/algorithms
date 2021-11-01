"""
Given an integer n, return an array ans of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""
from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ones = bin(i).count("1")
            ans.append(ones)
        return ans


class Solution2:
    def count_bits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ones = self._count_bin_ones(i)
            ans.append(ones)
        return ans

    def _count_bin_ones(self, num: int) -> int:
        ones = 0
        while num != 0:
            if num % 2 == 1:
                ones += 1
            num = num // 2

        return ones


class Solution3:
    def count_bits(self, n: int) -> List[int]:
        ones = [0] * (n + 1)
        for i in range(n + 1):
            if i & 1 == 0:
                ones[i] = ones[i >> 1]
            else:
                ones[i] = ones[i >> 1] + 1
        return ones


if __name__ == '__main__':
    s = Solution3()
    print(s.count_bits(2))
    print(s.count_bits(5))
