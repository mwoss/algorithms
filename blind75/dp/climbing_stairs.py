def climb_stairs(n: int) -> int:
    # if you visualize this problem, you will see it's basically a Fibonacci sequence
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return curr


if __name__ == '__main__':
    print(climb_stairs(2))
    print(climb_stairs(3))
