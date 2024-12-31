class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    def push(self, item):
        """Insert an item to the stack (top of the stack)."""
        self.stack = [item] + self.stack  # Add the item at the beginning of the list
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.isEmpty():
            return "Stack is empty!"
        top_item = self.stack[0]  # Access the top item
        self.stack = self.stack[1:]  # Remove the top item by slicing the list
        return f"Popped: {top_item}"

    def peek(self):
        """View the top item without removing it."""
        if self.isEmpty():
            return "Stack is empty!"
        return f"Top item: {self.stack[0]}"

    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def display(self):
        """Display the entire stack."""
        if self.isEmpty():
            print("Stack is empty!")
        else:
            print("Stack contents:", self.stack)

# Example Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  # Output: Stack contents: [30, 20, 10]

print(stack.pop())  # Output: Popped: 30
stack.display()  # Output: Stack contents: [20, 10]

print(stack.peek())  # Output: Top item: 20
print(stack.isEmpty())  # Output: False
