class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # time:O(n), space:O(1)
        reach = 0

        for i in range(len(nums)):
            num = nums[i]
            if i > reach:
                return False
        
            reach = max(reach, num + i)

        return True
        