class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        def _insert(root, value):
            if not root:
                return BSTNode(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            elif value > root.value:
                root.right = _insert(root.right, value)
            return root
        self.root = _insert(self.root, value)

    # Search for a value in the BST
    def search(self, value):
        def _search(root, value):
            if not root:
                return False
            if root.value == value:
                return True
            elif value < root.value:
                return _search(root.left, value)
            else:
                return _search(root.right, value)
        return _search(self.root, value)

    # Delete a value from the BST
    def delete(self, value):
        def _delete(root, value):
            if not root:
                return root
            if value < root.value:
                root.left = _delete(root.left, value)
            elif value > root.value:
                root.right = _delete(root.right, value)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = self.find_min(root.right)
                root.value = temp.value
                root.right = _delete(root.right, temp.value)
            return root

        self.root = _delete(self.root, value)

    # Find the minimum value in the BST
    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Find the maximum value in the BST
    def find_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current

    # Calculate the height of the BST
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Count the total number of nodes in the BST
    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    # Count the number of leaf nodes in the BST
    def count_leaf_nodes(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)

    # Check if the tree is a valid BST
    def is_valid_bst(self, node, left=float('-inf'), right=float('inf')):
        if not node:
            return True
        if not (left < node.value < right):
            return False
        return (self.is_valid_bst(node.left, left, node.value) and 
                self.is_valid_bst(node.right, node.value, right))

    # Inorder Traversal (Left, Root, Right)
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    # Preorder Traversal (Root, Left, Right)
    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

    # Level-order Traversal (Breadth-First)
    def level_order_traversal(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.value, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

# Example Usage
bst = BinarySearchTree()

# Insert values
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

# Traversals
print("Inorder Traversal:")
bst.inorder_traversal(bst.root)  # Output: 20 30 40 50 60 70 80

print("\nPreorder Traversal:")
bst.preorder_traversal(bst.root)  # Output: 50 30 20 40 70 60 80

print("\nPostorder Traversal:")
bst.postorder_traversal(bst.root)  # Output: 20 40 30 60 80 70 50

print("\nLevel-order Traversal:")
bst.level_order_traversal()  # Output: 50 30 70 20 40 60 80

# Properties
print("\nHeight of Tree:", bst.height(bst.root))  # Output: 3
print("Total Nodes:", bst.count_nodes(bst.root))  # Output: 7
print("Leaf Nodes:", bst.count_leaf_nodes(bst.root))  # Output: 4
print("Minimum Value:", bst.find_min(bst.root).value)  # Output: 20
print("Maximum Value:", bst.find_max(bst.root).value)  # Output: 80
print("Is Valid BST:", bst.is_valid_bst(bst.root))  # Output: True

# Search for values
print("Search 40:", bst.search(40))  # Output: True
print("Search 100:", bst.search(100))  # Output: False

# Delete a value
bst.delete(50)
print("\nInorder Traversal after deleting 50:")
bst.inorder_traversal(bst.root)  # Output: 20 30 40 60 70 80
