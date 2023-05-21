from collections import defaultdict
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen_nums = set()

    for num in nums:
        if num in seen_nums:
            return True

        seen_nums.add(num)

    return False


if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
