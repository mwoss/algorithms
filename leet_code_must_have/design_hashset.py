"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

* void add(key) Inserts the value key into the HashSet.
* bool contains(key) Returns whether the value key exists in the HashSet or not.
* void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""
from typing import Optional, List, Tuple


class MyHashSet:

    def __init__(self):
        self._size: int = 0
        self._capacity: int = 8
        self._lf: float = 0.75
        self.table: List[Optional[int]] = [None] * self._capacity

    def add(self, key: int) -> None:
        if self._size / self._capacity > self._lf:
            self._resize_table()

        hash_index = self._hash(key)
        while self.table[hash_index] is not None:
            if self.table[hash_index] == key:
                return

            hash_index = (hash_index + 1) % self._capacity  # move to the next potential free spot

        self.table[hash_index] = key
        self._size += 1

    def remove(self, key: int) -> None:
        hash_index = self._hash(key)

        while self.table[hash_index] is not None:
            if self.table[hash_index] == key:
                self.table[hash_index] = "#DELETED#"
                self._size -= 1
                return

            hash_index = (hash_index + 1) % self._capacity  # move to the next potential free spot

    def contains(self, key: int) -> bool:
        hash_index = self._hash(key)

        while self.table[hash_index] is not None:
            if self.table[hash_index] == key:
                return True
            hash_index = (hash_index + 1) % self._capacity  # move to the next potential free spot

        return False

    def _hash(self, key: int) -> int:
        return key % self._capacity

    def _resize_table(self):
        self._capacity *= 2
        self._size = 0
        temp_table = [None] * self._capacity

        for val in self.table:
            if val is not None and val != "#DELETED#":

                hash_index = self._hash(val)

                while temp_table[hash_index] is not None:
                    hash_index = (hash_index + 1) % self._capacity  # move to the next potential free spot
                temp_table[hash_index] = val
                self._size += 1

        self.table = temp_table


class MyHashSet2:

    def __init__(self):
        # implementation without resizing
        self._size = 10
        self.table = [[] for _ in range(self._size)]  # buckets used as a collision resolving

    def add(self, key: int) -> None:
        idx, bucket = self._get_index(key)
        if idx == -1:
            bucket.append(key)

    def remove(self, key: int) -> None:
        idx, bucket = self._get_index(key)
        if idx == -1:
            return
        bucket.remove(key)

    def contains(self, key: int) -> bool:
        idx, _ = self._get_index(key)
        return idx != -1

    def _hash(self, key):
        return key % self._size

    def _get_index(self, key) -> Tuple[int, list]:
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        for idx, element in enumerate(bucket):
            if element == key:
                return idx, bucket
        return -1, bucket


if __name__ == '__main__':
    hashset = MyHashSet2()

    actions = ["add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    nums = [[1], [2], [1], [3], [2], [2], [2], [2]]

    res = []
    for act, num in zip(actions, nums):
        func = getattr(hashset, act)
        res.append(func(num[0]))

    print(res)
    print(hashset.table)
