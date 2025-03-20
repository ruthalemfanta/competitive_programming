class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, maxx, minn):
            if not node:
                return maxx - minn
            maxx = max(maxx, node.val)
            minn = min(minn, node.val)
            left = helper(node.left, maxx, minn)
            right = helper(node.right, maxx, minn)

            return max(maxx - minn, max(left, right))

        return helper(root, float('-inf'), float('inf'))
