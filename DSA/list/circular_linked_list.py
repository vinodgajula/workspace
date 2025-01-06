class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Insert at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head

    # Delete a node by value
    def delete(self, key):
        if not self.head:
            print("The list is empty.")
            return
        
        # If the node to be deleted is the head
        if self.head.data == key:
            if self.head.next == self.head:  # Single node in the list
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return

        # For non-head nodes
        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
            if temp.data == key:
                prev.next = temp.next
                return
        
        print("Node with value", key, "not found.")

    # Search for a node
    def search(self, key):
        if not self.head:
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    # Traverse the list
    def traverse(self):
        if not self.head:
            print("The list is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")

    # Count the number of nodes
    def count_nodes(self):
        if not self.head:
            return 0
        count = 0
        temp = self.head
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count

# Example Usage
cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.insert_at_beginning(5)
cll.insert_at_beginning(4)
cll.traverse()  # Output: 4 -> 5 -> 10 -> 20 -> 30 -> HEAD

print("Node count:", cll.count_nodes())  # Output: 5
cll.delete(10)
cll.traverse()  # Output: 4 -> 5 -> 20 -> 30 -> HEAD

print("Search 20:", cll.search(20))  # Output: True
print("Search 100:", cll.search(100))  # Output: False
