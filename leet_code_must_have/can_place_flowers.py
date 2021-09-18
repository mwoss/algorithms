from typing import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        i = 0
        while i < len(flowerbed) - 2:
            if not any(flowerbed[i:i + 3]):
                n -= 1
                i += 2
            else:
                i += 1

        return n <= 0


class Solution2:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                prev = 0 if i == 0 else flowerbed[i - 1]
                next = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
                if next == 0 and prev == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0


if __name__ == '__main__':
    s = Solution()
    print(s.can_place_flowers([1, 0, 0, 0, 1], 1))
    print(s.can_place_flowers([1], 0))
