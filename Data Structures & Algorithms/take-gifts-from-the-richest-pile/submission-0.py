import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            remaining = int(math.sqrt(largest))

            heapq.heappush(heap, -remaining)
        return -sum(heap)
        