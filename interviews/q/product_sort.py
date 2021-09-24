"""
Given an array of n item values, sort that array in ascending order, first by the number of items with
the certain value, then by values themselves.

Examples:
    arr = [4, 5, 6, 5, 4, 3]
    output = [3, 6, 4, 4, 5, 5]
"""
from collections import Counter
from typing import List


def item_sort(arr: List[int]) -> List[int]:
    occurrences = Counter(arr)
    return sorted(arr, key=lambda e: (occurrences[e], e))


if __name__ == '__main__':
    print(item_sort([4, 5, 6, 5, 4, 3]))
