class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        if not board:
            return None

        rows = len(board)
        cols = len(board[0])
        ans = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 1:
                return 

            board[r][c] = 2
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for row in range(rows):
            for col in [0, cols-1]:
                dfs(row, col)

        for col in range(cols):
            for row in [0, rows-1]:
                dfs(row, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    ans += 1

        return ans
        