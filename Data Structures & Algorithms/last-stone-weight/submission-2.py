class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        # [-6, -4, -3, -2, -2]
        while len(heap) > 1:
            first_largest = -heapq.heappop(heap)  #6 #3  #2 
            second_largest = -heapq.heappop(heap) #4 #2  #2 
            #[-1]
            if first_largest != second_largest:
                smashed = (first_largest - second_largest) #2 #1
                heapq.heappush(heap, -smashed)  
                #[-3, -2, -2, -2]
                #[-2, -2, -1]

        if heap:
            return -heap[0]
        else: 
            return 0

        