class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # Build graph
        for u, v, w in times:
            graph[u].append((v, w))

        INF = float("inf")
        dist = [INF] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:

            curr_dist, node = heapq.heappop(heap)

            # Ignore outdated entry
            if curr_dist > dist[node]:
                continue

            for nei, weight in graph[node]:

                new_dist = curr_dist + weight

                if new_dist < dist[nei]:

                    dist[nei] = new_dist

                    heapq.heappush(heap, (new_dist, nei))

        answer = max(dist[1:])

        return answer if answer != INF else -1
            