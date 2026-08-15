class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        res = []

        def dfs(r, c, visit):
            visit.add((r,c))
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visit or heights[nr][nc] < heights[r][c]:
                    continue
            
                dfs(nr, nc, visit)

            

        for r in range(rows):
            dfs(r, 0, pacific)
        
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, cols-1, atlantic)
        
        for c in range(cols):
            dfs(rows-1, c, atlantic)


        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r, c) in atlantic:
                    res.append([r,c])


        return res

    
        