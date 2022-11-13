def hamming_weight(n: int) -> int:
    return bin(n).count("1")


def hamming_weight_optimized(n: int) -> int:
    result = 0
    while n > 0:
        if n & 1:
            result += 1
        n = n >> 1
    return result


if __name__ == '__main__':
    print(hamming_weight(3))
    print(hamming_weight(256))
    print(hamming_weight(356))

    print(hamming_weight_optimized(3))
    print(hamming_weight_optimized(256))
    print(hamming_weight_optimized(356))
