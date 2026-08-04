class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        def canFinish(target):
            hour = 0
            for p in piles:
                hour += math.ceil(p/target)

                if hour > h:
                    return False
            return hour <= h
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if canFinish(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


        


        
            