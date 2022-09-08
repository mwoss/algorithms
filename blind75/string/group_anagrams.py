from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for str in strs:
        sorted_str = "".join(sorted(str))
        groups[sorted_str].append(str)
    return list(groups.values())


def group_anagrams_2(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    counters = [0] * 26
    for str in strs:
        sorted_str = _counting_sort(str, counters)
        groups[sorted_str].append(str)
    return list(groups.values())


def _counting_sort(value: str, counters: List[int]) -> str:
    for char in value:
        counters[ord(char) - 97] += 1

    output = ""
    for idx, count in enumerate(counters):
        if count > 0:
            output += chr(idx + 97) * count
            counters[idx] = 0

    return output


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))
    print(group_anagrams_2(strs))

    strs2 = [""]
    print(group_anagrams(strs2))
    print(group_anagrams_2(strs2))

    strs3 = ["a"]
    print(group_anagrams(strs3))
    print(group_anagrams_2(strs3))
