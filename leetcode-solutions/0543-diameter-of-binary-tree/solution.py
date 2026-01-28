# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.calculateHeight(root)
        return self.max_diameter
    def calculateHeight(self,node):
        if not node: 
            return 0
        left_h = self.calculateHeight(node.left)
        right_h = self.calculateHeight(node.right)
        diameter = left_h + right_h
        self.max_diameter = max(self.max_diameter,diameter)
        return 1 +max(left_h,right_h)
