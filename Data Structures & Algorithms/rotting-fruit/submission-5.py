class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs
        # initial fresh fruit is 0, and deque is q, minutes is 0
        # loop through grid, if fresh fruit, increase fresh frui by 1, if rotten store r,c into q
        # while q is not empty, and we we fresh fruits
        # loop through q:
        # polleft q, get rotten fruit r,c
        # check four nei of fresh frui
        # if nei is in the boundary and is fresh
        # update this fresh to rotten, decrease fresh by 1, add nei (r,c) into q
        # when loop through q is done, increase minutes by 1
        # in the end, if there are still fresh fruit return -1, else return minutes
        # Time(rows * cols) , Space(rows * cols) 

        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fresh = 0
        q = deque()
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
            
        if fresh == 0:
            return minutes
        return -1



