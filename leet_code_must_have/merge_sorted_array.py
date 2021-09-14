"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1. To accommodate this, nums1 has a length
of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = sorted(nums1[:m] + nums2)
        for i in range(0, len(res)):
            nums1[i] = res[i]


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        num1_iter, num2_iter = 0, 0

        while num1_iter < m and num2_iter < n:
            if nums1[num1_iter] < nums2[num2_iter]:
                res.append(nums1[num1_iter])
                num1_iter += 1
            else:
                res.append(nums2[num2_iter])
                num2_iter += 1

        if num1_iter < m:
            res.extend(nums1[num1_iter:m])
        else:
            res.extend(nums2[num2_iter:n])

        for i in range(0, len(res)):
            nums1[i] = res[i]


class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Gotcha: Iterate from the end to the beginning, as those array are sorted
        nums1_iter, nums2_iter, res_iter = m - 1, n - 1, m + n - 1

        while nums1_iter >= 0 and nums2_iter >= 0:
            if nums1[nums1_iter] < nums2[nums2_iter]:
                nums1[res_iter] = nums2[nums2_iter]
                nums2_iter -= 1
            else:
                nums1[res_iter] = nums1[nums1_iter]
                nums1_iter -= 1

            res_iter -= 1

        # we need to move nums2 only, as we are returning nums1 and nums1 is already sorted
        while nums2_iter >= 0:
            nums1[res_iter] = nums2[nums2_iter]
            nums2_iter -= 1
            res_iter -= 1


if __name__ == '__main__':
    s = Solution3()
    nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    m, n = 3, 3
    s.merge(nums1, 3, nums2, n)
    print(nums1)

