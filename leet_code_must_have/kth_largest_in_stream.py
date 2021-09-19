"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

* KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
* int add(int val) Appends the integer val to the stream and returns
the element representing the kth largest element in the stream.
"""
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


class KthLargest2:

    def __init__(self, k: int, nums: List[int]):
        self.pq, self.k = nums, k
        heapq.heapify(self.pq)
        while len(self.pq) > k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        else:
            heapq.heappushpop(self.pq, val)
        return self.pq[0]


class KthLargest3:

    def __init__(self, k: int, nums: List[int]):
        self.pq, self.k = [], k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]
