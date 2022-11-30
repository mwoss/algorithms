from typing import List


def missing_number(nums: List[int]) -> int:
    missing = 0
    for idx, num in enumerate(nums):
        missing = missing ^ num
    return missing


if __name__ == '__main__':
    print(missing_number([3, 0, 1]))
    print(missing_number([0, 1]))
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
