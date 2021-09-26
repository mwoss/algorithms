"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
from math import factorial
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrace(nums, [], result)
        return result

    def backtrace(self, nums: List[int], permutation: List[int], result: List[List[int]]):
        if len(permutation) == len(nums):
            result.append(permutation[:])
            return

        for num in nums:
            if num in permutation:
                continue
            permutation.append(num)
            self.backtrace(nums, permutation, result)
            permutation.pop()


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for nums in nums:
            curr_permutations = []
            for perm in permutations:
                for i in range(len(perm) + 1):
                    curr_permutations.append(perm[:i] + [nums] + perm[i:])
            permutations = curr_permutations

        return permutations


if __name__ == '__main__':
    s = Solution2()
    print(s.permute([1, 2, 3]))
