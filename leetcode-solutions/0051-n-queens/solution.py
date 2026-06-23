class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag = set()
        anti = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r - c) in diag or (r + c) in anti:
                    continue

                
                col.add(c)
                diag.add(r - c)
                anti.add(r + c)
                board[r][c] = "Q"

                dfs(r + 1)

                
                board[r][c] = "."
                col.remove(c)
                diag.remove(r - c)
                anti.remove(r + c)

        dfs(0)
        return res
