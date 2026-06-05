class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)-1
        while i<=l:
            if nums[i] != val:
                i+=1
            else:
                nums[i] = nums[l]
                l-=1
        return i
        
        