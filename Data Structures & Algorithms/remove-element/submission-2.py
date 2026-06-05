class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [],val=3 => k=0, []
        # [1] val=1 => k = 0, [1]
        # [1] val=2 => k =1, [1]
        # len(nums) 
        
        # create an empty[]
        res = []
        # for loop nums, check element is equal to val or no 
        for num in nums:
        # if not , put an empty[]
            if num != val:
                res.append(num)
        # return len of crated list as k, 
        k = len(res)
        # replace given list first k elements with ele where in created list 
        for i in range(k):
            nums[i] = res[i]
        # return the updated given list
        print(nums)
        return k
        # time: (n) space: k:O(1),output list O(m) 

        





        
        
        