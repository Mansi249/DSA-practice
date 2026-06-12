from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for i in asteroids:
            
            while stack and i < 0 and stack[-1] > 0:
                diff = stack[-1]+i
                if diff<0:
                    stack.pop()
                    
                elif diff>0:
                    i = 0
                    break
                else:
                    stack.pop()
                    i=0
                    break
            if i!=0:
                stack.append(i)
        return list(stack)


            
