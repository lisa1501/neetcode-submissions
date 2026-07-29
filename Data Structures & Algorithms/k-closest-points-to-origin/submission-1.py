class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xi, yi in points:
            distance = xi*xi + yi*yi
            heapq.heappush(heap, (-distance, xi, yi))

            while len(heap) > k:
                heapq.heappop(heap)

        return [(xi, yi) for distance, xi, yi in heap]

        
        