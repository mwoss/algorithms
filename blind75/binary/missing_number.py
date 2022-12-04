from typing import List


def missing_number(nums: List[int]) -> int:
    missing = len(nums)
    for i in range(len(nums)):
        missing = missing ^ i
        missing = missing ^ nums[i]
    return missing


def missing_number_2(nums: List[int]) -> int:
    n = len(nums)  # 0 is not counted
    current_sum = sum(nums)
    full_sum = n * (n + 1) // 2

    return full_sum - current_sum


if __name__ == '__main__':
    print(missing_number([3, 0, 1]))
    print(missing_number([0, 1]))
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))

    print(missing_number_2([3, 0, 1]))
    print(missing_number_2([0, 1]))
    print(missing_number_2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
