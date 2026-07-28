import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def binarySearch(target):
            l = 0
            r = n
            while l < r:
                mid = (l + r) // 2
                
                if nums[mid] >= target:
                    r = mid 
                else:
                    l = mid + 1
            return l

        start = binarySearch(target)    
        end = binarySearch(target + 1) - 1 

        if start == n or nums[start] != target:
            return [-1,-1]
        return [start, end]
        
        