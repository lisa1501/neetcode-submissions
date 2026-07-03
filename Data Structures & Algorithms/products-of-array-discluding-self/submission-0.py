class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        # [1,2,4,6]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        # [1,1,2,8]
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
        return res




    

        
        