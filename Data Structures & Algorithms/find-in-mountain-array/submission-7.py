class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l = 0 
        r = n 
        while l < r:
            mid = (l+r) //2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1
            else:
                r = mid 
        peak = l

        def binary_search(l, r, ascending):
            while l<=r:
                m = (l+r)//2
                val = mountainArr.get(m)
                if val == target:
                    return m
                if (val < target) == ascending:
                    l = m+1
                else:
                    r = m-1
            return -1

        left_res = binary_search(0, peak, True)
        right_res = binary_search(peak, n-1, False)

        if left_res == -1:
            return right_res
        return left_res



        
        


        