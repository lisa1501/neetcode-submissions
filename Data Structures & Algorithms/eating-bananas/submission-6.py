class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # koko eats banana minimum speed is 1，max is max(piles)
        # binary serach, mid 
        # helper func, check if koko can eat all piles in h hours speed is mid
        # if can, move max speed to mid
        # if can not, move min speed to mid + 1
        # time: O(n*logm) n: len(piles), m: max(piles) space: O(1)

        def canFinish(target):
            hour = 0
            for p in piles:
                hour += math.ceil(p/target)

                if hour > h:
                    return False
            return True

        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if canFinish(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


        


        
            