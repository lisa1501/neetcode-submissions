class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:

        # step 1: push to small (max heap)
        heapq.heappush(self.small, -num)

        # step 2: balance order
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # step 3: rebalance size
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        
        if len(self.large) < len(self.small):
            return -self.small[0]
        return (-self.small[0] + self.large[0])/2