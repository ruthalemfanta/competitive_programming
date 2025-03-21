# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        stack = [(root, str(root.val))]
        summ = 0

        while stack:
            node, cur = stack.pop()
            if node.left:
                stack.append((node.left, cur + str(node.left.val)))
            if node.right:
                stack.append((node.right, cur + str(node.right.val)))
            if not node.left and not node.right:
                summ += int(cur)

        return summ 
