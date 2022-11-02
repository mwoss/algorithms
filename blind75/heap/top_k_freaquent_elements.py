import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    most_frequent, nums_count = [], Counter(nums)

    for num, count in nums_count.items():
        heapq.heappush(most_frequent, (count, num))

        if most_frequent[0][1] == num and len(most_frequent) > k:
            # we can do it, because it is guaranteed that the answer is unique, so if the "smallest" element in heap
            # is equal to current element it means it's for sure that element, and we can safely remove it
            heapq.heappop(most_frequent)

    return [num for _, num in most_frequent]


def top_k_frequent_2(nums: List[int], k: int) -> List[int]:
    # lazy version of above solution using built in heapq library capabilities :3
    nums_count = Counter(nums)
    most_frequent = heapq.nlargest(k, nums_count.items(), key=lambda e: e[0])
    return [num for _, num in most_frequent]


if __name__ == '__main__':
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent([1], 1))

    print(top_k_frequent_2([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent_2([1], 1))
