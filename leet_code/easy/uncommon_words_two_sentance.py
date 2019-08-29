"""
We are given two sentences A and B.  (A sentence is a string of space separated words.
Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words.
You may return the list in any order.

Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""

from collections import defaultdict
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        uniq_words = defaultdict(lambda: 0)

        for word in A.split(" "):
            uniq_words[word] += 1

        for word in B.split(" "):
            uniq_words[word] += 1

        return [k for k, v in uniq_words.items() if v == 1]
