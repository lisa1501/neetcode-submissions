class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = "0"
                for dr, dc in dirs:
                    dfs(row+dr, col+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
                    
                    
        return islands
        