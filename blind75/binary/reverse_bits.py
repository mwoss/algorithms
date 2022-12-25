def reverse_bits(n: int) -> int:
    bit_repr = bin(n)[2:]
    missing_bits = '0' * (32 - len(bit_repr))
    reversed_bits = bit_repr[::-1] + missing_bits
    return int(reversed_bits, 2)


def reverse_bits_optimized(n: int) -> int:
    if n == 0:
        return 0

    result = 0
    for i in range(32):
        result = result << 1
        result += n & 1
        n = n >> 1
    return result


if __name__ == '__main__':
    print(reverse_bits(43261596))
    print(reverse_bits(4294967293))

    print(reverse_bits_optimized(43261596))
    print(reverse_bits_optimized(4294967293))
