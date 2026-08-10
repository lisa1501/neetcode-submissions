class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
         # time:O(n), space:O(k)
        reminder = {0 : -1}
        cur_sum = 0

        for i, num in enumerate(nums):
            cur_sum += num
            re = cur_sum % k

            if re not in reminder:
                reminder[re] = i
            elif i - reminder[re] > 1:
                return True
        return False
        