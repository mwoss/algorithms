from collections import Counter


def contain_duplicate(nums):
    c = Counter(nums)
    for count in c.values():
        if count > 1:
            return True
    return False
