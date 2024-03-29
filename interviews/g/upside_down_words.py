"""
Having the list of words filter out all words that looks the same as its original form when we look at them up side down
Up side down letter mapping is already provided (look LETTER_MAPPING).
"""
from typing import List, Iterator

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
    # it can be optimized by using two pointers (left, right) and iterating throughout
    # both strings in the same time without allocating memory for reversed word
    for nl, udl in zip(word, word[::-1]):
        if udl not in LETTER_MAPPING or nl != LETTER_MAPPING[udl]:
            return False
    return True


if __name__ == '__main__':
    words = ["pod", "red", "yeah", "lol", "nerd"]
    print(filter_upside_down_words(words))
