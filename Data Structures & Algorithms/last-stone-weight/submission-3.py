class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first_large = -heapq.heappop(heap)
            second_large = -heapq.heappop(heap)
            if first_large != second_large:
                smashed = first_large - second_large

                heapq.heappush(heap, -smashed)

        if heap:
            return -heap[0]
        return 0

        
        