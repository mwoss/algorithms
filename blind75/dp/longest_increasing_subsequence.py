from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)


def length_of_lis_optimized(nums: List[int]) -> int:
    subsequence = []
    for num in nums:
        if len(subsequence) == 0 or subsequence[-1] < num:
            subsequence.append(num)
        else:
            idx = bisect_left(subsequence, num)
            subsequence[idx] = num

    return len(subsequence)


if __name__ == '__main__':
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print(length_of_lis([0, 1, 0, 3, 2, 3]))
    print(length_of_lis([7, 7, 7, 7, 7, 7, 7]))

    print(length_of_lis_optimized([10, 9, 2, 5, 3, 7, 101, 18]))
    print(length_of_lis_optimized([0, 1, 0, 3, 2, 3]))
    print(length_of_lis_optimized([7, 7, 7, 7, 7, 7, 7]))
