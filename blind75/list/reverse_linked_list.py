from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def print_list(head: Optional[ListNode]):
    while head:
        print(head.val)
        head = head.next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head

    prev, head = head, head.next
    prev.next = None

    while head is not None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev


if __name__ == '__main__':
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rll = reverse_list(ll)

    print_list(rll)
