from typing import List


def count_bits(n: int) -> List[int]:
    results = []
    for i in range(n + 1):
        results.append(bin(i).count("1"))
    return results


if __name__ == '__main__':
    print(count_bits(2))
    print(count_bits(5))
