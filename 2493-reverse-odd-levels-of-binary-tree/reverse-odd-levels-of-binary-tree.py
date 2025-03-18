# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []

        self.reverse(root.left, root.right, 1)
        return root

    def reverse(self, l, r, level):
        if not l: return 
        if level % 2:
            l.val, r.val = r.val, l.val
        self.reverse(l.left, r.right, level + 1)
        self.reverse(l.right, r.left, level + 1)

        