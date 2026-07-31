class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)
            

# The islands borders the Pacific Ocean from the top and left sides, 
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(0, c, pacific)
# borders the Atlantic Ocean from the bottom and right sides.
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        for c in range(cols):
            dfs(rows-1, c, atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append((r,c))
        return ans