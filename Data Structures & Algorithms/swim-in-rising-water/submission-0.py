class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[float("inf")] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:

            curr_time, r, c = heapq.heappop(heap)

            if (r, c) == (n - 1, n - 1):
                return curr_time

            if curr_time > dist[r][c]:
                continue

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:

                    new_time = max(
                        curr_time,
                        grid[nr][nc]
                    )

                    if new_time < dist[nr][nc]:

                        dist[nr][nc] = new_time

                        heapq.heappush(
                            heap,
                            (new_time, nr, nc)
                        )

        return -1
        