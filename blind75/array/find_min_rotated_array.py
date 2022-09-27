from typing import List


def find_min(nums: List[int]) -> int:
    # time complexity: O(n)
    return min(nums)


def find_min_optimized(nums: List[int]) -> int:
    # time complexity: O(lgn)
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[right] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return nums[left]


if __name__ == '__main__':
    print(find_min([3, 4, 5, 1, 2]))
    print(find_min([4, 5, 6, 7, 0, 1, 2]))
    print(find_min([11, 13, 15, 17]))

    print("------------------")

    print(find_min_optimized([3, 4, 5, 1, 2]))
    print(find_min_optimized([4, 5, 6, 7, 0, 1, 2]))
    print(find_min_optimized([11, 13, 15, 17]))
