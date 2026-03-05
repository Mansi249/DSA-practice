class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid),len(grid[0])
        max_area = 0
        def dfs(r,c):
            if r<0 or r>= rows or c<0 or c>= cols or grid[r][c] ==0:
                return 0
            grid[r][c] = 0
            current_island_count = 1
            current_island_count += dfs(r,c+1)
            current_island_count += dfs(r,c-1)
            current_island_count += dfs(r-1,c)
            current_island_count += dfs(r+1,c)
            return current_island_count
        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] ==1:
                    island_size = dfs(r,c)
                    max_area = max(max_area,island_size)
        return max_area
