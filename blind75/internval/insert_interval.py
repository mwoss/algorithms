from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # solution with returning new list
    updated_intervals = []

    for start, end in intervals:
        if end < new_interval[0]:
            updated_intervals.append([start, end])
        elif start > new_interval[1]:
            updated_intervals.append(new_interval)
            new_interval = [start, end]
        else:
            new_interval[0] = min(new_interval[0], start)
            new_interval[1] = max(new_interval[1], end)

    updated_intervals.append(new_interval)

    return updated_intervals


if __name__ == '__main__':
    print(insert([[1, 3], [6, 9]], [2, 5]))
    print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
