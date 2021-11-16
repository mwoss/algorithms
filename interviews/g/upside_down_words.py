"""
README: TODO
"""
from typing import List, Generator, Iterator

LETTER_MAPPING = {
    "a": "e",
    "e": "a",
    "y": "h",
    "h": "y",
    "w": "m",
    "m": "w",
    "o": "o",
    "d": "p",
    "p": "d",
    "l": "l",
}


def filter_upside_down_words(words: List[str]) -> List[str]:
    upside_down_words = []
    for word in words:
        if is_upside_down_word(word):
            upside_down_words.append(word)
    return upside_down_words


def filter_upside_down_words_2(words: List[str]) -> Iterator[str]:
    for word in words:
        if is_upside_down_word(word):
            yield word


def is_upside_down_word(word: str) -> bool:
    for nl, udl in zip(word, word[::-1]):
        if udl not in LETTER_MAPPING or nl != LETTER_MAPPING[udl]:
            return False
    return True


if __name__ == '__main__':
    words = ["pod", "red", "yeah", "lol", "nerd"]
    print(filter_upside_down_words(words))
