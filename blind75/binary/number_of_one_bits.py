def hamming_weight(n: int) -> int:
    return bin(n).count("1")


def hamming_weight_optimized(n: int) -> int:
    ones = 0
    while n > 0:
        ones = ones + (n & 1)
        n = n >> 1
    return ones


def hamming_weight_more_optimized(n: int) -> int:
    ones = 0
    while n > 0:
        n = n & (n - 1)
        ones += 1
    return ones


if __name__ == '__main__':
    print("-- hamming_weight --")
    print(hamming_weight(3))
    print(hamming_weight(256))
    print(hamming_weight(356))
    print(hamming_weight(1253267))

    print("-- hamming_weight_optimized --")
    print(hamming_weight_optimized(3))
    print(hamming_weight_optimized(256))
    print(hamming_weight_optimized(356))
    print(hamming_weight_optimized(1253262))

    print("-- hamming_weight_more_optimized --")
    print(hamming_weight_more_optimized(3))
    print(hamming_weight_more_optimized(256))
    print(hamming_weight_more_optimized(356))
    print(hamming_weight_more_optimized(1253262))
