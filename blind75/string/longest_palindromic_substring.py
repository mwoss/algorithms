def longest_palindrome_brute(s: str) -> str:
    longest = ''
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            if _is_palindrome(s[i:j]) and len(longest) < j - i:
                longest = s[i:j]
    return longest


def _is_palindrome(s: str):
    return s == s[::-1]


if __name__ == '__main__':
    print(longest_palindrome_brute('babad'))
    print(longest_palindrome_brute('cbbd'))
