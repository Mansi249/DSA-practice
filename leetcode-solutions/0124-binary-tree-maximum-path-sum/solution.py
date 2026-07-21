# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def get_max_sum(node):
            if not node:
                return 0
            left_sum = max(get_max_sum(node.left),0)
            right_sum = max(get_max_sum(node.right),0)
            self.max_sum = max(self.max_sum,(node.val + left_sum + right_sum))
            return node.val + max(right_sum,left_sum)
        get_max_sum(root)
        return self.max_sum

