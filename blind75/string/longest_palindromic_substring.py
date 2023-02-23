def longest_palindrome_brute(s: str) -> str:
    if len(s) < 2:
        return s

    longest = ''
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            if _is_palindrome(s[i:j]) and len(longest) < j - i:
                longest = s[i:j]
    return longest


def _is_palindrome(s: str):
    return s == s[::-1]


def longest_palindrome(s: str) -> str:
    if len(s) < 2:
        return s

    str_len, longest = len(s), s[0]

    dp = [[False for _ in range(str_len)] for _ in range(str_len)]

    for i in range(str_len):
        dp[i][i] = True

    for i in range(0, str_len - 1):
        for j in range(i + 1, str_len):
            if s[i] == s[j] and (dp[i + 1][j - 1] or j - i == 1):
                dp[i][j] = True
                if len(longest) < j - i + 1:
                    longest = s[i:j + 1]

    return longest


if __name__ == '__main__':
    print(longest_palindrome_brute('babad'))
    print(longest_palindrome_brute('cbbd'))

    print(longest_palindrome('babad'))
    print(longest_palindrome('cbbd'))
