class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]

        heapq.heapify(heap)

        for i in range(k):
            num, idx = heapq.heappop(heap)

            num *= multiplier

            nums[idx] = num

            heapq.heappush(heap, (num, idx))

        return nums



