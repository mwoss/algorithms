"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pairs = [(num, occ) for num, occ in counter.items()]
        pairs.sort(key=lambda e: e[1], reverse=True)
        return [pair[0] for pair in pairs[:k]]


class Solution2:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pq = []
        for num, occ in counter.items():
            heapq.heappush(pq, (occ, num))

            if len(pq) > k:
                heapq.heappop(pq)

        return [elem[1] for elem in pq]


class Solution3:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)

        flatten_freq = [freq for bucket in buckets for freq in bucket]

        return flatten_freq[-k:]


if __name__ == '__main__':
    s = Solution3()
    print(s.top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print(s.top_k_frequent([1], 1))
