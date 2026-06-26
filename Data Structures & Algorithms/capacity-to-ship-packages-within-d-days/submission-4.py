class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canShip(target):
            need_days = 1
            curr = 0
            for weight in weights:
                curr += weight
                if curr > target:
                    need_days +=1
                    curr = weight
                     
            return need_days <= days
                
        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        


        
        