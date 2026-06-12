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


        # 2. Search ascending side
        l, r = 0, peak

        while l <= r:
            mid = (l + r) // 2

            value = mountainArr.get(mid)

            if value == target:
                return mid

            if value < target:
                l = mid + 1
            else:
                r = mid - 1

        # 3. Search descending side
        l, r = peak + 1, n - 1

        while l <= r:
            mid = (l + r) // 2

            value = mountainArr.get(mid)

            if value == target:
                return mid

            if value > target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


        