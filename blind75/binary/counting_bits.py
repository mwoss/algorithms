from typing import List


def count_bits(n: int) -> List[int]:
    results = []
    for i in range(n + 1):
        results.append(bin(i).count("1"))
    return results


def count_bits_optimized(n: int) -> List[int]:
    results = [0] * (n + 1)  # we skip 0 as we already know it has zero "1s"
    for i in range(1, n + 1):
        results[i] = results[i // 2] + i % 2
    return results


if __name__ == '__main__':
    print(count_bits(2))
    print(count_bits(5))

    print("================")

    print(count_bits_optimized(2))
    print(count_bits_optimized(5))
