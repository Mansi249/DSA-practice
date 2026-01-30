# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.Validate(root,float('-inf'),float('+inf'))
    def Validate(self,node,low,high):
        if not node: return True
        if not (low<node.val<high):
            return False
        return (self.Validate(node.left,low,node.val) and 
        self.Validate(node.right,node.val,high))
        
