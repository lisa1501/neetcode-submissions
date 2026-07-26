class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        INF = float("inf")

        # dist[node][flights_used]
        dist = [[INF] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        heap = [(0, src, 0)]  # (cost, city, flights_used)

        while heap:

            cost, city, flights = heapq.heappop(heap)

            if city == dst:
                return cost

            if cost > dist[city][flights]:
                continue

            if flights == k + 1:
                continue

            for nxt, price in graph[city]:

                new_cost = cost + price

                if new_cost < dist[nxt][flights + 1]:

                    dist[nxt][flights + 1] = new_cost

                    heapq.heappush(
                        heap,
                        (new_cost, nxt, flights + 1),
                    )

        return -1
        