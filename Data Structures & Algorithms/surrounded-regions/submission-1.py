class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != "O":
                return 
            board[row][col] = "#"

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

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "#":
                    board[r][c] = "O"
                



        