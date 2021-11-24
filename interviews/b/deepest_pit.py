"""
A non-empty zero-indexed array A consisting of N integers is given.
A pit in this array is any triplet of integers (P, Q, R) such that: 0 ≤ P < Q < R < N;

sequence [A[P], A[P+1], ..., A[Q]] is strictly decreasing, i.e. A[P] > A[P+1] > ... > A[Q];

sequence A[Q], A[Q+1], ..., A[R] is strictly increasing, i.e. A[Q] < A[Q+1] < ... < A[R].

The depth of a pit (P, Q, R) is the number min{A[P] − A[Q], A[R] − A[Q]}. For example, consider array
A consisting of 10 elements such that:

A[0] =  0
A[1] =  1
A[2] =  3
A[3] = -2
A[4] =  0
A[5] =  1
A[6] =  0
A[7] = -3
A[8] =  2
A[9] =  3

Triplet (2, 3, 4) is one of pits in this array, because sequence [A[2], A[3]] is strictly decreasing (3 > −2)
and sequence [A[3], A[4]] is strictly increasing (−2 < 0). Its depth is min{A[2] − A[3], A[4] − A[3]} = 2.
Triplet (2, 3, 5) is another pit with depth 3.
Triplet (5, 7, 8) is yet another pit with depth 4. There is no pit in this array deeper than 4.
"""
from typing import List


def deepest_pit_simple(arr: List[int]) -> int:
    max_depth = 0
    for p in range(0, len(arr) - 2):
        for q in range(p + 1, len(arr) - 1):
            for r in range(q + 1, len(arr)):
                max_depth = max(max_depth, min(arr[p] - arr[q], arr[r] - arr[q]))
    return max_depth if max_depth else -1


def deepest_pit_optimal(arr: List[int]) -> int:
    max_depth = 0
    p, q, r = 0, -1, -1

    for i in range(1, len(arr)):
        if q < 0 and arr[i - 1] < arr[i]:
            q = i - 1

        if q >= 0 > r and (arr[i] <= arr[i - 1] or i + 1 == len(arr)):
            if arr[i] <= arr[i - 1]:
                r = i - 1
            else:
                r = i

            max_depth = max(max_depth, min(arr[p] - arr[q], arr[r] - arr[q]))
            p = i - 1
            q = r = -1

    if max_depth == 0:
        return -1

    return max_depth


def deepest_pit_optimal_2(arr: List[int]) -> int:
    """
    More solutions can be found here:
    * https://hakanyurdakul.com/deepest-pit/
    * https://github.com/trod/puzzles/blob/master/codility/DeepestPit.java
    * https://codereview.stackexchange.com/questions/214743/deepest-pit-of-an-array
    * https://stackoverflow.com/questions/46877274/confusion-regarding-deepest-pit-within-an-array
    """


if __name__ == '__main__':
    print(deepest_pit_simple([10, 8, 5, 6, 8, 4, 2, 6, 7]))
