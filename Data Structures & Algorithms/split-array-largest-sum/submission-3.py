class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)

        def canSplit(target):
            subArr = 1
            cur = 0
            for num in nums:
                cur += num
                if cur > target:
                    subArr +=1
                    cur = num
            return subArr <= k

        while l <= r:
            mid = (l+r) // 2
            if canSplit(mid):
                r = mid -1
            else:
                l = mid + 1
        return l