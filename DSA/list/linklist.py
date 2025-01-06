class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list (no nodes)

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head  # Point new node to the old head
        self.head = new_node  # Update head to the new node
        print(f"Inserted {data} at the beginning")

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If list is empty, make new node the head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Make the last node point to new node
        print(f"Inserted {data} at the end")

    def delete_node(self, key):
        """Delete the first occurrence of a node with given data."""
        if self.head is None:
            print("List is empty!")
            return

        # If the node to be deleted is the head
        if self.head.data == key:
            self.head = self.head.next  # Move head to the next node
            print(f"Deleted {key} from the beginning")
            return

        current = self.head
        while current.next:  # Traverse the list
            if current.next.data == key:
                current.next = current.next.next  # Skip the node to delete
                print(f"Deleted {key} from the list")
                return
            current = current.next

        print(f"Node with data {key} not found!")

    def traverse(self):
        """Traverse and print all the nodes in the list."""
        if self.head is None:
            print("List is empty!")
            return

        current = self.head
        while current:
            #print(current.data, end=" -> ")
            print(f"current value: {current.data}")
            current = current.next
            print(f"next value {current}")
        print("None")

    def search(self, key):
        """Search for a node with specific data."""
        current = self.head
        while current:
            if current.data == key:
                return f"Node with data {key} found!"
            current = current.next
        return f"Node with data {key} not found!"

# Example Usage
#ll = LinkedList()

#ll.insert_at_beginning(10)
#ll.insert_at_end(20)
#ll.insert_at_end(30)
#ll.insert_at_beginning(5)

#ll.traverse()  # Output: 5 -> 10 -> 20 -> 30 -> None

#print(ll.search(20))  # Output: Node with data 20 found!
#print(ll.search(100))  # Output: Node with data 100 not found!

#ll.delete_node(10)
#ll.traverse()  # Output: 5 -> 20 -> 30 -> None
