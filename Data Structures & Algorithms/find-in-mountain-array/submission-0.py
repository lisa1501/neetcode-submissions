class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find peak
        l, r = 0, n - 1
        length = mountainArr.length()

        while l < r:
            mid = (l + r) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid

        peak = l


        def binary_search(l, r, ascending):
            while l <= r:
                m = (l + r) >> 1
                val = mountainArr.get(m)
                if val == target:
                    return m
                if ascending == (val < target):
                    l = m + 1
                else:
                    r = m - 1
            return -1

        # Search left portion
        res = binary_search(0, peak, True)
        if res != -1:
            return res

        # Search right portion
        return binary_search(peak, length - 1, False)


        