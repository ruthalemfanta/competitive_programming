# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        q = deque([root])
        res= []
        loop = 0
        while q:
            level = []
            if loop % 2:
                for i in range(len(q) - 1, -1, -1):
                    level.append(q[i].val)
            else:
                for i in range(len(q)):
                    level.append(q[i].val)
            
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            loop += 1

            res.append(level)

        return res

