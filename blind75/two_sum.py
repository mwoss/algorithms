from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        buffer = {}
        for idx, num in enumerate(nums):
            desire = target - num
            if desire not in buffer:
                buffer[num] = idx
            else:
                return [idx, buffer[desire]]

        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.two_sum([2, 7, 11, 15], 9))
    print(s.two_sum([3, 2, 4], 6))
    print(s.two_sum([3, 3], 6))
