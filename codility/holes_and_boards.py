"""
You are given n binary values x0, x1, . . . , xn−1, such that xi ∈ {0, 1}. This array
represents holes in a roof (1 is a hole). You are also given k boards of the same size. The goal
is to choose the optimal (minimal) size of the boards that allows all the holes to be covered
by boards
"""


def boards(A, k):
    result = -1
    beg, end = 0, len(A) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if check(A, mid) <= k:
            beg = mid + 1
            result = mid
        else:
            end = mid - 1

    return result


def check(A, length):
    boards_num = 0
    last = -1
    for i in range(len(A)):
        if A[i] == 1 and last < -1:
            boards_num += 1
            last = i + length - 1

    return boards_num
