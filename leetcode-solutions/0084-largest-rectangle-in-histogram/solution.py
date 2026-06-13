from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        max_area = float('-inf')
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                element = heights[stack.pop()]
                if stack:
                    pse = stack[-1]
                else:
                    pse = -1
                area = element*(i-pse-1)
                max_area = max(max_area,area)
            stack.append(i)
        while stack:
            element = heights[stack.pop()]
            if stack:
                pse = stack[-1]
            else :
                pse = -1
            nse = len(heights)
            area = element*(nse-pse-1)
            max_area = max(max_area,area)
        return max_area
