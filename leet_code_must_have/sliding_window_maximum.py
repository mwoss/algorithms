from collections import deque
from typing import List


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(0, len(nums) - k + 1):
            result.append(max(nums[i:i + k]))
        return result


class Solution2:

    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        if k == 1:
            return nums

        result = []
        mono_queue = self.MonotonicQueue()

        for i in range(k - 1):
            mono_queue.push(nums[i])

        for i in range(k - 1, len(nums)):
            mono_queue.push(nums[i])
            result.append(mono_queue.max())
            mono_queue.pop()

        return result

    class MonotonicQueue:
        def __init__(self):
            # first element store the actual value
            # second element store information about how much elements were removed between it and one before it
            self.queue = deque()

        def push(self, val: int):
            count = 0
            while self.queue and self.queue[-1][0] < val:
                count += self.queue[-1][1] + 1
                self.queue.pop()
            self.queue.append((val, count))

        def pop(self):
            if self.queue[0][1] > 0:
                self.queue[0] = (self.queue[0][0], self.queue[0][1] - 1)
                return
            self.queue.popleft()


if __name__ == '__main__':
    s = Solution2()
    # print(s.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.max_sliding_window([7, 2, 4], 2))
