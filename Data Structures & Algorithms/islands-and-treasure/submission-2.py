class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # time: o(n*m) space:o(n*m)
        n = len(grid) 
        m = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0),(-1,0)]
        # multi source bfs
        # store all (r,c) in a deque, if grid[r][c] == 0
        q = deque()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append((r, c))
        # while deque is not empty
        while q:
        # pop from deque, check four direction
            r, c = q.popleft()
        # if they are in the boundary and == 2147483647,
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0<=nr<n and 0<=nc<m and grid[nr][nc] == 2147483647:

        # updated dir to grid[r][c] += 1, then store new dir to q
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))


        