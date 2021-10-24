"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""
import heapq
from typing import List


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


class Solution2:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)

            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]


class Solution2:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)

            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]


class Solution3:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        low, high, capacity = 0, len(nums) - 1, len(nums) - k
        while low < high:
            pivot = self.partition(nums, low, high)
            if pivot < capacity:
                low = pivot + 1
            elif pivot > capacity:
                high = pivot - 1
            else:
                break

        print(nums)
        return nums[-k]

    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = low
        for i in range(low, high):
            if nums[i] <= nums[high]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
        nums[high], nums[pivot] = nums[pivot], nums[high]
        return pivot


if __name__ == '__main__':
    s = Solution3()
    print(s.find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(s.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
