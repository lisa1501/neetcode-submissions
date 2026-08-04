class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def count(product):
            count = 0

            for a in nums1:

                if a > 0:
                    count += bisect.bisect_right(nums2, product // a)

                elif a < 0:
                    target = -((-product) // a)
                    idx = bisect.bisect_left(nums2, target)
                    count += len(nums2) - idx

                else:
                    if product >= 0:
                        count += len(nums2)

            return count

        lo = -(10**10) 
        hi = 10**10

        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        return lo