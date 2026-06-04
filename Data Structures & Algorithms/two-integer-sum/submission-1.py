class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # list nums [4.5 3.5] 8.0 
        #  nums = [5,5], target = 0 => has exactly one pair, nothing
        # nums = [3,4,5,6], target = 2 => don't have this edge case
    
    # 1. create hashmap, collect key is num, value index of this number
    # 2. for loop of given list, 
    # 3. if the target-num is not in hashmap, put this num in this hashmap, 
    # 4. else return [], the value of target-num, num

    # time : O(n) space: O(1)

        count = {}
        for i in range(len(nums)):
            cur_num = nums[i] 
            diff = target - cur_num 
            if diff not in count:
                count[cur_num] = i 
            else:
                return [count[diff], i] 
    






        