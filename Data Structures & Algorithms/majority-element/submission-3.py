class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # [1] => [1]
        # [5,5,1,1,1,5,5,6,6,6,6] =>not edge case

        # create dic, 
        # for loop given list
        # key num in nums, val is frequency

        # for loop dic,
        # check if current key val is >n//2, 
        # return the key.
        # time O(n) , sapce O(n). O(1) 

        # [5,1,1,1,3,5,5] 1: 5 
        #  assign res=0, count=0
        #  [5,5,1,1,1,5,5]
        res = count = 0
        # for loop given list 
        for num in nums:
        # count =0, res=num, count+1
            if count == 0:
                res = num
                count+=1
        # if count is not eqaul to 0
            else:
                # check the cur num is res or no
                # yes, count+1, no count-1
                if num != res:
                    # [5,5,1,1,3,1,5,5]
                    count -= 1
                else:
                    count += 1
        # couunt eq 0, res to cur num , count+1 
        # cur num is eq res, count

        # count-1,  count is 0, res to current num, else keep count-1
        return res 
        # time O(n) , space O(1)




        