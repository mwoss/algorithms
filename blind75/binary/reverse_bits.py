def reverse_bits(n: int) -> int:
    bit_repr = bin(n)[2:]
    missing_bits = '0' * (32 - len(bit_repr))
    reversed_bits = bit_repr[::-1] + missing_bits
    return int(reversed_bits, 2)


if __name__ == '__main__':
    print(reverse_bits(43261596))
    print(reverse_bits(4294967293))
