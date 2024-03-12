import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    most_frequent, nums_count = [], Counter(nums)

    for num, count in nums_count.items():
        heapq.heappush(most_frequent, (count, num))

        if len(most_frequent) > k:
            heapq.heappop(most_frequent)

    return [heapq.heappop(most_frequent)[1] for _ in range(k)]


def top_k_frequent_2(nums: List[int], k: int) -> List[int]:
    # lazy version of above solution using built in heapq library capabilities :3
    nums_count = Counter(nums)
    most_frequent = heapq.nlargest(k, nums_count.items(), key=lambda e: e[0])
    return [num for _, num in most_frequent]


def top_k_frequent_optimized(nums: List[int], k: int) -> List[int]:
    # bucket sort approach
    nums_count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in nums_count.items():
        buckets[count].append(num)

    result = []
    for i in range(len(nums), -1, -1):
        bucket = buckets[i]
        for freq_num in bucket:
            if len(result) == k:
                return result
            result.append(freq_num)

    return result


if __name__ == '__main__':
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent([1, 1, 1, 2, 2, 3, 4, 4, 4], 2))
    print(top_k_frequent([1], 1))

    print(top_k_frequent_2([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent_2([1], 1))

    print(top_k_frequent_optimized([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent_optimized([1, 1, 1, 2, 2, 3, 4, 4, 4], 2))
    print(top_k_frequent_optimized([1], 1))
