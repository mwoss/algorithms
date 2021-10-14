"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


class Solution:
    def reverse_words(self, s: str) -> str:
        words = [w for w in s.strip().split(" ") if w != ""]
        return " ".join(word for word in words[::-1])


class Solution2:
    def reverse_words(self, s: str) -> str:
        return " ".join(reversed(s.split()))


class Solution3:
    def reverse_words(self, s: str) -> str:
        arr = list(s)
        self._reverse(arr, 0, len(arr) - 1)
        self._reverse_words(arr)
        cleaned = self._clean_spaces(arr)
        return "".join(cleaned)

    def _reverse(self, arr: list, start: int, end: int):
        # reverse array (string) in place
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def _reverse_words(self, arr: list):
        i, j = 0, 0
        while j < len(arr):
            while j < len(arr) and arr[j] == " ":
                j += 1
            i = j
            while j < len(arr) and arr[j] != " ":
                j += 1
            self._reverse(arr, i, j - 1)

    def _clean_spaces(self, arr: list):
        i, j = 0, 0
        while j < len(arr):
            while j < len(arr) and arr[j] == " ":
                j += 1
            while j < len(arr) and arr[j] != " ":
                arr[i] = arr[j]
                i += 1
                j += 1
            while j < len(arr) and arr[j] == " ":
                j += 1
            if j < len(arr):
                arr[i] = " "
                i += 1

        return arr[:i]


if __name__ == '__main__':
    s = Solution3()
    print(s.reverse_words("the sky is blue"))
    print(s.reverse_words("  hello world  "))
    print(s.reverse_words("  Bob    Loves  Alice   "))
