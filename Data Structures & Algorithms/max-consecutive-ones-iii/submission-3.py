class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # time:O(n) n is len(nums), space:O(1)
        l = 0
        zeros = 0
        ans = 0

        for r in range(len(nums)):
            # add right
            if nums[r] == 0:
                zeros += 1
            # invalid
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            # valid
            ans = max(ans, r - l + 1)

        return ans


        
        
        