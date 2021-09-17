from typing import List

from collections import defaultdict


def encode(s):
    # hash given string by occurrences of letter
    mappings = {}
    encoded = []
    for c in s:
        if c not in mappings:
            mappings[c] = len(mappings)
        encoded.append(mappings[c])
    return str(encoded)


def group_isomorphic(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        encoded = encode(s)
        groups[encoded].append(s)

    return list(groups.values())


if __name__ == '__main__':
    print(group_isomorphic(['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']))
