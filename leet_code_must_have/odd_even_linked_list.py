"""
Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        tail = self._get_tail(head)
        size = self._get_length(head)

        odd, even = head, head.next
        while size != 0:
            odd.next = even.next
            odd = odd.next

            tail.next = even
            even.next = None
            tail = even
            even = odd.next

            size -= 2

        return head

    def _get_tail(self, head: Optional[ListNode]) -> ListNode:
        while head and head.next:
            head = head.next
        return head

    def _get_length(self, head: Optional[ListNode]) -> int:
        length = 0
        while head and head.next:
            head = head.next
            length += 1
        return length


class Solution2:
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            # make sublist of odd and even nodes
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = even.next

        # connect last node of odd nodes to first one of even nodes
        odd.next = even_head

        return head


def print_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == '__main__':
    s = Solution2()
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    odd_even_list1 = s.odd_even_list(head1)

    print_list(odd_even_list1)

    head2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    odd_even_list2 = s.odd_even_list(head2)

    print_list(head2)
