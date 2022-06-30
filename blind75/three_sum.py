from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) <= 2:
        return []

    result = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(e) for e in result]

def three_sum_optimized(nums: List[int]) -> List[List[int]]:
    result = set()
    nums = sorted(nums)

    for i in range(len(nums) - 2):
        pass


if __name__ == '__main__':
    print(three_sum([]))
    print(three_sum([0]))
    print(three_sum([-1, 0, 1, 2, -1, 4]))
