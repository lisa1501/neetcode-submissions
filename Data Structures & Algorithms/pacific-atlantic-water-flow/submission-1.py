class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0,1), (0,-1),(1,0), (-1,0)]

        def dfs(row, col, visited):
            visited.add((row, col))
            
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or heights[nr][nc] < heights[row][col]:
                    continue

                dfs(nr, nc, visited)
        # The islands borders the Pacific Ocean from the top and left sides,
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)
        # borders the Atlantic Ocean from the bottom and right sides.
        for c in range(cols):
            dfs(rows-1, c, atlantic)

        for r in range(rows):
            dfs(r, cols-1, atlantic)
            
        ans = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    ans.append((row, col))
        return ans

        
