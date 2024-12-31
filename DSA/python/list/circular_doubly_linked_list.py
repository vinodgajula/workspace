class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None  # Renamed from 'prev' to 'previous'

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            new_node.next = new_node
            new_node.previous = new_node
            return
        last = self.head.previous
        last.next = new_node
        new_node.previous = last
        new_node.next = self.head
        self.head.previous = new_node

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            new_node.next = new_node
            new_node.previous = new_node
            return
        last = self.head.previous
        new_node.next = self.head
        new_node.previous = last
        last.next = new_node
        self.head.previous = new_node
        self.head = new_node

    # Traverse forward
    def traverse_forward(self):
        if not self.head:
            print("The list is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:  # Stop when we circle back to the head
                break
        print("HEAD")

    # Traverse backward
    def traverse_backward(self):
        if not self.head:
            print("The list is empty.")
            return
        temp = self.head.previous  # Start from the last node
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.previous
            if temp == self.head.previous:  # Stop when we circle back to the last node
                break
        print("HEAD")

# Example Usage
cdll = CircularDoublyLinkedList()
cdll.insert_at_end(10)
cdll.insert_at_end(20)
cdll.insert_at_beginning(5)
cdll.insert_at_beginning(1)

print("Forward Traversal:")
cdll.traverse_forward()  # Output: 1 <-> 5 <-> 10 <-> 20 <-> HEAD

print("Backward Traversal:")
cdll.traverse_backward()  # Output: 20 <-> 10 <-> 5 <-> 1 <-> HEAD
