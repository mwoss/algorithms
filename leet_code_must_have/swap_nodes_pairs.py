"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        res_head = head.next
        prev, curr_node, next_node = None, head, head.next

        while curr_node and curr_node.next:
            curr_node.next = next_node.next
            next_node.next = curr_node

            if prev is not None:
                prev.next = next_node

            prev = curr_node
            curr_node = curr_node.next

            # kinda messy, but due to lack of do-while loop in Python we have to do shit like this
            if curr_node is not None and curr_node.next is not None:
                next_node = curr_node.next

        return res_head


class Solution2:
    def swap_pairs_dummy_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            first, second = curr.next, curr.next.next

            first.next = second.next
            second.next = first
            curr.next = second

            curr = curr.next.next

        return dummy.next


if __name__ == '__main__':
    s = Solution2()
    node_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))

    res = s.swap_pairs_dummy_node(node_list)

    while res:
        print(res.val, end=" ")
        res = res.next
