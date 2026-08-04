class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search on answer
        # binary search 
        # lo is man(nums) hi is sum(nums)
        # while lo smaller than hi
        # mid 
        # on answer
        # helper func return a bool, can split mid => target or not
        # initilize sub arr is 1, cur sum is 0
        # loop through nums, 
        # cur sum by num in nums, 
        # if cur sum >= target, increase sub arr by 1, re sign cur sum to current num
        # return sub arr <= k
        # time:O(nlogs) space:(1), n len nums, s sum(nums)
        def canSplit(target):
            cur_sum = 0
            sub_arr = 1
            for num in nums:
                cur_sum += num
                if cur_sum > target:
                    sub_arr += 1
                    if sub_arr > k:
                       return False
                    cur_sum = num
            return True

        lo = max(nums)
        hi = sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if canSplit(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


        