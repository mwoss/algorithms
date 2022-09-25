from typing import List


def find_min(nums: List[int]) -> int:
    # time complexity: O(n)
    return min(nums)


def find_min_optimized(nums: List[int]) -> int:
    # time complexity: O(lgn)
    # TODO: implement modified bin search
    pass


if __name__ == '__main__':
    print(find_min([3, 4, 5, 1, 2]))
    print(find_min([4, 5, 6, 7, 0, 1, 2]))
    print(find_min([11, 13, 15, 17]))
