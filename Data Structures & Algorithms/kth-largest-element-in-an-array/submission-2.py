class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [2,3,1,5,4], k = 2
        # nums = [1,2,3,4,5], k = 2 ruturn nums[-k]
        # 4

        # empty list = heap []
        # loop through nums, 
        # push num to heap,[1,2,3] => [2,3,4] = [3,4,5]
        # if len empty list = heap is greater than k, 
        # then pop heap [1,2,3] => [2,3],[2,3,4]=>[3,4], [3,4,5]=>[4,5]
        # return heap[0]

        # time: O(n*logk)
        # space:O(k)

        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
        