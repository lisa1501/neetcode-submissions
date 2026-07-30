class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        total = 0
        l = 0
        for r in range(len(arr)):
            total += arr[r]

            if r - l + 1 > k :
                total -= arr[l]
                l += 1

            if r - l + 1 == k and (total // k) >= threshold:
                ans += 1
        return ans
            
            
        
        
        