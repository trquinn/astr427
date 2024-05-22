# A Node is an object containing data in "value" and a reference to the next
# Node in "next".  This will be an element in a singly linked list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Basic implementation of a LIFO (last in first out) using a singly linked list
class Stack:
    def __init__(self, node=None):
        self.head = node

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.head is None


# Basic implementation of a FIFO (first in first out) using a singly linked list
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.head is None
