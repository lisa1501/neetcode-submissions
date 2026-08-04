class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # can ship min is max(weights), max is sum(weights)
        # binary search, mid: this is target packages weight sum can ship in one day
        # initialize needs day 1, cur weight is 0
        # for loop weights, 
        # increase cur weight by w from loop
        # if cur weight greater than target, increase need day by 1, set cur weight to w
        # if need_days > days => False, 
        # end return True
        # time: O(n*logn) n: len(weights), space: O(1)
        lo = max(weights)
        hi = sum(weights)

        def canFinish(target):
            need_days = 1
            cur_weight = 0
            for w in weights:
                cur_weight += w
                if cur_weight > target:
                    need_days += 1
                    if need_days > days:
                        return False
                    cur_weight = w
            return True

        while lo < hi:
            mid = (lo + hi) // 2
            if canFinish(mid):
                hi = mid 
            else:
                lo = mid + 1
        return lo
        


        
        