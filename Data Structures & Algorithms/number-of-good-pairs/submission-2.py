class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Time:  O(n) Space: O(n)
        freq = {}
        res = 0
        for num in nums:
            res += freq.get(num, 0)
            freq[num] = freq.get(num, 0) + 1
        return res