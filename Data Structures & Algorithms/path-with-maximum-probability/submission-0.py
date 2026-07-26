class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for (u,v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        prob = [0] * n
        prob[start_node] = 1
        heap = [(-1, start_node)]

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -curr_prob

            if node == end_node:
                return curr_prob

            if curr_prob < prob[node]:
                continue

            for nei, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob

                if new_prob > prob[nei]:
                    prob[nei] = new_prob
                    heapq.heappush(
                        heap,
                        (-new_prob, nei)
                    )

        return 0
        