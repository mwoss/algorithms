from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        number_to_index = {}
        for idx, num in enumerate(nums):
            to_find = target - num
            if to_find in number_to_index:
                return [number_to_index[to_find], idx]
            number_to_index[num] = idx

        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.two_sum([2, 7, 11, 15], 9))
    print(s.two_sum([3, 2, 4], 6))
    print(s.two_sum([3, 3], 6))
