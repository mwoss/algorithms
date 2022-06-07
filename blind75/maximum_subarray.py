from typing import List


def max_subarray(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i - 1] + nums[i])
    return max(nums)


if __name__ == '__main__':
    print(max_subarray([1]))
    print(max_subarray([5, 4, -1, 7, 8]))
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
