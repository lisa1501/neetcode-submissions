import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)
        print(heap)

        for i in range(k):
            largest = -heapq.heappop(heap)
            squared = int(math.sqrt(largest))
            heapq.heappush(heap, -squared)
        return -sum(heap)  

        