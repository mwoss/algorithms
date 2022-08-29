from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for str in strs:
        sorted_str = "".join(sorted(str))
        groups[sorted_str].append(str)
    return list(groups.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))

    strs2 = [""]
    print(group_anagrams(strs2))

    strs3 = ["a"]
    print(group_anagrams(strs3))
