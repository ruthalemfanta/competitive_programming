# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min_value(self, node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        
        return current_node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  
            if not root.left:
                return root.right 
            elif not root.right:
                return root.left

            temp = self.find_min_value(root.right)
            root.val = temp.val

            root.right = self.deleteNode(root.right, temp.val)       

        return root                        
            