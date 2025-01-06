class Node:
    def __init__(self, data):
        self.previous = None        # Pointer to the previous node
        self.data = data            # Store the data
        self.next = None            # Pointer to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            new_node.next = self.head  # Point new node to the current head
            self.head.previous = new_node  # Point the current head's previous to the new node
            self.head = new_node       # Update head to the new node
        print(f"Inserted {data} at the beginning")

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Update last node's next to the new node
            new_node.previous = current  # Point new node's previous to the last node
        print(f"Inserted {data} at the end")

    def delete_node(self, key):
        """Delete the first occurrence of a node with the given data."""
        if self.head is None:  # If the list is empty
            print("List is empty!")
            return

        # Case 1: The node to be deleted is the head
        if self.head.data == key:
            if self.head.next is None:  # If there's only one node
                self.head = None
            else:
                self.head = self.head.next  # Move head to the next node
                self.head.previous = None  # Remove reference to the old head
            print(f"Deleted {key} from the beginning")
            return

        # Case 2: Traverse to find the node to delete
        current = self.head
        while current:
            if current.data == key:
                if current.next:  # If it's not the last node
                    current.next.previous = current.previous
                if current.previous:  # If it's not the first node
                    current.previous.next = current.next
                print(f"Deleted {key} from the list")
                return
            current = current.next

        print(f"Node with data {key} not found!")

    def traverse_forward(self):
        """Traverse the list in the forward direction."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Traverse the list in the backward direction."""
        if self.head is None:
            print("List is empty!")
            return

        # Go to the last node
        current = self.head
        while current.next:
            current = current.next

        # Traverse backward
        while current:
            print(current.data, end=" -> ")
            current = current.previous
        print("None")

dll = DoublyLinkedList()
print(dll.head)
dll.insert_at_beginning(10)
print(vars(dll.head))
dll.insert_at_beginning(20)
print(vars(dll.head))
print(vars(dll.head.next))
print(vars(dll.head.next.previous))
#dll.insert_at_end(30)
#dll.insert_at_end(40)

# print("Traverse forward:")
# dll.traverse_forward()

# print("Traverse backward:")
# dll.traverse_backward()

# dll.delete_node(20)
# print("After deleting 20:")
# dll.traverse_forward()
