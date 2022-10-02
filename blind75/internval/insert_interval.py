from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # skip list sounds like a good fit here
    pass


if __name__ == '__main__':
    print(insert([[1, 3], [6, 9]], [2, 5]))
    print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
