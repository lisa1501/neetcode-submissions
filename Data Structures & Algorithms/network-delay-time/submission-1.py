class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time: O(ElogV), space:O(V+E), E num of times, V num of vertices
        graph = defaultdict(list)
        for source, target, time in times:#O(E)
            graph[source].append([target, time])

        info = float('inf')
        times = [info] * (n+1)
        times[k] = 0

        heap = [(0,k)]

        while heap:
            send_time, source = heapq.heappop(heap)

            if send_time > times[source]:
                continue

            for target, need_time in graph[source]:#O(E)
                new_time = send_time + need_time
                if new_time < times[target]:
                    times[target] = new_time
                    heapq.heappush(heap, (new_time, target))#O(logv)

        ans = max(times[1:])

        if ans != info:
            return ans
        return -1



