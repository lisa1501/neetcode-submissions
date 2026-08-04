class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # early return -1, if grid very first or very last is 1
        # queue store (r,c, distance) initialize with (0,0,1)
        # 8 directiions 
        # set visited initialize with (0,0)

        # while queue is not empty
        # poplleft current (r,c, distance)
        # if current is the very last element, return disance
        # loop through dirs, get 8 nei of current 
        # if nei nr,nc is in boundary, not in visited and and == 0
        # add nr,nc into visited
        # queue stores (nr, nc, distance+1)
        # time:O(n*n) space:O(n*n)

        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        dirs = [(-1,-1),(-1,0), (-1,1),
                (0,-1),         (0,1),
                (1,-1), (1,0),  (1,1)]
        visited = set()
        visited.add((0,0))
        q = deque([(0,0,1)])

        while q:
            r,c, dist = q.popleft()
            if r == n-1 and c == n-1:
                return dist
            
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc,dist+1))

        # grid=[[0,1,1,1,0],
        #       [1,1,1,1,0],
        #       [1,1,0,0,0],
        #       [1,0,0,1,1],
        #       [0,0,0,0,0]]
        return -1

       




