class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        def bfs(row, col):
            grid[row][col] = 0
            q = deque([(row, col)])
            area = 1

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res