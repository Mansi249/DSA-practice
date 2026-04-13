from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i :[] for i in range(numCourses)}
        indegree = [0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1
        queue = deque()
        for x in range(numCourses):
            if indegree[x]==0:
                queue.append(x)
        count = 0
        while queue:
            node = queue.popleft()
            count+=1
            for x in graph[node]:
                indegree[x] -=1
                if indegree[x]==0:
                    queue.append(x)
        return count == numCourses

