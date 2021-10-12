"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detect_cycle(self, head: ListNode) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast, entry = head, head, head
        while slow.next and slow.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                while slow is not entry:
                    slow = slow.next
                    entry = entry.next
                return entry

        return None


if __name__ == '__main__':
    s = Solution()
    l1_node, l2_node = ListNode(1), ListNode(2)
    l1_node.next = l2_node
    l2_node.next = l1_node
    print(s.detect_cycle(l1_node).val)

    l1_node, l2_node, l3_node, l4_node = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    l1_node.next = l2_node
    l2_node.next = l3_node
    l3_node.next = l4_node
    l4_node.next = l2_node
    print(s.detect_cycle(l1_node).val)
