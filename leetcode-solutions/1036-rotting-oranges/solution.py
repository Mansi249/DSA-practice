import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = collections.deque()
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while q and fresh >0 :
            time +=1
            for i in range(len(q)):
                curr_r , curr_c = q.popleft()
                for dr,dc in directions:
                    nr , nc = curr_r + dr , curr_c + dc
                    if (0<=nr < rows) and (0 <= nc< cols) and (grid[nr][nc] == 1):
                        fresh -=1
                        grid[nr][nc] =2 
                        q.append((nr,nc))
        return time if fresh ==0 else -1

