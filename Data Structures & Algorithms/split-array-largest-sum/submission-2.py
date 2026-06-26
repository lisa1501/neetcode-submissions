class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)

        def canSplit(target):
            subArr = 1
            curr_sum = 0
            for num in nums:
                 curr_sum += num
                 if curr_sum > target:
                    subArr+=1
                    curr_sum = num
            return subArr <= k
                
        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                r = mid -1
            else:
                l = mid + 1

        return l

        