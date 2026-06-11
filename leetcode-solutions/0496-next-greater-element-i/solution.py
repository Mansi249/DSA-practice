from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        res_map = {}
        for i in range(len(nums2)-1,-1,-1):
            val = nums2[i]
            while stack and stack[-1]<= val:
                stack.pop()
            if not stack:
                res_map[val]= -1
            else:
                res_map[val]= stack[-1]
            stack.append(val)
        ans = []
        for num in nums1:
            ans.append(res_map[num])
        return ans

            

