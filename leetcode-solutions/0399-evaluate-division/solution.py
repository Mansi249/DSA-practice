from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)
        for (A, B), val in zip(equations, values):
            graph[A][B] = val
            graph[B][A] = 1.0 / val
            
        def bfs(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
                
            queue = deque([(start, 1.0)])
            visited = {start}
            
            while queue:
                curr, curr_prod = queue.popleft()
                
                if curr == end:
                    return curr_prod
                    
                for neighbor, value in graph[curr].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_prod * value))
                        
            return -1.0

        
        return [bfs(q[0], q[1]) for q in queries]

