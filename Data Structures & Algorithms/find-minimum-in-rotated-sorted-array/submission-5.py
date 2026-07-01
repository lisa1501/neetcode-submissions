class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # lo-> 0 , hi -> last index 
        # while lo < hi
        # middle index num from nums
        # compare middle idx num with hi index num 
        # if middle idx num < hi idx num
        # move hi to mid
        # else move lo to mid + 1
        # return nums[lo]

        # time : O(logn) space: O(1)

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]


        





        