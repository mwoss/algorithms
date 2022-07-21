from typing import Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return False

    slow, fast = head, head

    while slow.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print(has_cycle(node1))

    node5 = ListNode(1)
    node6 = ListNode(2)

    node5.next = node6
    node6.next = node5

    print(has_cycle(node5))

    node7 = ListNode(1)

    print(has_cycle(node7))
