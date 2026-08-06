# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left,root.right)
    def isMirror(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return self.isMirror(p.right,q.left) and self.isMirror(p.left,q.right)

