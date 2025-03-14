# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.left = []
        self.right = []
        if not root:
            return []
        self.traverseleft(root)
        self.traverseright(root)
        print(self.left, self.right)
        return self.left == self.right


    def traverseleft(self, node):
        if node:
            if not node.left and node.right:
                self.left.append('null')
            self.left.append(node.val)
            self.traverseleft(node.left)
            self.traverseleft(node.right)


    def traverseright(self, node):
        if node:
            if not node.right and node.left:
                self.right.append('null')
            self.right.append(node.val)
            self.traverseright(node.right)
            self.traverseright(node.left)





            

        