"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and
retrieve keys in a dataset of strings. There are various applications of this data structure,
such as autocomplete and spellchecker.

Implement the Trie class:
* Trie() Initializes the trie object.
* void insert(String word) Inserts the string word into the trie.
* boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
 and false otherwise.
* boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has
 the prefix prefix, and false otherwise.
"""
from collections import defaultdict
from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_end

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


class TrieNodeBucket:
    def __init__(self):
        self.children: List[Optional[TrieNodeBucket]] = [None] * 26
        self.is_end = False

    def contains(self, letter: str) -> bool:
        return self.children[ord(letter) - 97] is not None

    def get(self, letter: str) -> Optional["TrieNodeBucket"]:
        return self.children[ord(letter) - 97]

    def put(self, letter: str) -> None:
        self.children[ord(letter) - 97] = TrieNodeBucket()


class Trie2:
    def __init__(self):
        self.root = TrieNodeBucket()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if not current.contains(letter):
                current.put(letter)
            current = current.get(letter)
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if not current.contains(letter):
                return False
            current = current.get(letter)
        return current.is_end

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if not current.contains(letter):
                return False
            current = current.get(letter)
        return True


if __name__ == '__main__':
    t = Trie2()
    t.insert("lool")
    print(t.search("lool"))
    print(t.search("XDDD"))
    print(t.starts_with("lo"))
