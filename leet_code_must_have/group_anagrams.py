from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            bucket = "".join(sorted(word))
            groups[bucket].append(word)

        return list(groups.values())


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        counters = [0] * 26
        for word in strs:
            bucket = self._counting_sort_words(word, counters)
            groups[bucket].append(word)

        return list(groups.values())

    def _counting_sort_words(self, word: str, counters: list) -> str:
        for letter in word:
            counters[ord(letter) - 97] += 1

        output = ""
        for idx, count in enumerate(counters):
            if count > 0:
                output += chr(idx + 97) * count
                counters[idx] = 0

        return output


if __name__ == '__main__':
    s = Solution2()
    words = ["aew", "wea", "lool", "ooll", "xd"]
    print(s.groupAnagrams(words))
