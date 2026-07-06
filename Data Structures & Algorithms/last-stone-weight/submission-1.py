class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first_largest = -heapq.heappop(heap)
            second_largest = -heapq.heappop(heap)

            if first_largest != second_largest:
                smashed = (first_largest - second_largest)
                heapq.heappush(heap, -smashed)
        
        if heap:
            return -heap[0]
        else:
            return 0

        