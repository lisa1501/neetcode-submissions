class Solution:
    def jump(self, nums: List[int]) -> int:
        # time:O(n), space:O(1)
        jumps = 0
        l = 0
        r = 0
        
        while r < len(nums) - 1:
            reach = 0

            for i in range(l, r+1):
                reach = max(reach, i + nums[i])
            
            l = r
            r = reach
            jumps += 1

        return jumps
        