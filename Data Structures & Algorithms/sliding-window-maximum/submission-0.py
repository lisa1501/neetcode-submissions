class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for r in range(len(nums)):

            # Remove smaller elements
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            dq.append(r)

            # Remove expired index
            if dq[0] <= r - k:
                dq.popleft()

            # Window formed
            if r >= k - 1:
                ans.append(nums[dq[0]])

        return ans
        