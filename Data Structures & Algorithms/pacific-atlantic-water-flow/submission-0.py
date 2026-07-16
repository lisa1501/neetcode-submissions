class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols
                ):
                    continue

                if (nr, nc) in visited:
                    continue

                # Reverse flow:
                # only climb to equal or higher cells
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)

        # Pacific (top row + left column)
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic (bottom row + right column)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        answer = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    answer.append([row, col])

        return answer
        