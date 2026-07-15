class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        if not board:
            return 

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != 1:
                return 
            board[row][col] = 0

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        # top and bottom border
        for c in range(cols):
            for r in [0, rows-1]:
                dfs(r, c)
        # left and right border
        for r in range(rows):
            for c in [0, cols-1]:
                dfs(r, c)

        ans = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    ans += 1

        return ans