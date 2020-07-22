"""
An integer M and a non-empty array A consisting of N non-negative integers are given.
All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements
A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers.
That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:
def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].
"""


def solution(M, A):
    slice_len = 0
    used_ints = set()
    slice_sum = 0

    for value in A:
        if slice_sum >= 1000000000:
            return 1000000000

        if value in used_ints:
            slice_sum += slice_len * (slice_len + 1) // 2
            slice_len = 1
            used_ints.clear()
        else:
            slice_len += 1
            used_ints.add(value)

    slice_sum += slice_len * (slice_len + 1) // 2

    return min(slice_sum, 1000000000)


def solution2(M, A):
    seen_nums = [False] * (M + 1)  # from 0 to M
    left = right = 0
    slice_count = 0

    while left < len(A) and right < len(A):
        if seen_nums[A[right]] is False:
            # case: distinct elements
            slice_count += (right - left + 1)

            if slice_count >= 1000000000:
                return 1000000000

            seen_nums[A[right]] = True
            right += 1
        else:
            # case: not distinct
            seen_nums[A[left]] = False
            left += 1

    return slice_count


if __name__ == '__main__':
    A = [3, 4, 5, 5, 2]
    print(solution2(5, A))
