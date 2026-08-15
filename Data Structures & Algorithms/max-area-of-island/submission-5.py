class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col):
            area = 0
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                grid[row][col] = 0
                area += 1
                for dr, dc in dirs:
                    area += dfs(row+dr, col+dc)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r,c)) 
                    
        return ans
        