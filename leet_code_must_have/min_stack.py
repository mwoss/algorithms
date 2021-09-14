"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
"""


class Node:
    def __init__(self, val: int = None, min_val: int = None, next_node: 'Node' = None):
        self.val = val
        self.min = min_val
        self.next = next_node


class MinStack:

    def __init__(self):
        """
        Stack represented as a linked list, where each node
        contains information about the smallest element underneath it.
        """
        self.head = None

    def push(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(self.head.min, val), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def get_min(self) -> int:
        return self.head.min
