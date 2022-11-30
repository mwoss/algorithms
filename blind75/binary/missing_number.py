from typing import List


def missing_number(nums: List[int]) -> int:
    missing = len(nums)
    for i in range(len(nums)):
        missing = missing ^ i
        missing = missing ^ nums[i]
    return missing


if __name__ == '__main__':
    print(missing_number([3, 0, 1]))
    print(missing_number([0, 1]))
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
