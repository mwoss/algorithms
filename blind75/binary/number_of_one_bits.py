def hamming_weight(n: int) -> int:
    return bin(n).count("1")


if __name__ == '__main__':
    print(hamming_weight(3))
    print(hamming_weight(256))
    print(hamming_weight(356))
