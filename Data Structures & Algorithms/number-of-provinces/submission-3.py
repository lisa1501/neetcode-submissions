class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        q = deque()
        n = len(isConnected)
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                res += 1
                visited[i] = True
                q.append(i)
                while q:
                    node = q.popleft()
                    for nei in range(n):
                        if not visited[nei] and isConnected[node][nei] == 1:
                            visited[nei] = True
                            q.append(nei)

        return res
        
