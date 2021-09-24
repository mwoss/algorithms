"""
Given an array of numbers , find the index of the smallest array element, for which the sums of all elements
to the let and to the right are equal. The array may not be reordered.
The array is at least 3 element long and the solution always exists.

Examples:
    arr = [1, 2, 3, 4, 6]
    -> the pivot index is 3, because 1+2+3=6
"""
from typing import List


def balanced_sum(arr: List[int]) -> int:
    left_sum, right_sum = arr[0], sum(arr) - arr[0]
    for i in range(1, len(arr)):
        if left_sum == right_sum - arr[i]:
            return i

        left_sum += arr[i]
        right_sum -= arr[i]

    return -1


def balanced_sum2(arr: List[int]) -> int:
    if len(arr) == 3:
        return 1

    left_sum, right_sum = arr[0], arr[-1]
    left_i, right_i = 1, len(arr) - 2
    while left_sum != right_sum:
        if left_sum + arr[left_i] <= right_sum:
            left_sum += arr[left_i]
            left_i += 1
        else:
            right_sum += arr[right_i]
            right_i -= 1

    return left_i


if __name__ == '__main__':
    print(balanced_sum2([1, 2, 3, 4, 6]))
    print(balanced_sum2([6, 4, 3, 2, 1]))
    print(balanced_sum2([1, 2, 1]))
    print(balanced_sum2([1, 2, 3, 3]))
