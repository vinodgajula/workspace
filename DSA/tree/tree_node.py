# Class to represent a tree node
class TreeNode:
    def __init__(self, value):
        self.value = value  # Value of the node
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        # Print the current node with indentation
        print(" " * level * 4 + str(self.value))
        for child in self.children:
            child.display(level + 1)  # Recursive call to display children

    def search(self, target):
        # Search for a node by value
        if self.value == target:
            return self
        for child in self.children:
            result = child.search(target)
            if result:
                return result
        return None

    def count_nodes(self):
        # Count total nodes in the tree
        total = 1  # Count the current node
        for child in self.children:
            total += child.count_nodes()
        return total

    def count_leaf_nodes(self):
        # Count total leaf nodes (nodes with no children)
        if not self.children:
            return 1  # Leaf node
        total = 0
        for child in self.children:
            total += child.count_leaf_nodes()
        return total

    def height(self):
        # Calculate the height of the tree
        if not self.children:
            return 1  # Leaf node
        return 1 + max(child.height() for child in self.children)

    def delete_subtree(self, target):
        # Delete a subtree rooted at a given target
        for i, child in enumerate(self.children):
            if child.value == target:
                del self.children[i]
                return True
            if child.delete_subtree(target):
                return True
        return False

    def find_parent(self, target):
        # Find the parent of a node with the given value
        for child in self.children:
            if child.value == target:
                return self
            result = child.find_parent(target)
            if result:
                return result
        return None

    def find_depth(self, target, depth=0):
        # Find the depth of a node in the tree
        if self.value == target:
            return depth
        for child in self.children:
            result = child.find_depth(target, depth + 1)
            if result is not None:
                return result
        return None

    def is_balanced(self):
        # Check if the tree is balanced (subtrees differ in height by at most 1)
        heights = [child.height() for child in self.children]
        return max(heights) - min(heights) <= 1 if heights else True


# Example: Organizational Hierarchy
root = TreeNode("CEO")

# Add direct reports to CEO
cto = TreeNode("CTO")
cfo = TreeNode("CFO")
coo = TreeNode("COO")
root.add_child(cto)
root.add_child(cfo)
root.add_child(coo)

# Add team under CTO
head_of_engineering = TreeNode("Head of Engineering")
cto.add_child(head_of_engineering)

# Add engineers under Head of Engineering
engineer1 = TreeNode("Engineer1")
engineer2 = TreeNode("Engineer2")
head_of_engineering.add_child(engineer1)
head_of_engineering.add_child(engineer2)

# Add team under CFO
head_of_finance = TreeNode("Head of Finance")
cfo.add_child(head_of_finance)

# Add accountants under Head of Finance
accountant1 = TreeNode("Accountant1")
accountant2 = TreeNode("Accountant2")
head_of_finance.add_child(accountant1)
head_of_finance.add_child(accountant2)

# Add team under COO
head_of_operations = TreeNode("Head of Operations")
coo.add_child(head_of_operations)

# Add operations staff under Head of Operations
staff1 = TreeNode("Operations Staff1")
staff2 = TreeNode("Operations Staff2")
head_of_operations.add_child(staff1)
head_of_operations.add_child(staff2)

# Perform various operations
print("Organizational Hierarchy:")
root.display()

print("\nTotal Nodes:", root.count_nodes())
print("Leaf Nodes:", root.count_leaf_nodes())
print("Tree Height:", root.height())
print("Is 'Engineer1' in the tree?", "Yes" if root.search("Engineer1") else "No")
parent_node = root.find_parent("Engineer1")
print("Parent of 'Engineer1':", parent_node.value if parent_node else "None")
print("Depth of 'Engineer1':", root.find_depth("Engineer1"))
print("Is the tree balanced?", root.is_balanced())

print("\nAfter Deleting 'Head of Operations':")
root.delete_subtree("Head of Operations")
root.display()
