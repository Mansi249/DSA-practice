class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        def dfs(i):
            isConnected[i][i] = 0
            for j in range(n):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 0
                    isConnected[j][i] = 0
                    dfs(j)
        for i in range(n):
            if isConnected[i][i] ==1:
                provinces+=1
                dfs(i)
        return provinces
