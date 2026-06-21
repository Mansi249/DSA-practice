from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(index, target):
            if target == 0:
                res.append(path.copy())
                return

            if index == len(candidates) or target < 0:
                return

            
            path.append(candidates[index])
            dfs(index + 1, target - candidates[index])
            path.pop()

            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            
            dfs(index + 1, target)

        dfs(0, target)
        return res
