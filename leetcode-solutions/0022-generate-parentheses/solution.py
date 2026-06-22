class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(openCount,closeCount):
            if openCount == n and closeCount ==n:
                res.append("".join(path))
                return
            if openCount<n:
                path.append("(")
                dfs(openCount+1,closeCount)
                path.pop()
            if closeCount<openCount:
                path.append(")")
                dfs(openCount,closeCount+1)
                path.pop()
        dfs(0,0)
        return res

