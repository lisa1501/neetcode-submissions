class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))

        return res
        