# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.res = []
        self.pre(root)
        return self.res

    def pre(self, root):
        if root:
            self.res.append(root.val)
            self.pre(root.left)
            self.pre(root.right)



        