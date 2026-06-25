class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # mid is the single element
            if ((mid == 0 or nums[mid - 1] != nums[mid]) and
                (mid == len(nums) - 1 or nums[mid] != nums[mid + 1])):
                return nums[mid]

            if nums[mid - 1] == nums[mid]:
                leftSize = mid - 1  
            else: 
                leftSize = mid

            if leftSize % 2 == 1:
                r = mid - 1
            else:
                l = mid + 1
        