class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # time:O(n), space:O(1)
        res = 0
        prefix = 0
        cnt = [1,0]
        MOD = 10**9 + 7
        for num in arr:
            prefix = (prefix + num) % 2
            res = (res + cnt[1-prefix]) % MOD
            cnt[prefix] += 1
        return res