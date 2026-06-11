from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        for i in range(len(nums)-1,-1,-1):
            val = nums[i]
            while stack and stack[-1]<= val:
                stack.pop()
            stack.append(val)
        ans = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            val = nums[i]
            while stack and stack[-1]<=val:
                stack.pop()
            if not stack:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(val)
        return ans



