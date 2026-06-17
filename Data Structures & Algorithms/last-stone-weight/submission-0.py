class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        print(heap)
        heapq.heapify(heap)
        print(heap)

        while len(heap)>1:
            largest = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if largest != second:
                heapq.heappush(heap, -(largest-second))
                print(heap)
        if heap:
            return -heap[0]
        else:
            return 0
        