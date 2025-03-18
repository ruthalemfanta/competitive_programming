# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node, n, stack):
            if not node:
                return []  
            stack.append(node)

            if node.val == n.val:
                return stack  

            if n.val < node.val:
                return search(node.left, n, stack)
            else:
                return search(node.right, n, stack)

        ps = search(root, p, [])  
        qs = search(root, q, [])
        b = []

        for i in ps:
            if i in qs:
                b.append(i)
        return b[-1]
