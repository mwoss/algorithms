from collections import Counter


def get_unique_character(s: str):
    characters_count = Counter(s)
    for idx, char in enumerate(s):
        if characters_count[char] == 1:
            return idx + 1
    return -1
