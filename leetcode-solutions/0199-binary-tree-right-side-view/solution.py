# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        if not root: return []
        while q:
            
            for _ in range(len(q)):
                node = q.popleft()
                last_node_val = node.val
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)

            res.append(last_node_val)
        return res
