class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0:
                return 0

            l = 0
            total = 0
            ans = 0
            for r in range(len(nums)):
                total += nums[r]

                while total > goal:
                    total -= nums[l]
                    l += 1
                ans += r - l + 1
            return ans
        return atMost(goal) - atMost(goal - 1)
        