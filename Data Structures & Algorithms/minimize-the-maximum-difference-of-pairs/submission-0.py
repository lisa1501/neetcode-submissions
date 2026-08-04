class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        lo = 0 
        hi = nums[-1] - nums[0]
        res = hi

        def isValid(target):
            i = 0
            count = 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= target:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True
            return False

        while lo < hi:
            mid = (lo + hi) // 2
            if isValid(mid):
                hi = mid
                res = min(res, hi)
            else:
                lo = mid + 1
        return res
        