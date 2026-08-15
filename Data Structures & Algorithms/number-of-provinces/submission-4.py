class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 1. What are the NODES? n cities 
        # 2. What are the EDGES? isConnected[i][j] = 1, i<->j
        # 3. Directed or Undirected? Undirected
        # 4. Weighted? No
        # 5. What is the QUESTION? Number of Connected Components
        # 6. What constraint changes the basic algorithm? 
                # We need to make sure we don't count the same province multiple times.
        # 7. template
        # 8. time: O(n*n) space: O(n)

        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(node):
            visited.add(node)

            for nei in range(n):
                if isConnected[node][nei] == 1 and nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                provinces += 1
                dfs(node)

        return provinces
        
