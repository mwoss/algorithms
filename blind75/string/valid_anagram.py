def is_anagram(s: str, t: str) -> bool:
    letter_count = [0] * 26  # input strings consists of lowercase English letters

    for s_letter in s:
        letter_count[ord(s_letter) - 97] += 1

    for t_letter in t:
        letter_count[ord(t_letter) - 97] -= 1

    return all(count == 0 for count in letter_count)


def is_anagram_2(s: str, t: str) -> bool:
    """
    Other approaches:
    1. We could simply use sorting and compare both strings
    2. We could use map. Use letters as keys and increment/decrement count similarly to implemented solution.
       This solution would support broader range of letters (unicode characters too).
    """


if __name__ == '__main__':
    print(is_anagram("anagram", "nagaram"))
    print(is_anagram("rat", "car"))
