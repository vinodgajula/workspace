class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a new node in level-order
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = new_node
                break
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right = new_node
                break
            else:
                queue.append(temp.right)

    # Search for a value in the tree
    def search(self, data):
        if not self.root:
            return False
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.data == data:
                return True
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return False

    # Delete a node from the tree
    def delete(self, data):
        if not self.root:
            return None
        queue = [self.root]
        target_node = None
        last_node = None
        parent_of_last = None

        # Find the target node and the last node
        while queue:
            temp = queue.pop(0)
            if temp.data == data:
                target_node = temp
            if temp.left:
                parent_of_last = temp
                queue.append(temp.left)
            if temp.right:
                parent_of_last = temp
                queue.append(temp.right)
            last_node = temp

        if not target_node:
            return "Node not found"
        
        # Replace the target node's data with the last node's data
        if target_node and last_node:
            target_node.data = last_node.data
            if parent_of_last and parent_of_last.right == last_node:
                parent_of_last.right = None
            elif parent_of_last and parent_of_last.left == last_node:
                parent_of_last.left = None

    # Inorder Traversal (Left, Root, Right)
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    # Preorder Traversal (Root, Left, Right)
    def preorder_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

    # Level-order Traversal
    def level_order_traversal(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

    # Calculate the height of the tree
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Count the number of nodes in the tree
    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    # Count the number of leaf nodes in the tree
    def count_leaf_nodes(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)

    # Check if the tree is a full binary tree
    def is_full_binary_tree(self, node):
        if not node:
            return True
        if not node.left and not node.right:
            return True
        if node.left and node.right:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

# Initialize Binary Tree
tree = BinaryTree()

# Insert nodes
for val in range(1, 12):
    tree.insert(val)

# Display the tree (traversals)
print("Inorder Traversal:")
tree.inorder_traversal(tree.root)  # Output: 4 2 5 1 6 3 7

print("\nPreorder Traversal:")
tree.preorder_traversal(tree.root)  # Output: 1 2 4 5 3 6 7

print("\nPostorder Traversal:")
tree.postorder_traversal(tree.root)  # Output: 4 5 2 6 7 3 1

print("\nLevel-order Traversal:")
tree.level_order_traversal()  # Output: 1 2 3 4 5 6 7

# Tree Properties
print("\nHeight of Tree:", tree.height(tree.root))  # Output: 3
print("Total Nodes:", tree.count_nodes(tree.root))  # Output: 7
print("Leaf Nodes:", tree.count_leaf_nodes(tree.root))  # Output: 4
print("is_full_binary_tree:", tree.is_full_binary_tree(tree.root))  # Output: 4
# Search for a value
print("Is 5 in the tree?", tree.search(5))  # Output: True
print("Is 10 in the tree?", tree.search(10))  # Output: False

# Delete a node
tree.delete(3)
print("\nLevel-order Traversal after deleting 3:")
tree.level_order_traversal()  # Output: 1 2 7 4 5 6

