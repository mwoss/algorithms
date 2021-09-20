"""
Let's call an array arr a mountain if the following properties hold:

* arr.length >= 3
* There exists some i with 0 < i < arr.length - 1 such that:
    * arr[0] < arr[1] < ... arr[i-1] < arr[i]
    * arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array arr that is guaranteed to be a mountain, return any i such
that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
"""
from typing import List


class Solution:
    def peak_index_in_mountain_array(self, arr: List[int]) -> int:
        peak_idx, peak_val = 0, arr[0]
        for idx, val in enumerate(arr):
            if val > peak_val:
                peak_idx, peak_val = idx, val
        return peak_idx


class Solution2:
    def peak_index_in_mountain_array(self, arr: List[int]) -> int:
        # use modified bin-search
        arr = [0] + arr + [0]  # to easily handle edge cases, when peak is at arr[0] or arr[-1]
        left, mid, right = 0, len(arr) // 2, len(arr) - 1

        while left < right:
            if arr[mid - 1] > arr[mid]:
                right = mid
            if arr[mid + 1] > arr[mid]:
                left = mid
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid - 1 if mid != 1 or len(arr) - 1 else mid

            mid = (left + right) // 2

        return mid


class Solution3:
    def peak_index_in_mountain_array(self, arr: List[int]) -> int:
        # use modified bin-search
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    s = Solution3()
    print(s.peak_index_in_mountain_array([0, 2, 1, 0]))
