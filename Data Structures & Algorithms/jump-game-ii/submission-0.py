class Solution:
    def jump(self, nums: List[int]) -> int:
        # time:O(n), space:O(1)
        reach = 0
        jumps = 0
        # End of the current jump's reachable range
        current_end = 0

        for i in range(len(nums)-1):
            num = nums[i]
            reach = max(reach, num + i)
            # We have reached the end of the current jump's range.
            if i == current_end:
                jumps += 1
                current_end = reach

        return jumps 
        