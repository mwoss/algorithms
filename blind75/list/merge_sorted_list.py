from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None or list2 is None:
        return list1 or list2

    head = current = ListNode()

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list2
    if list2 is not None:
        current.next = list1

    return head.next


def print_list(l: Optional[ListNode]):
    while l is not None:
        print(l.val)
        l = l.next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(5, ListNode(9)))
    l2 = ListNode(2, ListNode(4, ListNode(6)))
    print_list(merge_two_lists(l1, l2))
