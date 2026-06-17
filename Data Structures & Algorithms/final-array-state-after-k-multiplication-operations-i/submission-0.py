class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        print(heap)
        heapq.heapify(heap)
        print(heap)

        for _ in range(k):

            value, idx = heapq.heappop(heap)

            value *= multiplier

            nums[idx] = value

            heapq.heappush(heap, (value, idx))

        return nums