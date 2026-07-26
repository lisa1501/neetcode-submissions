class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        

        def dfs(node):
            isConnected[node][node] = 0
            
            for nei in range(n):
                for nei in range(n):
                    if node != nei and isConnected[node][nei] == 1 and isConnected[nei][nei] == 1:
                        dfs(nei)
        res = 0
        for i in range(n):
            for i in range(n):
                if isConnected[i][i] == 1:
                    dfs(i)
                    res += 1
        return res