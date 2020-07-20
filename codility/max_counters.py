"""
You are given N counters, initially set to 0, and you have two possible operations on them:
increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.

A non-empty array A of M integers is given. This array represents consecutive operations:
if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers,
returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:
N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""


def solution(N, A):
    # M * N worst time complexity :<
    counters = [0] * N
    current_max = 0

    for e in A:
        if 1 <= e <= N:
            counters[e - 1] += 1
            if counters[e - 1] > current_max:
                current_max = counters[e - 1]
        elif e == N + 1:
            counters = [current_max] * N

    return counters


def solution2(N, A):
    # linear time complexity O(M)
    counters = [0] * N
    current_max = 0
    last_updated = 0

    for e in A:
        if 1 <= e <= N:
            if counters[e - 1] < last_updated:
                counters[e - 1] = last_updated + 1
            else:
                counters[e - 1] += 1
            if counters[e - 1] > current_max:
                current_max = counters[e - 1]
        elif e == N + 1:
            last_updated = current_max

    counters = [last_updated if c < last_updated else c for c in counters]
    return counters


if __name__ == '__main__':
    print(solution2(5, [3, 4, 4, 6, 1, 4, 4]))
