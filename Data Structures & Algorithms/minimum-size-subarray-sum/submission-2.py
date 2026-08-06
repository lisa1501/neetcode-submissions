class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        total = 0

        l = 0
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                total -= nums[l]
                ans = min(ans, r-l+1)
                l += 1
            
        if ans == float('inf'):
            return 0
        return ans
        