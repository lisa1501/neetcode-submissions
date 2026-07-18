class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc

                    if(0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "0"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
                    
        return islands