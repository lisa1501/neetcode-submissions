class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        max_freq = 0
        res = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                freq[nums[r]] += 1

            max_freq = max(max_freq, freq[nums[r]])

            while (r - l + 1) - max_freq > k:
                freq[nums[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))
            
        return res
        
        