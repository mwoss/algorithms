def count_substrings(s: str) -> int:
    palindrom_count, str_len = 0, len(s)
    for i in range(str_len):
        for j in range(i + 1, str_len + 1):
            if _is_palindrome(s[i:j]):
                palindrom_count += 1
    return palindrom_count


def _is_palindrome(s: str) -> bool:
    return s == s[::-1]


if __name__ == '__main__':
    print(count_substrings("abc"))
    print(count_substrings("aaa"))
