class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def canFinish(speed):
            hours = 0
            for pile in piles:
                hours+=math.ceil(pile / speed)
            return hours<=h

        while l<r:
            mid = (l+r)//2

            if canFinish(mid):
                r = mid
            else:
                l = mid+1
        return l
        