def length_of_longest_substring(s: str) -> int:
    seen = set()
    current, longest = 0, 0

    for char in s:
        if char in seen:
            current -= 1
        else:
            current += 1

        seen.add(char)

        longest = max(longest, current)

    return longest


if __name__ == '__main__':
    print(length_of_longest_substring("abcabcbb"))
    print(length_of_longest_substring("bbbbb"))
    print(length_of_longest_substring("pwwkew"))
