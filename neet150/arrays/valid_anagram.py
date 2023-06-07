def is_anagram(s: str, t: str) -> bool:
    letter_count = [0] * 26

    for letter in s:
        letter_count[ord(letter) - 97] += 1

    for letter in t:
        letter_count[ord(letter) - 97] -= 1

    for count in letter_count:
        if count != 0:
            return False

    return True


if __name__ == '__main__':
    print(is_anagram("anagram", "nagaram"))
    print(is_anagram("rat", "car"))
