# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def helper(root):
            if not root:
                return (0, 0)

            if not root.left and not root.right:
                self.count += 1
                return (root.val, 1)
            left_sum, left_roots = helper(root.left) 
            right_sum, right_roots = helper(root.right) 

            avg = (left_sum + root.val + right_sum) // (left_roots + 1 + right_roots)

            if avg == root.val:
                self.count += 1

            return (left_sum + root.val + right_sum,left_roots + 1 + right_roots )
        helper(root)

        return self.count


        