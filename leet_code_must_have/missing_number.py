from typing import List


def missing_number(nums: List[int]) -> int:
    res = 0
    for i, num in enumerate(nums):
        res ^= i
        res ^= num

    return res ^ len(nums)


if __name__ == '__main__':
    print(missing_number([0, 1, 2, 4]))
