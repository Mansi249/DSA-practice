from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        indegree = [0]*numCourses
        for a,b in prerequisites :
            graph[b].append(a)
            indegree[a] +=1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for x in graph[node]:
                indegree[x] -=1
                if indegree[x] ==0:
                    queue.append(x)
        if len(result) == numCourses:
            return result
        else:
            return []
