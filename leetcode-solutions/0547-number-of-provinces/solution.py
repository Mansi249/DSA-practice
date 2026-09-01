class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = [0]*n
        def dfs(i):
            isConnected[i][i] = 0
            for j in range(n):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    isConnected[i][j] = 0
                    visited[j] = 1
                    dfs(j)
        for i in range(n):
            if visited[i] == 0:
                provinces+=1
                dfs(i)
        return provinces    
