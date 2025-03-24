# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.summ = 0
        def helper(root):
            if not root:
                return 

            helper(root.right)
            self.summ += root.val
            root.val = self.summ

            helper(root.left)

        helper(root)
        return root