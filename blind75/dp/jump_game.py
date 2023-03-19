from typing import List


def can_jump(nums: List[int]) -> bool:
    n = len(nums)
    reachable = [False] * n

    for idx in range(0, n - 1):
        furthest_jump = min(idx + nums[idx], n - 1)
        reachable[idx] = True
        reachable[furthest_jump] = True

    return reachable[-1]


def can_jump_optimized(nums: List[int]) -> bool:
    # memory optimzied solution
    n = len(nums) - 1

    furthest_reachable = 0
    for idx in range(0, n - 1):
        furthest_reachable = max(furthest_reachable, idx + nums[idx])

    return furthest_reachable == n


if __name__ == '__main__':
    print(can_jump([2, 3, 1, 1, 4]))
    print(can_jump([3, 2, 1, 0, 4]))

    print(can_jump_optimized([2, 3, 1, 1, 4]))
    print(can_jump_optimized([3, 2, 1, 0, 4]))
