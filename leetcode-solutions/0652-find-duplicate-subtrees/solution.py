# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        triplet_to_id = {}
        id_to_count = {}
        res = []
        
        def getId(node):
            if not node:
                return 0
            left_id = getId(node.left)
            right_id = getId(node.right)
            triplet = (node.val,left_id,right_id)
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id)+1
            sub_id = triplet_to_id[triplet]
            id_to_count[sub_id] = id_to_count.get(sub_id,0)+1
            if id_to_count[sub_id] == 2:
                res.append(node)
            return sub_id
        getId(root)
        return res

