# Class to represent a binary tree node
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value  # Value of the node (question/decision)
        self.left = None    # Left child (No branch)
        self.right = None   # Right child (Yes branch)

    def display(self, level=0):
        # Print the tree structure (right subtree first for better visualization)
        if self.right:
            self.right.display(level + 1)
        print(" " * 4 * level + "-> " + str(self.value))
        if self.left:
            self.left.display(level + 1)


# Example: Loan eligibility decision tree
root = BinaryTreeNode("Is income > 50K?")  # Root decision node

# Left branch (No)
root.left = BinaryTreeNode("Has guarantor?")
root.left.left = BinaryTreeNode("Loan Denied")
root.left.right = BinaryTreeNode("Loan Approved with guarantor")

# Right branch (Yes)
root.right = BinaryTreeNode("Has credit score > 700?")
root.right.left = BinaryTreeNode("Loan Approved with higher interest")
root.right.right = BinaryTreeNode("Loan Approved")

# Display the binary decision tree
print("Binary Decision Tree Structure:")
root.display()
