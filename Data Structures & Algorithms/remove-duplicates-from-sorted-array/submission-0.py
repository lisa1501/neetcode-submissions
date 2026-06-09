class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # [2,2,2,2] => k=1
        # [] no a edge case
        # [1,1,2,_,3,4] => no a edge case
        # [1,2,3,4] => k=4
        # [1] => k=1
        

        # [1,1,2,3,4]
        #    ^ k =1
        # [1,1,2,3,4]
        #    ^ [1,2,2,3,4] k+=1 =2
        #           ^  1,2,3,3,4] k+=1 =3
        # 1,2,3,3,4]
        #       ^  1,2,3,4,4] k+=1 =4

        # time: O(n)space O(1)

        #  [2,10,10,30,30,30]
        # twp pointers
        # 1st pointer k, start with k=1
        k = 1
        # 2nd pointer r start index 1, compare with next ele (r and r+=1)
        for sec in range(1, len(nums)):
            # if elements r and r+1 is not equal to each other , 
            if nums[sec] != nums[sec-1]: # 2!=10, # 10!=30
                 # just update the element on index k, 
                nums[k] = nums[sec] # [2,10,10,30,30,30]# [2,10,30,30,30,30]
                # increase k by one
                k+=1 # k=2, k=3
        # return this k
        return k
        
       
        
            
                
                
        

        