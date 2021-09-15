# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:
# Input: [1,2,0]
# Output: 3

# Example 2:
# Input: [3,4,-1,1]
# Output: 2

# Example 3:
# Input: [7,8,9,11,12]
# Output: 1

# time complexity and memory complexity
# use cases


# space - O(n)
# time - O(nlogn + n + n) = O(nlong)


from collections import Counter
from typing import List


def best_solution(arr):
    # time complexity - O(N)
    # space complexity - O(N)
    unique = set(arr)
    result = 1

    while result in unique:
        result += 1

    return result


def better_solution(arr):
    postive_arr = [e for e in arr if e > 0]

    counter = Counter(postive_arr)

    # Input: [7,8,9 11,11,12]

    min_e = min(postive_arr)
    max_e = max(postive_arr)
    for val in range(min_e, max_e + 1):
        if val not in counter:
            return val

    if min_e > 1:
        return 1

    return max_e + 1


def find_smallest_positive_integer(arr: List[int]):
    postive_arr = [e for e in arr if e > 0]

    postive_arr.sort()

    postive_unique_arr = get_unique_elem_arr(postive_arr)

    for i, e in enumerate(postive_unique_arr):
        if i + 1 != e:
            return i + 1

    return 1 if len(postive_unique_arr) == 0 else postive_unique_arr[-1] + 1


def get_unique_elem_arr(arr):
    # we know that we operate on sorted arr, with only positive integer

    curr_index = 0
    while curr_index < len(arr) - 1:
        if arr[curr_index] == arr[curr_index + 1]:
            del arr[curr_index]
        else:
            curr_index += 1

    return arr

def test_empty_array_should_return_1():
    arr = []

    result_integer = find_smallest_positive_integer(arr)

    assert result_integer == 1


def test_array_with_all_negative_numbers_should_return_1():
    arr = [-5, -2, -10, -151]

    result_integer = find_smallest_positive_integer(arr)

    assert result_integer == 1


def test_mixed_array_should_return_the_next_smallest_possitive_initeger():
    # Given
    arr1 = [1, 2, 0]
    arr2 = [3, 4, -1, 1]

    # When
    result_integer1 = find_smallest_positive_integer(arr1)
    result_integer2 = find_smallest_positive_integer(arr2)

    # Then
    assert result_integer1 == 3
    assert result_integer2 == 2


def test_big_posotive_integer_array_should_return_smaller_integer():
    arr = [7, 8, 9, 11, 12]

    result_integer = find_smallest_positive_integer(arr)

    assert result_integer == 1


# [2,1,1]
def test_array_with_not_uqniue_integers_should_return_proper_solution():
    # Given
    arr1 = [2, 1, 1]
    arr2 = [-5, -5, -3, 0, 1, 2, 3, 4, 4, 4, 5, 5]

    # When
    result_integer1 = find_smallest_positive_integer(arr1)
    result_integer2 = find_smallest_positive_integer(arr2)

    # Then
    assert result_integer1 == 3
    assert result_integer2 == 6


test_empty_array_should_return_1()
test_array_with_all_negative_numbers_should_return_1()
test_mixed_array_should_return_the_next_smallest_possitive_initeger()
test_big_posotive_integer_array_should_return_smaller_integer()

test_array_with_not_uqniue_integers_should_return_proper_solution()