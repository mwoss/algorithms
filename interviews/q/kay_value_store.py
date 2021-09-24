"""
Implement key-value store that has fixed size.
If the store is full remove element that was used the most far in the time (seems like LRU cache to me).
Implement get/put/delete methods.
"""
from typing import TypeVar

T = TypeVar("T")


class NodeData:
    def __init__(self, key: str, value: T):
        self.key = key
        self.value = value


class ListNode:
    def __init__(self, data: NodeData):
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoubleLinkedList:
    def __init__(self):
        # we don't have to care about null prev and next pointers as this is internal data structure
        # and ListNode with null prev and next should never be passed to methods unintentionally
        self.head = None
        self.tail = None

    def insert_front(self, value: T) -> ListNode:
        node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node

        return node

    def move_front(self, node: ListNode):
        if node is self.head:
            return
        if node is self.tail:
            self.tail = node.prev_node
            node.prev_node.next_node = None
            node.prev_node = None
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node
            return

        self._isolate(node)
        node.next_node = self.head
        self.head.prev_node = node
        self.head = node

    def remove(self, node: ListNode):
        if node is self.head:
            new_head = self.head.next_node
            new_head.prev_node = None
            self.head.next_node = None
            self.head = new_head
            return
        if node is self.tail:
            new_tail = self.tail.prev_node
            new_tail.next_node = None
            self.tail.prev_node = None
            self.tail = new_tail
            return

        self._isolate(node)

    def remove_last(self) -> ListNode:
        new_tail, old_tail = self.tail.prev_node, self.tail
        new_tail.next_node = None
        self.tail.prev_node = None
        self.tail = new_tail
        return old_tail

    @staticmethod
    def _isolate(node: ListNode) -> ListNode:
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        node.prev_node = None
        node.next_node = None
        return node


class LRUCache:
    def __init__(self, size: int):
        self.max_size = size
        self._store = {}
        self._usage_list = DoubleLinkedList()

    def get(self, key: str) -> T:
        node = self._store.get(key)

        if node is None:
            raise KeyError(f"Key [{key}] does not exists in key-value store")

        self._usage_list.move_front(node)
        return node

    def set(self, key: str, value: T) -> None:
        node = self._store.get(key)

        if node is not None:
            node.data.value = value
            self._usage_list.move_front(node)
            return

        if len(self._store) == self.max_size:
            expired = self._usage_list.remove_last()
            del self._store[expired.data.key]

        self._store[key] = self._usage_list.insert_front(NodeData(key, value))

    def delete(self, key: str) -> None:
        node = self._store.get(key)

        if node is None:
            raise KeyError(f"Key [{key}] does not exists in key-value store")

        self._usage_list.remove(node)
        del self._store[node.data.key]


if __name__ == '__main__':
    cache = LRUCache(5)

    cache.set("a", 5)
    cache.set("b", 2)
    cache.set("c", 5)
    cache.set("d", 1)
    cache.set("e", 6)

    cache.delete("d")

    cache.set("d", 10)
    cache.set("d", 12)

    cache.set("x", 20)

    cache.delete('d')
