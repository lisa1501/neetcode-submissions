class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # loop through grid, find first land 
        # if element (r,c) is 1, dfs, 
        # dfs: 
        # if (r,c) out of boundary or (r,c)  is 1 , skip
        # else store (r,c) in a queue, marked grid[(r,c)] to visited, changed nei to 2, 4 direc dfs
        # initialize distance with value 0
        # Multi-source BFS 
        # while q, check 4 nei of (r,c), 
        # if nei out of boundary or nei is 2 continue
        # if nei is 1, return distance, this means we reached to second island
        # else nei is 0 , changed nei to 2, and store nei into q, 
        # Time: O(n*n), Space: O(n*n)
        n = len(grid)
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 

            grid[r][c] = 2
            q.append((r,c))

            for dr, dc in dirs:
                nr, nc = r + dr, c +dc
                dfs(nr, nc)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
            if q: 
                break

        distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] == 2:
                        continue

                    if grid[nr][nc] == 1:
                        return distance

                    grid[nr][nc] = 2
                    q.append((nr, nc))

            distance += 1
   

                

                