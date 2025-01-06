class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Initialize the queue with None
        self.front = -1  # Points to the front element
        self.rear = -1   # Points to the rear element

    def enqueue(self, item):
        """Add an element to the queue."""
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
        else:
            if self.front == -1:  # First element being added
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front element."""
        if self.front == -1:  # Queue is empty
            return "Queue is empty!"
        else:
            removed_item = self.queue[self.front]
            self.queue[self.front] = None  # Optional: Clear the slot
            if self.front == self.rear:  # Queue becomes empty
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return removed_item

    def peek(self):
        """View the front element without removing it."""
        if self.front == -1:
            return "Queue is empty!"
        return self.queue[self.front]

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front == -1

    def is_full(self):
        """Check if the queue is full."""
        return (self.rear + 1) % self.size == self.front

    def display(self):
        """Display the queue."""
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents:", end=" ")
            index = self.front
            while index != self.rear:
                print(self.queue[index], end=" ")
                index = (index + 1) % self.size
            print(self.queue[index])  # Print the last element

# Example Usage
#cq = CircularQueue(5)  # Create a circular queue of size 5

#cq.enqueue(10)
#cq.enqueue(20)
#cq.enqueue(30)
#cq.enqueue(40)
#cq.display()  # Output: 10 20 30 40

#print("Dequeued:", cq.dequeue())  # Output: 10
#cq.display()  # Output: 20 30 40

#cq.enqueue(50)
#cq.enqueue(60)
#cq.display()  # Output: 20 30 40 50 60

#cq.enqueue(70)  # Queue is full!

class PriorityQueue:
    def __init__(self):
        self.queue = []  # List to store (priority, value) pairs

    def enqueue(self, item, priority):
        """Add an item with its priority."""
        self.queue.append((priority, item))  # Append a tuple (priority, item)
        print(f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        """Remove and return the item with the highest priority."""
        if self.is_empty():
            return "Queue is empty!"
        
        # Find the item with the highest priority (lowest priority value)
        highest_priority_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] < self.queue[highest_priority_index][0]:  # Lower priority value = higher priority
                highest_priority_index = i

        # Remove and return the highest priority item
        priority, item = self.queue[highest_priority_index]
        del self.queue[highest_priority_index]
        return f"Dequeued: {item} with priority {priority}"

    def peek(self):
        """View the item with the highest priority without removing it."""
        if self.is_empty():
            return "Queue is empty!"
        
        # Find the item with the highest priority
        highest_priority_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] < self.queue[highest_priority_index][0]:
                highest_priority_index = i

        return f"Front item: {self.queue[highest_priority_index][1]} with priority {self.queue[highest_priority_index][0]}"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def display(self):
        """Display the queue with priorities."""
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents (priority, value):", self.queue)

# Example Usage
# pq = PriorityQueue()
# pq.enqueue("Task 1", 3)
# pq.enqueue("Task 2", 1)
# pq.enqueue("Task 3", 2)

# pq.display()
# print(pq.peek())  # Output: Front item: Task 2 with priority 1

# print(pq.dequeue())  # Output: Dequeued: Task 2 with priority 1
# pq.display()  # Output: [(3, 'Task 1'), (2, 'Task 3')]

# pq.enqueue("Task 4", 0)
# pq.display()  # Output: [(3, 'Task 1'), (2, 'Task 3'), (0, 'Task 4')]

class Deque:
    def __init__(self):
        self.deque = []  # Initialize an empty list to represent the deque

    def enqueueFront(self, item):
        """Insert an item at the front of the deque."""
        self.deque = [item] + self.deque  # Add item to the front by concatenating lists
        print(f"Enqueued at front: {item}")

    def enqueueRear(self, item):
        """Insert an item at the rear of the deque."""
        self.deque = self.deque + [item]  # Add item to the rear by concatenating lists
        print(f"Enqueued at rear: {item}")

    def dequeueFront(self):
        """Remove and return the front item."""
        if self.isEmpty():
            return "Deque is empty!"
        front_item = self.deque[0]  # Access the front item
        self.deque = self.deque[1:]  # Remove the front item by slicing
        return f"Dequeued from front: {front_item}"

    def dequeueRear(self):
        """Remove and return the rear item."""
        if self.isEmpty():
            return "Deque is empty!"
        rear_item = self.deque[-1]  # Access the rear item
        self.deque = self.deque[:-1]  # Remove the rear item by slicing
        return f"Dequeued from rear: {rear_item}"

    def peekFront(self):
        """View the front item without removing it."""
        if self.isEmpty():
            return "Deque is empty!"
        return f"Front item: {self.deque[0]}"

    def peekRear(self):
        """View the rear item without removing it."""
        if self.isEmpty():
            return "Deque is empty!"
        return f"Rear item: {self.deque[-1]}"

    def isEmpty(self):
        """Check if the deque is empty."""
        return len(self.deque) == 0

    def display(self):
        """Display the entire deque."""
        if self.isEmpty():
            print("Deque is empty!")
        else:
            print("Deque contents:", self.deque)

# Example Usage
# dq = Deque()
# dq.enqueueRear(10)
# dq.enqueueFront(20)
# dq.enqueueRear(30)
# dq.display()  # Output: Deque contents: [20, 10, 30]

# print(dq.dequeueFront())  # Output: Dequeued from front: 20
# dq.display()  # Output: Deque contents: [10, 30]

# print(dq.dequeueRear())  # Output: Dequeued from rear: 30
# dq.display()  # Output: Deque contents: [10]


