from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) <= 2:
        return max(nums)

    robbed_amount = [0] * len(nums)
    robbed_amount[0] = nums[0]
    robbed_amount[1] = nums[1]
    robbed_amount[2] = nums[0] + nums[2]

    for i in range(3, len(nums)):
        prev_robbery = nums[i] + robbed_amount[i - 2]
        prev_prev_robbery = nums[i] + robbed_amount[i - 3]
        robbed_amount[i] = max(prev_robbery, prev_prev_robbery)

    return max(robbed_amount[-2], robbed_amount[-1])


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
