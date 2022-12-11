"""
We have a string that contains 0s and 1s for example 000110101101 (or list).
You can switch places of any 0s and 1s. Find the minimal number of swaps that will result in sorted list/string,
where all 0s are at the beginning and all 1s are at the end.
"""

from collections import Counter
from typing import List


def minimal_swaps_count(nums: List[int]) -> int:
    # assume nums contains 0s and 1s only
    el_count = Counter(nums)
    swap_range = min(el_count[0], el_count[1])
    el_count_swap_range = Counter(nums[:swap_range])
    return min(el_count_swap_range[0], el_count_swap_range[1])


if __name__ == '__main__':
    nums = [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
    print(minimal_swaps_count(nums))
