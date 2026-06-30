class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        mod = 1000000007
        n = len(nums)
        arr = [1] * n
        nums.sort()
        for i in range(1, len(arr)):
            arr[i] = (arr[i-1] * 2) % mod

        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                res += arr[r-l]
                res %= mod
                l +=1
            else:
                r -=1
        print(arr)
        return res