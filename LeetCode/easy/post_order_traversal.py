class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)  
        traverse(node.right) 
        result.append(node.val)
    
    traverse(root)
    return result

# Example usage:
# Creating the tree mentioned above
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform postorder traversal
print(postorder_traversal(root))  # Output: [4, 5, 2, 3, 1]
