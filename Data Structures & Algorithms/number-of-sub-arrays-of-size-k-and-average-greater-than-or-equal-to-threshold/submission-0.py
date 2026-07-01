class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        ans = 0
        cur_sum = 0
        target = k * threshold
        for r in range(len(arr)):
            cur_sum += arr[r]
            if r - l + 1 > k:
                cur_sum -= arr[l]
                l += 1
            if r - l + 1 == k:
                if cur_sum >= target:
                    ans += 1
        return ans

        
        