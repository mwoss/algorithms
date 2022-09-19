def count_substrings(s: str) -> int:
    palindrome_count, str_len = 0, len(s)
    for i in range(str_len):
        for j in range(i + 1, str_len + 1):
            if _is_palindrome(s[i:j]):
                palindrome_count += 1
    return palindrome_count


def _is_palindrome(s: str) -> bool:
    # can be optimized by iterating from start and end until meeting in the middle of string
    return s == s[::-1]


def count_substrings_2(s: str) -> int:
    palindrome_count, str_len = 0, len(s)
    palindromes_matrix = [[False] * str_len for _ in range(str_len)]

    for i in range(str_len - 1, -1, -1):
        for j in range(i, str_len):
            if s[i] == s[j] and (i - j < 2 or palindromes_matrix[i + 1][j - 1]):
                palindromes_matrix[i][j] = True
                palindrome_count += 1

    return palindrome_count


def count_substrings_3(s: str) -> int:
    count = 0
    for i in range(len(s)):
        count += check_palindrome(s, i, i)
        count += check_palindrome(s, i, i + 1)
    return count


def check_palindrome(s: str, i: int, j: int) -> int:
    count = 0
    while i >= 0 and j < len(s) and s[i] == s[j]:
        count += 1
        i -= 1
        j += 1
    return count


if __name__ == '__main__':
    print(count_substrings("abc"))
    print(count_substrings("aaa"))
    print(count_substrings("aaaaaa"))
    print("-------------------------")

    print(count_substrings_2("abc"))
    print(count_substrings_2("aaa"))
    print(count_substrings_2("aaaaaa"))
    print("-------------------------")

    print(count_substrings_3("abc"))
    print(count_substrings_3("aaa"))
    print(count_substrings_3("aaaaaa"))
    print("-------------------------")
