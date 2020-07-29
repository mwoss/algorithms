def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def fibonacci_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_rec(n - 2) + fibonacci_rec(n - 1)


if __name__ == '__main__':
    print(fibonacci(7))
    print(fibonacci_rec(7))
