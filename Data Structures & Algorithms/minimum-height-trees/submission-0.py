class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        print(graph)

        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        print(leaves)

        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()

                for nei in graph[leaf]:
                    graph[nei].remove(leaf)
                    if len(graph[nei]) == 1:
                        leaves.append(nei)

                graph.pop(leaf)

        return list(leaves)
        