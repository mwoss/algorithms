"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N,
is called a slice of array A (notice that the slice contains at least two elements).
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice.
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:
def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the
minimal average. If there is more than one slice with a minimal average,
you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:
N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""


# the best explanation of this problem can be found here :
# https://stackoverflow.com/questions/21635397/min-average-two-slice-codility

def prefix_sum(arr):
    n = len(arr)
    res_arr = [0] * (n + 1)

    for i in range(1, n + 1):
        res_arr[i] = res_arr[i - 1] + arr[n - 1]

    return res_arr


def count_total(pref, x, y):
    # x is inclusive, y is exclusive
    return pref[y + 1] - pref[x]


def solution(A):
    if len(A) == 2:
        return 0

    min_slice_two = A[0] + A[1]
    min_index_two = 0

    min_slice_three = A[0] + A[1] + A[2]
    min_index_three = 0

    for i in range(2, len(A)):
        slice_two = A[i - 1] + A[i]
        if slice_two < min_slice_two:
            min_slice_two = slice_two
            min_index_two = i - 1

        slice_three = slice_two + A[i - 2]
        if slice_three < min_slice_three:
            min_slice_three = slice_three
            min_index_three = i - 2

    avg_slice_two = min_slice_two * 3  # get the same average over a slice of length 6
    avg_slice_three = min_slice_three * 2  # get the same average over a slice of length 6

    if avg_slice_two == avg_slice_three:
        return min(min_index_two, min_index_three)
    elif avg_slice_two < avg_slice_three:
        return min_index_two

    return min_index_three
