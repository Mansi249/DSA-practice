from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(index, target):
            if target == 0:
                result.append(path.copy())
                return

            if index == len(candidates) or target < 0:
                return

            
            path.append(candidates[index])
            dfs(index, target - candidates[index])   
            path.pop()

           
            dfs(index + 1, target)

        dfs(0, target)
        return result
