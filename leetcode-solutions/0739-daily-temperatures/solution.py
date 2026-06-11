from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            val = temperatures[i]
            while stack and temperatures[stack[-1]]<= val:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]-i
            stack.append(i)
        return ans

