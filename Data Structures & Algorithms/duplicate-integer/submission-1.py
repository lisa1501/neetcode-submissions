class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num] = freq.get(num, 0) + 1
        return False
        
            
        