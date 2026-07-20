class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        q = deque([(0, 0 , 1)])
        visited = set()
        visited.add((0,0))
        dirs = [(-1,1),(-1,0),(-1,1),
                (0,-1),       (0,1),
                (1,-1), (1,0), (1,1)]

        while q:
            r,c,dist = q.popleft()
            if r == n - 1 and c == n - 1:
                return dist

            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    q.append((nr,nc,dist+1))
                    visited.add((nr,nc))
        return -1


        