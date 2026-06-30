class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 1 <= nums.length <= 1000 
        # len(nums) == 1, return nums[0] k =1, 2, 
        # has duplicate ele is an edge case
        # Return the minimized largest sum of the split.
        # find out max num and sum of givne list
        # start = max num,  end is sum
        # mid => (start + end ) //2
        # use this mid check can we split or no
        # if split, move end pointer to mid
        # else starting pointer to mid
        # return starting point
        # helper function=> canSplit
        
        # given list is one sub array
        # sign a variable => cur sum = 0
        #  loop given list , increase cur sum by adding current ele in nums
        # if cur sum by adding current ele is greater than mid , 
        # we need another sub arr, and re assign cur sum = current num 
        # sub arr <= k

        # time: O(logn) + nlog(n)
        # space: O(1)

        # nums = [2,4,10,1,5], k = 2
        def canSplit(target): #16 #12
            cur_sum = 0
            sub_arr = 1
            for num in nums: 
                cur_sum += num 
                # 0+2 < 16
                # 0+2+4 < 16
                # 0+2+4 +10 == 16
                # 1 + 5 > 16


                # 0 + 2 + 4 +10= 16>12
                # 10+ 1 +5
                if cur_sum > target: # 0+2+4 +10 +1 > 16,
                    sub_arr += 1 # sub_arr=2 ,2 
                    cur_sum = num # 1 , 10
            return sub_arr <= k # 2 <=2 ,  2<=2
                    

        l = max(nums) # 10
        r = sum(nums) # 22

        while l <= r: # l =10, r 15, 
            mid = (l + r) //2  #16 # 12
            if canSplit(mid): 
                r = mid - 1 # r = 15 ,  10
            else:
                l = mid + 1
        return l


        