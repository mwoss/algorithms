

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    if head is None:
        return head

    # 1 -> 2 -> 3 -> 4 -> 5 -> null
    mid_node = find_middle(head)
    tail = reverse_in_place(mid_node)



def find_middle(head: ListNode) -> ListNode:
    slow, fast = head, head
    while slow.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_in_place(head: ListNode):
    curr, prev = head, None
    while head.next:
        temp = head.next
        curr.next = prev
        prev = curr
        curr = temp

    head.next = curr

    return head


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
