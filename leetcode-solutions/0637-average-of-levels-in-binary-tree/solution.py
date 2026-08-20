# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            val = 0
            for i in range(size):
                node = queue.popleft()
                val+= node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(val/size)
        return res
