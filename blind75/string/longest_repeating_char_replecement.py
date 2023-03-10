from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    start, longest = 0, 0
    frequencies = defaultdict(lambda: 0)
    max_frequency = 0

    for end in range(len(s)):
        frequencies[s[end]] += 1

        max_frequency = max(max_frequency, frequencies[s[end]])

        while end - start - max_frequency + 1 > k:
            frequencies[s[start]] -= 1
            start += 1

        longest = max(longest, end - start + 1)

    return longest


if __name__ == '__main__':
    print(character_replacement("ABAB", 2))
    print(character_replacement("AABABBA", 1))
    print(character_replacement("AABABBAAAAB", 4))
    print(character_replacement("AABACBACBAB", 3))
    print(character_replacement("ZHAYYYDHJAYY", 5))
    print(character_replacement("ABBBABBABABABBBCAGBDBAABBFHAXAAF", 6))
    print(character_replacement("AAAAAAAAAB", 0))
    print(character_replacement("XDDXDDDDXDSADXDDD", 10))
