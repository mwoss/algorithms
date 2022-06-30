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
    if len(nums) <= 2:
        return []

    nums.sort()  # it mutates input list

    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            target = nums[i] + nums[j] + nums[k]
            if target == 0:
                result.append([nums[i], nums[j], nums[k]])
                while nums[j] == nums[j + 1]: j += 1
                while nums[k] == nums[k - 1]: k -= 1
                j += 1
                k += 1
            elif target < 0:
                j += 1
            else:
                k -= 1

    return list(result)


if __name__ == '__main__':
    print(three_sum([]))
    print(three_sum([0]))
    print(three_sum([-1, 0, 1, 2, -1, 4]))

    print(three_sum_optimized([]))
    print(three_sum_optimized([0]))
    print(three_sum_optimized([-1, 0, 1, 2, -1, 4]))
