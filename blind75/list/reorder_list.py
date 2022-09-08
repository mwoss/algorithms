from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    if head is None:
        return head

    mid_node = find_middle(head)
    rev_head = reverse_in_place(mid_node)

    curr, curr_rev = head, rev_head
    while curr_rev.next:
        temp_curr = curr.next
        temp_curr_rev = curr_rev.next
        curr.next = curr_rev
        curr_rev.next = temp_curr

        curr = temp_curr
        curr_rev = temp_curr_rev


def find_middle(head: ListNode) -> ListNode:
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_in_place(head: ListNode):
    curr, prev = head, None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def print_list(head: Optional[ListNode]):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reorder_list(l1)
    print_list(l1)
