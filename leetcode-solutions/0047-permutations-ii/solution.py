from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        used = [False]*len(nums)
        def dfs():
            if len(path)==len(nums):
                result.append(path.copy())
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i-1]==nums[i] and used[i-1]==False:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs()
                path.pop()
                used[i] = False
        dfs()
        return result

