class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0
            ):
                return

            grid[r][c] = 0

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Left & Right borders
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        # Top & Bottom borders
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        answer = 0
        
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1:
                    answer += 1

        return answer
        