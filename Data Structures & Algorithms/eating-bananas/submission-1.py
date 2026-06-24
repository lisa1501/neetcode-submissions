class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # piles = [1,4,3,2], h = 9
        #。        1，2，2 1=6
    # h is not 1.4 False

    # find min and max pile,
    # binary search, middle rate of min and max pile,
    # check can we eat piles by rate of this middle rate
    # if yes, calculate hours by the middle rate, if this hours <= given h,
    #    keep trying to find next middle between pre middle and smallest, 
    # if not , calculate hours by the middle rate, if this hours > given h,
    #     this middle is not working, we need to increase smallest rate
    #return smallest rate , 
    # O(logN), O(1)

        l = 1 #4
        r = max(piles) #25

        while l < r:
            mid = (l + r) // 2 # 14
            hours = sum([math.ceil(pile/mid) for pile in piles])
            print(hours)

            if hours <= h:
                r = mid
            else:
                l = mid+1#

        return l


        
            