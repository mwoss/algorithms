"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
return the number of tuples (i, j, k, l) such that:

* 0 <= i, j, k, l < n
* nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""
from collections import Counter
from typing import List


class Solution:
    def four_sum_count(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        for num1 in nums1:
            for num2 in nums2:
                for num3 in nums3:
                    for num4 in nums4:
                        if num1 + num2 + num3 + num4 == 0:
                            count += 1
        return count


class Solution2:
    def four_sum_count(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums_map = Counter()

        for num1 in nums1:
            for num2 in nums2:
                sums_map[num1 + num2] += 1

        count = 0
        for num3 in nums3:
            for num4 in nums4:
                count += sums_map.get(-(num3 + num4), 0)

        return count


if __name__ == '__main__':
    s = Solution2()
    print(s.four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))
    print(s.four_sum_count([0], [0], [0], [0]))
