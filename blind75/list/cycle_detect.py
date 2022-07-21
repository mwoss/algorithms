from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while slow.next is not None or fast.next is not None:
        if slow is fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False
