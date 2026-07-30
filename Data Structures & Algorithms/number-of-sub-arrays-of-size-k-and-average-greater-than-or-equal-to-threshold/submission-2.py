class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        total = 0
        l = 0
        target = k * threshold
        for r in range(len(arr)):
            total += arr[r]

            if r - l + 1 > k :
                total -= arr[l]
                l += 1

            if r - l + 1 == k and total >= target:
                ans += 1
        return ans
            
            
        
        
        