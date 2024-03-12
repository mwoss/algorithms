from collections import defaultdict
from typing import List, Tuple


def target_sum(nums: List[int], target: int) -> Tuple[int, int]:
    number_to_index = {}
    for idx, num in enumerate(nums):
        to_find = target - num
        if to_find in number_to_index:
            return number_to_index[to_find], idx
        number_to_index[num] = idx

    raise Exception(f"There's no number pair that sums up to {target}")


def target_sum_non_repeats(nums: List[int], target: int) -> Tuple[int, int]:
    number_to_index = defaultdict(set)
    for curr_idx, num in enumerate(nums):
        to_find = target - num

        is_target_found = False

        if to_find in number_to_index and number_to_index[to_find]:
            first_sum_part_idx = number_to_index[to_find].pop()
            is_target_found = True
            yield first_sum_part_idx, curr_idx

        if is_target_found is False:
            number_to_index[num].add(curr_idx)


if __name__ == '__main__':
    print(target_sum([1, 2, 6, 4], 5))
    print(target_sum([1, 2, 6, 4, 4], 5))

    print(list(target_sum_non_repeats([1, 1, 2, 6, 4, 4], 5)))
    print(list(target_sum_non_repeats([5, 5, 5, 5, 5], 10)))
