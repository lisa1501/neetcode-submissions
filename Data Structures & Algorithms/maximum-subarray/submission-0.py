class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time:O(n), space:O(1)
        max_cur_sum = nums[0]
        max_sub_sum = nums[0]

        for i in range(1,len(nums)):
            # max subarray sum ending at i
            max_cur_sum = max(nums[i], max_cur_sum + nums[i])
            # max subarray sum anywhere so far
            max_sub_sum = max(max_sub_sum, max_cur_sum)
        return max_sub_sum
        