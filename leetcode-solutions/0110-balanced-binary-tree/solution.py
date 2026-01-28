# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root) != -1

    def checkHeight(self,node):
        if not node:
            return 0
        left_h = self.checkHeight(node.left)
        if left_h == -1 : 
            return -1
        right_h = self.checkHeight(node.right)
        if right_h == -1 : 
            return -1
        if abs(left_h - right_h) >1:
            return -1

        return 1+ max(left_h,right_h)
