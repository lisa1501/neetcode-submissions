import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            first = -heapq.heappop(heap)
            reduced = int(math.sqrt(first))
            heapq.heappush(heap, -reduced)
        
        return -sum(heap)

        