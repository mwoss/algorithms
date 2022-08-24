def is_palindrome(s: str) -> bool:
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]


def is_palindrome_2(s: str) -> bool:
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())

    l, r = 0, len(cleaned_s) - 1
    while l < r:
        if cleaned_s[l] != cleaned_s[r]:
            return False
        l += 1
        r -= 1

    return True


def is_palindrome_3(s: str) -> bool:
    pass


if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))

    print(is_palindrome_2("A man, a plan, a canal: Panama"))
    print(is_palindrome_2("race a car"))
