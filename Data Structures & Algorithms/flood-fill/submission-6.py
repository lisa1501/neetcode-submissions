class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original = image[sr][sc]
        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        q = deque([(sr, sc)])
        image[sr][sc] = color
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image
        