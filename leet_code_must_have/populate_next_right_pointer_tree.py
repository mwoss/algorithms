"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return root

        queue = deque([root])

        while queue:
            curr_size = len(queue)
            for i in range(curr_size):
                curr_node = queue.popleft()
                next_node = queue[0] if i < curr_size - 1 else None

                curr_node.next = next_node

                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)

        return root


class Solution2:
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return root

        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left is not None:
                    curr.next = node.left
                    curr = curr.next
                if node.right is not None:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next

        return root


if __name__ == '__main__':
    s = Solution2()
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    s.connect(tree)
