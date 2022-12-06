from typing import List


def length_of_list(nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)


if __name__ == '__main__':
    print(length_of_list([10, 9, 2, 5, 3, 7, 101, 18]))
    print(length_of_list([0, 1, 0, 3, 2, 3]))
    print(length_of_list([7, 7, 7, 7, 7, 7, 7]))
