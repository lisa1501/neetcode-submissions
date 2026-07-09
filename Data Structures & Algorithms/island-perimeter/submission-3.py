class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0):
                return 1

            if (r, c) in visited:
                return 0

            visited.add((r, c))

            perimeter = 0

            perimeter += dfs(r+1, c)
            perimeter += dfs(r-1, c)
            perimeter += dfs(r, c+1)
            perimeter += dfs(r, c-1)
            
            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0