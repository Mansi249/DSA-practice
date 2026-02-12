import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        
        q = collections.deque()
        
        def bfs(r, c):
            
            
            grid[r][c] = "0" 
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            
            while q: 
                curr_r, curr_c = q.popleft() 
                
                for dr, dc in directions:
                    nr = curr_r + dr
                    nc = curr_c + dc
                    
                    
                    if (0 <= nr < rows) and (0 <= nc < cols) and (grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0" 
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    q.append((r, c)) 
                    bfs(r, c)        
                    
        return islands
