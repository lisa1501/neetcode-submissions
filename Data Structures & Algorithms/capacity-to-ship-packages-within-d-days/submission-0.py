class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(target):
            need_days = 1
            curr = target
            for weight in weights:
                if weight > curr:
                    need_days +=1
                    curr = target
                curr -= weight
                    
            return need_days <= days
                
        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
        


        
        