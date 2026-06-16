class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ans = float('inf')

        for r in range(k-1, len(nums)):
            l = r - k + 1
            ans = min(
                ans,
                nums[r] - nums[l]
            )
        return ans

        