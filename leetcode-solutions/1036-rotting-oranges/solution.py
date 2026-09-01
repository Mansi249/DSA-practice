class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    queue.append([r,c])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue and fresh>0 :
            time+=1
            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()
                for dr,dc in directions:
                    sr,sc = curr_r+ dr, curr_c + dc
                    if (0<=sr<rows) and (0<=sc< cols) and grid[sr][sc]==1:
                        fresh-=1
                        grid[sr][sc] = 2
                        queue.append([sr,sc])
        return time if fresh ==0 else -1

