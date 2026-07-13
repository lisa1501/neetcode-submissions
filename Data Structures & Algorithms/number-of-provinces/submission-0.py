class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)

        def dfs(city):

            visited.add(city)

            for neighbor in range(n):

                if (
                    isConnected[city][neighbor] == 1
                    and neighbor not in visited
                ):
                    dfs(neighbor)

        answer = 0

        for city in range(n):

            if city not in visited:

                dfs(city)

                answer += 1

        return answer
        