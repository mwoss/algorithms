from collections import defaultdict
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in words:
        bucket = "".join(sorted(word))
        groups[bucket].append(word)

    return list(groups.values())


def group_anagrams_count_sort(words: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    counters = [0] * 26
    for word in words:
        bucket = counting_sort_words(word, counters)
        groups[bucket].append(word)

    return list(groups.values())


def counting_sort_words(word: str, counters: list) -> str:
    for letter in word:
        counters[ord(letter) - 97] += 1

    output = ""
    for idx, count in enumerate(counters):
        if count > 0:
            output += chr(idx + 97) * count
            counters[idx] = 0

    return output


if __name__ == '__main__':
    words = ["aew", "wea", "lool", "ooll", "xd"]
    print(group_anagrams_count_sort(words))
